"""REST API for the receipt recognizer: the web backend sends a photo, gets JSON back.

    uvicorn api:app --host 0.0.0.0 --port 8000        (or: make api)
    docs: http://localhost:8000/docs

POST /api/v1/recognize   multipart form, field "file" = receipt photo (JPEG / PNG / WebP / BMP / TIFF /
                         HEIC from an iPhone) or a PDF (first page; at most 5 pages)
                         optional query: engine=rapidocr|tesseract|hybrid, preprocess, postprocess
GET  /api/v1/health      ready check (models are loaded at start-up)

Requests are processed one at a time: OCR is CPU-bound and already uses all cores, so parallel
requests would only slow each other down. Run several containers for more throughput.
"""
import sys
import threading
import time
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Literal

import cv2
import numpy as np
from fastapi import FastAPI, File, HTTPException, Query, UploadFile

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from receipt.config import load_config  # noqa: E402
from receipt.pipeline import MAX_PDF_PAGES, decode_image, process  # noqa: E402

CFG = load_config()
# A website must answer quickly: QR retries stop after 3 s. Measured on 90 real photos: 50 of 52 codes
# still decode (52 without a limit), QR time mean 2.0 s instead of 9.2 s, worst case 6.5 s instead of 44 s.
CFG["qr"]["time_budget"] = 3.0
MAX_BYTES = 15 * 1024 * 1024
ENGINES = ("rapidocr", "tesseract", "hybrid")
_lock = threading.Lock()
_state = {"ready": False}


def _plain(x):
    """numpy types -> plain Python, so the result can be returned as JSON."""
    if isinstance(x, dict):
        return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_plain(v) for v in x]
    if isinstance(x, np.generic):
        return x.item()
    if isinstance(x, np.ndarray):
        return x.tolist()
    return x


@asynccontextmanager
async def lifespan(app):
    # warm-up: load the OCR and QR models once, so the first real request is not slower
    blank = np.full((400, 300, 3), 255, np.uint8)
    cv2.putText(blank, "Jami 1000.00", (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
    process(blank, CFG, engine="rapidocr")
    _state["ready"] = True
    yield


app = FastAPI(title="Receipt recognition API", version="1.0",
              description="Uzbek fiscal receipts: OCR + QR → JSON with fields, items, checks.", lifespan=lifespan)


@app.get("/api/v1/health")
def health():
    return {"status": "ok" if _state["ready"] else "starting", "engines": list(ENGINES)}


@app.post("/api/v1/recognize")
def recognize(file: UploadFile = File(..., description="photo of a receipt"),
              engine: Literal["rapidocr", "tesseract", "hybrid"] = Query("rapidocr"),
              preprocess: bool = True, postprocess: bool = True):
    data = file.file.read(MAX_BYTES + 1)
    if not data:
        raise HTTPException(400, "Empty file.")
    if len(data) > MAX_BYTES:
        raise HTTPException(413, f"File larger than {MAX_BYTES // 2**20} MB.")
    img, pages = decode_image(data)
    if img is None:
        if pages > MAX_PDF_PAGES:
            raise HTTPException(415, f"PDF has {pages} pages; at most {MAX_PDF_PAGES} are accepted.")
        raise HTTPException(415, "Not a readable file (expected JPEG, PNG, WebP, BMP, TIFF, HEIC or PDF).")

    t = time.perf_counter()
    with _lock:
        out = process(img, CFG, engine=engine, preprocess=preprocess, postprocess=postprocess)
    return _plain({
        "result": out["result"],            # fields, items, qr — see README "Output JSON"
        "checks": out["checks"],            # arithmetic and OCR <-> QR, status match / mismatch / no_data
        "consistent": out["consistent"],
        "field_source": out["field_source"],  # where each value came from: ocr or qr
        "source_lines": out["source_lines"],  # OCR line (text, confidence) each OCR field was read from
        "text": out["text"],                  # full recognised text, line by line
        "engine": engine,
        "timings": {**out["timings"], "request": time.perf_counter() - t},
        "image_size": {"width": img.shape[1], "height": img.shape[0]},
        "pages": pages,  # PDF: only the first page is recognised
    })
