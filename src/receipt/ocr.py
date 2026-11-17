"""OCR engines behind one interface.

Every engine returns a list of lines in reading order:
    {"text": str, "conf": 0..1, "box": [x0, y0, x1, y1], "words": [{"text", "conf", "box"}]}
"""
import shutil

import cv2
import numpy as np

ENGINES = ("tesseract", "easyocr", "rapidocr", "hybrid")  # hybrid: rapidocr + tesseract (pipeline.py)
_easyocr_readers = {}
_rapidocr = {}


def _rgb(img):
    return cv2.cvtColor(img, cv2.COLOR_GRAY2RGB) if img.ndim == 2 else cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def _union(boxes):
    b = np.array(boxes)
    return [int(b[:, 0].min()), int(b[:, 1].min()), int(b[:, 2].max()), int(b[:, 3].max())]


def _make_line(words):
    words = sorted(words, key=lambda w: w["box"][0])
    return {
        "text": " ".join(w["text"] for w in words),
        "conf": float(np.mean([w["conf"] for w in words])),
        "box": _union([w["box"] for w in words]),
        "words": words,
    }


def _word_slope(w):
    """Slope (dy/dx) of a word's top edge, or None if its rotated box is too short to tell."""
    p = w.get("poly")
    if p is None:
        return None
    (x0, y0), (x1, y1) = p[0], p[1]  # top-left, top-right
    if x1 - x0 < 120:
        return None
    s = (y1 - y0) / (x1 - x0)
    return s if abs(s) < 0.2 else None


def local_slopes(words, window=300):
    """Text slope around every word: median slope of the long words within `window` px above and
    below. Crumpled receipts are curved, so the slope changes from top to bottom."""
    known = [((w["box"][1] + w["box"][3]) / 2, _word_slope(w)) for w in words]
    known = [(y, s) for y, s in known if s is not None]
    if len(known) < 5:
        return [0.0] * len(words)
    glob = float(np.median([s for _, s in known]))
    out = []
    for w in words:
        cy = (w["box"][1] + w["box"][3]) / 2
        near = [s for y, s in known if abs(y - cy) <= window]
        out.append(float(np.median(near)) if len(near) >= 3 else glob)
    return out


def group_into_lines(words):
    """Cluster word boxes into text lines.

    The vertical position of a word is measured along the local text slope (y - slope * x), so on
    a tilted or curved receipt a value on the right stays on the line of its label on the left
    instead of joining the next line."""
    if not words:
        return []
    slopes = local_slopes(words)
    levels = {}
    for w, s in zip(words, slopes):
        cx, cy = (w["box"][0] + w["box"][2]) / 2, (w["box"][1] + w["box"][3]) / 2
        levels[id(w)] = cy - s * cx
    heights = [max(w["box"][3] - w["box"][1] - abs(s) * (w["box"][2] - w["box"][0]), 1)
               for w, s in zip(words, slopes)]  # an axis-aligned box of tilted text is too tall
    tol = 0.5 * float(np.median(heights))
    words = sorted(words, key=lambda w: levels[id(w)])
    lines, cur, cur_y = [], [], None
    for w in words:
        cy = levels[id(w)]
        if cur and abs(cy - cur_y) > tol:
            lines.append(cur)
            cur = []
        cur.append(w)
        cur_y = float(np.mean([levels[id(x)] for x in cur]))
    lines.append(cur)
    return [_make_line(l) for l in lines]


def run_tesseract(img, cfg):
    import pytesseract

    tc = cfg["ocr"]["tesseract"]
    pytesseract.pytesseract.tesseract_cmd = tc.get("cmd") or shutil.which("tesseract") or "tesseract"
    d = pytesseract.image_to_data(
        _rgb(img), lang=tc["lang"],
        config=f"--oem {tc['oem']} --psm {tc['psm']} -c preserve_interword_spaces=1",
        output_type=pytesseract.Output.DICT,
    )
    groups = {}
    for i, text in enumerate(d["text"]):
        conf = float(d["conf"][i])
        if not text.strip() or conf < 0:
            continue
        key = (d["block_num"][i], d["par_num"][i], d["line_num"][i])
        x, y, w, h = d["left"][i], d["top"][i], d["width"][i], d["height"][i]
        groups.setdefault(key, []).append({"text": text.strip(), "conf": conf / 100, "box": [x, y, x + w, y + h]})
    lines = [_make_line(ws) for ws in groups.values()]
    return sorted(lines, key=lambda l: (l["box"][1] + l["box"][3]) / 2)


def run_easyocr(img, cfg):
    import easyocr

    ec = cfg["ocr"]["easyocr"]
    key = tuple(ec["langs"])
    if key not in _easyocr_readers:
        _easyocr_readers[key] = easyocr.Reader(list(key), gpu=ec.get("gpu", False), verbose=False)
    res = _easyocr_readers[key].readtext(_rgb(img), detail=1, paragraph=False)
    words = []
    for pts, text, conf in res:
        pts = np.array(pts)
        words.append({"text": text, "conf": float(conf), "poly": pts.tolist(),
                      "box": [int(pts[:, 0].min()), int(pts[:, 1].min()), int(pts[:, 0].max()), int(pts[:, 1].max())]})
    return group_into_lines(words)


def rapidocr_engine(params=None):
    """One RapidOCR instance per configuration (loading the ONNX models takes a second).
    params may name another recognition model: rec_model_path + rec_keys_path (relative to the project)."""
    from .config import ROOT

    params = dict(params or {})
    for k in ("rec_model_path", "rec_keys_path", "det_model_path"):
        if params.get(k):
            params[k] = str(ROOT / params[k])
    key = tuple(sorted(params.items()))
    if key not in _rapidocr:
        from rapidocr_onnxruntime import RapidOCR
        _rapidocr[key] = RapidOCR(**params)
    return _rapidocr[key]


def run_rapidocr(img, cfg):
    """PaddleOCR PP-OCRv4 models run through ONNX Runtime (RapidOCR): fast on CPU, strong on digits;
    its recognizer has no Cyrillic, so Cyrillic text comes out wrong."""
    res, _ = rapidocr_engine(cfg["ocr"].get("rapidocr", {}))(img if img.ndim == 3 else cv2.cvtColor(img, cv2.COLOR_GRAY2BGR))
    words = []
    for pts, text, conf in res or []:
        pts = np.array(pts)
        words.append({"text": text, "conf": float(conf), "poly": pts.tolist(),
                      "box": [int(pts[:, 0].min()), int(pts[:, 1].min()), int(pts[:, 0].max()), int(pts[:, 1].max())]})
    return group_into_lines(words)


def run_ocr(engine, img, cfg):
    if engine == "tesseract":
        return run_tesseract(img, cfg)
    if engine == "easyocr":
        return run_easyocr(img, cfg)
    if engine == "rapidocr":
        return run_rapidocr(img, cfg)
    raise ValueError(f"unknown OCR engine: {engine}")
