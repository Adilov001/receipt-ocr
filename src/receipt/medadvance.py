"""The recognition result in the format of the MedAdvance backend (github.com/airi-club/MedAdvance).

MedAdvance stores a fiscal receipt as `Receipt.fields` (10 strings, checked by
backend/receipts/validation.py) and keeps `Receipt.recognition` (JSON) for an OCR provider.
`to_medadvance()` builds both: `fields` pass that validation as they are, so the backend can
copy them into the receipt draft; the rest (sources, warnings, items) is for `recognition`.

Field names and values follow MedAdvance (src/fiscalParser.js):
    date "YYYY-MM-DD", time "HH:MM:SS", amount "56000.00", receipt, seller, inn (9 or 14 digits),
    fiscalSign, fiscalModule, payment "Банковская карта" | "Наличные", currency "UZS".
A value that would fail the MedAdvance validation is left empty and explained in `warnings`.
Texts shown to the user are in Russian, like the MedAdvance interface.
"""
import re
from datetime import date

FIELDS = ("date", "time", "amount", "receipt", "seller", "inn", "fiscalSign", "fiscalModule", "payment", "currency")
REQUIRED = ("date", "time", "amount", "receipt")  # needed to save a fiscal receipt in MedAdvance
LIMITS = {"receipt": 40, "seller": 160}  # max length, as in validation.py (160 for every other field)
PAYMENT = {"card": "Банковская карта", "cash": "Наличные"}
DESCRIPTIONS = {
    "date": "Дата покупки на чеке", "time": "Время покупки на чеке", "amount": "Итоговая сумма чека",
    "receipt": "Номер чека", "seller": "Название продавца", "inn": "ИНН продавца",
    "fiscalSign": "Фискальный признак", "fiscalModule": "Фискальный модуль",
    "payment": "Способ оплаты на чеке", "currency": "Валюта на чеке",
}
# MedAdvance field <- our field
SOURCE_FIELD = {
    "date": "datetime", "time": "datetime", "amount": "total", "receipt": "receipt_number",
    "seller": "seller_name", "inn": "seller_tin", "fiscalSign": "fiscal_sign", "fiscalModule": "fiscal_module",
    "payment": "payment", "currency": "total",
}
QR_LABELS = {"datetime": "Дата и время", "receipt_number": "Номер чека", "fiscal_sign": "Фискальный признак",
             "fiscal_module": "Фискальный модуль", "total": "Сумма"}
ISO_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})(?:T(\d{2}:\d{2}(?::\d{2})?))?")


def _text(value):
    return "" if value is None else str(value).strip()


def _money(value):
    return f"{value:.2f}" if isinstance(value, (int, float)) and value > 0 else ""


def to_medadvance(out, pages=1, today=None):
    """out: the dict returned by pipeline.process(). Returns
    {fields, sources, missing, warnings, summary} for MedAdvance."""
    r = out["result"]
    today = today or date.today()
    warnings = []

    m = ISO_RE.match(_text(r.get("datetime")))
    day, clock = (m.group(1), m.group(2) or "") if m else ("", "")
    if day:
        try:
            if date.fromisoformat(day) > today:
                warnings.append(f"Дата на чеке ({day}) позже сегодняшней — похоже, она прочитана неверно. Укажите дату вручную.")
                day = ""
        except ValueError:
            day = ""
    if len(clock) == 5:
        clock += ":00"

    inn = re.sub(r"\D", "", _text(r.get("seller_tin")))
    if inn and len(inn) not in (9, 14):
        warnings.append(f"ИНН продавца прочитан не полностью ({inn}). Проверьте его.")
        inn = ""

    fields = {
        "date": day, "time": clock,
        "amount": _money(r.get("total")),
        "receipt": _text(r.get("receipt_number")),
        "seller": _text(r.get("seller_name")),
        "inn": inn,
        "fiscalSign": _text(r.get("fiscal_sign")),
        "fiscalModule": _text(r.get("fiscal_module")),
        "payment": PAYMENT.get(r.get("payment"), ""),
        "currency": "UZS" if _money(r.get("total")) else "",
    }
    for key, value in fields.items():
        limit = LIMITS.get(key, 160)
        if len(value) > limit:
            fields[key] = "" if key == "receipt" else value[:limit].rstrip()

    qr_raw = (r.get("qr") or {}).get("raw") or ""
    rebuilt = "" if qr_raw else ((r.get("qr") or {}).get("rebuilt") or "")
    sources = {}
    for key, value in fields.items():
        if not value:
            continue
        ours = SOURCE_FIELD[key]
        if out.get("field_source", {}).get(ours) == "qr" and qr_raw:
            sources[key] = {"text": qr_raw, "confidence": 1.0, "description": "Из QR-кода чека"}
        else:
            line = (out.get("source_lines") or {}).get(ours) or {}
            sources[key] = {"text": line.get("text") or value, "confidence": round(float(line.get("conf", 0.9)), 3),
                            "description": DESCRIPTIONS[key]}

    if r.get("payment") == "other":
        warnings.append("На чеке оплата картой и наличными — укажите способ оплаты вручную.")
    for check in out.get("checks", []):
        if check["status"] != "mismatch":
            continue
        name = check["check"]
        if name == "Σ items = total":
            warnings.append(f"Сумма позиций чека ({check['expected']}) не совпадает с итогом ({check['actual']}). Проверьте сумму покупки.")
        elif name.startswith("item "):
            warnings.append(f"Позиция {name.split(':')[0][5:]}: количество × цена не равно сумме позиции. Проверьте позиции чека.")
        elif check.get("kind") == "qr":
            field = name.replace("OCR ↔ QR: ", "")
            warnings.append(f"{QR_LABELS.get(field, field)} в тексте ({check['actual']}) отличается от QR-кода "
                            f"({check['expected']}). Использовано значение из QR-кода.")
    if rebuilt:
        warnings.append(f"QR-код чека не прочитан. Ссылка для проверки чека собрана из реквизитов: {rebuilt} — "
                        "откройте её, чтобы сверить чек на soliq.uz.")
    elif not qr_raw:
        warnings.append("QR-код чека не прочитан: реквизиты взяты из текста. Проверьте их или загрузите фото, где QR-код крупнее.")
    if pages > 1:
        warnings.append(f"В PDF {pages} страниц. Поля извлечены с первой страницы.")

    return {
        "fields": fields,
        "sources": sources,
        "missing": [k for k in REQUIRED if not fields[k]],
        "warnings": warnings,
        "summary": {
            "qr": qr_raw, "qrRebuilt": rebuilt, "documentType": "fiscal",
            "items": [{k: it.get(k) for k in ("name", "quantity", "price", "total")} for it in r.get("items") or []],
            "consistent": bool(out.get("consistent")),
        },
    }
