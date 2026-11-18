"""Normalization rules shared by post-processing and evaluation.

Post-processing (clean_line, parse_amount, ...) repairs OCR output.
Metric normalization (norm_text_for_metric, norm_field) puts ground truth and
prediction into one canonical form before comparing them; it is applied to
both sides identically and is the single place these rules are defined.
"""
import re
import unicodedata
from datetime import datetime

# ' ’ ‘ ` ʻ ʼ ´
APOSTROPHES = "'’‘`ʻʼ´"
OKINA = "ʻ"  # used in oʻ, gʻ
TUTUQ = "ʼ"  # tutuq belgisi (separator sign)
_APOS_RE = re.compile("[" + re.escape(APOSTROPHES) + "]")

_CYR = "АВЕКМНОРСТХаеорсухіј"
_LAT = "ABEKMHOPCTXaeopcyxij"
CYR2LAT = str.maketrans(_CYR, _LAT)
LAT2CYR = str.maketrans(_LAT, _CYR)

DIGIT_FIX = str.maketrans("OoОоlI|", "0000111")

SEPARATOR_RE = re.compile(r"^[\s\-=*_~.#+]{3,}$")
_CURRENCY_RE = re.compile(r"(so[ʻʼ'`’‘]?m|сўм|сум|sum|uzs)\.?", re.I)

# Amount as printed on receipts: 32 000.00 / 12 500,00 / 32000 / 1'500.00
AMOUNT_RE = re.compile(r"\d{1,3}(?:[  ']\d{3})+(?:[.,]\d{1,2})?|\d+(?:[.,]\d{1,2})?")


def unify_apostrophes(text):
    """oʻ/gʻ get U+02BB, every other apostrophe becomes the tutuq U+02BC."""
    if not text:
        return text

    def repl(m):
        i = m.start()
        prev = text[i - 1] if i else ""
        return OKINA if prev in "oOgG" else TUTUQ

    return _APOS_RE.sub(repl, text)


def _is_cyr(ch):
    return "Ѐ" <= ch <= "ӿ"


def fix_mixed_script(word):
    """In a word that mixes alphabets, convert look-alike letters to the majority alphabet."""
    cyr = sum(_is_cyr(c) for c in word)
    lat = sum(c.isascii() and c.isalpha() for c in word)
    if not cyr or not lat:
        return word
    return word.translate(CYR2LAT if lat >= cyr else LAT2CYR)


def fix_digits(token):
    """O→0, l→1 etc. in tokens that are mostly digits (amounts, codes)."""
    alnum = [c for c in token if c.isalnum()]
    digits = sum(c.isdigit() for c in alnum)
    if digits and len(alnum) >= 2 and digits / len(alnum) >= 0.5:
        return token.translate(DIGIT_FIX)
    return token


_L = r"[^\W\d_]"  # any letter


def fix_letters(word):
    """Digits read inside a word are letters: 'p0s' -> 'pos', 's1z' -> 'siz', 'koʻchas1' -> 'koʻchasi'.
    Only a 0 / 1 between two letters, or a final 1 after 4+ letters; codes (LG420211609580, v1.9.1)
    and numbers are not touched."""
    def to(letter):  # same case as the letter before it
        return lambda m: letter.upper() if m.group(1).isupper() else letter

    word = re.sub(rf"({_L})0(?={_L})", lambda m: m.group(1) + to("o")(m), word)
    word = re.sub(rf"({_L})1(?={_L})", lambda m: m.group(1) + to("i")(m), word)
    return re.sub(rf"(?<={_L}{{3}})({_L})1$", lambda m: m.group(1) + to("i")(m), word)


# Fixed label words of Uzbek fiscal receipts (printed by the fiscal module / terminal software,
# the same on every receipt of a layout). No shop, product or address names.
LABEL_WORDS = """sana vaqt chek savdo raqami narx qqs siz mxik naqd naqdsiz karta turi shaxsiy kontaksiz
operatsiya terminal savdogar versiyasi uzcard humo javob kodi toʻlov uchun jami dasturiy taʼminot fiskal
imzo xaridning miqdorida keshbek olish huquqiga boʻldingiz manzil avtorizatsiya ishlab chiqaruvchi
toʻlandi kassir sotuvchi smena pozitsiyalar kartasi tasdiqlanadi""".split()
_LABEL_KEYS = {re.sub(r"[ʻʼ'`’‘]", "", w): w for w in LABEL_WORDS}


def _like(word, template):
    """Give `template` the case style of `word` (UPPER, Title or lower)."""
    if word.isupper():
        return template.upper()
    return template[0].upper() + template[1:] if word[:1].isupper() else template


def fix_label_words(line):
    """Snap OCR near-misses of receipt label words: one wrong letter in 5+ letter words (two in 8+):
    'iskal' -> 'Fiskal', 'operatstya' -> 'operatsiya'; and, for the first word of a line only, up to
    3 letters lost at the receipt's left edge: 'minal' -> 'Terminal', 'sturiy' -> 'Dasturiy'."""
    from rapidfuzz.distance import Levenshtein

    words = line.split(" ")
    for i, w in enumerate(words):
        core = re.sub(r"[^\w ʻʼ'`’‘]", "", w)
        k = re.sub(r"[ʻʼ'`’‘]", "", core).casefold()
        if len(k) < 4 or not k.isalpha() or k in _LABEL_KEYS:
            continue
        best = min(_LABEL_KEYS, key=lambda v: Levenshtein.distance(k, v))
        d = Levenshtein.distance(k, best)
        ok = len(k) >= 5 and d <= (2 if len(k) >= 8 else 1) and abs(len(best) - len(k)) <= 1
        if not ok and i == 0:  # left edge cut: a label word that lost 1-3 leading letters
            tails = [v for v in _LABEL_KEYS if v.endswith(k) and 1 <= len(v) - len(k) <= 3]
            if len(tails) == 1:
                best, ok = tails[0], True
        if ok:
            words[i] = w.replace(core, _like(core, _LABEL_KEYS[best]))
    return " ".join(words)


