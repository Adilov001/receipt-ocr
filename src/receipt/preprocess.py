"""Receipt image preprocessing. Each step can be switched off in the config for ablation."""
import cv2
import numpy as np


def _order(pts):
    pts = np.asarray(pts, dtype=np.float32).reshape(4, 2)
    s, d = pts.sum(1), np.diff(pts, axis=1).ravel()
    return np.array([pts[s.argmin()], pts[d.argmin()], pts[s.argmax()], pts[d.argmax()]], dtype=np.float32)


def _paper_mask(img, size=800):
    """Mask of bright, unsaturated pixels (receipt paper) on a downscaled copy; returns (mask, scale)."""
    scale = size / max(img.shape[:2])
    small = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
    hsv = cv2.cvtColor(small, cv2.COLOR_BGR2HSV)
    sat, val = hsv[..., 1], hsv[..., 2]
    thr, _ = cv2.threshold(val, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    mask = ((sat < 35) & (val > max(thr, 150))).astype(np.uint8) * 255
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((7, 7), np.uint8))
    return mask, scale


def paper_mask(img):
    """Full-resolution mask of the largest paper region (used to keep deskew on the receipt text)."""
    mask, _ = _paper_mask(img)
    n, lab, st, _ = cv2.connectedComponentsWithStats(mask)
    if n < 2:
        return None
    big = (lab == 1 + st[1:, cv2.CC_STAT_AREA].argmax()).astype(np.uint8) * 255
    big = cv2.morphologyEx(big, cv2.MORPH_CLOSE, np.ones((25, 25), np.uint8))
    return cv2.resize(big, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_NEAREST)


def find_receipt(img):
    """Quadrilateral of the receipt (bright, unsaturated paper), or None."""
    mask, scale = _paper_mask(img)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return None
    c = max(contours, key=cv2.contourArea)
    area = cv2.contourArea(c) / mask.size
    if area < 0.08 or area > 0.97:
        return None
    # A receipt is a solid rectangle; a blob merged with the background is not.
    # Better no crop than a crop that cuts the receipt.
    (_, _), (rw, rh), _ = cv2.minAreaRect(c)
    if cv2.contourArea(c) / max(rw * rh, 1) < 0.8:
        return None
    approx = cv2.approxPolyDP(c, 0.02 * cv2.arcLength(c, True), True)
    if len(approx) == 4 and cv2.isContourConvex(approx):
        quad = approx.reshape(4, 2)
    else:
        quad = cv2.boxPoints(cv2.minAreaRect(c))
    return _order(quad / scale)


def warp(img, quad):
    tl, tr, br, bl = quad
    w = int(max(np.linalg.norm(tr - tl), np.linalg.norm(br - bl)))
    h = int(max(np.linalg.norm(bl - tl), np.linalg.norm(br - tr)))
    dst = np.array([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]], dtype=np.float32)
    out = cv2.warpPerspective(img, cv2.getPerspectiveTransform(quad, dst), (w, h),
                              borderMode=cv2.BORDER_REPLICATE)
    return out if h >= w else cv2.rotate(out, cv2.ROTATE_90_CLOCKWISE)


