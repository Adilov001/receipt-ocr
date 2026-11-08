"""Quality metrics. Definitions follow section 5 of the specification."""
from collections import Counter

from rapidfuzz.distance import Levenshtein

from . import FIELDS
from .normalize import norm_field, norm_item, norm_text_for_metric


def edit_counts(ref, hyp):
    """(S + D + I, N) for sequences (str for CER, list of words for WER)."""
    return Levenshtein.distance(ref, hyp), len(ref)


def cer(ref, hyp, lowercase=True):
    r, h = norm_text_for_metric(ref, lowercase), norm_text_for_metric(hyp, lowercase)
    d, n = edit_counts(r, h)
    return d / n if n else float(bool(h))


def wer(ref, hyp, lowercase=True):
    r, h = norm_text_for_metric(ref, lowercase).split(), norm_text_for_metric(hyp, lowercase).split()
    d, n = edit_counts(r, h)
    return d / n if n else float(bool(h))


def text_counts(ref, hyp, lowercase=True):
    """Raw counts for corpus-level aggregation: (char_err, char_n, word_err, word_n)."""
    r, h = norm_text_for_metric(ref, lowercase), norm_text_for_metric(hyp, lowercase)
    ce, cn = edit_counts(r, h)
    we, wn = edit_counts(r.split(), h.split())
    return ce, cn, we, wn


def field_matches(gt, pred, fields=FIELDS):
    """{field: True/False} for every field of the ground truth (null must be predicted as null)."""
    return {f: norm_field(f, gt.get(f)) == norm_field(f, pred.get(f)) for f in fields if f in gt}


def field_accuracy(gt, pred, fields=FIELDS):
    m = field_matches(gt, pred, fields)
    return sum(m.values()) / len(m) if m else 0.0


def item_counts(gt_items, pred_items):
    """(true positives, predicted, ground truth): an item is correct if all four attributes match."""
    g = Counter(norm_item(i) for i in gt_items or [])
    p = Counter(norm_item(i) for i in pred_items or [])
    tp = sum((g & p).values())
    return tp, sum(p.values()), sum(g.values())


def prf(tp, n_pred, n_gt):
    p = tp / n_pred if n_pred else (1.0 if not n_gt else 0.0)
    r = tp / n_gt if n_gt else (1.0 if not n_pred else 0.0)
    f1 = 2 * p * r / (p + r) if p + r else 0.0
    return p, r, f1