def clean_line(text):
    text = unicodedata.normalize("NFC", text)
    text = unify_apostrophes(text)
    text = re.sub(r"(?<=[\d\s])×(?=[\s\d])", "x", text)  # look-alike multiplication sign
    words = [fix_letters(fix_digits(fix_mixed_script(w))) for w in text.split()]
    return fix_label_words(" ".join(words))


def is_separator(text):
    return bool(SEPARATOR_RE.match(text or ""))


def parse_number(s, ndigits=2):
    """'12 500,00 soʻm' -> 12500.0, '1,000' -> 1.0, '1.234.567,89' -> 1234567.89."""
    if s is None:
        return None
    if isinstance(s, (int, float)):
        return round(float(s), ndigits)
    t = _CURRENCY_RE.sub("", unify_apostrophes(str(s)))
    t = re.sub(r"[\s  'ʼʻ]", "", t)
    m = re.search(r"-?\d[\d.,]*", t)
    if not m:
        return None
    num = m.group().rstrip(".,")
    if "," in num and "." in num:
        dec = "," if num.rfind(",") > num.rfind(".") else "."
        num = num.replace("." if dec == "," else ",", "").replace(dec, ".")
    elif num.count(",") > 1 or num.count(".") > 1:
        num = num.replace("," if num.count(",") > 1 else ".", "")
    else:
        num = num.replace(",", ".")
    try:
        return round(float(num), ndigits)
    except ValueError:
        return None


def parse_amount(s):
    return parse_number(s, 2)


def parse_qty(s):
    return parse_number(s, 3)


def naive_number(s):
    """Baseline parser without post-processing: drop spaces, comma as decimal point."""
    try:
        return float(str(s).replace(" ", "").replace(",", "."))
    except (TypeError, ValueError):
        return None


_DT_PATTERNS = [
    (re.compile(r"(\d{2})[.\-/ ](\d{2})[.\-/ ](\d{4})[ T,]*(\d{1,2})[:.](\d{2})(?:[:.](\d{2}))?"), "dmy"),
    (re.compile(r"(\d{4})[.\-/](\d{2})[.\-/](\d{2})[ T,]*(\d{1,2})[:.](\d{2})(?:[:.](\d{2}))?"), "ymd"),
    (re.compile(r"(?<!\d)(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})(?!\d)"), "ymd"),
]


def parse_datetime(s):
    """Any receipt/QR date-time -> 'YYYY-MM-DDThh:mm:ss' or None."""
    if not s:
        return None
    for rx, order in _DT_PATTERNS:
        for m in rx.finditer(str(s)):
            g = m.groups()
            y, mo, d = (g[2], g[1], g[0]) if order == "dmy" else (g[0], g[1], g[2])
            try:
                dt = datetime(int(y), int(mo), int(d), int(g[3]), int(g[4]), int(g[5] or 0))
            except ValueError:
                continue
            return dt.strftime("%Y-%m-%dT%H:%M:%S")
    return None


# ---------------------------------------------------------------- metric normalization

def _norm_numbers(line):
    """Number normalization of the spec (4.5): no spaces between digit groups, the decimal comma
    becomes a point: "24 000,00" -> "24000.00", "1,000 Kg" -> "1.000 Kg"."""
    line = re.sub(r"(?<=\d)[ \u00a0](?=\d{3}(?!\d))", "", line)
    return re.sub(r"(?<=\d),(?=\d)", ".", line)


def norm_text_for_metric(text, lowercase=True):
    """Canonical full text for CER/WER, applied to the label and to the OCR text alike:
    NFC, unified apostrophes, single spaces, numbers normalized as in the spec (digit-group
    spaces removed, decimal comma -> point), no empty or separator-only lines."""
    text = unify_apostrophes(unicodedata.normalize("NFC", text or ""))
    lines = []
    for line in text.splitlines():
        line = _norm_numbers(" ".join(line.split()))
        if line and not is_separator(line):
            lines.append(line.lower() if lowercase else line)
    return "\n".join(lines)


AMOUNT_FIELDS = {"vat", "total"}
DIGIT_FIELDS = {"seller_tin", "receipt_number", "fiscal_sign"}
TEXT_FIELDS = {"seller_name", "address"}


def norm_name(s):
    s = unify_apostrophes(unicodedata.normalize("NFC", str(s))).casefold()
    s = re.sub(r"[\"«»“”„.,;:()]", " ", s)
    s = re.sub(r"-\s+", "-", s)  # a line break after "64-" in a wrapped address
    return " ".join(s.split())


def norm_field(field, value):
    if value is None or value == "":
        return None
    if field in AMOUNT_FIELDS:
        return parse_amount(value)
    if field == "datetime":
        return parse_datetime(value) or str(value)
    if field in DIGIT_FIELDS:
        return re.sub(r"\D", "", str(value)) or None
    if field == "fiscal_module":
        return re.sub(r"[^A-Z0-9]", "", str(value).upper()) or None
    if field == "payment":
        return str(value).strip().lower()
    return norm_name(value)


def norm_item(item):
    return (
        norm_name(item.get("name") or ""),
        parse_qty(item.get("quantity")),
        parse_amount(item.get("price")),
        parse_amount(item.get("total")),
    )
