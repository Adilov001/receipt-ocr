"""QR decoding on a public dataset of Russian receipts (robustness check, not a reported metric).

    python scripts/eval_external_qr.py data/external/ru_receipts

Data: huggingface.co/datasets/cdek-ocr/receipt-ocr-ru (MIT), test split: test.jsonl + images/.
The extraction rules are written for Uzbek receipts and are not used here; only the QR decoder.
The spec allows public sets for debugging only, so these numbers are reported separately.

A Russian fiscal QR looks like  t=20250915T1531&s=727.13&fn=...&i=...&fp=...&n=1 :
a decode counts as *verified* when its sum `s` equals the labelled total (and its date, when
present, the labelled date), so a wrong decode cannot pass as a success.
"""
import json
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from urllib.parse import parse_qs

import cv2

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from receipt.qr import _failed_boxes, decode_qr  # noqa: E402


def _num(s):
    try:
        return round(float(str(s).replace(",", ".").replace(" ", "")), 2)
    except (TypeError, ValueError):
        return None


def _date(label):  # "15.09.25" -> "20250915"
    try:
        d, m, y = label.split(".")
        return f"{2000 + int(y) if len(y) == 2 else int(y):04d}{int(m):02d}{int(d):02d}"
    except (AttributeError, ValueError):
        return None


def check(args):
    root, rec = args
    path = Path(root) / "images" / Path(rec["image"]).name
    img = cv2.imread(str(path))
    if img is None:
        return {"image": path.name, "status": "unreadable image"}
    q = decode_qr(img)
    found = q["decoded"] or bool(_failed_boxes(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)))
    out = {"image": path.name, "found": found, "decoded": q["decoded"], "attempt": q["attempt"], "raw": q["raw"]}
    if not q["decoded"]:
        out["status"] = "found, not decoded" if found else "no QR found"
        return out
    p = {k: v[0] for k, v in parse_qs(q["raw"]).items()}
    total = _num((rec.get("total") or {}).get("text"))
    date = _date((rec.get("date") or {}).get("text"))
    s_ok = total is not None and _num(p.get("s")) == total
    t_ok = date is None or str(p.get("t", "")).startswith(date)
    if "s" not in p:
        out["status"] = "decoded, not fiscal"
    elif total is None:
        out["status"] = "decoded, no label to check"
    else:
        out["status"] = "decoded, verified" if s_ok and t_ok else "decoded, differs from label"
    return out


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "data/external/ru_receipts"
    recs = [json.loads(line) for line in open(Path(root) / "test.jsonl", encoding="utf-8")]
    with ProcessPoolExecutor(4) as ex:
        res = list(ex.map(check, [(root, r) for r in recs]))
    n = len(res)
    count = lambda st: sum(r["status"] == st for r in res)  # noqa: E731
    found = sum(bool(r.get("found")) for r in res)
    decoded = sum(bool(r.get("decoded")) for r in res)
    plain = sum(r.get("attempt") == "plain" for r in res)
    print(f"receipts: {n}")
    print(f"QR found (decoded or located): {found} ({100 * found / n:.1f} %)")
    print(f"QR decoded: {decoded} ({100 * decoded / n:.1f} %); on the first try: {plain}")
    for st in ("decoded, verified", "decoded, no label to check", "decoded, differs from label", "decoded, not fiscal",
               "found, not decoded", "no QR found", "unreadable image"):
        print(f"  {st:28s} {count(st)}")
    if found:
        print(f"decoded among receipts with a QR found: {100 * decoded / found:.1f} %")
    Path(root, "qr_results.json").write_text(json.dumps(res, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
