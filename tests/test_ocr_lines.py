"""Line grouping must keep a value on the line of its label when the receipt is tilted or curved."""
from receipt.ocr import group_into_lines


def _word(text, x, y, slope, w=300, h=40):
    """A word box at (x, y) on text that falls `slope` px per px to the right."""
    poly = [[x, y], [x + w, y + slope * w], [x + w, y + slope * w + h], [x, y + h]]
    xs, ys = [p[0] for p in poly], [p[1] for p in poly]
    return {"text": text, "conf": 0.9, "poly": poly, "box": [min(xs), min(ys), max(xs), max(ys)]}


ROWS = [("Sana va vaqt", "04-11-2026 21:03:56"), ("Chek", "36812"), ("Savdo raqami", "14994611046810"),
        ("Narx", "24 000.00"), ("Naqdsiz", "24 000.00"), ("Jami", "24 000.00")]


def _receipt(slope_at, n=6):
    rows = (ROWS * 5)[:n]
    words = []
    for i, (label, value) in enumerate(rows):
        y, s = 100 + 60 * i, slope_at(i)
        words.append(_word(label, 0, y, s))
        words.append(_word(value, 900, y + s * 900, s))  # the value sits lower by slope * distance
    return rows, words


def test_tilted_receipt_keeps_label_and_value_together():
    rows, words = _receipt(lambda i: 0.08)  # 4.6 degrees: a value 900 px away is 72 px (> 1 line) lower
    assert [l["text"] for l in group_into_lines(words)] == [f"{a} {b}" for a, b in rows]


def test_curved_receipt_uses_local_slope():
    # crumpled paper: flat at the top, ~6 % slope at the bottom (as measured on photo r08_c,
    # about 0.3 % more per line); one global slope would put the lower values on the wrong line
    rows, words = _receipt(lambda i: -0.003 * i, n=24)
    assert [l["text"] for l in group_into_lines(words)] == [f"{a} {b}" for a, b in rows]


def test_straight_receipt_unchanged():
    rows, words = _receipt(lambda i: 0.0)
    assert [l["text"] for l in group_into_lines(words)] == [f"{a} {b}" for a, b in rows]
