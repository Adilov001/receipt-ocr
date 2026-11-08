PY ?= .venv/bin/python

.PHONY: setup test augment split prefill eval app

setup:            ## create venv and install pinned dependencies (also: brew install tesseract tesseract-lang)
	python3.12 -m venv .venv && .venv/bin/pip install -r requirements.txt

test:             ## unit tests: number normalization, QR parsing, metrics, extraction
	$(PY) -m pytest -q

augment:          ## two synthetic variants (shadow+tilt, faded+blur+perspective) per real photo
	$(PY) scripts/augment.py

split:            ## seller-disjoint dev/test split -> data/split.json
	$(PY) scripts/make_split.py

prefill:          ## draft ground truth for receipts without one (correct by hand!)
	$(PY) scripts/prefill_gt.py

eval:             ## all metrics + ablation -> reports/results.md
	$(PY) scripts/evaluate.py --split test --ablation --ablation-split dev

app:              ## web UI on http://127.0.0.1:7860
	$(PY) app.py
