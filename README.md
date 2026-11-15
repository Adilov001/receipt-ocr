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

Test split: 16 receipts from 3 sellers that were **never used for tuning** (ERA Barkamol, the
DIYOR NEFT petrol station, the ERA AVTOMOBILIST gas station; the petrol layout is not in dev at all).
CPU: MacBook (x86-64). All tables: `reports/results.md`; dev split and ablation: `reports/dev/results.md`.

### Real photos (23 whole-receipt photos)

| engine                        | config                  |   fields % |   item F1 % |   CER % |   WER % |   QR plain % |   QR final % |   consistent % |   s / receipt |
|:------------------------------|:------------------------|-----------:|------------:|--------:|--------:|-------------:|-------------:|---------------:|--------------:|
| Tesseract 5                   | baseline (raw photo)    |        7   |         0   |    88.9 |    93.5 |         47.8 |         60.9 |            0   |           6.8 |
| Tesseract 5                   | + preprocessing         |       18.3 |         5   |    38.1 |    73   |         47.8 |         60.9 |            4.3 |           8.4 |
| Tesseract 5                   | + pre + post-processing |       55.7 |        15   |    38.1 |    73   |         47.8 |         60.9 |            4.3 |           8.5 |
| EasyOCR                       | baseline (raw photo)    |       27.4 |         0   |    60.6 |    87.2 |         47.8 |         60.9 |            0   |          42.2 |
| EasyOCR                       | + preprocessing         |       29.6 |         0   |    29.3 |    73.9 |         47.8 |         60.9 |            4.3 |          18.5 |
| EasyOCR                       | + pre + post-processing |       55.7 |         0   |    29.3 |    73.9 |         47.8 |         60.9 |            0   |          19.1 |
| RapidOCR (PP-OCRv4, ONNX)     | baseline (raw photo)    |       57.4 |        35.6 |    47.7 |    65.8 |         47.8 |         60.9 |           26.1 |           6.6 |
| RapidOCR (PP-OCRv4, ONNX)     | + preprocessing         |       59.1 |        50   |    22.2 |    50.2 |         47.8 |         60.9 |           52.2 |           7.2 |
| RapidOCR (PP-OCRv4, ONNX)     | + pre + post-processing |       80   |        66.7 |    22.3 |    50.2 |         47.8 |         60.9 |           60.9 |           7   |
| Hybrid (RapidOCR + Tesseract) | baseline (raw photo)    |       57.4 |        35.6 |    47.7 |    65.8 |         47.8 |         60.9 |           26.1 |           9.9 |
| Hybrid (RapidOCR + Tesseract) | + preprocessing         |       59.1 |        50   |    22.2 |    50.2 |         47.8 |         60.9 |           52.2 |          11.8 |
| Hybrid (RapidOCR + Tesseract) | + pre + post-processing |       80   |        66.7 |    22.3 |    50.2 |         47.8 |         60.9 |           56.5 |          11.4 |

### Field accuracy per field (RapidOCR, pre + post, real photos)

|                          |   seller_name |   seller_tin |   address |   datetime |   receipt_number |   fiscal_module |   fiscal_sign |   vat |   total |   payment |
|:-------------------------|--------------:|-------------:|----------:|-----------:|-----------------:|----------------:|--------------:|------:|--------:|----------:|
| RapidOCR, real photos, % |          73.9 |         65.2 |      26.1 |       91.3 |               87 |            91.3 |            87 |  91.3 |    95.7 |      91.3 |

### Synthetic variants (14 photos: shadow + tilt, faded + blur + perspective + JPEG)

