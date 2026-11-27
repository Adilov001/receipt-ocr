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


def test_pharmacy_items_with_fractions():
    text = """1. Омиезо капс 20мг №30 (Комомес)
Ishlab chiqaruvchi: Комбитик
MK: 0108908001750981217EEbSuaNn5vOw
(10/30) x 16 000 = 5 333,33
sh. j. QQS (12%) 571,43
2. Аллохол таб №50
Ishlab chiqaruvchi: Бельмедпрепарат
(10/50) x 18 000 = 3 600
sh. j. QQS (12%) 385,71
Savdo: 8 933,33
sh. j. QQS: 957,14
To'landi: 8 933,33"""
    f, items, _, _ = _run(text)
    assert [(i["name"], i["quantity"], i["price"], i["total"]) for i in items] == [
        ("Омиезо капс 20мг №30 (Комомес)", 0.333, 16000.0, 5333.33),
        ("Аллохол таб №50", 0.2, 18000.0, 3600.0)]
    assert f["total"] == 8933.33 and f["vat"] == 957.14


def test_address_block_until_next_label():
    text = """ERA
Tinda
ADHAMJON MAMADALIYEV ASKARALIYEVICH
Manzil Farg'ona viloyati ,
Farg ona shahar , 64-
Barkamol MFyYangi asr
Yur,Manz1l ko chasi 130-uy
FARG'ONA VILOYATI,
FARG'ONA SHAHRI
STIR/JSHSHR 31709886970015"""
    f, *_ = _run(text)
    # all wrapped lines kept, a garbled "Yur" label still stops the block, the line that slid
    # onto the Yur row comes back, "Farg ona" (apostrophe read as a space) is joined
    assert f["address"] == "Fargʻona viloyati, Fargʻona shahar , 64-, Barkamol MFY Yangi asr, koʻchasi 130-uy"
    assert f["seller_name"] == "Tinda"


def test_label_merged_with_owner_name_is_not_address():
    text = """ERA
ERA
Manzil KIRGULI O'RAMCHASI
Farg'ona viloyati.
Hamkorlik MFY, Nizomiy
STIR/JSHSHR 312599814"""
    f, *_ = _run(text)
    assert f["address"] == "Fargʻona viloyati, Hamkorlik MFY, Nizomiy"  # "viloyati." comma read as a stop
    assert f["seller_name"] == "ERA"


def test_seller_printed_in_capitals_is_kept():
    # petrol station: the name is printed twice in capitals and there is no "Manzil" label
    text = """DIYOR NEFT PETROLEUM
DIYOR NEFT PETROLEUM
YANGI MARG'ILON YANGI OBOD MFY, BARKAMOL
AVLOD KO'CHASI, 34
STIR: 309031294"""
    f, *_ = _run(text)
    assert f["seller_name"] == "DIYOR NEFT PETROLEUM"
    assert f["address"].startswith("YANGI MARGʻILON")


def test_address_vocabulary_is_strict():
    from receipt.extract import correct_address_words as fix
    assert fix("Farg'ond shahar, koʻchas1") == "Fargʻona shahar, koʻchasi"
    assert fix("Yangiobod MFY, Konizar qishlo'gi") == "Yangiobod MFY, Konizar qishlo'gi"  # real words stay
