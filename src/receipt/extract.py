"""Rule-based field extraction from OCR lines (Uzbek Latin/Cyrillic and Russian labels).

Each extractor finds a label line and looks for a value of the expected shape on
the same line first, then on neighbouring lines (right-aligned values on tilted
or crumpled receipts often land one line up or down).
Returns (fields, items, sources) where sources[field] = index of the OCR line used.
"""
import re

from .normalize import (AMOUNT_RE, is_separator, naive_number, parse_amount, parse_datetime,
                        parse_qty, unify_apostrophes)
from .repair import agree, consensus, could_be_zero, repair_datetime, repair_item

A = "[ʻʼ'`’‘]?"  # optional apostrophe of any kind

L = {
    "tin": re.compile(r"\b(stir|stia|inn|инн|стир|jshshr|жшшир|pinfl)\b", re.I),  # "STIA": OCR misread (dev r35)
    "datetime": re.compile(r"\b(sana|vaqt|дата|время|сана|вақт)\b", re.I),
    "receipt_number": re.compile(r"(^|\s)(chek|чек)(\s*(raqami|№|no\.?|#))?(?!\s*(turi|kodi|-?\s*invo))\b", re.I),
    "fiscal_sign": re.compile(r"(fiskal\s*(imzo|belgi|alomat)|фискал\w*\s*(признак|имзо|белги)|\bфп\b|\bfp\b|\bfb\s*:)", re.I),
    # fiscal receipt number printed as "RS:" (pharmacy); preferred over the shop's own "Chek:" counter
    "rs": re.compile(r"\brs\s*:", re.I),
    "fiscal_module": re.compile(r"(\bfm\b|\bфм\b|fiskal\s*modul|фискал\w*\s*модул|\bzfm\b)", re.I),
    "vat_total": re.compile(rf"(jami\s*q[qo0a][sz]\b|q[qo0]s\s*jami|итого\s*ндс|жами\s*ққс|ққс\s*жами|ндс\s*итого)", re.I),
    "vat": re.compile(r"\b(qqs|ндс|ққс)\b(?!\s*siz)", re.I),
    "total": [
        # "TOʻLOV UCHUN: 3590,00" (Korzinka) without "jami"
        re.compile(rf"to{A}lov\s*uchun(\s*jami)?|тўлов\s*учун(\s*жами)?", re.I),
        re.compile(rf"jami\s*to{A}lov|umumiy\s*to{A}lov|итого\s*к\s*оплате|к\s*оплате|всего\s*к\s*оплате", re.I),
        re.compile(rf"to{A}landi|тўланди|оплачено", re.I),
        re.compile(r"\b(итого|итог|всего|жами|общий|общая\s*сумма)\b(?!\s*(ндс|ққс))", re.I),  # "ОБЩИЙ" (OKA)
        re.compile(r"(?<!qqs )(?<!qqs)\bjami\b(?!\s*qqs)", re.I),  # not "QQS JAMI 12%=739.29" (VAT)
    ],
    "card": re.compile(r"(naqdsiz|cashless|plastik|bank\s*karta|bank\s*card|безнал|карт[аой]|uzcard|humo|нақдсиз)", re.I),
    "cash": re.compile(r"(\bnaqd\b(?!\s*siz)|наличн|\bнақд\b)", re.I),
    "address": re.compile(
        rf"(ko{A}ch|kuchasi|tuman|shahar|shahri|viloyat|mahalla|\bmfy\b|massiv|\buy\b|\bул\.|улиц|район|"
        rf"\bг\.|област|кўча|туман|шаҳ|вилоят|manzil|адрес|манзил)", re.I),
    "address_label": re.compile(r"^\s*(yur\.?\s*manzil|yuridik\s*manzil|manzil|адрес|манзил)\s*[:.]?\s*", re.I),
    "vat_free": re.compile(r"(q[q0o]s\s*siz|без\s*ндс|ққс\s*сиз)", re.I),
    "narx": re.compile(r"^\s*(narx|нарх|цена)\b", re.I),
    "org": re.compile(r"\b(mchj|xk|yatt|qk|aj|ooo|ооо|мчж|ип|чп|ао|ат|llc|ltd)\b|[\"«“]", re.I),
    # the fiscal receipt number, printed next to the FM; a shop's own counter ("Savdo Cheki: 309") is not it
    "receipt_number_fiscal": re.compile(r"(chek|check|чек)\s*raqam\w*", re.I),
    # register / shift / order lines at the top of a receipt (never the shop name)
    "service": re.compile(r"\b(smena|kassa\s*raqami|navbatdagi|buyurtma|kassir)\b", re.I),
}
# "CHEK-INVOYS, KFC Файз": document type printed before the shop name
DOC_TYPE_RE = re.compile(r"^\s*(chek[\s\-]*invo\w*|savdo\s*cheki?|xarid\s*cheki?)\s*[,.:]?\s*", re.I)
ANY_LABEL = re.compile("|".join(
    p.pattern for k, p in L.items() if k not in ("total", "address", "org", "address_label", "receipt_number_fiscal")),
    re.I)

