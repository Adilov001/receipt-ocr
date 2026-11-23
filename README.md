# Receipt recognition (OCR + QR) for Uzbek fiscal receipts

From a photo of a receipt the system recognises the text (Tesseract 5 / EasyOCR), decodes the
fiscal QR code (zxing-cpp + OpenCV), extracts the fields as JSON, checks the arithmetic and
compares the OCR values with the QR, and shows everything in a Gradio UI on CPU.

```
photo → preprocessing → OCR + QR → field extraction → reconciliation → JSON + metrics
         crop/mask,       2 engines   rules (uz-latn,     qty×price, Σ=total,
         deskew, light,               uz-cyrl, ru)        OCR ↔ QR
         contrast
```

**Baseline:** an OCR engine on the raw photo with no pre- or post-processing.
Every other configuration is compared with it on the same test split.

## Quick start

```bash
brew install tesseract tesseract-lang        # needs uzb, uzb_cyrl, rus traineddata
make setup                                   # Python 3.12 venv + pinned requirements.txt
make test                                    # unit tests
make app                                     # UI → http://127.0.0.1:7860
make split && make eval                      # all metrics → reports/results.md
```

`make eval` recomputes every metric with one command. OCR output is cached in `.cache/ocr`
together with its measured time, so a second run is fast and the timings stay honest.

## REST API (for integration)

```bash
make api                                   # or: uvicorn api:app --host 0.0.0.0 --port 8000
docker build -t receipt-ocr . && docker run -p 8000:8000 receipt-ocr   # same, in Docker
```

Interactive docs (Swagger): `http://localhost:8000/docs`.

| method | path | what |
|---|---|---|
| `GET` | `/api/v1/health` | `{"status": "ok"}` once the models are loaded |
| `POST` | `/api/v1/recognize` | multipart field `file` = receipt photo → JSON |

```bash
curl -X POST "http://localhost:8000/api/v1/recognize" -F "file=@receipt.jpg"
```

Response (shortened):

```json
{
  "result": {"seller_name": "ERA", "seller_tin": "306263261", "datetime": "2026-11-18T13:29:12",
             "receipt_number": "1738", "fiscal_module": "VG544170024923", "fiscal_sign": "006628644216",
             "items": [{"name": "Мучные продукты", "quantity": 1.0, "price": 69000.0, "total": 69000.0}],
             "vat": 7392.86, "total": 69000.0, "payment": "card",
             "qr": {"raw": "https://ofd.soliq.uz/check?...", "decoded": true, "fields": {}}},
  "checks": [{"check": "Σ items = total", "status": "match", "expected": 69000.0, "actual": 69000.0}],
  "consistent": true,
  "field_source": {"total": "ocr", "fiscal_sign": "qr"},
  "timings": {"preprocess": 0.5, "qr": 2.4, "ocr": 2.4, "request": 5.4}
}
```

* Formats: JPEG, PNG, WebP, BMP, TIFF, HEIC (iPhone), PDF (first page only, at most 5 pages), up to 15 MB.
  The response field `pages` gives the page count of a PDF.
* Errors: `400` empty file, `413` too large, `415` not an image, `422` wrong parameter.
* Optional query parameters: `engine=rapidocr|tesseract|hybrid` (default `rapidocr`), `preprocess`, `postprocess`.
* Missing fields are `null`; amounts are numbers; `status` of each check is `match` / `mismatch` / `no_data`.
* Requests run one at a time (OCR uses all CPU cores); for more throughput run several containers.

## Layout

