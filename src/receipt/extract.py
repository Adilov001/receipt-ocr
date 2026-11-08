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
    "tin": re.compile(r"\b(stir|inn|инн|стир|jshshr|жшшир|pinfl)\b", re.I),
    "datetime": re.compile(r"\b(sana|vaqt|дата|время|сана|вақт)\b", re.I),
    "receipt_number": re.compile(r"(^|\s)(chek|чек)(\s*(raqami|№|no\.?|#))?(?!\s*(turi|kodi))\b", re.I),
    "fiscal_sign": re.compile(r"(fiskal\s*(imzo|belgi|alomat)|фискал\w*\s*(признак|имзо|белги)|\bфп\b|\bfp\b)", re.I),
    "fiscal_module": re.compile(r"(\bfm\b|\bфм\b|fiskal\s*modul|фискал\w*\s*модул|\bzfm\b)", re.I),
    "vat_total": re.compile(rf"(jami\s*qqs|qqs\s*jami|итого\s*ндс|жами\s*ққс|ққс\s*жами|ндс\s*итого)", re.I),
    "vat": re.compile(r"\b(qqs|ндс|ққс)\b(?!\s*siz)", re.I),
    "total": [
        re.compile(rf"to{A}lov\s*uchun\s*jami|тўлов\s*учун\s*жами", re.I),
        re.compile(rf"jami\s*to{A}lov|итого\s*к\s*оплате|к\s*оплате|всего\s*к\s*оплате", re.I),
        re.compile(r"\b(итого|итог|всего|жами)\b(?!\s*(ндс|ққс))", re.I),
        re.compile(r"\bjami\b(?!\s*qqs)", re.I),
    ],
    "card": re.compile(r"(naqdsiz|plastik|bank\s*karta|безнал|карт[аой]|uzcard|humo|нақдсиз)", re.I),
    "cash": re.compile(r"(\bnaqd\b(?!\s*siz)|наличн|\bнақд\b)", re.I),
    "address": re.compile(
        rf"(ko{A}ch|kuchasi|tuman|shahar|shahri|viloyat|mahalla|\bmfy\b|massiv|\buy\b|\bул\.|улиц|район|"
        rf"\bг\.|област|кўча|туман|шаҳ|вилоят|manzil|адрес|манзил)", re.I),
    "address_label": re.compile(r"^\s*(yur\.?\s*manzil|yuridik\s*manzil|manzil|адрес|манзил)\s*[:.]?\s*", re.I),
    "vat_free": re.compile(r"(qqs\s*siz|без\s*ндс|ққс\s*сиз)", re.I),
    "narx": re.compile(r"^\s*(narx|нарх|цена)\b", re.I),
    "org": re.compile(r"\b(mchj|xk|yatt|qk|aj|ooo|ооо|мчж|ип|чп|ао|ат|llc|ltd)\b|[\"«“]", re.I),
}
ANY_LABEL = re.compile("|".join(
    p.pattern for k, p in L.items() if k not in ("total", "address", "org", "address_label")), re.I)

TIN_RE = re.compile(r"(?<!\d)(\d{14}|\d{9})(?!\d)")
RECEIPT_NO_RE = re.compile(r"(?<![\d.:\-/])\d{1,10}(?![\d.:\-/])")
FISCAL_SIGN_RE = re.compile(r"(?<!\d)\d{10,14}(?!\d)")
FM_RE = re.compile(r"\b[A-Z]{2}[\dOIL]{12}\b")  # OCR may read 0 as O inside the code
QTY_RE = re.compile(
    r"(?<![\d.,])(?P<qty>\d{1,5}(?:[.,]\d{1,3})?)\s*(?P<unit>[^\W\d_]{0,6}\.?)\s*[xхX×*]\s*"
    r"(?P<price>\d{1,3}(?:[  ']\d{3})+(?:[.,]\d{1,2})?|\d+(?:[.,]\d{1,2})?)")
ITEM_INDEX_RE = re.compile(r"^\s*\d{1,3}[.)]?\s+(?=\D)")


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


