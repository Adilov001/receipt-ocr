"""Create data/split.json: sellers are assigned to dev or test, never both."""
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from receipt.config import ROOT, load_config  # noqa: E402
from receipt.dataset import load_meta, make_split  # noqa: E402

cfg = load_config(sys.argv[1] if len(sys.argv) > 1 else None)
rows = load_meta(cfg)
split = make_split(rows, cfg["data"]["test_fraction"], cfg["data"]["seed"])
(ROOT / cfg["data"]["split"]).write_text(json.dumps(split, indent=2, ensure_ascii=False))

for name in ("dev", "test"):
    part = [r for r in rows if r["seller"] in split[name]]
    qr = sum(r["has_qr"] for r in part)
    conds = Counter(c for r in part for c in r["conditions"])
    print(f"{name}: {len(split[name])} sellers, {len({r['receipt_id'] for r in part})} receipts, "
          f"{len(part)} images, {qr} with QR | {dict(conds)}")
