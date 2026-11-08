import pytest

from receipt.metrics import cer, field_accuracy, field_matches, item_counts, prf, wer


def test_cer_basic():
    assert cer("abcd", "abcd") == 0
    assert cer("abcd", "abxd") == pytest.approx(0.25)          # 1 substitution / 4
    assert cer("abcd", "ab") == pytest.approx(0.5)             # 2 deletions / 4
    assert cer("ab", "abcdef") == pytest.approx(2.0)           # insertions can exceed 100 %


def test_cer_uses_normalization():
    assert cer("Toʻlov uchun jami", "TO'LOV  UCHUN JAMI") == 0


def test_wer_basic():
    assert wer("jami 32 000.00", "jami 32 000.00") == 0
    assert wer("jami 32 000.00", "jami 32 900.00") == pytest.approx(1 / 3)
    assert wer("a b c d", "a c d") == pytest.approx(0.25)


def test_field_accuracy_with_nulls():
    gt = {"total": 32000.0, "vat": 0.0, "seller_name": None, "datetime": "2026-11-04T13:47:26"}
    pred = {"total": "32 000,00", "vat": None, "seller_name": None, "datetime": "04-11-2026 13:47:26"}
    m = field_matches(gt, pred)
    assert m == {"total": True, "vat": False, "seller_name": True, "datetime": True}
    assert field_accuracy(gt, pred) == pytest.approx(0.75)


def test_items_f1():
    gt = [{"name": "Keks pishiriq", "quantity": 1, "price": 32000, "total": 32000},
          {"name": "Non", "quantity": 2, "price": 4000, "total": 8000}]
    pred = [{"name": "keks pishiriq", "quantity": "1,000", "price": "32 000,00", "total": "32 000.00"},
            {"name": "Non", "quantity": 2, "price": 4000, "total": 9000},       # wrong total
            {"name": "Extra", "quantity": 1, "price": 1, "total": 1}]
    tp, n_pred, n_gt = item_counts(gt, pred)
    assert (tp, n_pred, n_gt) == (1, 3, 2)
    p, r, f1 = prf(tp, n_pred, n_gt)
    assert p == pytest.approx(1 / 3) and r == pytest.approx(0.5) and f1 == pytest.approx(0.4)


def test_prf_empty():
    assert prf(0, 0, 0) == (1.0, 1.0, 1.0)
    assert prf(0, 2, 0)[2] == 0.0
