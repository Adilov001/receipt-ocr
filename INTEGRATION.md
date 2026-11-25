# Integration with MedAdvance

How the MedAdvance backend ([airi-club/MedAdvance](https://github.com/airi-club/MedAdvance), Django,
`backend/receipts`) can use this service for **fiscal receipts**. Nothing in MedAdvance is changed by
this repository: this document is the contract, and the code sample at the end is for the MedAdvance team.

## The service

| | |
|---|---|
| Endpoint | `POST /api/v1/recognize`, multipart form, field `file` |
| Files | JPEG, PNG, WebP, BMP, TIFF, HEIC/HEIF (iPhone), PDF (first page; at most 5 pages), up to 15 MB |
| Port | **8001** (`make api` or `docker run -p 8001:8001 receipt-ocr`); MedAdvance runs on 8000 |
| Access | header `X-API-Key: <key>` or `Authorization: Bearer <key>`, when `RECEIPT_OCR_API_KEY` is set on the service (no variable = open, for local development) |
| Health | `GET /api/v1/health` → `{"status": "ok"}` when the models are loaded (about 20 s after start) |
| Time | about 5–7 s per photo on a laptop CPU; requests are processed one at a time, so run several containers for more users |
| Timeout | use 60 s on the client side |

Send only **fiscal** receipts (document type `fiscal`): the rules are written for Uzbek cash-register
receipts with the soliq.uz QR code. Bank receipts are not supported yet.

## The answer: the `medadvance` block

The answer has the full result (`result`, `checks`, `text`, ...; see README "Output JSON") and a
`medadvance` block made for MedAdvance:

```json
{
  "fields": {
    "date": "2026-11-12", "time": "16:00:46", "amount": "24000.00", "receipt": "12264",
    "seller": "ERA", "inn": "31802964140017", "fiscalSign": "472779471534",
    "fiscalModule": "LG420211609580", "payment": "Банковская карта", "currency": "UZS"
  },
  "sources": {
    "amount": {"text": "24 000.00 UZS", "confidence": 0.94, "description": "Итоговая сумма чека"},
    "fiscalSign": {"text": "Fiskal imzo 472779471534", "confidence": 0.994, "description": "Фискальный признак"}
  },
  "missing": [],
  "warnings": [],
  "summary": {
    "qr": "https://ofd.soliq.uz/check?t=LG420211609580&r=12264&c=20261112160046&s=472779471534",
    "qrRebuilt": "", "documentType": "fiscal", "consistent": true,
    "items": [{"name": "Aralashmalar", "quantity": 1.0, "price": 24000.0, "total": 24000.0}]
  }
}
```

(`sources` shortened; it has an entry for every non-empty field.)

| Key | Meaning |
|---|---|
| `fields` | the 10 fiscal fields of `Receipt.fields`, same names and formats as `src/fiscalParser.js`. They **pass `validate_fields("fiscal", …)` of `backend/receipts/validation.py` as they are**: a value that would fail (a future date, an INN that is not 9 or 14 digits, a receipt number over 40 characters) is left empty and explained in `warnings`. Empty field = `""`. |
| `sources` | per field: the receipt line it was read from (`text`), OCR confidence 0–1, a description. Values taken from the QR code have `"Из QR-кода чека"` and confidence 1. |
| `missing` | required fields (`date`, `time`, `amount`, `receipt`) that are empty: the user must fill them before **Save** |
| `warnings` | texts in Russian for the user: OCR and QR differ, items do not add up, mixed payment, QR not read |
| `summary.qr` | the decoded soliq.uz link (empty if the QR code was not read) |
| `summary.qrRebuilt` | when the QR code was not read: the check link rebuilt from the printed requisites (15 of 16 right on our photos) |
| `summary.items` | the receipt's items (name, quantity, price, total) |
| `summary.consistent` | true when the items add up to the total and nothing contradicts the QR code |

Field formats: `date` `YYYY-MM-DD`; `time` `HH:MM:SS`; `amount` `"56000.00"`; `payment`
`"Банковская карта"` or `"Наличные"` (empty for mixed payment); `currency` `"UZS"`.

## Errors

| Status | When | Body |
|---|---|---|
| 400 | empty file | `{"detail": "Empty file."}` |
| 401 | missing or wrong key | `{"detail": "Missing or wrong API key (header X-API-Key)."}` |
| 413 | file over 15 MB | `{"detail": "File larger than 15 MB."}` |
| 415 | not an image/PDF, or a PDF with more than 5 pages | `{"detail": "..."}` |
| 422 | wrong form (no `file` field) | FastAPI validation error |

A receipt that is readable but where nothing was found is **not** an error: the answer is 200 with
empty fields in `missing`. On a network error or timeout, MedAdvance can keep the receipt as a draft
for manual entry.

## Suggested use in the MedAdvance backend (for the MedAdvance team)

Where a fiscal receipt is created (`ReceiptListCreateView.perform_create`), after the file is saved:

```python
import os
import requests

OCR_URL = os.getenv("RECEIPT_OCR_URL", "http://127.0.0.1:8001")
OCR_KEY = os.getenv("RECEIPT_OCR_API_KEY", "")

def recognize_fiscal(receipt):
    """Fill a new fiscal receipt draft from the OCR service; on any error leave it for manual entry."""
    try:
        with receipt.file.open("rb") as f:
            r = requests.post(f"{OCR_URL}/api/v1/recognize",
                              files={"file": (receipt.original_name, f, receipt.content_type)},
                              headers={"X-API-Key": OCR_KEY} if OCR_KEY else {}, timeout=60)
        r.raise_for_status()
    except requests.RequestException:
        return
    answer = r.json()["medadvance"]
    receipt.recognition = answer                              # the reserved JSON field
    filled = {k: v for k, v in answer["fields"].items() if v}
    typed = {k: v for k, v in (receipt.fields or {}).items() if v}
    receipt.fields = {**filled, **typed}                      # values the user typed win
    receipt.save(update_fields=("recognition", "fields", "updated_at"))
```

Settings on the MedAdvance side: `RECEIPT_OCR_URL` and `RECEIPT_OCR_API_KEY` in `backend/.env`;
`requests` in `backend/requirements.txt`. Running OCR inside the request takes 5–7 s; for many users
a background task (Celery, RQ) is better.

## Keeping the contract

`tests/test_medadvance.py` runs a copy of MedAdvance's `backend/receipts/validation.py`
(`tests/medadvance_validation.py`, from commit `01f5227`) on the `medadvance.fields` of every
labelled receipt. If MedAdvance changes its fields or validation, update that copy and the tests
show what has to change here.
