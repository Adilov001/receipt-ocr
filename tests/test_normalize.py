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