| Path | What |
|---|---|
| `configs/default.yaml` | every parameter (preprocessing steps, OCR languages, tolerances, experiments) |
| `src/receipt/preprocess.py` | receipt detection + perspective warp, background masking, deskew, illumination, CLAHE, binarization |
| `src/receipt/ocr.py` | Tesseract, EasyOCR and RapidOCR behind one interface (lines with boxes and confidence) |
| `src/receipt/repair.py` | repair of the dotted zero read as 8/6/9, using the copies of each amount printed on the receipt |
| `src/receipt/qr.py` | QR decoding with retries (crop of a code found but not read, WeChat CNN + super-resolution, ROI warp, CLAHE, Otsu, adaptive) and link parsing |
| `src/receipt/normalize.py` | numbers, apostrophes, look-alike letters, dates; **metric normalization rules** |
| `src/receipt/extract.py` | field and item extraction |
| `src/receipt/reconcile.py` | arithmetic checks, OCR ↔ QR comparison |
| `src/receipt/metrics.py` | CER, WER, field accuracy, item F1 |
| `scripts/evaluate.py` | engines × configs table, by condition and language, ablation, error analysis |
| `app.py` | Gradio UI |
| `scripts/mask_pii.py`, `scripts/augment.py` | masking of personal data; synthetic variants |
| `models/wechat_qrcode/` | WeChat QR detector + super-resolution models (OpenCV contrib) |

## Output JSON

```json
{
  "seller_name": "...", "seller_tin": "31709886970015", "address": "...",
  "datetime": "2026-11-04T13:47:26", "receipt_number": "36785",
  "fiscal_module": "NA000000006920", "fiscal_sign": "352606397030",
  "items": [{"name": "Keks pishiriq", "quantity": 1.0, "price": 32000.0, "total": 32000.0}],
  "vat": 0.0, "total": 32000.0, "payment": "card",
  "qr": {"raw": "https://ofd.soliq.uz/...", "params": {"t": "...", "r": "...", "c": "...", "s": "..."},
         "fields": {"fiscal_module": "...", "receipt_number": "...", "datetime": "...", "fiscal_sign": "..."}}
}
```

Missing fields are `null`. `payment` is `cash`, `card` or `other`. The QR parameter → field mapping
lives in `configs/default.yaml` (`qr.param_map`).

## Dataset

| | |
|---|---|
| Unique receipts | **29** real paper receipts (Fergana region, Oct–Nov 2026) from **7 sellers** |
| Sellers | `era_tinda` 8, `era_barkamol` 14, `akmal_farm` 3 (pharmacy, Cyrillic), `era_hamkorlik` 1, `diyor_neft` 1 (petrol station, own layout), `era_avtomobilist` 1, `era_avtogaz` 1 (gas stations) |
| Real photos | **78**: 49 whole-receipt photos + 29 photos of the lower half (totals + QR close-up) |
| Synthetic | 40 variants of the first 20 real photos (`scripts/augment.py`), reported separately |
| With QR | every receipt prints a fiscal QR code |
| Conditions | clean, crumpled, shadow, held in hand, tilted, sideways, blurred; synthetic: shadow, faded, perspective |
| Split | seller-disjoint (`data/split.json`): **dev** = `era_tinda`, `akmal_farm`, `era_hamkorlik`, `era_avtogaz` (13 receipts); **test** = `era_barkamol`, `diyor_neft`, `era_avtomobilist` (16 receipts) |
| Holdout | 6 receipts from 6 new shops (`h01`–`h06`: clothing store, café, supermarket, KFC, pharmacy, another ERA shop), 12 photos, collected after development, measured once (`--split holdout`) |
| Personal data | cardholder, cashier and pharmacy staff names blacked out (`scripts/mask_pii.py`, two OCR passes, every image checked); card numbers are already masked by the terminal |

**Lower-half photos** (`*_q.jpg`, condition `partial`) show only the totals and the QR code; they count for the
QR decode rate only, not for text or field metrics.

**Why synthetic variants.** The first 20 photos got two
generated versions: (1) a shadow across the receipt + rotation, (2) faded print + blur + perspective +
strong JPEG compression. A variant shares the receipt id, seller and ground truth of its source photo
and therefore always sits in the same split: there is no leakage between dev and test.
They are marked `synthetic` in `data/meta.csv` and reported separately in the per-condition table.

**Ground truth.** `data/gt/<id>.json` holds the fields, items and QR text. Every label was typed from the photos and then checked against the paper receipt. The QR text of a receipt
whose code cannot be decoded was rebuilt from the printed fiscal module, receipt number, date and fiscal
sign; on the 4 codes that do decode the rebuilt text matches byte for byte. `data/gt/<id>.txt` holds the
full text line by line (test receipts only; logos and masked names are not part of the text).
`seller_name` is the shop name printed under the logo (logos are pictures, not text).