DATE_ONLY_RE = re.compile(r"(?<![\d.])\d{2}[.\-/]\d{2}[.\-/]\d{4}(?![\d.])")
TIME_ONLY_RE = re.compile(r"(?<![\d.:])\d{1,2}:\d{2}(?::\d{2})?(?![\d:])")
TIN_RE = re.compile(r"(?<!\d)(\d{14}|\d{9})(?!\d)")
RECEIPT_NO_RE = re.compile(r"(?<![\d.:\-/])\d{1,10}(?![\d.:\-/])")
FISCAL_SIGN_RE = re.compile(r"(?<!\d)\d{10,14}(?!\d)")
FM_RE = re.compile(r"\b[A-Z]{2}[\dOIL]{12}\b")  # OCR may read 0 as O inside the code
_PRICE = r"\d{1,3}(?:,\d{3})+(?:\.\d{1,2})?(?![\d,])|\d{1,3}(?:[  'ʼ’]\d{3})+(?:[.,]\d{1,2})?|\d+(?:[.,]\d{1,2})?"
_CURRENCY = r"(?:so[ʻʼ'`’‘]?m|сўм|сум|uzs)"
# "1,000 Kg X 24 000,00" (ERA) | "(10/30) x 16 000 = 5 333,33" (pharmacy: packs of a box)
# "19,520 kub. metr X 5 700,00" (gas) | "10 L X 12 200 SO'M = 122 000" (petrol)
QTY_RE = re.compile(
    r"(?<![\d.,])(?P<qty>\(\s*\d{1,4}\s*/\s*\d{1,4}\s*\)|\d{1,5}(?:[.,]\d{1,3})?)\s*"
    r"(?P<unit>(?:[^\W\d_]{1,6}\.?\s*){0,2})"
    rf"[xхX×*]\s*(?P<price>{_PRICE})\s*(?:{_CURRENCY}\b\.?)?(?:\s*=\s*(?P<total>{_PRICE}))?", re.I)
FRACTION_RE = re.compile(r"\(\s*(\d{1,4})\s*/\s*(\d{1,4})\s*\)")
# lines between an item's name and its quantity line that are not the name
ITEM_META_RE = re.compile(r"(ishlab|chiqaruvchi|ишлаб|^\s*(mk|мк|mxik|мхик)\b|qqs|ққс|ндс|narx|нарх)", re.I)
ITEM_INDEX_RE = re.compile(r"^\s*\d{1,3}[.)]?\s*(?=[^\W\d_])")  # "1 Xurmo", "1. Xurmo", "1Xurmo"


def _text(line):
    return unify_apostrophes(line["text"] if isinstance(line, dict) else line)


def _search_near(lines, label_re, value_re, order=(0, -1, 1)):
    """Return (match_text, line_index) for the first label whose neighbourhood holds a value."""
    texts = [_text(l) for l in lines]
    for i, t in enumerate(texts):
        m = label_re.search(t)
        if not m:
            continue
        for d in order:
            j = i + d
            if not 0 <= j < len(texts):
                continue
            hay = t[m.end():] if d == 0 else texts[j]
            if d != 0 and label_re.search(hay):
                continue
            v = value_re.search(hay)
            if v:
                return v.group(), j
    return None, None


def _last_amount(text):
    found = AMOUNT_RE.findall(text)
    return found[-1] if found else None


class _AmountRe:
    """Value 'regex' that returns the last amount on the line (amounts are right-aligned)."""

    def search(self, text):
        a = _last_amount(text)
        return _Match(a) if a else None


class _Match:
    def __init__(self, g):
        self._g = g

    def group(self):
        return self._g


AMOUNT_LAST = _AmountRe()