def extract_items(lines, num):
    texts = [_text(l) for l in lines]
    items = []
    for i, t in enumerate(texts):
        m = QTY_RE.search(t)
        if not m or parse_datetime(t):
            continue
        rest = t[m.end():]
        total = _last_amount(rest)
        if total is not None and len(total) < 3:
            total = None  # a stray digit after the price, not the line total
        if total is None and i + 1 < len(texts) and not QTY_RE.search(texts[i + 1]):
            nxt = texts[i + 1].strip()
            if AMOUNT_RE.fullmatch(nxt) or L["narx"].search(nxt):
                total = _last_amount(nxt)
        total_raw = total
        name = t[:m.start()].strip()
        if len(re.sub(r"[^\w]", "", name)) < 3 and i > 0:
            name = texts[i - 1].strip()
        name = ITEM_INDEX_RE.sub("", name).strip(" .:-")
        qty, price = num(m.group("qty"), 3), num(m.group("price"), 2)
        total = num(total, 2) if total else None
        if total is None and qty is not None and price is not None:
            total = round(qty * price, 2)
        items.append({"name": name or None, "quantity": qty, "price": price, "total": total, "_line": i,
                      "_raw_qty": m.group("qty"), "_raw_price": m.group("price"), "_raw_total": total_raw})
    return items


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

    v, i = _search_near(lines, L["datetime"], re.compile(r"\d{2}[.\-/]\d{2}[.\-/]\d{4}[ T,]*\d{1,2}[:.]\d{2}(?:[:.]\d{2})?"))
    if v is None:
        for j, t in enumerate(texts):
            if parse_datetime(t):
                v, i = t, j
                break
    dt = parse_datetime(v) if v else None
    if dt and postprocess and not 2020 <= int(dt[:4]) <= 2035:
        dt = None  # "2826": a misread zero gave a valid but impossible year
    if dt is None and v and postprocess:
        dt = repair_datetime(v)
    put("datetime", dt, i)

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

    v, i = _search_near(lines, L["vat_total"], AMOUNT_LAST, order=(0, 1, -1))
    if v is None:
        v, i = _search_near(lines, L["vat"], AMOUNT_LAST, order=(0,))
    vat = num(v) if v else None
    if postprocess and v and vat and could_be_zero(v) and any(L["vat_free"].search(t) for t in texts):
        vat = 0.0  # every item is "QQS siz" (VAT-free) and the reading may be 0.00 misread
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
        others = [a for t in texts
                  if L["card"].search(t) or L["narx"].search(t) or re.search(r"\buzs\b", t, re.I)
                  or re.match(r"^\s*(jami|жами|итого)\s", t, re.I)
                  for a in AMOUNT_RE.findall(t) if len(re.sub(r"\D", "", a)) >= 3]
        others += [it[k] for it in items for k in ("_raw_price", "_raw_total")]
        others = [o for o in others if o and o != v]
        # 1) the total line, confirmed by another copy  2) two other copies that agree  3) the line as read
        total = (agree(v, others) if v else None) or consensus(others) or total
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

    # address: first group of consecutive address-like lines near the top
    addr, first = [], None
    for j, t in enumerate(texts[:20]):
        if L["address"].search(t) and not L["tin"].search(t):
            if first is not None and (j != first + len(addr) or L["address_label"].search(t)):
                break
            first = j if first is None else first
            addr.append(L["address_label"].sub("", t).strip(" ,"))
        elif addr:
            break
    put("address", ", ".join(a for a in addr if a) or None, first)

    # seller: an organisation-looking line at the top, else the first wordy non-label line
    seller, si = None, None
    if postprocess and first is not None:
        # shop name printed under the logo: the nearest wordy line above the address,
        # skipping the owner's full name (3+ capitalised words)
        for j in range(first - 1, -1, -1):
            t = texts[j].strip()
            chars = [c for c in t if not c.isspace()]
            letters = sum(c.isalpha() for c in chars)
            if letters < 3 or letters / max(len(chars), 1) < 0.7 or ANY_LABEL.search(t):
                continue
            if len(t.split()) >= 3 and t.upper() == t:
                continue
            seller, si = t, j
            break
    for j, t in enumerate(texts[:8] if seller is None else []):
        if L["org"].search(t) and not ANY_LABEL.search(t) and not L["address"].search(t):
            seller, si = t.strip(), j
            break
    if seller is None:
        for j, t in enumerate(texts[:5]):
            letters = sum(c.isalpha() for c in t)
            if letters >= 4 and not ANY_LABEL.search(t) and not L["address"].search(t):
                seller, si = t.strip(), j
                break
    put("seller_name", seller, si)

    return f, items, src, lines
