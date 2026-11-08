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
    lines, timings["ocr"], timings["ocr_cached"] = _ocr_cached(engine, pre["final"], cfg, cache_dir, key)

    t = time.perf_counter()
    if postprocess:
        lines = [{**l, "text": clean_line(l["text"])} for l in lines]
    fields, items, sources, used_lines = extract(lines, postprocess=postprocess)
    checks = reconcile(fields, items, qr_parsed["fields"], cfg)

    field_source = {k: "ocr" for k, v in fields.items() if v is not None}
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
