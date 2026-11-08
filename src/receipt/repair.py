"""Repair of the 0 -> 8/6/9 confusion using the redundancy of a receipt.

Receipt printers often print zero with a dot or slash inside ("0" with a dot),
and OCR reads it as 8, 6 or 9: "24 000.00" becomes "24 888.66".
The same amount is printed several times (Narx, Naqdsiz, Jami, To'lov uchun jami),
and each copy is misread differently. For every reading we list the values it
could really be (any 8/6/9 may be a 0) and keep the value most readings agree on.
"""
import itertools
import re
from collections import Counter

from .normalize import parse_amount, parse_datetime, parse_qty

CONFUSED = "689"  # digits a dotted zero is misread as
CONFUSED_DATE = "6892"  # dates are checked for validity, so 2 -> 0 is safe there
MAX_POSITIONS = 10  # 2**10 candidates per reading at most


def candidates(text, parse=parse_amount, confused=CONFUSED):
    """{value: number_of_substitutions} for every way of turning confusable digits into 0."""
    if text is None:
        return {}
    out = {}
    for s in _decimal_variants(str(text).strip()):
        pos = [i for i, c in enumerate(s) if c in confused][:MAX_POSITIONS]
        for k in range(len(pos) + 1):
            for subset in itertools.combinations(pos, k):
                chars = list(s)
                for i in subset:
                    chars[i] = "0"
                v = parse("".join(chars))
                if v is not None and (v not in out or k < out[v]):
                    out[v] = k
    return out


def _decimal_variants(s):
    """'24 008 60' may be '24 008.60' with the decimal point lost."""
    return [s, re.sub(r"\s(\d{2})$", r".\1", s)] if re.search(r"\d\s\d{2}$", s) else [s]


def _roundness(v):
    """Whole sum first, then trailing zeros: UZS prices are round (8 000 rather than 8 009)."""
    if v != int(v):
        return -1
    n, z = int(v), 0
    while n and n % 10 == 0:
        n, z = n // 10, z + 1
    return z


def agree(main, others):
    """Value of `main` (a reading) that most `others` readings can also be.

    Ties go to whole sums (cents are almost always .00), then to fewer
    substitutions in `main`, then to round sums. Returns None if no other reading agrees.
    """
    cand = candidates(main)
    if not cand:
        return None
    sets = [candidates(o) for o in others if o is not None]
    support = Counter()
    for v in cand:
        support[v] = sum(v in s for s in sets)
    best = max(cand, key=lambda v: (support[v], v == int(v), -cand[v], _roundness(v)))
    return best if support[best] > 0 else None


def consensus(readings, min_votes=2):
    """Value that at least `min_votes` readings can all be (when the total line itself is unreadable)."""
    sets = [candidates(r) for r in readings if r is not None]
    votes = Counter(v for c in sets for v in c if v > 0)
    if not votes:
        return None
    best = max(votes, key=lambda v: (votes[v], v == int(v), -sum(c.get(v, 0) for c in sets), _roundness(v)))
    return best if votes[best] >= min_votes else None


def could_be_zero(text):
    return 0.0 in candidates(text)


def repair_item(item, receipt_total=None, single=False):
    """Choose quantity, price and total so that quantity × price = total (with fewest digit changes)."""
    q = candidates(item.get("_raw_qty"), parse_qty) or ({item["quantity"]: 0} if item.get("quantity") is not None else {})
    p = candidates(item.get("_raw_price")) or ({item["price"]: 0} if item.get("price") is not None else {})
    t = candidates(item.get("_raw_total")) or ({item["total"]: 0} if item.get("total") is not None else {})
    best, best_cost = None, None
    for (qv, qc), (pv, pc) in itertools.product(q.items(), p.items()):
        tv = round(qv * pv, 2)
        if t:
            match = [c for v, c in t.items() if abs(v - tv) <= 0.05]
            if not match:
                continue
            tc = min(match)
        else:
            tc = 0
        # a single item must cost exactly the receipt total: strong evidence
        cost = qc + pc + tc - (3 if single and receipt_total is not None and abs(tv - receipt_total) <= 0.05 else 0)
        if best_cost is None or cost < best_cost:
            best, best_cost = (qv, pv, tv), cost
    if best:
        item["quantity"], item["price"], item["total"] = best
    return item


def repair_datetime(text):
    """Fix confusable digits so the date/time becomes valid (day <= 31, hour < 24, ...)."""
    if text is None:
        return None
    cand = candidates(text, parse=lambda s: s, confused=CONFUSED_DATE)
    for s in sorted(cand, key=cand.get):
        v = parse_datetime(s)
        if v and 2020 <= int(v[:4]) <= 2035:
            return v
    return None
