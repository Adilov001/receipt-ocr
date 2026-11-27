"""Recompute every metric with one command.

    python scripts/evaluate.py                 # engines x configs on the test split
    python scripts/evaluate.py --ablation      # + preprocessing ablation (on the dev split)

Writes CSV tables and reports/results.md.
"""
import argparse
import sys
import time
import traceback
from collections import defaultdict
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from receipt import FIELDS  # noqa: E402
from receipt.config import ROOT, load_config, with_overrides  # noqa: E402
from receipt.dataset import is_text_source, load_gt, rows_for  # noqa: E402
from receipt.metrics import field_matches, item_counts, prf, text_counts  # noqa: E402
from receipt.normalize import CYR2LAT, norm_field, unify_apostrophes  # noqa: E402
from receipt.pipeline import load_image, process  # noqa: E402
from receipt.qr import decode_qr  # noqa: E402


def classify_error(field, gt, pred, gt_all):
    """Rough cause of a field error, for the error analysis."""
    if pred is None:
        return "not found"
    if gt is None:
        return "spurious value"
    others = [f for f in FIELDS if f != field and norm_field(f, gt_all.get(f)) is not None
              and str(norm_field(f, gt_all.get(f))) == str(norm_field(field, pred))]
    if others:
        return f"wrong line picked (value of {others[0]})"
    g, p = str(gt), str(pred)
    if field in ("total", "vat"):
        gv, pv = norm_field(field, gt), norm_field(field, pred)
        if gv and pv and any(abs(pv * 10 ** k - gv) < 0.01 for k in (-3, -2, -1, 1, 2, 3)):
            return "thousand/decimal separator"
        return "digits/amounts misread"
    if field in ("seller_tin", "receipt_number", "fiscal_sign", "fiscal_module"):
        gd, pd_ = norm_field(field, gt), norm_field(field, pred)
        return "digits missing/extra" if gd and pd_ and len(gd) != len(pd_) else "digits misread"
    if field == "datetime":
        return "date/time misread"
    ga, pa = unify_apostrophes(g).replace("ʻ", "").replace("ʼ", ""), unify_apostrophes(p).replace("ʻ", "").replace("ʼ", "")
    if norm_field(field, ga) == norm_field(field, pa):
        return "apostrophe"
    if norm_field(field, g.translate(CYR2LAT)) == norm_field(field, p.translate(CYR2LAT)):
        return "alphabet mixing (Latin/Cyrillic look-alikes)"
    return "text misread / wrong span"


def _qr_only(r, gt, label, engine):
    t = time.perf_counter()
    q = decode_qr(load_image(r["path"]))
    gq = ((gt or {}).get("qr") or {}).get("raw")
    ok = bool(q["raw"]) and (gq is None or q["raw"].strip() == gq.strip())
    return {"config": label, "engine": engine, "image": r["image"], "receipt_id": r["receipt_id"],
            "seller": r["seller"], "lang": r.get("lang", ""), "conditions": ";".join(r["conditions"]),
            "seconds": time.perf_counter() - t, "qr_plain": q["plain_success"] and ok, "qr_final": q["decoded"] and ok}


def evaluate(cfg, rows, engine, pre, post, cache_dir, label):
    agg = defaultdict(float)
    per_image, errors = [], []
    for r in rows:
        gt, gt_text = load_gt(cfg, r["receipt_id"])
        if "partial" in r["conditions"]:
            # lower half of a receipt (totals + QR close-up): counts only for the QR decode rate
            per_image.append(_qr_only(r, gt, label, engine))
            continue
        try:
            out = process(load_image(r["path"]), cfg, engine=engine, preprocess=pre, postprocess=post, cache_dir=cache_dir)
        except Exception:
            traceback.print_exc()
            continue
        res = out["result"]
        rec = {"config": label, "engine": engine, "image": r["image"], "receipt_id": r["receipt_id"],
               "seller": r["seller"], "lang": r.get("lang", ""), "conditions": ";".join(r["conditions"]),
               "seconds": out["timings"]["total"], "consistent": out["consistent"]}
        if gt_text and not is_text_source(r["image"], gt):
            ce, cn, we, wn = text_counts(gt_text, out["text"], cfg["eval"]["lowercase"])
            rec.update(char_err=ce, char_n=cn, word_err=we, word_n=wn)
        if gt:
            m = field_matches(gt, res)
            rec.update({f"field_{k}": v for k, v in m.items()})
            rec["field_acc"] = sum(m.values()) / len(m) if m else None
            tp, npred, ngt = item_counts(gt.get("items", []), res["items"])
            rec.update(item_tp=tp, item_pred=npred, item_gt=ngt, item_f1=prf(tp, npred, ngt)[2])
            for f, ok in m.items():
                if not ok:
                    errors.append({"config": label, "engine": engine, "image": r["image"], "conditions": ";".join(r["conditions"]),
                                   "field": f, "gt": gt.get(f), "pred": res.get(f),
                                   "cause": classify_error(f, gt.get(f), res.get(f), gt)})
            gq = (gt.get("qr") or {}).get("raw")
        else:
            gq = None
        if r["has_qr"]:
            ok_raw = (lambda raw: bool(raw) and (gq is None or raw.strip() == gq.strip()))
            rec["qr_plain"] = res["qr"]["plain_success"] and ok_raw(res["qr"]["raw"])
            rec["qr_final"] = res["qr"]["decoded"] and ok_raw(res["qr"]["raw"])
        per_image.append(rec)
    return per_image, errors


