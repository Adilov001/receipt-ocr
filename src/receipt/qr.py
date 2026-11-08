"""QR detection, decoding with retries, and parsing of the fiscal link."""
from urllib.parse import parse_qs, urlparse

import cv2
import numpy as np

from .normalize import parse_amount, parse_datetime

try:
    import zxingcpp
except ImportError:  # pragma: no cover
    zxingcpp = None


def _gray(img):
    return img if img.ndim == 2 else cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def _decode_once(img):
    """Return (text, polygon) or (None, None). zxing-cpp first, OpenCV as fallback."""
    if zxingcpp is not None:
        try:
            for r in zxingcpp.read_barcodes(img, formats=zxingcpp.BarcodeFormat.QRCode):
                if r.text:
                    p = r.position
                    poly = [[p.top_left.x, p.top_left.y], [p.top_right.x, p.top_right.y],
                            [p.bottom_right.x, p.bottom_right.y], [p.bottom_left.x, p.bottom_left.y]]
                    return r.text, np.array(poly, dtype=np.float32)
        except Exception:
            pass
    try:
        text, pts, _ = cv2.QRCodeDetector().detectAndDecode(img)
        if text:
            return text, pts.reshape(-1, 2).astype(np.float32)
    except cv2.error:
        pass
    return None, None


def _locate(img):
    try:
        ok, pts = cv2.QRCodeDetector().detect(img)
        if ok and pts is not None:
            return pts.reshape(-1, 2).astype(np.float32)
    except cv2.error:
        pass
    return None


def _warp_region(gray, pts, size=600, margin=0.15):
    c = pts.mean(axis=0)
    pts = c + (pts - c) * (1 + 2 * margin)
    dst = np.array([[0, 0], [size, 0], [size, size], [0, size]], dtype=np.float32)
    m = cv2.getPerspectiveTransform(pts.astype(np.float32), dst)
    return cv2.warpPerspective(gray, m, (size, size), borderValue=255)


def _scaled(fn, s):
    def wrapped(g):
        return cv2.resize(fn(g), None, fx=s, fy=s, interpolation=cv2.INTER_CUBIC if s > 1 else cv2.INTER_AREA)
    return wrapped


def _retries():
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    otsu = lambda g: cv2.threshold(g, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    adapt = lambda g: cv2.adaptiveThreshold(g, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 10)
    sharpen = lambda g: cv2.addWeighted(g, 1.8, cv2.GaussianBlur(g, (0, 0), 3), -0.8, 0)
    ident = lambda g: g
    return [
        ("downscale_0.5", _scaled(ident, 0.5)),
        ("upscale_2", _scaled(ident, 2.0)),
        ("clahe", clahe.apply),
        ("otsu", otsu),
        ("adaptive", adapt),
        ("sharpen", sharpen),
        ("otsu_downscale", _scaled(otsu, 0.5)),
    ]


def decode_qr(img, extra_images=(), retries=True):
    """Decode the QR code of a receipt photo.

    Returns dict(raw, decoded, attempt, plain_success, polygon, polygon_on).
    'plain' = a single attempt on the unprocessed image; everything after it
    counts as "after processing" in the QR decode metric.
    """
    out = {"raw": None, "decoded": False, "attempt": None, "plain_success": False,
           "polygon": None, "polygon_on": None}
    gray = _gray(img)
    text, poly = _decode_once(gray)
    if text:
        out.update(raw=text, decoded=True, attempt="plain", plain_success=True,
                   polygon=poly.tolist(), polygon_on="original")
        return out
    if not retries:
        return out

    # 1) locate the code, warp it to a square, then enhance
    pts = _locate(gray)
    if pts is not None:
        out.update(polygon=pts.tolist(), polygon_on="original")
        roi = _warp_region(gray, pts)
        for name, fn in [("roi", lambda g: g)] + _retries():
            text, _ = _decode_once(fn(roi))
            if text:
                out.update(raw=text, decoded=True, attempt=f"roi+{name}")
                return out

    # 2) whole-image transforms
    for name, fn in _retries():
        try:
            text, poly = _decode_once(fn(gray))
        except cv2.error:
            continue
        if text:
            out.update(raw=text, decoded=True, attempt=name)
            return out

    # 3) the preprocessed receipt image(s)
    for i, ex in enumerate(extra_images):
        text, poly = _decode_once(_gray(ex))
        if text:
            out.update(raw=text, decoded=True, attempt=f"preprocessed_{i}",
                       polygon=poly.tolist(), polygon_on=f"preprocessed_{i}")
            return out
    return out


def parse_qr(raw, param_map=None):
    """Split the QR payload into URL parts, raw parameters and mapped receipt fields."""
    param_map = param_map or {"t": "fiscal_module", "r": "receipt_number", "c": "datetime", "s": "fiscal_sign"}
    res = {"raw": raw, "url": None, "host": None, "path": None, "params": {}, "fields": {}}
    if not raw:
        return res
    raw = raw.strip()
    if raw.lower().startswith(("http://", "https://")):
        u = urlparse(raw)
        res.update(url=raw, host=u.hostname, path=u.path)
        query = u.query
    else:
        query = raw
    if "=" in query:
        params = parse_qs(query.replace(";", "&"), keep_blank_values=True)
        res["params"] = {k: v[0] for k, v in params.items()}
    for key, value in res["params"].items():
        field = param_map.get(key)
        if not field:
            continue
        if field == "datetime":
            value = parse_datetime(value) or value
        elif field in ("total", "vat"):
            value = parse_amount(value)
        res["fields"][field] = value
    return res
