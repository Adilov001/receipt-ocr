import cv2
import numpy as np
import pytest

from receipt.qr import decode_qr, parse_qr

URL = "https://ofd.soliq.uz/check?t=NA000000006920&r=36785&c=20261104134726&s=352606397030"


def test_parse_ofd_link():
    q = parse_qr(URL)
    assert q["host"] == "ofd.soliq.uz"
    assert q["path"] == "/check"
    assert q["params"] == {"t": "NA000000006920", "r": "36785", "c": "20261104134726", "s": "352606397030"}
    assert q["fields"] == {
        "fiscal_module": "NA000000006920",
        "receipt_number": "36785",
        "datetime": "2026-11-04T13:47:26",
        "fiscal_sign": "352606397030",
    }


def test_parse_unknown_params_kept_but_not_mapped():
    q = parse_qr("https://example.uz/x?t=AB123&foo=1")
    assert q["params"] == {"t": "AB123", "foo": "1"}
    assert q["fields"] == {"fiscal_module": "AB123"}


def test_parse_non_url_payload():
    assert parse_qr("hello")["params"] == {}
    assert parse_qr(None)["fields"] == {}


def _qr_image(text, scale=6):
    code = cv2.QRCodeEncoder.create().encode(text)
    code = cv2.resize(code, None, fx=scale, fy=scale, interpolation=cv2.INTER_NEAREST)
    canvas = np.full((code.shape[0] + 200, code.shape[1] + 200), 255, np.uint8)
    canvas[100:-100, 100:-100] = code
    return canvas


def test_decode_clean():
    out = decode_qr(_qr_image(URL))
    assert out["decoded"] and out["plain_success"] and out["raw"] == URL


@pytest.mark.parametrize("angle", [0, 15, 40])
def test_decode_rotated_and_faded(angle):
    img = _qr_image(URL)
    h, w = img.shape
    img = cv2.warpAffine(img, cv2.getRotationMatrix2D((w / 2, h / 2), angle, 1), (w, h), borderValue=255)
    img = (img.astype(np.float32) * 0.35 + 150).astype(np.uint8)   # low contrast, like faded thermal print
    out = decode_qr(img)
    assert out["decoded"] and out["raw"] == URL


def test_rebuilt_check_url():
    from receipt.qr import rebuild_check_url
    f = {"fiscal_module": "LG420230605218", "receipt_number": "289471", "datetime": "2026-11-20T13:56:17",
         "fiscal_sign": "045133448457"}
    url = "https://ofd.soliq.uz/check?t=LG420230605218&r=289471&c=20261120135617&s=045133448457"
    assert rebuild_check_url(f, "Sana va vaqt 20-11-2026 13:56:17") == url
    assert rebuild_check_url(f, "20-11-2026 13:56") is None  # no seconds printed: they would be a guess
    assert rebuild_check_url({**f, "datetime": "2026-11-20T13:56:00"}, "Sana: 20.11.2026 13:56:00") is None  # order time
    assert rebuild_check_url({**f, "fiscal_sign": "45133448457"}, "13:56:17") is None  # 11 digits
    assert rebuild_check_url({**f, "fiscal_sign": "420230605218"}, "13:56:17") is None  # the FM digits
    assert rebuild_check_url({**f, "receipt_number": None}, "13:56:17") is None
