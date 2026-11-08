from receipt.config import load_config
from receipt.extract import extract
from receipt.normalize import clean_line
from receipt.reconcile import MATCH, MISMATCH, is_consistent, reconcile

# Text of a real receipt (the sample photo), as clean OCR would read it after deskew.
RECEIPT = """\
"SHIRIN TAOM" MChJ
Yur.Manzil Mustaqillik ko'chasi 130-uy
FARG'ONA VILOYATI, FARG'ONA SHAHRI
STIR/JSHSHR 31709886970015
Sana va vaqt 04-11-2026 13:47:26
Chek 36785
Savdo raqami 14994611046783
Savdo
1 Keks pishiriq
1,000 Kg X 32 000,00 32 000.00
QQS siz 0
MXIK 01905007001000000
--------------------------------
Naqd 0.00
Naqdsiz 32 000.00
Karta turi Shaxsiy
KONTAKSIZ OPERATSIYA
Sana 04-11-2026 13:47:22
Jami 32 000.00
To'lov uchun jami
32 000.00 UZS
Jami QQS 0.00
Terminal S/R 1170914994
FM ID NA000000006920
Fiskal imzo 352606397030
"""


def _run(text=RECEIPT, post=True):
    lines = [clean_line(l) if post else l for l in text.splitlines()]
    return extract(lines, postprocess=post)


def test_fields():
    f, items, src, _ = _run()
    assert f["seller_name"] == '"SHIRIN TAOM" MChJ'
    assert f["seller_tin"] == "31709886970015"
    assert f["datetime"] == "2026-11-04T13:47:26"
    assert f["receipt_number"] == "36785"
    assert f["fiscal_module"] == "NA000000006920"
    assert f["fiscal_sign"] == "352606397030"
    assert f["total"] == 32000.0
    assert f["vat"] == 0.0
    assert f["payment"] == "card"
    assert "FARG" in f["address"] and "130-uy" in f["address"]
    assert src["total"] > src["datetime"]


def test_items():
    _, items, _, _ = _run()
    assert items == [{"name": "Keks pishiriq", "quantity": 1.0, "price": 32000.0, "total": 32000.0, "_line": 9}]


def test_value_on_neighbour_line():
    f, *_ = _run("STIR/JSHSHR\n305123456\nFiskal imzo\n123456789012")
    assert f["seller_tin"] == "305123456"
    assert f["fiscal_sign"] == "123456789012"


def test_ocr_noise_fixed_by_postprocessing():
    noisy = RECEIPT.replace("32 000.00 UZS", "32 0O0.00 UZS").replace("NA000000006920", "NAOOO0000O6920")
    f, *_ = _run(noisy, post=True)
    assert f["total"] == 32000.0 and f["fiscal_module"] == "NA000000006920"


def test_reconcile():
    cfg = load_config()
    f, items, _, _ = _run()
    qr = {"fiscal_module": "NA000000006920", "receipt_number": "36785",
          "datetime": "2026-11-04T13:47:26", "fiscal_sign": "352606397039"}
    checks = reconcile(f, [{k: v for k, v in i.items() if k != "_line"} for i in items], qr, cfg)
    status = {c["check"]: c["status"] for c in checks}
    assert status["item 1: qty × price = total"] == MATCH
    assert status["Σ items = total"] == MATCH
    assert status["OCR ↔ QR: receipt_number"] == MATCH
    assert status["OCR ↔ QR: fiscal_sign"] == MISMATCH
    assert not is_consistent(checks)


def test_long_code_is_not_an_item():
    _, items, _, _ = _run("MXIK 0190500700100006x0\n1 Non\n2 x 4 000.00 8 000.00")
    assert [(i["name"], i["quantity"], i["total"]) for i in items] == [("Non", 2.0, 8000.0)]
