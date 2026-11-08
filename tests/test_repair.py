from receipt.extract import extract
from receipt.normalize import clean_line
from receipt.repair import agree, candidates, consensus, could_be_zero, repair_datetime, repair_item


def test_candidates_turn_confusable_digits_into_zero():
    c = candidates("24 888.66")
    assert c[24888.66] == 0
    assert c[24000.0] == 5
    assert 24000.0 in c and 12.0 not in c


def test_agree_picks_value_supported_by_other_copies():
    # real readings of one receipt: To'lov uchun jami, Narx, Naqdsiz
    assert agree("24 888.66", ["24 880.68", "24 008 60"]) == 24000.0


def test_agree_needs_support_and_consensus_needs_two_votes():
    assert agree("8 933.33", ["1 234.00"]) is None
    assert consensus(["8 000.00", "8 609.60"]) == 8000.0   # Narx + Naqdsiz, total line unreadable
    assert consensus(["8 809.00"]) is None


def test_zero_and_dates():
    assert could_be_zero("8.") and could_be_zero("0.00") and not could_be_zero("15.00")
    assert repair_datetime("94-11-2226 21:93:56") == "2026-11-04T21:03:56"


def test_repair_item_keeps_arithmetic():
    item = {"quantity": 1.008, "price": 30008.68, "total": 30600.08,
            "_raw_qty": "1,008", "_raw_price": "30 008,68", "_raw_total": "30 600.08"}
    repair_item(item, receipt_total=30000.0, single=True)
    assert (item["quantity"], item["price"], item["total"]) == (1.0, 30000.0, 30000.0)


def test_extract_repairs_dotted_zero_receipt():
    text = """Tinda
ADHAMJON MAMADALIYEV ASKARALIYEVICH
Manzil Farg'ona viloyati ,
STIR/JSHSHR 31709886970015
Sana va vaqt 94-11-2226 21:93:56
1 Ikkinchi navli un
1,000 Kg X 24 000,00
Narx | 24 880.68
QQS siz 9
Naqd | 6
Naqdsiz 24 008 60
To'lov uchun jami
24 888.66
Jami QQS _ 8."""
    f, items, _, _ = extract([clean_line(l) for l in text.splitlines()], postprocess=True)
    assert f["total"] == 24000.0 and f["vat"] == 0.0 and f["payment"] == "card"
    assert f["datetime"] == "2026-11-04T21:03:56" and f["seller_name"] == "Tinda"
    assert [(i["quantity"], i["price"], i["total"]) for i in items] == [(1.0, 24000.0, 24000.0)]