class _RateAmountRe:
    """VAT value: the amount after "12.0%=" when printed so (other amounts may follow on the line), else the last."""

    def search(self, text):
        m = re.search(r"%\s*=\s*(" + AMOUNT_RE.pattern + ")", text)
        return _Match(m.group(1)) if m else AMOUNT_LAST.search(text)


AMOUNT_AFTER_RATE = _RateAmountRe()


def _qty(raw, num):
    """'1,000' -> 1.0; '(10/30)' -> 0.333 (10 packs of a box of 30)."""
    m = FRACTION_RE.fullmatch(raw.strip())
    if m and int(m.group(2)):
        return round(int(m.group(1)) / int(m.group(2)), 3)
    return num(raw, 3)


def _item_name(texts, i, before):
    """Name: text before the quantity on the same line, else the nearest line above that is not
    item metadata (manufacturer, marking code, VAT) - pharmacy names sit 2-3 lines higher."""
    name = before.strip()
    if len(re.sub(r"[^\w]", "", name)) >= 3:
        return _clean_name(name)
    for j in range(i - 1, max(i - 4, -1), -1):
        t = texts[j].strip()
        if QTY_RE.search(t) or L["total"][0].search(t) or parse_datetime(t) or L["receipt_number"].search(t):
            break
        if ITEM_META_RE.search(t) or len(re.sub(r"[^\w]", "", t)) < 3:
            continue
        return _clean_name(t)
    return None


def _clean_name(t):
    """Drop the item number and stray one-character tokens OCR adds at the edges ("\\ Шприц", "Margarin I")."""
    words = ITEM_INDEX_RE.sub("", t).strip(" .:-").split()
    while words and len(words[0]) == 1 and not words[0].isdigit():
        words.pop(0)
    while words and len(words[-1]) == 1 and not words[-1].isdigit():
        if len(words) > 1 and re.search(r"\d", words[-2]):
            break  # a unit after a number: "Hydrolife suv 1,5 л", "Pepsi Cola 0,26 л"
        words.pop()
    return " ".join(words) or None


# "BC:4780044573864 Narx: 3ʼ400.00*1Wt.=3ʼ400.00soʼm" | "Narx1: 18ʼ500.00*0.435Kr.=8ʼ048.00soʼm":
# price first, then quantity and unit, then the line total; the name is on the line above.
# OCR misreads of the label ("Narn:", "Nar :", "Narl:", dev r35) count only with the colon
NARX_ITEM_RE = re.compile(
    rf"\b(?:(?:narx|нарх)\w*\s*:?|nar\w{{0,2}}\s*:)\s*(?P<price>{_PRICE})\s*[*xхX×]\s*(?P<qty>\d{{1,5}}(?:[.,]\d{{1,3}})?)\s*"
    rf"(?:[^\W\d_]{{1,4}}\.?)?\s*=\s*(?P<total>{_PRICE})", re.I)
# "Картофель фри 80 1-dona 5 252 soʻm" (Papa Johnʼs): quantity, then the line total; OCR may cut "dona"
DONA_ITEM_RE = re.compile(rf"(?<![\d,.])(?P<qty>\d{{1,4}})\s*-\s*do\w*\s+(?P<total>{_PRICE})\s*{_CURRENCY}", re.I)
# "1. Suv gazsiz Bonaqua Still PET 500ml" with the price alone on the next line (Korzinka, quantity 1)
INDEXED_NAME_RE = re.compile(r"^\s*\d{1,3}\.\s*[^\W\d_]")
MASKED_CARD_RE = re.compile(r"\d{4}\s*\*{3,}")  # "4337******8482": not qty × price
BARCODE_RE = re.compile(r"\b(bc|шк)\s*:\s*\d*", re.I)
# "kombo Nomi   summa" header, then "ЧИЗБУРГЕР ЛАНЧ БОКС  44000.00": one combo = one item, quantity 1;
# the "+8800.00" lines under it are the combo's parts, not items
COMBO_HEAD_RE = re.compile(r"\bkombo\s*nomi\b", re.I)
COMBO_ANY_RE = re.compile(r"\bkombo\b", re.I)  # "Kombo tarkibi" / "kombo Nomi": the items have started
MXIK_RE = re.compile(r"\b(mxik|ikpu|икпу)\b", re.I)  # product class code line: an item, not a shop name
# OCR reads the Latin "KFC" of a shop name as the Cyrillic look-alikes "КЕС" (dev r33)
OOO_RE = re.compile(r"^0{3}(?=\s*[\"«“]|\s+[A-ZА-Я])")
KFC_RE = re.compile(r"^[KК][FЕE][CС](?=[\s.,]|$)\.?\s*")