| engine                        | config                  |   fields % |   item F1 % |   CER % |   WER % |   QR plain % |   QR final % |   consistent % |   s / receipt |
|:------------------------------|:------------------------|-----------:|------------:|--------:|--------:|-------------:|-------------:|---------------:|--------------:|
| Tesseract 5                   | baseline (raw photo)    |        0.7 |         0   |    97.8 |    98.8 |         28.6 |         42.9 |            0   |           5.4 |
| Tesseract 5                   | + preprocessing         |       10   |         0   |    57.2 |    90.5 |         28.6 |         42.9 |            0   |           7.8 |
| Tesseract 5                   | + pre + post-processing |       32.1 |         0   |    57.2 |    90.5 |         28.6 |         42.9 |            0   |           8.2 |
| EasyOCR                       | baseline (raw photo)    |        5   |         0   |    85.2 |   100.5 |         28.6 |         42.9 |            0   |          40.5 |
| EasyOCR                       | + preprocessing         |        9.3 |         0   |    62.1 |    91.1 |         28.6 |         42.9 |            0   |          21.2 |
| EasyOCR                       | + pre + post-processing |       26.4 |         0   |    62.1 |    91.1 |         28.6 |         42.9 |            0   |          21.1 |
| RapidOCR (PP-OCRv4, ONNX)     | baseline (raw photo)    |       25.7 |         8.3 |    78.4 |    88.5 |         28.6 |         42.9 |           14.3 |           6   |
| RapidOCR (PP-OCRv4, ONNX)     | + preprocessing         |       24.3 |        27.3 |    50.5 |    76.6 |         28.6 |         42.9 |            7.1 |           6.7 |
| RapidOCR (PP-OCRv4, ONNX)     | + pre + post-processing |       47.9 |        36.4 |    50.5 |    76.6 |         28.6 |         42.9 |           21.4 |           6.4 |
| Hybrid (RapidOCR + Tesseract) | baseline (raw photo)    |       25.7 |         8.3 |    78.4 |    88.5 |         28.6 |         42.9 |           14.3 |           7.7 |
| Hybrid (RapidOCR + Tesseract) | + preprocessing         |       25.7 |        27.3 |    50.5 |    76.6 |         28.6 |         42.9 |            7.1 |          10.1 |
| Hybrid (RapidOCR + Tesseract) | + pre + post-processing |       49.3 |        36.4 |    50.5 |    76.6 |         28.6 |         42.9 |           21.4 |          10.9 |

### QR decoding by photo type

| kind      |   images |   QR plain % |   QR final % |
|:----------|---------:|-------------:|-------------:|
| lower half (QR close-up)   |       16 |         62.5 |         68.8 |
| whole receipt, real      |       23 |         47.8 |         60.9 |
| whole receipt, synthetic |       14 |         28.6 |         42.9 |

*QR plain* = one attempt on the raw photo; *final* = after retries (crop of the code zxing found but could
not read at several sizes, WeChat CNN detector with super-resolution, ROI warp, CLAHE, Otsu, …).

### Against the target values

| target | result (test, real photos) | status |
|---|---|---|
| field accuracy ≥ 85 % | **80.0 %** (total 95.7, date 91.3, FM 91.3, VAT 91.3, payment 91.3; address 26.1) | close; address is the main gap |
| item F1 ≥ 75 % | **66.7 %** | close |
| QR decoded ≥ 95 % | **60.9 %** whole photo, **68.8 %** QR close-up | not reached: printed codes with gaps, crumpled paper |
| CER ≤ 10 %, WER ≤ 20 % | **22.3 % / 50.2 %** | not reached |
| arithmetic checks 100 % correct | **100 %**: on all 29 labelled receipts every check is "совпадает", and deliberately broken values are caught (`tests/test_reconcile.py`) | reached |
| ≤ 10 s per receipt on CPU | **7.0 s** (RapidOCR); hybrid 11.4 s | reached |

**What the numbers say**

* **The OCR engine matters most.** RapidOCR runs PaddleOCR's PP-OCRv4 models through ONNX Runtime; on
  real photos it reaches 80 % field accuracy against 56 % for Tesseract and EasyOCR with the same
  pre- and post-processing, and it is the fastest. It is the default engine.
* **Preprocessing** halves CER for every engine (Tesseract 89 → 38 %, RapidOCR 48 → 22 %).
  **Post-processing** does not change the text but adds 20–37 points of field accuracy (label rules,
  dotted-zero repair, QR values) and turns item F1 from 50 % into 67 %.
