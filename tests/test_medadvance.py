"""The "medadvance" block passes the MedAdvance backend's own field validation (a copy of
backend/receipts/validation.py) and maps our result as MedAdvance expects."""
import json
import sys
import types
from datetime import date
from pathlib import Path

import pytest

from receipt.medadvance import FIELDS, to_medadvance

ROOT = Path(__file__).resolve().parents[1]


class _DjangoValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message_dict = message if isinstance(message, dict) else {"": [message]}


@pytest.fixture(scope="module")
def validate_fields():
    # validation.py imports django.core.exceptions.ValidationError; Django is not needed for this check
    fake = types.ModuleType("django.core.exceptions")
    fake.ValidationError = _DjangoValidationError
    sys.modules.setdefault("django", types.ModuleType("django"))
    sys.modules.setdefault("django.core", types.ModuleType("django.core"))
    sys.modules["django.core.exceptions"] = fake
    sys.path.insert(0, str(ROOT / "tests"))
    import medadvance_validation
    return medadvance_validation.validate_fields


def _out(**result):
    base = {"datetime": None, "total": None, "receipt_number": None, "seller_name": None, "seller_tin": None,
            "fiscal_sign": None, "fiscal_module": None, "payment": None, "items": [], "qr": {"raw": None}}
    return {"result": {**base, **result}, "checks": [], "consistent": False, "field_source": {}, "source_lines": {}}


LABELS = sorted(p.stem for p in (ROOT / "data/gt").glob("*.json"))


@pytest.mark.parametrize("rid", LABELS)
def test_every_labelled_receipt_passes_medadvance_validation(validate_fields, rid):
    gt = json.loads((ROOT / f"data/gt/{rid}.json").read_text())
    m = to_medadvance(_out(**{k: v for k, v in gt.items() if not k.startswith("_")}), today=date(2030, 1, 1))
    assert set(m["fields"]) == set(FIELDS)
    validate_fields("fiscal", m["fields"], partial=True)
    if not m["missing"]:
        validate_fields("fiscal", m["fields"], partial=False)  # can be saved as it is


def test_mapping():
    out = _out(datetime="2026-11-24T13:29", total=71000.0, receipt_number="2000", seller_name="FAST FOOD SYSTEM MCHJ",
               seller_tin="310839380", fiscal_sign="285421523353", fiscal_module="VG544170029013", payment="card",
               qr={"raw": "https://ofd.soliq.uz/check?t=VG544170029013&r=2000&c=20261124132918&s=285421523353"})
    out["field_source"] = {"fiscal_sign": "qr"}
    out["source_lines"] = {"total": {"text": "JAMI: 71000,00", "conf": 0.97}}
    m = to_medadvance(out, today=date(2026, 11, 25))
    assert m["fields"] == {"date": "2026-11-24", "time": "13:29:00", "amount": "71000.00", "receipt": "2000",
                           "seller": "FAST FOOD SYSTEM MCHJ", "inn": "310839380", "fiscalSign": "285421523353",
                           "fiscalModule": "VG544170029013", "payment": "Банковская карта", "currency": "UZS"}
    assert m["missing"] == [] and m["warnings"] == []
    assert m["sources"]["fiscalSign"]["description"] == "Из QR-кода чека"
    assert m["sources"]["amount"] == {"text": "JAMI: 71000,00", "confidence": 0.97, "description": "Итоговая сумма чека"}


def test_values_medadvance_would_reject_are_left_empty_with_a_warning(validate_fields):
    m = to_medadvance(_out(datetime="2027-01-05T10:00:00", seller_tin="3056458", total=5000.0, payment="other",
                           seller_name="X" * 200, receipt_number="1" * 50), pages=3, today=date(2026, 11, 25))
    f = m["fields"]
    assert f["date"] == "" and f["inn"] == "" and f["receipt"] == "" and len(f["seller"]) == 160
    assert f["payment"] == "" and m["missing"] == ["date", "receipt"]
    assert len(m["warnings"]) == 5  # future date, short INN, mixed payment, no QR, PDF pages
    validate_fields("fiscal", f, partial=True)


def test_unread_qr_gives_the_rebuilt_link():
    link = "https://ofd.soliq.uz/check?t=LG420211631939&r=234252&c=20261124213212&s=708619150117"
    m = to_medadvance(_out(total=20400.0, qr={"raw": None, "rebuilt": link}))
    assert m["summary"]["qrRebuilt"] == link and link in m["warnings"][0]