def _combo_item(texts, i, num):
    for t in texts[i + 1:i + 3]:
        a = _last_amount(t)
        name = t[:t.rfind(a)].strip() if a else ""
        if a and len(re.sub(r"[^\w]", "", name)) >= 3 and not t.strip().startswith("+"):
            v = num(a, 2)
            return {"name": _clean_name(name), "quantity": 1.0, "price": v, "total": v, "_line": i,
                    "_raw_qty": "1", "_raw_price": a, "_raw_total": a}
    return None


def extract_items(lines, num):
    texts = [_text(l) for l in lines]
    items = []
    for i, t in enumerate(texts):
        if COMBO_HEAD_RE.search(t):
            it = _combo_item(texts, i, num)
            if it:
                items.append(it)
            continue
        n = NARX_ITEM_RE.search(t)
        if n:
            before = BARCODE_RE.sub("", t[:n.start()])
            items.append({"name": _item_name(texts, i, before), "quantity": _qty(n.group("qty"), num),
                          "price": num(n.group("price"), 2), "total": num(n.group("total"), 2), "_line": i,
                          "_raw_qty": n.group("qty"), "_raw_price": n.group("price"),
                          "_raw_total": n.group("total")})
            continue
        dn = DONA_ITEM_RE.search(t)
        if dn:
            qty, total = _qty(dn.group("qty"), num), num(dn.group("total"), 2)
            price = round(total / qty, 2) if qty and total is not None else None
            items.append({"name": _item_name(texts, i, t[:dn.start()]), "quantity": qty, "price": price,
                          "total": total, "_line": i, "_raw_qty": dn.group("qty"), "_raw_price": None,
                          "_raw_total": dn.group("total")})
            continue
        nxt = texts[i + 1].strip() if i + 1 < len(texts) else ""
        if (INDEXED_NAME_RE.match(t) and not QTY_RE.search(t) and AMOUNT_RE.fullmatch(nxt)
                and len(re.sub(r"\D", "", nxt)) >= 3):
            v = num(nxt, 2)
            items.append({"name": _clean_name(t), "quantity": 1.0, "price": v, "total": v, "_line": i,
                          "_raw_qty": "1", "_raw_price": nxt, "_raw_total": nxt})
            continue
        m = QTY_RE.search(t)
        if not m or parse_datetime(t) or MASKED_CARD_RE.search(t):
            continue
        total = m.group("total")  # "= 5 333,33" on the same line
        if total is None:
            total = _last_amount(t[m.end():])
            if total is not None and len(total) < 3:
                total = None  # a stray digit after the price, not the line total
        if total is None and i + 1 < len(texts) and not QTY_RE.search(texts[i + 1]):
            nxt = texts[i + 1].strip()
            if AMOUNT_RE.fullmatch(nxt) or L["narx"].search(nxt):
                total = _last_amount(nxt)
        total_raw = total
        qty, price = _qty(m.group("qty"), num), num(m.group("price"), 2)
        total = num(total, 2) if total else None
        if total is None and qty is not None and price is not None:
            total = round(qty * price, 2)
        items.append({"name": _item_name(texts, i, t[:m.start()]), "quantity": qty, "price": price,
                      "total": total, "_line": i, "_raw_qty": m.group("qty"), "_raw_price": m.group("price"),
                      "_raw_total": total_raw})
    return items


# lines that end the "Manzil" address block
ADDRESS_STOP_RE = re.compile(
    rf"^\s*(yur\b|yuridik|\w{{0,2}}ir\s*/|stir|\w?shshr|inn|инн|стир|sana|\w{{0,2}}a\s*va\s*vaqt|сана|chek|чек|"
    rf"tel\b|тел\b|telefon|дорихона|kassir|savdo|ro{A}yxat|sn\s*kkm)", re.I)  # tolerant: "Yur,Manz1l", "IIR/DSHSHR"
