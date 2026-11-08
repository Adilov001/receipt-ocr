"""Receipt recognition: preprocessing, OCR, QR decoding, field extraction, reconciliation."""

FIELDS = [
    "seller_name", "seller_tin", "address", "datetime", "receipt_number",
    "fiscal_module", "fiscal_sign", "vat", "total", "payment",
]
