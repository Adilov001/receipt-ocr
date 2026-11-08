"""OCR engines behind one interface.

Every engine returns a list of lines in reading order:
    {"text": str, "conf": 0..1, "box": [x0, y0, x1, y1], "words": [{"text", "conf", "box"}]}
"""
import shutil

import cv2
import numpy as np

ENGINES = ("tesseract", "easyocr")
_easyocr_readers = {}


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


def group_into_lines(words):
    """Cluster word boxes into text lines by vertical center."""
    if not words:
        return []
    heights = [w["box"][3] - w["box"][1] for w in words]
    tol = 0.5 * float(np.median(heights))
    words = sorted(words, key=lambda w: (w["box"][1] + w["box"][3]) / 2)
    lines, cur, cur_y = [], [], None
    for w in words:
        cy = (w["box"][1] + w["box"][3]) / 2
        if cur and abs(cy - cur_y) > tol:
            lines.append(cur)
            cur = []
        cur.append(w)
        cur_y = float(np.mean([(x["box"][1] + x["box"][3]) / 2 for x in cur]))
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
        words.append({"text": text, "conf": float(conf),
                      "box": [int(pts[:, 0].min()), int(pts[:, 1].min()), int(pts[:, 0].max()), int(pts[:, 1].max())]})
    return group_into_lines(words)


def run_ocr(engine, img, cfg):
    if engine == "tesseract":
        return run_tesseract(img, cfg)
    if engine == "easyocr":
        return run_easyocr(img, cfg)
    raise ValueError(f"unknown OCR engine: {engine}")