REGION_RE = re.compile(r"(viloyat|вилоят|област)", re.I)
ADDRESS_WORDS = [  # standard words of Uzbek addresses (no shop-specific names)
    "viloyati", "viloyat", "shahri", "shahar", "tumani", "tuman", "mfy", "koʻchasi", "koʻcha", "qishlogʻi",
    "mahallasi", "massivi", "uy", "Fargʻona", "Margʻilon", "Qoʻqon", "Toshkent", "Samarqand", "Buxoro",
    "Andijon", "Namangan", "Navoiy", "Xorazm", "Qashqadaryo", "Surxondaryo", "Jizzax", "Sirdaryo",
    "Qoraqalpogʻiston", "Nukus", "Bagʻdod", "Yangi"]


def _word_key(w):
    return re.sub(r"[ʻʼ'`’‘]", "", w).casefold()


_ADDRESS_KEYS = {_word_key(w): w for w in ADDRESS_WORDS}


def correct_address_words(text):
    """Snap near-miss words to the address vocabulary: 'Fargʻond' -> 'Fargʻona', 'koʻchas1' -> 'koʻchasi'.
    One edit allowed for words of 5+ letters, two for 8+; case style of the original word is kept."""
    from rapidfuzz.distance import Levenshtein

    def fix(m):
        w = m.group(0)
        k = _word_key(w)
        if len(k) < 5 or k in _ADDRESS_KEYS:
            return w
        best = min(_ADDRESS_KEYS, key=lambda v: Levenshtein.distance(k, v))
        d = Levenshtein.distance(k, best)
        if d <= (2 if len(k) >= 8 else 1) and abs(len(best) - len(k)) <= 1:
            out = _ADDRESS_KEYS[best]
            return out.upper() if w.isupper() else out
        return w

    def join(m):  # the apostrophe of oʻ/gʻ read as a space: "Farg ona" -> "Fargʻona"
        k = _word_key(m.group(1) + m.group(2))
        if k in _ADDRESS_KEYS or min(Levenshtein.distance(k, v) for v in _ADDRESS_KEYS) <= 1 and len(k) >= 7:
            return m.group(1) + "ʻ" + m.group(2)
        return m.group(0)

    text = re.sub(r"\b([^\W\d_]{2,6}[gG]?)\s([^\W\d_]{2,6})\b", join, text)
    text = re.sub(r"(?i)\bmfy(?=[^\W\d_])", "MFY ", text)  # "MFyYangi" -> "MFY Yangi"
    text = re.sub(r"(?<=[a-zʻʼ])(?=MF[Yy]\b)", " ", text)  # "HamkorlikMFy" -> "Hamkorlik MFy"
    return re.sub(r"[^\W\d_][^\W_ʻʼ'`’‘]*(?:[ʻʼ'`’‘][^\W_]+)*", fix, text)


def extract_address(texts, postprocess=True):
    """Address of the shop: every line from the "Manzil" label to the next label.

    - text after the label on the same line is kept only if it looks like an address
      (on curved receipts OCR merges the label with the owner's name printed next to it);
    - an address line that slid onto the "Yur.Manzil" row (the legal address starts with the
      region on the next line) is moved back to the shop address.
    Receipts without a "Manzil" label: the first group of address-like lines near the top.
    Returns (address, index of the first address line)."""
    start = next((j for j, t in enumerate(texts[:25])
                  if L["address_label"].search(t) and not re.match(r"^\s*yur", t, re.I)), None)
    if start is None:
        addr, first = [], None
        for j, t in enumerate(texts[:20]):
            if L["address"].search(t) and not L["tin"].search(t):
                if first is not None and j != first + len(addr):
                    break
                first = j if first is None else first
                addr.append(t.strip(" ,"))
            elif addr:
                break
        out = ", ".join(a for a in addr if a) or None
        return (correct_address_words(out) if out and postprocess else out), first

    parts = []
    rest = L["address_label"].sub("", texts[start]).strip(" ,.:")
    if rest and (L["address"].search(rest) or REGION_RE.search(rest)):
        parts.append(rest)
    for j in range(start + 1, min(start + 8, len(texts))):
        t = texts[j].strip()
        if ADDRESS_STOP_RE.search(t):
            if re.match(r"^\s*yur", t, re.I):
                tail = re.sub(r"^\s*yur\W*\S*\s*", "", t, flags=re.I).strip(" ,.")  # also "Yur,Manz1l"
                nxt = texts[j + 1] if j + 1 < len(texts) else ""
                if tail and not REGION_RE.search(tail) and REGION_RE.search(nxt):
                    parts.append(tail)
            break
        if t:
            parts.append(t.strip(" ,"))
    out = ", ".join(p for p in parts if p) or None
    return (correct_address_words(out) if out and postprocess else out), start


