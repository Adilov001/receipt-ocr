"""Make synthetic shooting conditions from the real photos (we only had 15 paper receipts).

For every real photo two variants are written next to it and added to data/meta.csv:
  <name>_x1.jpg  shadow across the receipt + rotation      (synthetic;shadow;tilted)
  <name>_x2.jpg  faded print + blur + perspective + strong JPEG compression
                                                            (synthetic;faded;perspective)
A variant shares receipt_id and seller with its source photo, so it shares the
ground truth and always lands in the same split (no dev/test leakage).
Re-running is safe: existing variants are skipped.
"""
import csv
import sys
from pathlib import Path

import cv2
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from receipt.config import ROOT, load_config  # noqa: E402
from receipt.dataset import load_meta  # noqa: E402


def shadow_and_tilt(img, rng):
    h, w = img.shape[:2]
    # soft diagonal shadow: one side of the photo gets 40-55 % darker
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    a = rng.uniform(0, np.pi)
    d = (xx - w / 2) * np.cos(a) + (yy - h / 2) * np.sin(a)
    edge = 1 / (1 + np.exp(-d / (0.04 * max(h, w))))
    shade = 1 - rng.uniform(0.40, 0.55) * edge
    out = (img.astype(np.float32) * shade[..., None]).clip(0, 255).astype(np.uint8)
    angle = rng.choice([-1, 1]) * rng.uniform(4, 9)
    m = cv2.getRotationMatrix2D((w / 2, h / 2), angle, 1.0)
    return cv2.warpAffine(out, m, (w, h), borderMode=cv2.BORDER_REFLECT)


def faded_blur_perspective(img, rng):
    h, w = img.shape[:2]
    out = cv2.convertScaleAbs(img, alpha=0.55, beta=105)          # faded thermal print
    out = cv2.GaussianBlur(out, (0, 0), rng.uniform(1.2, 2.0))      # slight defocus
    j = 0.07
    src = np.float32([[0, 0], [w, 0], [w, h], [0, h]])
    dst = src + np.float32(rng.uniform(-j, j, (4, 2)) * [w, h])
    out = cv2.warpPerspective(out, cv2.getPerspectiveTransform(src, dst), (w, h), borderMode=cv2.BORDER_REFLECT)
    ok, buf = cv2.imencode(".jpg", out, [cv2.IMWRITE_JPEG_QUALITY, 35])
    return cv2.imdecode(buf, cv2.IMREAD_COLOR)


VARIANTS = [("x1", shadow_and_tilt, ["shadow", "tilted"]),
            ("x2", faded_blur_perspective, ["faded", "perspective"])]


def main():
    cfg = load_config()
    images = ROOT / cfg["data"]["images"]
    meta_path = ROOT / cfg["data"]["meta"]
    rows = load_meta(cfg)
    known = {r["image"] for r in rows}
    new = []
    for i, r in enumerate(r for r in rows if "synthetic" not in r["conditions"]):
        img = cv2.imread(str(images / r["image"]))
        for k, (tag, fn, conds) in enumerate(VARIANTS):
            name = f"{Path(r['image']).stem}_{tag}.jpg"
            if name in known:
                continue
            rng = np.random.default_rng(10 * i + k)  # fixed seed: same variants on every run
            cv2.imwrite(str(images / name), fn(img, rng), [cv2.IMWRITE_JPEG_QUALITY, 92])
            c = ["synthetic"] + sorted((set(r["conditions"]) - {"clean"}) | set(conds))
            new.append([name, r["receipt_id"], r["seller"], r["lang"], ";".join(c), int(r["has_qr"])])
    with meta_path.open("a", newline="") as f:
        csv.writer(f).writerows(new)
    print(f"added {len(new)} synthetic images; dataset now has {len(known) + len(new)}")


if __name__ == "__main__":
    main()