Parameters and rules were tuned on dev only; reported metrics are on test.
Public sets (SROIE, CORD) were not used for any reported number.

### Adding receipts

1. Mask personal data and put the photo in `data/images/` (e.g. `r07_a.jpg`, `r07_b.jpg` for two shots of receipt r07):
   `python scripts/mask_pii.py photo.jpg data/images/r07_a.jpg` (add `--box x0,y0,x1,y1` for anything it misses).
2. Add one row per photo to `data/meta.csv`:
   ```
   image,receipt_id,seller,lang,conditions,has_qr
   r07_a.jpg,r07,makro_yunusobod,uz_latn,clean,1
   r07_b.jpg,r07,makro_yunusobod,uz_latn,crumpled;shadow,1
   ```
   `lang`: `uz_latn`, `uz_cyrl`, `ru`, `mixed`. `conditions` (`;`-separated): `clean`, `crumpled`, `shadow`,
   `uneven_light`, `tilted`, `perspective`, `faded`, `long`, `handheld`.
3. `make prefill` writes draft ground truth `data/gt/<receipt_id>.json` and `.txt` from the pipeline.
   **Correct every value by hand** while looking at the paper receipt, then set `"_status": "verified"`.
   The `.txt` is the full text line by line in reading order (label and value on one line, as printed).
4. `make augment`, `make split`, then `make eval`.

## Metrics

Ground truth and prediction pass through the same normalization (`normalize.py`) before comparison:
NFC, apostrophes unified (oʻ/gʻ → U+02BB, others → U+02BC), whitespace collapsed, separator-only lines
removed, case ignored for CER/WER; amounts compared as numbers, digit fields as digits only.

* **CER** = (S + D + I) / N over characters (Levenshtein), aggregated over the corpus; can exceed 100 %.
* **WER**: same over words.
* **Field accuracy**: fields equal to ground truth / fields in ground truth (a `null` must be predicted as `null`).
* **Item F1**: an item counts only if name, quantity, price and total all match.
* **QR decoded**: decoded text equals the ground-truth QR text; *plain* = one attempt on the raw photo, *final* = after retries.
* **Consistent receipts**: Σ items = total holds and no check is a mismatch.
* **Speed**: mean seconds per receipt on CPU.

## Results

All numbers come from `make eval` (`reports/results.md`, `reports/holdout/results.md`). Rules and settings
were chosen on **dev** only. **Test** = 16 receipts from 3 sellers never used for tuning.
**Holdout** = 6 receipts from 6 *new* shops with different cash-register software, collected after all
development and measured **once**, with no change to the code afterwards.

### Test: real whole-receipt photos (23 photos, 16 receipts)

| engine                        | config                  |   fields % |   item F1 % |   CER % |   WER % |   consistent % |   s / receipt |
|:------------------------------|:------------------------|-----------:|------------:|--------:|--------:|---------------:|--------------:|
| Tesseract 5 | baseline (raw photo) | 7.0 | 0.0 | 89.0 | 94.1 | 0.0 | 8.2 |
| Tesseract 5 | + preprocessing | 26.1 | 0.0 | 42.4 | 92.1 | 0.0 | 14.0 |
| Tesseract 5 | + pre + post-processing | 59.1 | 19.0 | 42.3 | 91.3 | 30.4 | 13.3 |
| EasyOCR | baseline (raw photo) | 27.4 | 0.0 | 60.8 | 88.6 | 0.0 | 46.6 |
| EasyOCR | + preprocessing | 36.5 | 3.9 | 26.0 | 69.8 | 0.0 | 51.1 |
| EasyOCR | + pre + post-processing | 62.2 | 7.8 | 25.3 | 65.4 | 4.3 | 50.4 |
| RapidOCR (cyrillic PP-OCRv5) | baseline (raw photo) | 60.9 | 55.8 | 47.4 | 58.8 | 43.5 | 9.2 |
| RapidOCR (cyrillic PP-OCRv5) | + preprocessing | 77.0 | 73.9 | 10.0 | 24.6 | 73.9 | 9.6 |
| RapidOCR (cyrillic PP-OCRv5) | + pre + post-processing | **94.8** | **87.0** | **9.8** | 23.4 | **82.6** | 9.8 |
| Hybrid (RapidOCR + Tesseract) | baseline (raw photo) | 60.9 | 55.8 | 47.4 | 58.8 | 43.5 | 12.1 |
| Hybrid (RapidOCR + Tesseract) | + preprocessing | 77.4 | 73.9 | 10.0 | 24.6 | 73.9 | 17.6 |
| Hybrid (RapidOCR + Tesseract) | + pre + post-processing | 94.8 | 87.0 | 9.8 | 23.4 | 82.6 | 16.8 |

