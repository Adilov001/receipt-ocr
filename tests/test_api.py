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
    assert res["qr"]["decoded"] and res["qr"]["raw"] == gt["qr"]["raw"]
    assert {c["status"] for c in body["checks"]} <= {"match", "mismatch", "no_data"}
    assert body["timings"]["request"] > 0


def test_empty_and_not_an_image(client):
    assert client.post("/api/v1/recognize", files={"file": ("a.jpg", b"", "image/jpeg")}).status_code == 400
    r = client.post("/api/v1/recognize", files={"file": ("a.heic", b"not an image", "image/heic")})
    assert r.status_code == 415 and "HEIC" in r.json()["detail"]


def test_unknown_engine(client):
    with open(ROOT / "data/images/r17_a.jpg", "rb") as f:
        r = client.post("/api/v1/recognize?engine=foo", files={"file": ("r.jpg", f, "image/jpeg")})
    assert r.status_code == 422
