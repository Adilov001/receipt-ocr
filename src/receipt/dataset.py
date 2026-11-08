"""Dataset metadata, ground truth and the seller-disjoint dev/test split.

data/meta.csv, one row per image:
    image,receipt_id,seller,lang,conditions,has_qr
    r01_a.jpg,r01,korzinka_chilonzor,uz_latn,clean,1
    r01_b.jpg,r01,korzinka_chilonzor,uz_latn,crumpled;shadow,1
Several photos of one receipt share receipt_id (one ground truth) and always land in the same split.
"""
import csv
import json
import random

from .config import ROOT

CONDITIONS = ["clean", "crumpled", "shadow", "uneven_light", "tilted", "perspective", "faded", "long", "handheld",
              "sideways", "synthetic"]


def _p(rel):
    return ROOT / rel


def load_meta(cfg):
    rows = []
    with open(_p(cfg["data"]["meta"]), encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if not r.get("image"):
                continue
            r["conditions"] = [c.strip() for c in (r.get("conditions") or "").split(";") if c.strip()]
            r["has_qr"] = str(r.get("has_qr", "0")).strip() in ("1", "true", "yes")
            r["path"] = _p(cfg["data"]["images"]) / r["image"]
            rows.append(r)
    return rows


def make_split(rows, test_fraction=0.35, seed=42):
    """Assign whole sellers to test until it holds ~test_fraction of the images."""
    by_seller = {}
    for r in rows:
        by_seller.setdefault(r["seller"], 0)
        by_seller[r["seller"]] += 1
    sellers = sorted(by_seller)
    random.Random(seed).shuffle(sellers)
    target = test_fraction * len(rows)
    test, n = [], 0
    for s in sellers:
        if n >= target:
            break
        test.append(s)
        n += by_seller[s]
    return {"test": sorted(test), "dev": sorted(set(sellers) - set(test))}


def load_split(cfg):
    path = _p(cfg["data"]["split"])
    return json.loads(path.read_text()) if path.exists() else None


def rows_for(cfg, split):
    rows = load_meta(cfg)
    if split == "all":
        return rows
    sp = load_split(cfg)
    if sp is None:
        raise SystemExit("No split yet: run `make split` first.")
    return [r for r in rows if r["seller"] in sp[split]]


def load_gt(cfg, receipt_id):
    """(fields dict or None, full text or None)."""
    base = _p(cfg["data"]["gt"]) / receipt_id
    j, t = base.with_suffix(".json"), base.with_suffix(".txt")
    fields = json.loads(j.read_text(encoding="utf-8")) if j.exists() else None
    text = t.read_text(encoding="utf-8") if t.exists() else None
    return fields, text
