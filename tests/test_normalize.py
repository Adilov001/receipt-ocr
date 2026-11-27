import pytest

from receipt.normalize import (OKINA, TUTUQ, clean_line, fix_digits, fix_mixed_script, norm_field,
                               norm_text_for_metric, parse_amount, parse_datetime, parse_qty,
                               unify_apostrophes)


@pytest.mark.parametrize("s, expected", [
    ("12 500,00 soʻm", 12500.00),
    ("12 500,00 so'm", 12500.00),
    ("32 000.00", 32000.00),
    ("32 000.00 UZS", 32000.00),
    ("1 234 567,89 сўм", 1234567.89),
    ("1.234.567,89", 1234567.89),
    ("1,234,567.89", 1234567.89),
    ("5000 сум", 5000.0),
    ("0.00", 0.0),
    ("12'500.00", 12500.0),
    ("Jami: 7 800,50", 7800.5),
    ("", None),
    (None, None),
    ("abc", None),
])
def test_parse_amount(s, expected):
    assert parse_amount(s) == expected


def test_parse_qty_comma_decimal():
    assert parse_qty("1,000") == 1.0
    assert parse_qty("0,347") == 0.347
    assert parse_qty("2") == 2.0


@pytest.mark.parametrize("variant", ["'", "’", "‘", "`", "ʻ", "ʼ"])
def test_apostrophe_variants_unify(variant):
    assert unify_apostrophes(f"o{variant}zbek") == f"o{OKINA}zbek"
    assert unify_apostrophes(f"G{variant}ALLA") == f"G{OKINA}ALLA"
    assert unify_apostrophes(f"ta{variant}minot") == f"ta{TUTUQ}minot"


def test_mixed_script_words():
    assert fix_mixed_script("Tоshkent") == "Toshkent"     # Cyrillic о inside a Latin word
    assert fix_mixed_script("Тoшкент") == "Тошкент"       # Latin o inside a Cyrillic word
    assert fix_mixed_script("Toshkent") == "Toshkent"


def test_digit_lookalikes():
    assert fix_digits("32O0O.0O") == "32000.00"
    assert fix_digits("l2500") == "12500"
    assert fix_digits("Olma") == "Olma"                   # words are left alone


def test_clean_line():
    assert clean_line("To'lov  uchun  jami 32 0O0.00") == f"To{OKINA}lov uchun jami 32 000.00"


@pytest.mark.parametrize("s, expected", [
    ("04-11-2026 13:47:26", "2026-11-04T13:47:26"),
    ("04.11.2026 13:47", "2026-11-04T13:47:00"),
    ("2026-11-04 13:47:26", "2026-11-04T13:47:26"),
    ("20261104134726", "2026-11-04T13:47:26"),
    ("Sana va vaqt 04/11/2026 9:05:01", "2026-11-04T09:05:01"),
    ("99-99-2026 13:47", None),
    ("no date", None),
])
def test_parse_datetime(s, expected):
    assert parse_datetime(s) == expected


def test_metric_text_normalization():
    a = "Toʻlov  uchun jami\n------------\n\n32 000.00"
    b = "TO'LOV UCHUN JAMI\n32 000.00"
    assert norm_text_for_metric(a) == norm_text_for_metric(b)


def test_norm_field():
    assert norm_field("total", "32 000,00 so'm") == norm_field("total", 32000)
    assert norm_field("seller_tin", "STIR 123 456 789") == "123456789"
    assert norm_field("fiscal_module", "na000000006920") == "NA000000006920"
    assert norm_field("seller_name", '"ANVAR" MChJ') == norm_field("seller_name", "«Anvar» mchj")
    assert norm_field("address", None) is None


def test_digits_inside_words_become_letters():
    from receipt.normalize import clean_line
    assert clean_line("P0S versiyasi") == "POS versiyasi"
    assert clean_line("QQS s1z") == "QQS siz"
    assert clean_line("koʻchas1 130-uy") == "koʻchasi 130-uy"
    assert clean_line("1,000 Kg × 30 000.00") == "1,000 Kg x 30 000.00"
    # codes and numbers stay as they are
    assert clean_line("FM ID LG420211609580 Era POS v1.9.1 1Ikkinchi A0000000031010") == \
        "FM ID LG420211609580 Era POS v1.9.1 1Ikkinchi A0000000031010"


def test_label_words_are_snapped():
    from receipt.normalize import fix_label_words as f
    assert f("iskal imzo 352606397030") == "fiskal imzo 352606397030"  # the cut capital is unknown
    assert f("Operatstya raqani 21167") == "Operatsiya raqami 21167"
    assert f("minal 48050887") == "terminal 48050887"           # first letters lost at the edge
    assert f("sturiy taʼminot 3.5.5") == "dasturiy taʼminot 3.5.5"
    assert f("KONTAKSIZ OPERATSTYA") == "KONTAKSIZ OPERATSIYA"   # case style kept
    # real words, names and numbers are not touched
    assert f("1 Margarin 5 000.00") == "1 Margarin 5 000.00"
    assert f("Tinda ADHAMJON MAMADALIYEV") == "Tinda ADHAMJON MAMADALIYEV"
    assert f("Guruch Gilos Xurmo Aralashmalar") == "Guruch Gilos Xurmo Aralashmalar"


def test_apostrophe_restored_in_known_uzbek_words():
    from receipt.normalize import clean_line
    assert clean_line("Tolandi: 5000") == "Toʻlandi: 5000"
    assert clean_line("bo ldingiz!") == "boʻldingiz!"
    assert clean_line("Dasturiy ta ʼminot") == "Dasturiy taʼminot"
    assert clean_line("FARG ONA VILOYATI,") == "FARGʻONA VILOYATI,"
    assert clean_line("ANVARJON O G LI") == "ANVARJON O G LI"  # 3 pieces: not guessed


def test_comma_read_as_stop_after_address_words():
    from receipt.normalize import clean_line
    assert clean_line("Fargʻona shahri. Barkamol MFY.") == "Fargʻona shahri, Barkamol MFY,"
    assert clean_line("Jami. 5000") == "Jami. 5000"


def test_datetime_with_hour_colon_read_as_space():
    assert parse_datetime("Sana 04-11-2026 18 31:32") == "2026-11-04T18:31:32"
    assert parse_datetime("04-11-2026 18 31") is None  # no seconds: a space is not trusted
