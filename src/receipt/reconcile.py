"""Arithmetic checks and OCR <-> QR reconciliation."""
from .normalize import norm_field

MATCH, MISMATCH, NO_DATA = "match", "mismatch", "no_data"


def _close(a, b, cfg):
    tol = max(cfg["abs_tol"], cfg["rel_tol"] * max(abs(a), abs(b)))
    return abs(a - b) <= tol


def reconcile(fields, items, qr_fields, cfg):
    rc = cfg["reconcile"]
    checks = []

    for k, it in enumerate(items, 1):
        q, p, t = it.get("quantity"), it.get("price"), it.get("total")
        if None in (q, p, t):
            checks.append({"check": f"item {k}: qty × price = total", "status": NO_DATA,
                           "expected": None, "actual": t, "kind": "arithmetic"})
        else:
            exp = round(q * p, 2)
            checks.append({"check": f"item {k}: qty × price = total", "status": MATCH if _close(exp, t, rc) else MISMATCH,
                           "expected": exp, "actual": t, "kind": "arithmetic"})

    totals = [it.get("total") for it in items]
    total = fields.get("total")
    if not items or None in totals or total is None:
        st, exp = NO_DATA, (round(sum(totals), 2) if items and None not in totals else None)
    else:
        exp = round(sum(totals), 2)
        st = MATCH if _close(exp, total, rc) else MISMATCH
    checks.append({"check": "Σ items = total", "status": st, "expected": exp, "actual": total, "kind": "arithmetic"})

    for field, qv in (qr_fields or {}).items():
        ov = fields.get(field)
        a, b = norm_field(field, ov), norm_field(field, qv)
        st = NO_DATA if a is None or b is None else (MATCH if a == b else MISMATCH)
        checks.append({"check": f"OCR ↔ QR: {field}", "status": st, "expected": qv, "actual": ov, "kind": "qr"})
    return checks


def is_consistent(checks):
    """Passed the arithmetic check on the total and has no mismatch anywhere."""
    if any(c["status"] == MISMATCH for c in checks):
        return False
    total = [c for c in checks if c["check"] == "Σ items = total"]
    return bool(total) and total[0]["status"] == MATCH