def summarize(df):
    def s(col):
        return df[col].sum() if col in df else 0
    tp, npred, ngt = s("item_tp"), s("item_pred"), s("item_gt")
    qr = df[df["qr_final"].notna()] if "qr_final" in df else df.iloc[0:0]
    return pd.Series({
        "images": len(df),
        "CER %": 100 * s("char_err") / s("char_n") if s("char_n") else None,
        "WER %": 100 * s("word_err") / s("word_n") if s("word_n") else None,
        "field acc %": 100 * df["field_acc"].mean() if "field_acc" in df and df["field_acc"].notna().any() else None,
        "item F1 %": 100 * prf(tp, npred, ngt)[2] if ngt or npred else None,
        "QR plain %": 100 * qr["qr_plain"].astype(float).mean() if len(qr) else None,
        "QR final %": 100 * qr["qr_final"].astype(float).mean() if len(qr) else None,
        "consistent %": 100 * df["consistent"].astype(float).mean(),
        "sec/receipt": df["seconds"].mean(),
    })


def qr_rates(df):
    """QR decode rate per photo type, and per receipt: a receipt counts as decoded when any of its
    real photos (whole receipt or QR close-up) decodes, as when a user takes a second photo."""
    rows = []
    for (engine, config), d in df[df["qr_final"].notna()].groupby(["engine", "config"], sort=False):
        kind = d["conditions"].map(lambda c: "synthetic" if "synthetic" in c else ("close-up" if "partial" in c else "whole"))
        real = d[kind != "synthetic"]
        rows.append({"engine": engine, "config": config,
                     "whole photo %": 100 * d[kind == "whole"]["qr_final"].astype(float).mean(),
                     "QR close-up %": 100 * d[kind == "close-up"]["qr_final"].astype(float).mean(),
                     "per receipt (any real photo) %": 100 * real.groupby("receipt_id")["qr_final"].max().astype(float).mean()})
    return pd.DataFrame(rows).set_index(["engine", "config"]) if rows else pd.DataFrame()


def _real_whole(df):
    return df[~df["conditions"].str.contains("synthetic|partial", regex=True)]


def _metrics(d):
    tp, npred, ngt = d["item_tp"].sum(), d["item_pred"].sum(), d["item_gt"].sum()
    out = {"field acc %": 100 * d["field_acc"].mean(), "item F1 %": 100 * prf(tp, npred, ngt)[2],
           "consistent %": 100 * d["consistent"].astype(float).mean()}
    if "char_n" in d and d["char_n"].sum():
        out["CER %"] = 100 * d["char_err"].sum() / d["char_n"].sum()
        out["WER %"] = 100 * d["word_err"].sum() / d["word_n"].sum()
    return out


def confidence_intervals(df, n_boot=1000, seed=0):
    """Resample whole receipts (all photos of a receipt together) with replacement; report the
    2.5 / 97.5 percentiles. With ~16 test receipts the intervals are wide: that is the point."""
    import numpy as np

    rng = np.random.default_rng(seed)
    rows = []
    for (engine, config), d in _real_whole(df[df["config"] == "pre_post"]).groupby(["engine", "config"], sort=False):
        groups = [g for _, g in d.groupby("receipt_id")]
        point = _metrics(d)
        boots = {k: [] for k in point}
        for _ in range(n_boot):
            sample = pd.concat([groups[i] for i in rng.integers(0, len(groups), len(groups))])
            for k, v in _metrics(sample).items():
                boots[k].append(v)
        row = {"engine": engine, "receipts": len(groups)}
        for k, v in point.items():
            lo, hi = np.percentile([b for b in boots[k] if b == b], [2.5, 97.5])
            row[k] = f"{v:.1f} [{lo:.1f}–{hi:.1f}]"
        rows.append(row)
    return pd.DataFrame(rows).set_index("engine") if rows else pd.DataFrame()


def per_seller(df):
    d = _real_whole(df[df["config"] == "pre_post"])
    rows = []
    for (engine, seller), g in d.groupby(["engine", "seller"], sort=False):
        rows.append({"engine": engine, "seller": seller, "photos": len(g), **{k: round(v, 1) for k, v in _metrics(g).items()}})
    return pd.DataFrame(rows).set_index(["engine", "seller"]) if rows else pd.DataFrame()