def estimate_skew(gray, max_angle=8.0, step=0.25, mask=None):
    """Angle that maximizes the variance of the horizontal projection profile.
    With a paper mask, only ink on the receipt counts (background texture is ignored)."""
    scale = min(1000 / max(gray.shape), 1.0)
    small = cv2.resize(gray, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
    ink = cv2.adaptiveThreshold(small, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 25, 15)
    if mask is not None:
        m = cv2.resize(mask, (small.shape[1], small.shape[0]), interpolation=cv2.INTER_NEAREST)
        ink = cv2.bitwise_and(ink, cv2.erode(m, np.ones((15, 15), np.uint8)))
    h, w = ink.shape
    best, best_score = 0.0, -1.0
    for a in np.arange(-max_angle, max_angle + 1e-6, step):
        m = cv2.getRotationMatrix2D((w / 2, h / 2), a, 1.0)
        rot = cv2.warpAffine(ink, m, (w, h), flags=cv2.INTER_NEAREST)
        prof = rot.sum(axis=1, dtype=np.float64)
        score = np.var(np.diff(prof))
        if score > best_score:
            best, best_score = a, score
    return float(best)


def rotate(img, angle):
    h, w = img.shape[:2]
    m = cv2.getRotationMatrix2D((w / 2, h / 2), angle, 1.0)
    return cv2.warpAffine(img, m, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)


def flatten_illumination(gray):
    k = max(15, gray.shape[1] // 40) | 1
    bg = cv2.medianBlur(cv2.dilate(gray, np.ones((7, 7), np.uint8)), k)
    return cv2.divide(gray, bg, scale=255)


def _paper_aspect(img, mask):
    """Width / height of the receipt: the paper mask's bounding box, or the whole (warped) image."""
    if mask is not None:
        ys, xs = np.nonzero(mask)
        return (xs.max() - xs.min() + 1) / (ys.max() - ys.min() + 1)
    return img.shape[1] / img.shape[0]


def osd_rotation(gray):
    """Rotation (0/90/180/270, clockwise) Tesseract OSD suggests, or 0 if it is unsure or unavailable."""
    try:
        import shutil

        import pytesseract
        pytesseract.pytesseract.tesseract_cmd = shutil.which("tesseract") or "tesseract"
        small = cv2.resize(gray, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        osd = pytesseract.image_to_osd(small, config="--psm 0", output_type=pytesseract.Output.DICT)
        return osd["rotate"] if osd.get("orientation_conf", 0) >= 1.0 else 0
    except Exception:
        return 0


def _rot90(img, k):
    """Rotate by k * 90 degrees clockwise."""
    return np.rot90(img, -k).copy() if img is not None and k % 4 else img


def preprocess(img, cfg):
    """Run the enabled steps. Returns dict(final, stages, info)."""
    p = cfg["preprocess"]
    stages, info = {}, {}
    h, w = img.shape[:2]
    if max(h, w) > p["max_side"]:
        s = p["max_side"] / max(h, w)
        img = cv2.resize(img, None, fx=s, fy=s, interpolation=cv2.INTER_AREA)

    mask = None
    if p.get("crop"):
        quad = find_receipt(img)
        info["receipt_found"] = quad is not None
        if quad is not None:
            img = warp(img, quad)
            stages["crop"] = img
        else:
            mask = paper_mask(img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if p.get("orient") and _paper_aspect(gray, mask) > 1.2:
        # receipts are long and narrow: one lying sideways is turned upright (180° is fixed by OSD below)
        gray, mask = _rot90(gray, 1), _rot90(mask, 1)
        info["rotated"] = 90
        stages["orient"] = gray

    if p.get("deskew"):
        angle = estimate_skew(gray, p["deskew_range"], mask=mask)
        info["skew_deg"] = angle
        if abs(angle) > 0.2:
            gray = rotate(gray, angle)
            if mask is not None:
                h, w = mask.shape
                mask = cv2.warpAffine(mask, cv2.getRotationMatrix2D((w / 2, h / 2), angle, 1.0), (w, h),
                                      flags=cv2.INTER_NEAREST)
        stages["deskew"] = gray

    if mask is not None:
        # no clean 4-corner crop: blank out the background and cut to the paper's bounding box
        mask = cv2.dilate(mask, np.ones((41, 41), np.uint8))
        gray = np.where(mask > 0, gray, 255).astype(np.uint8)
        ys, xs = np.nonzero(mask)
        gray = gray[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
        stages["background_masked"] = gray

    if p.get("orient"):
        k = osd_rotation(gray) // 90
        if k:
            gray = _rot90(gray, k)
            info["rotated"] = (info.get("rotated", 0) + 90 * k) % 360
            stages["orient_osd"] = gray

    # Tesseract wants ~25-30 px letters: bring the receipt (not the whole photo) to min_width
    if gray.shape[1] < p["min_width"]:
        s = p["min_width"] / gray.shape[1]
        gray = cv2.resize(gray, None, fx=s, fy=s, interpolation=cv2.INTER_CUBIC)

    if p.get("illumination"):
        gray = flatten_illumination(gray)
        stages["illumination"] = gray

    if p.get("clahe"):
        gray = cv2.createCLAHE(clipLimit=p["clahe_clip"], tileGridSize=(8, 8)).apply(gray)
        stages["clahe"] = gray

    if p.get("binarize"):
        gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 15)
        stages["binarize"] = gray

    return {"final": gray, "stages": stages, "info": info}
