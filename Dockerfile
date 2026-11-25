# Receipt recognition API (CPU).  Build:  docker build -t receipt-ocr .
#                                 Run:    docker run -p 8001:8001 receipt-ocr   -> http://localhost:8001/docs
FROM python:3.12-slim

# Tesseract 5 with Uzbek (Latin + Cyrillic) and Russian models; libgl/libglib for OpenCV
RUN apt-get update && apt-get install -y --no-install-recommends \
        tesseract-ocr tesseract-ocr-uzb tesseract-ocr-uzb-cyrl tesseract-ocr-rus tesseract-ocr-osd \
        libgl1 libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt requirements-nodeps.txt ./
# CPU-only PyTorch (EasyOCR dependency) keeps the image small
RUN pip install --no-cache-dir --extra-index-url https://download.pytorch.org/whl/cpu -r requirements.txt \
    && pip install --no-cache-dir --no-deps -r requirements-nodeps.txt \
    && pip uninstall -y opencv-python-headless \
    && pip install --no-cache-dir --no-deps --force-reinstall opencv-contrib-python-headless==4.11.0.86 \
    && python -c "import cv2; assert hasattr(cv2, 'wechat_qrcode_WeChatQRCode')"

COPY configs ./configs
COPY models ./models
COPY src ./src
COPY api.py ./

EXPOSE 8001
HEALTHCHECK --interval=30s --timeout=5s --start-period=60s CMD python -c \
    "import urllib.request; urllib.request.urlopen('http://localhost:8001/api/v1/health')"
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8001"]