def md(df, floatfmt=".1f"):
    return df.to_markdown(floatfmt=floatfmt) if len(df) else "_no data_"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default=None)
    ap.add_argument("--split", default="test", choices=["dev", "test", "holdout", "holdout3", "all"])
    ap.add_argument("--engines", nargs="*", default=None)
    ap.add_argument("--ablation", action="store_true")
    ap.add_argument("--ablation-split", default="dev")
    ap.add_argument("--out", default=None, help="reports folder (default: eval.reports_dir from the config)")
    args = ap.parse_args()

    cfg = load_config(args.config)
    out_dir = ROOT / (args.out or cfg["eval"]["reports_dir"])
    out_dir.mkdir(parents=True, exist_ok=True)
    cache = ROOT / cfg["eval"]["cache_dir"]
    rows = rows_for(cfg, args.split)
    engines = args.engines or cfg["eval"]["engines"]
    print(f"{len(rows)} images in split '{args.split}'")

    all_imgs, all_err = [], []
    for engine in engines:
        for name, c in cfg["eval"]["configs"].items():
            print(f"-> {engine} / {name}", flush=True)
            imgs, errs = evaluate(cfg, rows, engine, c["preprocess"], c["postprocess"], cache, name)
            all_imgs += imgs
            all_err += errs
    df = pd.DataFrame(all_imgs)
    df.to_csv(out_dir / "per_image.csv", index=False)
    pd.DataFrame(all_err).to_csv(out_dir / "errors.csv", index=False)

    main_tbl = df.groupby(["engine", "config"], sort=False).apply(summarize, include_groups=False)
    main_tbl.to_csv(out_dir / "main_table.csv")

    field_cols = [f"field_{f}" for f in FIELDS if f"field_{f}" in df]
    per_field = (100 * df.groupby(["engine", "config"], sort=False)[field_cols].mean()).rename(columns=lambda c: c[6:]) if field_cols else pd.DataFrame()
    per_field.to_csv(out_dir / "per_field.csv")

    cond = df.assign(condition=df["conditions"].str.split(";")).explode("condition")
    by_cond = cond.groupby(["engine", "config", "condition"], sort=False).apply(summarize, include_groups=False)
    by_cond.to_csv(out_dir / "by_condition.csv")
    by_lang = df.groupby(["engine", "config", "lang"], sort=False).apply(summarize, include_groups=False)
    by_lang.to_csv(out_dir / "by_language.csv")

    parts = [f"# Results ({args.split} split, {df['image'].nunique()} images, "
             f"{df['receipt_id'].nunique()} receipts, {df['seller'].nunique()} sellers)\n",
             "## Engines × configurations\n", md(main_tbl),
             "\n\n## Field accuracy, %\n", md(per_field),
             "\n\n## By shooting condition\n", md(by_cond),
             "\n\n## By language\n", md(by_lang),
             "\n\n## QR decoded per photo and per receipt\n", md(qr_rates(df)),
             "\n\n## 95 % confidence intervals (bootstrap over receipts, real whole-receipt photos, "
             "pre + post)\n", md(confidence_intervals(df)),
             "\n\n## Per seller (real whole-receipt photos, pre + post)\n", md(per_seller(df))]

    if args.ablation:
        eng = cfg["eval"]["ablation_engine"]
        arows = rows_for(cfg, args.ablation_split)
        steps = cfg["eval"]["ablation_steps"]
        variants = [("none (raw image)", {s: False for s in steps})]
        for k in range(1, len(steps) + 1):
            variants.append(("+ " + steps[k - 1], {s: i < k for i, s in enumerate(steps)}))
        full = {s: cfg["preprocess"][s] for s in steps}
        for s in steps:
            if full[s]:
                variants.append((f"default without {s}", {**full, s: False}))
        ab = []
        (out_dir / "ablation_per_image.csv").unlink(missing_ok=True)
        for name, flags in variants:
            print(f"-> ablation: {name}", flush=True)
            imgs, _ = evaluate(with_overrides(cfg, flags), arows, eng, True, True, cache, name)
            d = pd.DataFrame(imgs)
            if len(d):
                ab.append(summarize(d).rename(name))
                d.assign(variant=name).to_csv(out_dir / "ablation_per_image.csv", mode="a", index=False,
                                              header=not (out_dir / "ablation_per_image.csv").exists())
        ab = pd.DataFrame(ab)
        ab.to_csv(out_dir / "ablation.csv")
        parts += [f"\n\n## Preprocessing ablation ({eng}, {args.ablation_split} split, post-processing on)\n", md(ab)]

    if all_err:
        e = pd.DataFrame(all_err)
        best = e[e["config"] == "pre_post"] if (e["config"] == "pre_post").any() else e
        parts += ["\n\n## Error causes (pre_post)\n", md(best.groupby(["engine", "cause"]).size().rename("count").to_frame(), ".0f"),
                  "\n\n## Error examples\n", md(best.head(40).set_index("image"), ".2f")]

    (out_dir / "results.md").write_text("\n".join(parts), encoding="utf-8")
    print(main_tbl.round(1).to_string())
    print(f"\nreports written to {out_dir}")


if __name__ == "__main__":
    main()
