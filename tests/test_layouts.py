"""Rules for the KFC and supermarket layouts (dev receipts r30-r33, chosen on dev only)."""
from receipt.config import load_config
from receipt.extract import extract
from receipt.normalize import parse_amount
from receipt.reconcile import MATCH, reconcile

# supermarket POS: "Narx: price*qty unit=total", apostrophe as thousands separator, "Chek raqami" next to FM
SUPERMARKET = """\
Smena raqami: 1176 Kassa raqami: 1
STIR: 305645847
Savdo Chek: 309 20-11-2026 13:56
1.SUV GAZLANMAGAN 1,5L ZAMIN
BC:4780044573864 Narx: 3'400.00*1Wt.=3'400.00so'm
MXIK: 02201001001163013 sh.J. QQS 12.00%=364.29
2.MUZ. VANIL STAKANCHIK 100GR IMKON PLYUS..
BC:4780011051975 Narx: 3'500.00*1Wt.=3'500.00so'm
MXIK: 02105001001000000 sh.J. QQS 12.00%=375.00
BANK CARD =6'900.00
Shaxsiy karta
QAYTIM =0.00 CHEGIRMA =0.00
QQS JAMI 12.0%=739.29 JAMI =6'900.00
FM raqami : LG420230605218 Chek raqami: 289471
Fiskal belgi: 045133448457 Seriya raqami: 100075
"""

# KFC: "CHEK-INVOYS, <shop>" header, combos under "kombo Nomi", "Umumiy to'lov"
KFC = """\
CHEK-INVOYS, KFC Файз
Telefon: +99878 129-7000, ISHGA TAKLIF QILAMIZ!
NAVBATDAGI BUYURTMA RAQAMI:
Buyurtma turi:
ZALDA
Sana: 19.11.2026 20:17:00
Kombo tarkibi
kombo Nomi summa
ЧИЗБУРГЕР ЛАНЧ БОКС 44000.00
12% 4714.29
КАРТОФЕЛЬ ФРИ МАЛЫЙ
COCA-COLA 0.4 +8800.00
kombo Nomi summa
ЧИЗБУРГЕР ЛАНЧ БОКС 44000.00
12% 4714.29
SPRITE 0.4 +8800.00
Umumiy to'lov: 88000.00
Sh. J. QQS: 12% 9428.57
BANKCARD (HUMO - UZCARD - VI 88000.00
4337********8482
Fiskal ma'lumot
Check raqami 10631
FM raqami: LG420211610349
Fiskal belgi: 072540327218
"""


def _run(text):
    f, items, _, _ = extract(text.splitlines())
    return f, items


def test_apostrophe_thousands_separator():
    assert parse_amount("6ʼ900.00") == 6900.0
    assert parse_amount("3'400.00") == 3400.0


def test_supermarket_layout():
    f, items = _run(SUPERMARKET)
    assert f["receipt_number"] == "289471"  # fiscal number, not the shop's "Savdo Chek: 309"
    assert f["seller_name"] is None  # register lines and items are not a shop name
    assert f["vat"] == 739.29  # the amount after "12.0%=", not the JAMI amount on the same line
    assert f["total"] == 6900.0
    assert f["payment"] == "card"
    assert [(i["name"], i["quantity"], i["price"], i["total"]) for i in items] == [
        ("SUV GAZLANMAGAN 1,5L ZAMIN", 1.0, 3400.0, 3400.0),
        ("MUZ. VANIL STAKANCHIK 100GR IMKON PLYUS", 1.0, 3500.0, 3500.0)]


def test_kfc_layout():
    f, items = _run(KFC)
    assert f["seller_name"] == "KFC Файз"
    assert f["receipt_number"] == "10631"
    assert f["total"] == 88000.0
    assert f["vat"] == 9428.57
    assert [(i["name"], i["quantity"], i["total"]) for i in items] == [("ЧИЗБУРГЕР ЛАНЧ БОКС", 1.0, 44000.0)] * 2


def test_masked_card_number_is_not_an_item():
    _, items = _run("Savdo\n4337******8482**82\nJami 10 000.00\n")
    assert items == []


def test_printed_minute_matches_qr_seconds():
    cfg = load_config()
    f, items = _run(KFC)
    checks = reconcile(f, items, {"datetime": "2026-11-19T20:17:51"}, cfg)
    assert [c["status"] for c in checks if c["check"] == "OCR ↔ QR: datetime"] == [MATCH]


def test_kfc_name_read_as_cyrillic_lookalikes():
    f, _ = _run("CHEK-INVOYS, КЕС.ЧИМГАН\n" + KFC.split("\n", 1)[1])
    assert f["seller_name"] == "KFC ЧИМГАН"


def test_combo_header_is_not_a_shop_name():
    # close-up photo without the top of the receipt: "Kombo tarkibi" must not become the seller
    f, _ = _run(KFC[KFC.index("Sana:"):])
    assert f["seller_name"] is None