Field accuracy per field (RapidOCR, pre + post):

|                          |   seller_name |   seller_tin |   address |   datetime |   receipt_number |   fiscal_module |   fiscal_sign |   vat |   total |   payment |
|:-------------------------|--------------:|-------------:|----------:|-----------:|-----------------:|----------------:|--------------:|------:|--------:|----------:|
| RapidOCR, real photos, % |          95.7 |         91.3 |      78.3 |       95.7 |             95.7 |           100   |          95.7 |   100 |   100   |      95.7 |

95 % confidence intervals (bootstrap over receipts, pre + post) — with 16 receipts the ranges are wide:

| engine    |   receipts | field acc %      | item F1 %         | consistent %     | CER %            | WER %            |
|:----------|-----------:|:-----------------|:------------------|:-----------------|:-----------------|:-----------------|
| tesseract |         16 | 59.1 [51.2–66.5] | 19.0 [0.0–39.0]   | 30.4 [11.5–52.4] | 42.3 [34.4–51.1] | 91.3 [71.0–110.4] |
| easyocr   |         16 | 62.2 [54.8–68.6] | 7.8 [0.0–20.4]    | 4.3 [0.0–13.6]   | 25.3 [19.2–30.7] | 65.4 [56.5–73.4]  |
| rapidocr  |         16 | 94.8 [91.4–98.0] | 87.0 [75.0–100.0] | 82.6 [68.0–95.5] | 9.8 [5.6–13.9]   | 23.4 [17.2–29.5]  |
| hybrid    |         16 | 94.8 [91.3–98.0] | 87.0 [75.0–100.0] | 82.6 [68.2–95.7] | 9.8 [5.3–14.3]   | 23.4 [17.2–29.8]  |

### Holdout: 6 new shops, measured once (6 whole-receipt photos)

Measured on 18 Nov, *before* the receipt crop was switched off; a new holdout is needed to check that change.

| engine                       | config                  |   fields % |   item F1 % |   consistent % |   s / receipt |
|:-----------------------------|:------------------------|-----------:|------------:|---------------:|--------------:|
| Tesseract 5                  | baseline (raw photo)    |       21.7 |         0.0 |            0.0 |          14.4 |
| Tesseract 5                  | + preprocessing         |       25.0 |        33.3 |            0.0 |          11.1 |
| Tesseract 5                  | + pre + post-processing |       40.0 |        33.3 |            0.0 |          11.4 |
| RapidOCR (cyrillic PP-OCRv5) | baseline (raw photo)    |       65.0 |        50.0 |           50.0 |          10.1 |
| RapidOCR (cyrillic PP-OCRv5) | + preprocessing         |       53.3 |        53.3 |           33.3 |          10.3 |
| RapidOCR (cyrillic PP-OCRv5) | + pre + post-processing |       63.3 |        53.3 |           33.3 |          10.0 |

|                      |   seller_name |   seller_tin |   address |   datetime |   receipt_number |   fiscal_module |   fiscal_sign |   vat |   total |   payment |
|:---------------------|--------------:|-------------:|----------:|-----------:|-----------------:|----------------:|--------------:|------:|--------:|----------:|
| RapidOCR, holdout, % |            50 |           83 |        50 |         50 |               83 |             100 |            83 |    50 |      33 |        50 |

