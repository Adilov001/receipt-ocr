"""Write draft ground truth (data/gt/<receipt_id>.json + .txt) from the pipeline output.

The drafts only save typing: open each one next to the photo, correct every
field and the full text by hand, then set "_status": "verified".
Existing files are never overwritten.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from receipt.config import ROOT, load_config  # noqa: E402
from receipt.dataset import load_meta  # noqa: E402
from receipt.pipeline import load_image, process  # noqa: E402

cfg = load_config()
gt_dir = ROOT / cfg["data"]["gt"]
gt_dir.mkdir(parents=True, exist_ok=True)

first = {}
for r in load_meta(cfg):
    # prefer the cleanest photo of each receipt
    if r["receipt_id"] not in first or "clean" in r["conditions"]:
        first[r["receipt_id"]] = r

for rid, r in sorted(first.items()):
    j, t = gt_dir / f"{rid}.json", gt_dir / f"{rid}.txt"
    if j.exists() and t.exists():
        continue
    print(f"{rid}: {r['image']}", flush=True)
    out = process(load_image(r["path"]), cfg, engine="tesseract", cache_dir=ROOT / cfg["eval"]["cache_dir"])
    res = out["result"]
    draft = {"_status": "draft", "_image": r["image"]}
    draft.update({k: v for k, v in res.items() if k != "qr"})
    draft["qr"] = {"raw": res["qr"]["raw"]} if res["qr"]["raw"] else ({"raw": "FILL_ME"} if r["has_qr"] else None)
    if not j.exists():
        j.write_text(json.dumps(draft, indent=2, ensure_ascii=False), encoding="utf-8")
    if not t.exists():
        t.write_text(out["text"] + "\n", encoding="utf-8")
print(f"drafts in {gt_dir}")
