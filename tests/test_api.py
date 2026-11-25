"""REST API: a real receipt photo gives the expected JSON; bad uploads give clear errors."""
import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def client():
    import api
    with TestClient(api.app) as c:  # runs the start-up warm-up
        yield c


def test_health(client):
    r = client.get("/api/v1/health")
    assert r.status_code == 200 and r.json()["status"] == "ok"


def test_recognize_real_receipt(client):
    gt = json.loads((ROOT / "data/gt/r17.json").read_text())
    with open(ROOT / "data/images/r17_a.jpg", "rb") as f:
        r = client.post("/api/v1/recognize", files={"file": ("r17_a.jpg", f, "image/jpeg")})
    assert r.status_code == 200
    body = r.json()
    res = body["result"]
    assert res["total"] == gt["total"] and res["fiscal_sign"] == gt["fiscal_sign"]
    assert "Jami" in body["text"] and body["source_lines"]["total"]["text"]
    assert res["qr"]["decoded"] and res["qr"]["raw"] == gt["qr"]["raw"]
    assert {c["status"] for c in body["checks"]} <= {"match", "mismatch", "no_data"}
    assert body["timings"]["request"] > 0


def test_empty_and_not_an_image(client):
    assert client.post("/api/v1/recognize", files={"file": ("a.jpg", b"", "image/jpeg")}).status_code == 400
    r = client.post("/api/v1/recognize", files={"file": ("a.heic", b"not an image", "image/heic")})
    assert r.status_code == 415


def _as(fmt, src, **kw):
    """A real receipt photo re-encoded as HEIC (iPhone) or PDF, in memory."""
    import io

    import pillow_heif
    from PIL import Image
    pillow_heif.register_heif_opener()
    buf = io.BytesIO()
    imgs = [Image.open(src).convert("RGB")] * kw.pop("pages", 1)
    imgs[0].save(buf, format=fmt, save_all=len(imgs) > 1, append_images=imgs[1:], **kw)
    return buf.getvalue()


@pytest.mark.parametrize("fmt,name,mime", [("HEIF", "r17.heic", "image/heic"), ("PDF", "r17.pdf", "application/pdf")])
def test_heic_and_pdf_give_the_same_fields(client, fmt, name, mime):
    gt = json.loads((ROOT / "data/gt/r17.json").read_text())
    data = _as(fmt, ROOT / "data/images/r17_a.jpg", **({"resolution": 300} if fmt == "PDF" else {"quality": 95}))
    r = client.post("/api/v1/recognize", files={"file": (name, data, mime)})
    assert r.status_code == 200, r.text
    body = r.json()
    assert body["pages"] == 1
    assert body["result"]["total"] == gt["total"] and body["result"]["fiscal_module"] == gt["fiscal_module"]


def test_pdf_with_too_many_pages(client):
    data = _as("PDF", ROOT / "data/images/r17_q.jpg", pages=6, resolution=72)
    r = client.post("/api/v1/recognize", files={"file": ("many.pdf", data, "application/pdf")})
    assert r.status_code == 415 and "6 pages" in r.json()["detail"]


def test_unknown_engine(client):
    with open(ROOT / "data/images/r17_a.jpg", "rb") as f:
        r = client.post("/api/v1/recognize?engine=foo", files={"file": ("r.jpg", f, "image/jpeg")})
    assert r.status_code == 422


def test_medadvance_block(client):
    with open(ROOT / "data/images/r17_a.jpg", "rb") as f:
        body = client.post("/api/v1/recognize", files={"file": ("r17_a.jpg", f, "image/jpeg")}).json()
    gt = json.loads((ROOT / "data/gt/r17.json").read_text())
    m = body["medadvance"]
    assert m["fields"]["amount"] == f"{gt['total']:.2f}" and m["fields"]["fiscalSign"] == gt["fiscal_sign"]
    assert m["fields"]["date"] == gt["datetime"][:10] and m["missing"] == []
    assert m["summary"]["qr"] == gt["qr"]["raw"]


def test_api_key(client, monkeypatch):
    monkeypatch.setenv("RECEIPT_OCR_API_KEY", "test-key-123")
    data = (ROOT / "data/images/r17_a.jpg").read_bytes()
    assert client.post("/api/v1/recognize", files={"file": ("a.jpg", data, "image/jpeg")}).status_code == 401
    r = client.post("/api/v1/recognize", files={"file": ("a.jpg", b"", "image/jpeg")}, headers={"X-API-Key": "wrong"})
    assert r.status_code == 401
    r = client.post("/api/v1/recognize", files={"file": ("a.jpg", b"", "image/jpeg")}, headers={"X-API-Key": "test-key-123"})
    assert r.status_code == 400  # key accepted, then the empty file is refused
    r = client.post("/api/v1/recognize", files={"file": ("a.jpg", b"", "image/jpeg")},
                    headers={"Authorization": "Bearer test-key-123"})
    assert r.status_code == 400
    assert client.get("/api/v1/health").status_code == 200  # health stays open