The holdout shows how much of the result is specific to the **ERA receipt layout** that dominates dev and
test: on an ERA shop never seen before (h06) 90 % of fields are right, on the other layouts (café, KFC,
supermarket, pharmacy, a different POS) 40–80 %. Most holdout errors are *not found* (13 of 22): label words
these layouts use and the rules don't know (`Umumiy to'lov`, `Kassa raqami`, `Savdo Cheki`, `JAMI =`).
Fiscal fields read from the QR (FM, fiscal sign, receipt number) stay at 83–100 %.

### QR decoding

| photos | test | holdout |
|---|---:|---:|
| whole receipt | 60.9 % | 50.0 % |
| QR close-up | 68.8 % | 83.3 % |
| per receipt (any real photo decodes) | 81.2 % | 83.3 % |

Public dataset check (decoder unchanged, `scripts/eval_external_qr.py`, 150 Russian receipts from
`cdek-ocr/receipt-ocr-ru`): QR found 92 %, decoded 74 %, 80 % of the found codes; every decode that has a
labelled total matches it.

### Against the target values (test, real photos, RapidOCR + pre + post)

| target | test | holdout (new layouts) | status |
|---|---:|---:|---|
| field accuracy ≥ 85 % | **94.8 %** [91.4–98.0] | 63.3 % | reached on test; not on new layouts |
| item F1 ≥ 75 % | **87.0 %** [75.0–100] | 53.3 % | reached on test |
| CER ≤ 10 % | **9.8 %** [5.6–13.9] | — (no full-text labels) | reached on test (just) |
| WER ≤ 20 % | 23.4 % [17.2–29.5] | — | not reached |
| QR decoded ≥ 95 % | 60.9 % per photo, 81.2 % per receipt | 50 % / 83.3 % | not reached |
| arithmetic checks 100 % correct | **100 %** (`tests/test_reconcile.py`, all 29 labelled dev + test receipts) | | reached |
| ≤ 10 s per receipt on CPU | **6.4 s** mean through the API in Docker (3 s QR limit); 21 of 23 photos ≤ 10 s, max 11.7 s on a busy Mac. Offline evaluation without the QR limit: 9.8 s | 8.2 s | reached on average |

### What changed in the last iteration (each step chosen on dev, then confirmed on test)

| step | test fields | items F1 | CER | WER |
|---|---:|---:|---:|---:|
| start (RapidOCR bundled model) | 82.6 | 79.2 | 16.9 | 46.1 |
| A1: recognizer `cyrillic_PP-OCRv5` (chosen among 5 on dev) | 84.3 | 82.6 | 14.4 | 30.3 |
| A2: address = block from `Manzil` to the next label | 87.4 | 82.6 | 14.4 | 30.3 |
| A3: line grouping along the local text slope | 89.1 | 87.0 | 10.0 | 26.8 |
| label vocabulary, spec number normalization, look-alike letters | 89.6 | 87.0 | 9.4 | 24.3 |
| preprocessing: receipt crop switched off (ablation on dev) | **94.8** | **87.0** | 9.8 | **23.4** |

Tried on dev and **rejected** (made results worse): a white margin before OCR, 3 text-detector settings,
a larger rotation canvas, switching deskew off, the OpenCV Aruco QR decoder, rebuilding the QR grid.

### Quantization of the recognizer (spec bonus: speed-up and quality loss)

`scripts/quantize_rec.py`, recognizer `cyrillic_PP-OCRv5`, dev split (26 real photos), full pipeline:

| model | size | ms per text line (CPU, 4 threads) | field acc % | item F1 % | CER % | WER % |
|---|---:|---:|---:|---:|---:|---:|
| FP32 (used) | 7.7 MB | 21 | **86.9** | **74.3** | **12.3** | **30.2** |
| INT8 dynamic (MatMul) | 6.8 MB | 29 (slower) | — | — | — | — |
| INT8 static, Conv + MatMul (calibrated on 240 dev text lines) | **2.2 MB** | 20 | 53.5 | 9.2 | 27.3 | 64.4 |
| INT8 static, Conv only | 3.1 MB | 21 | text 43–74 % identical to FP32 on 3 photos | | | |

Post-training quantization makes the model 3.6× smaller but gives **no speed-up** on this x86 CPU (the
recognizer is small and convolution-bound; dynamic quantization even adds conversion cost) and
**loses a lot of accuracy** (CER 12 → 27 %): the thin-stroke thermal font needs the full precision of the
activations. Decision: keep FP32. Next options if size matters: quantization-aware training (QAT) on
our line crops, or FP16. Two fixes were needed to quantize this export at all: its weights are stored as
`Constant` nodes (moved to initializers) and its opset 7 `BatchNormalization` carries the removed
`spatial` attribute.

### Limits (read before trusting the numbers)

* Small data: 16 test and 6 holdout receipts; see the confidence intervals.
* Test is dominated by one layout (ERA, 12 of 16 receipts); the holdout shows the drop on new layouts.
* The test set was looked at after each development step (only to confirm, never to choose between
  variants); the holdout was measured once.
* Full-text labels (CER/WER) exist for 15 receipts; 8 dev ones were built from the ERA template.

### Preprocessing ablation (dev split, RapidOCR, post-processing on)

Field accuracy, %; steps are added one by one, then each step is removed from the default.

| variant                      |   real photos |   synthetic photos |
|:-----------------------------|--------------:|-------------------:|
| none (raw image)             |          80.0 |               59.2 |
| + crop                       |          86.5 |               48.8 |
| + orient                     |          85.4 |               49.2 |
| + deskew                     |          83.8 |               47.7 |
| + illumination               |          83.1 |               50.8 |
| + clahe                      |          86.9 |               51.9 |
| + binarize                   |          69.2 |               36.5 |
| default without crop         |          87.3 |               68.5 |
| default without orient       |          86.9 |               51.2 |
| default without deskew       |          86.9 |               50.8 |
| default without illumination |          85.0 |               54.2 |
| default without clahe        |          83.1 |               50.8 |

By shooting condition (number of photos in brackets; synthetic variants included):

| variant                      |   clean (14) |   crumpled (27) |   shadow (15) |   tilted (17) |   sideways (11) |   handheld (9) |   faded (13) |   perspective (13) |
|:-----------------------------|-------------:|----------------:|--------------:|--------------:|----------------:|---------------:|-------------:|-------------------:|
| none (raw image)             |           96 |              54 |            75 |            74 |              28 |             46 |           42 |                 42 |
| + crop                       |           94 |              54 |            54 |            55 |              55 |             44 |           46 |                 46 |
| + orient                     |           91 |              54 |            55 |            56 |              55 |             47 |           45 |                 45 |
| + deskew                     |           88 |              53 |            56 |            56 |              54 |             49 |           42 |                 42 |
| + illumination               |           87 |              55 |            57 |            57 |              55 |             48 |           46 |                 46 |
| + clahe                      |           89 |              58 |            57 |            59 |              61 |             47 |           48 |                 48 |
| + binarize                   |           79 |              37 |            45 |            43 |              42 |             34 |           30 |                 30 |
| default without crop         |           94 |              69 |            83 |            81 |              72 |             49 |           52 |                 52 |
| default without orient       |           89 |              57 |            56 |            58 |              59 |             44 |           48 |                 48 |
| default without deskew       |           92 |              56 |            55 |            56 |              60 |             43 |           47 |                 47 |
| default without illumination |           89 |              59 |            59 |            61 |              60 |             48 |           50 |                 50 |
| default without clahe        |           87 |              55 |            57 |            57 |              55 |             48 |           46 |                 46 |

* With the RapidOCR engine, **cropping the receipt hurts**, so it is **off by default** since 19 Nov (confirmed
  once on test: fields 89.6 → 94.8 %, consistent receipts 73.9 → 82.6 %, CER 9.4 → 9.8 %). On dev it is 87.3 % instead of
  86.9 % on real photos and **68.5 % instead of 51.9 %** on the synthetic shadow / tilt / perspective photos.
  RapidOCR has its own text detector, and the paper mask sometimes cuts off part of a shadowed or tilted
  receipt. (With Tesseract cropping was the most useful step, +11 points: the finding depends on the engine.)
* **Contrast (CLAHE)** helps most on real photos (83.1 → 86.9 %), especially sideways and crumpled ones.
* **Binarization hurts** everywhere (−17 to −20 points): it breaks the thin thermal strokes. Off by default.
* Shadow removal helps on crumpled photos and hurts slightly overall; deskew and orientation are close to neutral.

### Error analysis

![Main problems](reports/figures/problems.png)

1. **Dotted zero.** The ERA printer prints 0 with a dot inside; OCR reads it as 8, 6 or 9
   ("24 000.00" → "24 888.66"). `src/receipt/repair.py` uses the fact that the amount is printed 3–4 times
   (Narx, Naqdsiz, Jami, To'lov uchun jami): it lists what each copy could be if an 8/6/9 is a 0 and keeps
   the value the copies agree on; a value is never changed without support from another copy.
2. **Photo resolution decides the QR rate.** The first 16 photos came through Telegram, which halves
   the resolution: 4 of 16 decoded (ERA Tinda 0 of 9). The same receipts re-shot at full resolution: 40 of 62.
3. **Printed gaps in the QR code.** The ERA Tinda printer leaves white gaps inside black modules
   (a worn thermal print head). They use up most of the QR error correction, so zxing fails with a checksum
   error as soon as anything else is wrong. A retry binarizes the crop of the code that zxing found and
   thickens the black to fill the gaps (dev: 18 → 21 of 39 real photos decoded).
4. **An artefact of my own preprocessing.** Background division (shadow removal) estimates the paper
   brightness with a large blur; inside a big black QR module that estimate is dark too, so the module turns
   partly white (panel 2). The QR decoder therefore works on the original photo first.
5. **Orientation detector turned upright receipts upside down.** Tesseract OSD claimed "rotate 180°" on 10
   upright receipts; one of them (r11_c) was flipped and its text came out in reverse order (CER 81 %). Now a
   receipt is turned only when its own layout says so: the fiscal QR code is printed at the end, so a QR code
   found in the top 40 % means upside down (0 of 49 upright photos rotated, 39 of 49 flipped copies corrected).
   Sideways photos are turned by the aspect ratio of the receipt.
6. **Strong shadow cuts a hole in the receipt** (r20_a): the paper mask treats the shadowed half as
   background. Not fixed yet.
7. **Deskew at its limit** (r06): the projection-profile search stopped at −8°, the edge of its range.
8. **Long addresses** (field accuracy 26 %): one wrong letter in a 70-character address makes the field wrong,
   and wrapped address lines are sometimes cut. The metric is exact match, as required.

Automatic causes of the wrong fields (RapidOCR, pre + post, test): *not found* 57, *text misread /
wrong span* 35, *digits misread* 6, *digits/amounts misread* 5, *digits missing/extra* 3, *date/time misread* 3. Every wrong field is listed in
`reports/errors.csv` with its cause and shooting conditions; examples are in `reports/results.md`.

## Licenses

| Component | License |
|---|---|
| Tesseract 5 + tessdata (uzb, uzb_cyrl, rus) | Apache 2.0 |
| EasyOCR 1.7.2 and its models | Apache 2.0 |
| zxing-cpp 3.1.1 | Apache 2.0 |
| OpenCV 4.11 | Apache 2.0 |
| Gradio 6, pandas, RapidFuzz | Apache 2.0 / BSD / MIT |
| PyTorch 2.2.2 | BSD-3 |
| RapidOCR 1.4.4 + PaddleOCR PP-OCRv4 models | Apache 2.0 |
| ONNX Runtime 1.20 | MIT |
| pillow-heif 1.8 (HEIC decoding; bundles libheif, LGPL) | BSD-3 |
| pypdfium2 5.15 (PDF rendering; PDFium) | Apache 2.0 / BSD-3 |
| WeChat QR models (opencv_3rdparty) | Apache 2.0 |
| Dataset | own photos, personal data masked |
