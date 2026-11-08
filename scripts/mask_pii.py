"""Black out personal data on receipt photos before they go into the dataset.

    python scripts/mask_pii.py SRC.jpg DST.jpg

Masked: the cardholder name printed under the card type (UZCARD/HUMO/VISA) and
the names after "Sotuvchi"/"Kassir" (pharmacy staff). Card numbers are already
masked by the terminal (561468******8721).

How: the photo is preprocessed and read with Tesseract, the name lines are found
on the straightened receipt, and their boxes are mapped back to the original
photo with a homography found by SIFT feature matching.
Always check the result by eye; --box x0,y0,x1,y1 adds a manual box (original pixels).
"""
import argparse
import re
import sys
from pathlib import Path

import cv2
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from receipt.config import load_config  # noqa: E402
from receipt.ocr import run_tesseract  # noqa: E402
from receipt.preprocess import preprocess  # noqa: E402

CARD_RE = re.compile(r"UZ ?CAR|HUMO|VISA|MASTER", re.I)
STOP_RE = re.compile(r"^\s*(Jami|Javob|Operatsiya|AID|Avtor)", re.I)
STAFF_RE = re.compile(r"(Sotuvchi|Kassir)", re.I)


def name_boxes(lines):
    """Boxes (on the preprocessed image) of lines holding personal names."""
    boxes = []
    for i, l in enumerate(lines):
        if STAFF_RE.search(l["text"]):
            boxes.append(l["box"])
        if CARD_RE.search(l["text"]):
            for nxt in lines[i + 1:i + 3]:
                if STOP_RE.search(nxt["text"]) or re.search(r"\d{3}", nxt["text"]):
                    break
                boxes.append(nxt["box"])
    return boxes


def homography(src, dst):
    """Map points of `src` into `dst` (both grayscale)."""
    sift = cv2.SIFT_create(4000)
    s = 1200 / max(src.shape)
    d = 1200 / max(dst.shape)
    k1, d1 = sift.detectAndCompute(cv2.resize(src, None, fx=s, fy=s), None)
    k2, d2 = sift.detectAndCompute(cv2.resize(dst, None, fx=d, fy=d), None)
    matches = cv2.BFMatcher().knnMatch(d1, d2, k=2)
    good = [m for m, n in matches if m.distance < 0.75 * n.distance]
    if len(good) < 12:
        return None
    p1 = np.float32([k1[m.queryIdx].pt for m in good]) / s
    p2 = np.float32([k2[m.trainIdx].pt for m in good]) / d
    h, _ = cv2.findHomography(p1, p2, cv2.RANSAC, 8.0)
    return h


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--box", action="append", default=[], help="manual box x0,y0,x1,y1 in original pixels")
    args = ap.parse_args()

    cfg = load_config()
    img = cv2.imread(args.src)
    out = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    pre = preprocess(img, cfg)["final"]
    boxes = name_boxes(run_tesseract(pre, cfg))
    if boxes:
        h = homography(pre, gray)
        for x0, y0, x1, y1 in boxes:
            pad = 8
            pts = np.float32([[x0 - pad, y0 - pad], [x1 + pad, y0 - pad], [x1 + pad, y1 + pad], [x0 - pad, y1 + pad]])
            poly = cv2.perspectiveTransform(pts.reshape(-1, 1, 2), h).astype(np.int32) if h is not None else None
            if poly is not None:
                cv2.fillPoly(out, [poly], (0, 0, 0))
    for b in args.box:
        x0, y0, x1, y1 = map(int, b.split(","))
        cv2.rectangle(out, (x0, y0), (x1, y1), (0, 0, 0), -1)
    cv2.imwrite(args.dst, out, [cv2.IMWRITE_JPEG_QUALITY, 95])
    print(f"{Path(args.src).name}: {len(boxes)} auto + {len(args.box)} manual boxes")


if __name__ == "__main__":
    main()