def extract(lines, postprocess=True):
    """lines: OCR line dicts (or strings) in reading order."""
    lines = [l for l in lines if not is_separator(_text(l))]
    texts = [_text(l) for l in lines]

    if postprocess:
        def num(s, nd=2):
            return parse_qty(s) if nd == 3 else parse_amount(s)
    else:
        def num(s, nd=2):
            return naive_number(s)

    f, src = {}, {}

    def put(field, value, idx):
        f[field] = value
        if value is not None and idx is not None:
            src[field] = idx

    v, i = _search_near(lines, L["tin"], TIN_RE)
    put("seller_tin", v, i)

    v, i = _search_near(lines, L["datetime"], re.compile(r"\d{2}[.\-/]\d{2}[.\-/]\d{4}[ T,]*\d{1,2}(?:[:.]| (?=\d{2}[:.]\d{2}))\d{2}(?:[:.]\d{2})?"))
    if v is None:
        for j, t in enumerate(texts):
            if parse_datetime(t):
                v, i = t, j
                break
    if v is None:
        # "Чек №: 2562 25.11.2026" / "KACCA: Kassa-1 21:26" (OKA): the date and the time on two lines
        for j, t in enumerate(texts):
            d = DATE_ONLY_RE.search(t)
            if not d:
                continue
            tm = next((TIME_ONLY_RE.search(texts[k]) for k in (j + 1, j - 1)
                       if 0 <= k < len(texts) and TIME_ONLY_RE.search(texts[k])), None)
            if tm:
                v, i = f"{d.group()} {tm.group()}", j
                break
    dt = parse_datetime(v) if v else None
    if dt and postprocess and not 2020 <= int(dt[:4]) <= 2035:
        dt = None  # "2826": a misread zero gave a valid but impossible year
    if dt is None and v and postprocess:
        dt = repair_datetime(v)
    put("datetime", dt, i)

    v, i = _search_near(lines, L["rs"], RECEIPT_NO_RE, order=(0,))
    if v is None:
        v, i = _search_near(lines, L["receipt_number_fiscal"], RECEIPT_NO_RE, order=(0, 1))
    if v is None:  # a number on any "Chek" line first, then next to one ("SOTUV CHEK" / "CHEK 2402 ...")
        v, i = _search_near(lines, L["receipt_number"], RECEIPT_NO_RE, order=(0,))
    if v is None:
        v, i = _search_near(lines, L["receipt_number"], RECEIPT_NO_RE)
    put("receipt_number", v, i)

    v, i = _search_near(lines, L["fiscal_sign"], FISCAL_SIGN_RE, order=(0, 1, -1))
    put("fiscal_sign", v, i)

    upper = [{"text": t.upper()} for t in texts]
    v, i = _search_near(upper, L["fiscal_module"], FM_RE, order=(0, 1, -1))
    if v is None:
        for j, t in enumerate(upper):
            m = FM_RE.search(t["text"])
            if m:
                v, i = m.group(), j
                break
    if v is not None:
        v = v[:2] + v[2:].translate(str.maketrans("OIL", "011"))
    put("fiscal_module", v, i)

    v, i = _search_near(lines, L["vat_total"], AMOUNT_AFTER_RATE if postprocess else AMOUNT_LAST, order=(0, 1, -1))
    if v is None:
        # last VAT line: items print their own VAT first, the receipt's VAT comes after them
        for j in range(len(texts) - 1, -1, -1):
            m = L["vat"].search(texts[j])
            if m and _last_amount(texts[j][m.end():]):
                v, i = _last_amount(texts[j][m.end():]), j
                break
    vat = num(v) if v else None
    if postprocess and any(L["vat_free"].search(t) for t in texts) and not any(
            re.search(r"\d+\s*%", t) for t in texts if L["vat"].search(t)):
        # the items are "QQS siz" (VAT-free) and no VAT rate is printed: the receipt's VAT is 0;
        # a reading such as "0.6" or "1" is a misread 0.00
        vat = 0.0
    put("vat", vat, i)

    v = i = None
    for rx in L["total"]:
        v, i = _search_near(lines, rx, AMOUNT_LAST, order=(0, 1, -1))
        if v:
            break
    items = extract_items(lines, num)
    total = num(v) if v else None
    if postprocess:
        # other copies of the same amount: payment lines, the card slip "Jami", Narx, the "... UZS" line,
        # item prices/totals (every amount on those lines: OCR noise may follow the real one)
        others = [a for k, t in enumerate(texts)
                  if k != i  # the total line itself is not a second copy; an equal payment line is
                  and (L["card"].search(t) or L["narx"].search(t) or re.search(r"\buzs\b", t, re.I)
                  or re.match(r"^\s*(jami|жами|итого)\s", t, re.I))
                  for a in AMOUNT_RE.findall(t) if len(re.sub(r"\D", "", a)) >= 3]
        if len(items) == 1:  # one item: its price and line total are copies of the receipt total
            others += [items[0][k] for k in ("_raw_price", "_raw_total")]
        others = [o for o in others if o]
        # 1) the total line, confirmed by another copy  2) two other copies that agree  3) the line as read
        total = (agree(v, others) if v else None) or consensus(others) or total
        if total is None and items and all(it["total"] is not None for it in items):
            # no total line read: the sum of the items, if a payment line ("BANK CARD =6ʼ900.00") confirms it
            s = round(sum(it["total"] for it in items), 2)
            if any(parse_amount(o) == s for o in others):
                total = s
        for it in items:
            repair_item(it, total, single=len(items) == 1)
    for it in items:
        for k in ("_raw_qty", "_raw_price", "_raw_total"):
            it.pop(k, None)
    put("total", total, i)

    card, ci = _search_near(lines, L["card"], AMOUNT_LAST, order=(0,))
    cash, hi = _search_near(lines, L["cash"], AMOUNT_LAST, order=(0,))
    card_v, cash_v = (num(card) if card else None), (num(cash) if cash else None)
    if postprocess and cash and could_be_zero(cash) and (card_v or 0) > 0:
        cash_v = 0.0
    if (card_v or 0) > 0 and (cash_v or 0) > 0:
        pay, pi = "other", ci
    elif (card_v or 0) > 0:
        pay, pi = "card", ci
    elif (cash_v or 0) > 0:
        pay, pi = "cash", hi
    elif any(L["card"].search(t) for t in texts):
        pay, pi = "card", None
    elif any(L["cash"].search(t) for t in texts):
        pay, pi = "cash", None
    else:
        pay, pi = None, None
    put("payment", pay, pi)

    addr, first = extract_address(texts, postprocess)
    put("address", addr, first)

    # seller: an organisation-looking line at the top, else the first wordy non-label line
    seller, si = None, None
    if postprocess and first is not None:
        # shop name printed under the logo: the nearest wordy line above the address, skipping
        # address lines (curved paper lifts them above the "Manzil" label) and, once, the line with
        # the owner's / legal name in capitals ("ADHAMJON MAMADALIYEV ...", "\"AVTOGAZ\" MCHJ")
        owner_skipped = False
        for j in range(first - 1, -1, -1):
            t = texts[j].strip()
            chars = [c for c in t if not c.isspace()]
            letters = sum(c.isalpha() for c in chars)
            if letters < 3 or letters / max(len(chars), 1) < 0.7 or ANY_LABEL.search(t):
                continue
            if L["address"].search(t) or REGION_RE.search(t):
                continue
            if not owner_skipped and len(t.split()) >= 2 and t.upper() == t:
                owner_skipped = True
                continue
            seller, si = t, j
            break
    for j, t in enumerate(texts[:8] if seller is None else []):
        if L["org"].search(t) and not ANY_LABEL.search(t) and not L["address"].search(t):
            seller, si = t.strip(), j
            break
    if seller is None:
        for j, t in enumerate(texts[:5]):
            if postprocess and (QTY_RE.search(t) or NARX_ITEM_RE.search(t) or ITEM_INDEX_RE.match(t)
                                or COMBO_ANY_RE.search(t) or MXIK_RE.search(t) or BARCODE_RE.search(t)):
                break  # the items have started: the top of the receipt has no shop name
            name = DOC_TYPE_RE.sub("", t).strip() if postprocess else t.strip()
            letters = sum(c.isalpha() for c in name)
            if letters >= 4 and not ANY_LABEL.search(name) and not L["address"].search(name):
                seller, si = name, j
                break
    if postprocess and seller:
        seller = KFC_RE.sub("KFC ", seller).strip()
        seller = OOO_RE.sub("OOO", seller)  # "000 \"ALEXANDER BRANDS\"": OCR reads the letters O as zeros
    put("seller_name", seller, si)

    return f, items, src, lines
