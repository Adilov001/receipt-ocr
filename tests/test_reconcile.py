"""The arithmetic and OCR <-> QR checks must be 100 % correct on correct input.

Every labelled receipt is fed through reconcile() with its ground truth: all checks must say
"match". Then single values are broken on purpose: the right check must say "mismatch",
and a missing value must give "no data", never a false "match".
"""
import copy
import glob
import json

import pytest

from receipt.config import ROOT, load_config
from receipt.qr import parse_qr
from receipt.reconcile import MATCH, MISMATCH, NO_DATA, is_consistent, reconcile

CFG = load_config()
GT = {p.split("/")[-1][:-5]: json.load(open(p, encoding="utf-8")) for p in sorted(glob.glob(str(ROOT / "data/gt/r*.json")))}


def _run(gt):
    qr = parse_qr((gt.get("qr") or {}).get("raw"), CFG["qr"]["param_map"])["fields"]
    return reconcile(gt, gt["items"], qr, CFG)


def _status(checks, name):
    return next(c["status"] for c in checks if c["check"] == name)


@pytest.mark.parametrize("rid", sorted(GT))
def test_every_labelled_receipt_is_consistent(rid):
    checks = _run(GT[rid])
    assert all(c["status"] in (MATCH, NO_DATA) for c in checks), [c for c in checks if c["status"] == MISMATCH]
    assert _status(checks, "Σ items = total") == MATCH
    assert is_consistent(checks)


def test_all_receipts_checked():
    assert len(GT) >= 29


def test_wrong_total_is_a_mismatch():
    gt = copy.deepcopy(GT["r02"])
    gt["total"] += 100
    checks = _run(gt)
    assert _status(checks, "Σ items = total") == MISMATCH and not is_consistent(checks)


def test_wrong_item_price_is_a_mismatch():
    gt = copy.deepcopy(GT["r04"])  # pharmacy, 2 items with fractional quantities
    gt["items"][1]["price"] = 19000.0
    assert _status(_run(gt), "item 2: qty × price = total") == MISMATCH


def test_missing_values_give_no_data_not_match():
    gt = copy.deepcopy(GT["r02"])
    gt["items"][0]["price"] = None
    gt["total"] = None
    checks = _run(gt)
    assert _status(checks, "item 1: qty × price = total") == NO_DATA
    assert _status(checks, "Σ items = total") == NO_DATA
    assert not is_consistent(checks)


def test_rounding_tolerance():
    # 16.873 m³ × 5 500 = 92 801.50, the receipt prints 92 800.00 (0.002 % off): still a match
    checks = _run(GT["r24"])
    assert _status(checks, "item 1: qty × price = total") == MATCH
    gt = copy.deepcopy(GT["r24"])
    gt["items"][0]["total"] = 93800.0  # 1 % off: a real error
    assert _status(_run(gt), "item 1: qty × price = total") == MISMATCH


def test_qr_comparison_per_parameter():
    gt = copy.deepcopy(GT["r02"])
    gt["fiscal_sign"] = "930222273400"  # last digit wrong
    checks = _run(gt)
    assert _status(checks, "OCR ↔ QR: fiscal_sign") == MISMATCH
    assert _status(checks, "OCR ↔ QR: receipt_number") == MATCH
    assert not is_consistent(checks)


def test_no_qr_means_no_qr_checks():
    gt = copy.deepcopy(GT["r02"])
    gt["qr"] = None
    assert not [c for c in _run(gt) if c["kind"] == "qr"]