* **Hybrid** (RapidOCR + Tesseract for what RapidOCR misses and for Cyrillic) gives the same result on
  this test split, which is Latin-only apart from one item name, and costs 4 s more; it helps on the
  Cyrillic pharmacy receipts in dev.
* **Photo resolution decides QR decoding.** The first photos were sent through Telegram, which halves the
  resolution: 4 of 16 decoded. The same receipts re-shot at full resolution: 40 of 62.
* **Hard conditions still hurt:** on synthetic shadow / blur / perspective variants field accuracy drops to
  48 % and QR to 43 %.

### Preprocessing ablation (dev split, Tesseract, post-processing on)

Steps added one by one, and each step removed from the default:

| added step | field acc % | | default without | field acc % | drop |
|---|---:|---|---|---:|---:|
| none (raw image) | 1.9 | | — (default) | 17.0 | |
| + crop | 7.4 | | crop | 15.2 | −1.8 |
| + orient | 7.4 | | orient | 15.6 | −1.4 |
| + deskew | 10.0 | | deskew | 12.2 | −4.8 |
| + illumination | 12.6 | | illumination | 7.4 | **−9.6** |
| + clahe | **17.0** | | clahe | 12.6 | −4.4 |
| + binarize | 7.4 | | | | |

Shadow removal (illumination) matters most; deskew and contrast (CLAHE) come next. Adaptive binarization
**hurts** (17.0 → 7.4: it breaks thin thermal strokes), so it is off by default; that choice was made on dev.
Orientation adds little here because the perspective warp already turns most receipts upright; it is a
safety net for photos where no receipt outline is found. Dev numbers are lower than test because dev
(ERA Tinda) has the most crumpled receipts and none of its QR codes decode.

### Error analysis

![Main problems](reports/figures/problems.png)

1. **Dotted zero.** The ERA printer prints 0 with a dot inside; OCR reads it as 8, 6 or 9
   ("24 000.00" → "24 888.66"). `src/receipt/repair.py` uses the fact that the amount is printed 3–4 times
   (Narx, Naqdsiz, Jami, To'lov uchun jami): it lists what each copy could be if an 8/6/9 is a 0 and keeps
   the value the copies agree on; a value is never changed without support from another copy.
2. **QR codes that never decode.** Real photos decode by seller: ERA Tinda **0/9**, ERA Barkamol 2/5,
   Akmal Farm 2/2. The Tinda printer leaves white gaps in its codes (a worn thermal print head), which
   use up most of the QR error correction; zxing then fails with a checksum error as soon as anything
   else is wrong (code small in the frame, bent paper, blur). Separate sharp close-ups of r10 and r12 decoded
   on the first try, and their text matched our rebuilt ground truth exactly. On the other shops crumpling is
   what breaks the code. These fields then come from OCR only, and the OCR ↔ QR check says "нет данных".
3. **An artefact of my own preprocessing.** Background division (shadow removal) estimates the paper
   brightness with a large blur; inside a big black QR module that estimate is dark too, so the module
   turns partly white (panel 2: original vs preprocessed). It does not change the QR rate here (the codes
   fail on the original photo as well); the QR decoder works on the original photo first and uses the
   preprocessed image only as its last retry.
4. **Sideways photos** (7 of 16): handled by the orientation step (aspect ratio + Tesseract OSD).
5. **Deskew at its limit** (r06): the projection-profile search stopped at −8°, the edge of its range.
6. **Unreadable digits on paper**: two fiscal-sign digits were hidden by creases in the photos (r10, r12); both were checked on the paper receipts.

Automatic causes over all wrong fields (pre + post, both engines): *not found* 134, *text misread /
wrong span* 61, *digits/amounts misread* 20, *digits misread* 7, *date/time misread* 5,
*wrong line picked* 3, *digits missing/extra* 2, *spurious value* 1. Every wrong field is listed in
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
| WeChat QR models (opencv_3rdparty) | Apache 2.0 |
| Dataset | own photos, personal data masked |
