# Copy of backend/receipts/validation.py from github.com/airi-club/MedAdvance (main, commit 01f5227),
# unchanged: tests/test_medadvance.py checks that our "medadvance.fields" pass it.
# Update this copy when MedAdvance changes its validation.
import re
from datetime import date
from decimal import Decimal, InvalidOperation

from django.core.exceptions import ValidationError

MAX_FILE_SIZE = 10 * 1024 * 1024
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "pdf", "webp", "heic", "heif"}
BANK_FIELDS = {"date", "time", "amount", "bank", "card", "operation"}
FISCAL_FIELDS = {"date", "time", "amount", "receipt", "seller", "inn", "fiscalSign", "fiscalModule", "payment", "currency"}


def _signature(data):
    if data.startswith(b"\xff\xd8\xff"):
        return "jpeg"
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        return "png"
    if data.startswith(b"%PDF-"):
        return "pdf"
    if len(data) >= 12 and data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return "webp"
    if len(data) >= 12 and data[4:8] == b"ftyp" and any(tag in data[8:64].lower() for tag in (b"heic", b"heix", b"hevc", b"hevx", b"mif1", b"msf1")):
        return "heic"
    return None


def validate_receipt_file(upload):
    if not upload or not upload.size:
        raise ValidationError("Выберите непустой файл документа.")
    if upload.size > MAX_FILE_SIZE:
        raise ValidationError("Файл больше 10 МБ.")
    extension = upload.name.rsplit(".", 1)[-1].lower() if "." in upload.name else ""
    expected = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "pdf": "pdf", "webp": "webp", "heic": "heic", "heif": "heic"}.get(extension)
    upload.seek(0)
    signature = _signature(upload.read(64))
    upload.seek(0)
    if extension not in ALLOWED_EXTENSIONS or signature is None or signature != expected:
        raise ValidationError("Содержимое файла не соответствует разрешённым форматам JPG, PNG, PDF, WEBP и HEIC.")
    if signature in {"jpeg", "png", "webp"}:
        try:
            from PIL import Image, UnidentifiedImageError
            upload.seek(0)
            with Image.open(upload) as image:
                width, height = image.size
                image.verify()
            if min(width, height) < 240 or max(width, height) < 320:
                raise ValidationError("Загрузите изображение не менее 320 × 240 px.")
        except ImportError:
            # Pillow is optional for the backend; file signature and size remain checked.
            pass
        except ValidationError:
            raise
        except (OSError, UnidentifiedImageError) as error:
            raise ValidationError("Не удалось прочитать изображение.") from error
        finally:
            upload.seek(0)


def validate_fields(document_type, fields, partial=True):
    if not isinstance(fields, dict):
        raise ValidationError({"fields": "Поля чека должны быть JSON-объектом."})
    allowed = BANK_FIELDS if document_type == "bank" else FISCAL_FIELDS
    unknown = set(fields) - allowed
    errors = {}
    if unknown:
        errors["fields"] = f"Неизвестные поля: {', '.join(sorted(unknown))}."
    for name, value in fields.items():
        if not isinstance(value, (str, int, float)):
            errors[name] = "Ожидается строковое значение."
            continue
        text = str(value).strip()
        if len(text) > 160:
            errors[name] = "Максимальная длина поля — 160 символов."
    limits = {"bank": {"bank": 120, "operation": 120}, "fiscal": {"receipt": 40, "seller": 160}}
    for name, limit in limits[document_type].items():
        if fields.get(name) is not None and len(str(fields[name]).strip()) > limit:
            errors[name] = f"Максимальная длина поля — {limit} символов."
    if not partial:
        required = BANK_FIELDS if document_type == "bank" else {"date", "time", "amount", "receipt"}
        missing = [name for name in required if not str(fields.get(name, "")).strip()]
        if missing:
            errors["fields"] = f"Не заполнены обязательные поля: {', '.join(sorted(missing))}."
    if fields.get("date"):
        try:
            value = date.fromisoformat(str(fields["date"]))
            if value > date.today():
                errors["date"] = "Дата не может быть позже сегодняшней."
        except ValueError:
            errors["date"] = "Укажите действительную дату в формате ГГГГ-ММ-ДД."
    if fields.get("time") and not re.fullmatch(r"(?:[01]\d|2[0-3]):[0-5]\d(?::[0-5]\d)?", str(fields["time"])):
        errors["time"] = "Укажите время в формате ЧЧ:ММ или ЧЧ:ММ:СС."
    if errors:
        raise ValidationError(errors)

    amount = fields.get("amount")
    if amount not in (None, ""):
        try:
            amount_text = str(amount).replace(" ", "").replace(",", ".")
            if not re.fullmatch(r"\d+(?:\.\d{1,2})?", amount_text):
                raise InvalidOperation
            value = Decimal(amount_text)
            if value <= 0 or (document_type == "bank" and value > Decimal("999999999999.99")):
                raise ValueError
        except (TypeError, ValueError, InvalidOperation):
            errors["amount"] = "Сумма должна быть положительной и содержать не более двух знаков после запятой."
    if document_type == "bank" and fields.get("card") and not re.fullmatch(r"\d{4}", str(fields["card"])):
        errors["card"] = "Укажите последние четыре цифры карты."
    if document_type == "fiscal" and fields.get("inn") and not re.fullmatch(r"(?:\d{9}|\d{14})", str(fields["inn"])):
        errors["inn"] = "ИНН состоит из 9 цифр (ПИНФЛ — из 14)."
    if errors:
        raise ValidationError(errors)
