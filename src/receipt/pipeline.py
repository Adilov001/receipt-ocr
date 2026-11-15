"""End-to-end processing of one receipt image."""
import hashlib
import json
import time
from pathlib import Path

import cv2

from . import FIELDS
from .extract import extract
from .normalize import clean_line, norm_field
from .ocr import run_ocr
from .preprocess import preprocess as run_preprocess
from .qr import decode_qr, parse_qr
from .reconcile import is_consistent, reconcile

HYBRID = ("rapidocr", "tesseract")  # main engine, helper engine
CYRILLIC = set("абвгдеёжзийклмнопрстуфхцчшщъыьэюяўқғҳ")


def _cyrillic_share(text):
    letters = [c for c in text.lower() if c.isalpha()]
    return sum(c in CYRILLIC for c in letters) / max(len(letters), 1)


def _items_add_up(items, total):
    return bool(items) and total is not None and all(i.get("total") is not None for i in items) \
        and abs(sum(i["total"] for i in items) - total) <= 1.0


def merge_hybrid(main, helper, helper_text):
    """Fields from the main engine; a field it could not find is taken from the helper engine.
    Items: the list that adds up to the total; on Cyrillic receipts the helper's item names
    (the main engine's recognizer has no Cyrillic)."""
    (f1, it1, src1), (f2, it2, _) = main, helper
    fields = {k: (v if v is not None else f2.get(k)) for k, v in f1.items()}
    filled = [k for k, v in f1.items() if v is None and f2.get(k) is not None]
    items = it1
    if not _items_add_up(it1, fields.get("total")) and _items_add_up(it2, fields.get("total")):
        items = it2
    if _cyrillic_share(helper_text) > 0.2:
        # Cyrillic receipt: names and other text come from the helper engine
        for k in ("seller_name", "address"):
            if f2.get(k) is not None:
                fields[k] = f2[k]
        if items is it1 and it1 and len(it1) == len(it2):
            items = [{**a, "name": b["name"] or a["name"]} for a, b in zip(it1, it2)]
    return fields, items, src1, filled


def _ocr_cached(engine, img, cfg, cache_dir, key_extra):
    """OCR with an on-disk cache; the measured OCR time is cached too, so timings stay honest."""
    t = time.perf_counter()
    if not cache_dir:
        return run_ocr(engine, img, cfg), time.perf_counter() - t, False
    h = hashlib.sha1(img.tobytes() + json.dumps([engine, key_extra, cfg["ocr"][engine]], sort_keys=True).encode()).hexdigest()
    path = Path(cache_dir) / f"{h}.json"
    if path.exists():
        d = json.loads(path.read_text())
        return d["lines"], d["seconds"], True
    lines = run_ocr(engine, img, cfg)
    sec = time.perf_counter() - t
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"lines": lines, "seconds": sec}, ensure_ascii=False))
    return lines, sec, False


def process(img, cfg, engine="tesseract", preprocess=True, postprocess=True, cache_dir=None):
    """img: BGR numpy array. Returns the full result dict (see README for the JSON schema)."""
    timings = {}
    t0 = time.perf_counter()

    if preprocess:
        pre = run_preprocess(img, cfg)
    else:
        pre = {"final": img, "stages": {}, "info": {}}
    timings["preprocess"] = time.perf_counter() - t0

    t = time.perf_counter()
    qr = decode_qr(img, extra_images=[pre["final"]] if preprocess else [])
    qr_parsed = parse_qr(qr["raw"], cfg["qr"]["param_map"])
    timings["qr"] = time.perf_counter() - t

    key = dict(cfg["preprocess"]) if preprocess else "raw"
    engines = HYBRID if engine == "hybrid" else (engine,)
    runs = [_ocr_cached(e, pre["final"], cfg, cache_dir, key) for e in engines]
    timings["ocr"] = sum(r[1] for r in runs)
    timings["ocr_cached"] = all(r[2] for r in runs)

    t = time.perf_counter()
    extracted = []
    for run in runs:
        ls = run[0]
        if postprocess:
            ls = [{**l, "text": clean_line(l["text"])} for l in ls]
        extracted.append((ls, extract(ls, postprocess=postprocess)))
    lines = extracted[0][0]
    fields, items, sources, used_lines = extracted[0][1]
    filled_by_helper = []
    if engine == "hybrid":
        helper_lines, (hf, hi, hs, _) = extracted[1]
        fields, items, sources, filled_by_helper = merge_hybrid(
            (fields, items, sources), (hf, hi, hs), "\n".join(l["text"] for l in helper_lines))
    checks = reconcile(fields, items, qr_parsed["fields"], cfg)

    field_source = {k: ("ocr:" + HYBRID[1] if k in filled_by_helper else "ocr") for k, v in fields.items() if v is not None}
    if postprocess and cfg["postprocess"].get("fill_from_qr"):
        for field, qv in qr_parsed["fields"].items():
            if field in fields and norm_field(field, fields.get(field)) != norm_field(field, qv):
                fields[field] = qv
                field_source[field] = "qr"
    timings["extract"] = time.perf_counter() - t
    timings["total"] = timings["preprocess"] + timings["qr"] + timings["ocr"] + timings["extract"]

    result = {f: fields.get(f) for f in FIELDS}
    result["items"] = [{k: v for k, v in it.items() if not k.startswith("_")} for it in items]
    result["qr"] = {**qr_parsed, "decoded": qr["decoded"], "attempt": qr["attempt"],
                    "plain_success": qr["plain_success"]}

    return {
        "result": result,
        "checks": checks,
        "consistent": is_consistent(checks),
        "field_source": field_source,
        "sources": {f: used_lines[i]["box"] for f, i in sources.items()
                    if isinstance(used_lines[i], dict) and "box" in used_lines[i]},
        "item_sources": [used_lines[it["_line"]].get("box") for it in items],
        "lines": lines,
        "text": "\n".join(l["text"] for l in lines),
        "qr_polygon": qr["polygon"],
        "qr_polygon_on": qr["polygon_on"],
        "preprocessed": pre["final"],
        "stages": pre["stages"],
        "pre_info": pre["info"],
        "engine": engine,
        "timings": timings,
    }


def load_image(path):
    img = cv2.imread(str(path))
    if img is None:
        raise FileNotFoundError(path)
    return img
