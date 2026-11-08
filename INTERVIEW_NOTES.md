# Interview notes: how I built the receipt recognizer

## 30-second pitch

"From a phone photo of an Uzbek fiscal receipt, my system reads the text with OCR, decodes the
fiscal QR code, extracts the fields (seller, TIN, date, receipt number, items, total, payment) as JSON,
checks the arithmetic and compares OCR with the QR. It runs on CPU with a Gradio UI.
I collected 15 real receipts myself, labelled them by hand and measured everything on a test set
of shops the system never saw while I was tuning it."

## The pipeline in 7 steps (one sentence each)

| # | Step | What I say | File |
|---|---|---|---|
| 1 | Data | 15 real receipts, 16 photos + 32 generated variants; split **by shop** so test shops are never seen during tuning | `data/`, `scripts/augment.py`, `dataset.py` |
| 2 | Preprocessing | Find the receipt, flatten it (perspective), turn it upright, straighten it, remove shadows, raise contrast | `preprocess.py` |
| 3 | OCR | Two engines compared: Tesseract (fast) and EasyOCR (neural, slower) | `ocr.py` |
| 4 | QR | Decode with zxing-cpp; if it fails, retry on enlarged / sharpened / thresholded copies | `qr.py` |
| 5 | Extraction | Regex rules: find a label ("STIR", "Chek", "Fiskal imzo") and take the value next to it | `extract.py` |
| 6 | Repair + checks | Fix misread zeros using the repeated amounts; check qty × price = total and OCR vs QR | `repair.py`, `reconcile.py` |
| 7 | Evaluation + UI | CER, WER, field accuracy, item F1, QR rate, speed; Gradio app | `metrics.py`, `evaluate.py`, `app.py` |

## Decisions and why

- **Rules, not a trained model** → 15 receipts are far too few to train anything; rules work on CPU and I can explain every decision.
- **Split by shop, not by photo** → photos of the same receipt in dev and test would leak the answer and inflate the score.
- **Synthetic variants** → I could only collect 15 receipts. Each photo got a "shadow + tilt" and a "faded + blur + perspective" version. They keep the same label and the same split, and I report them separately.
- **Baseline = OCR on the raw photo** → every improvement is measured against it.
- **Tuning on dev only** → the test numbers are honest.

## The 3 hardest problems (great answer to "what was difficult?")

1. **Dotted zero.** The ERA printer prints 0 with a dot inside; OCR reads it as 8, 6 or 9
   ("24 000.00" → "24 888.66"). Fix: the same amount is printed 3–4 times (Narx, Naqdsiz, Jami, To'lov uchun jami).
   For every copy I list what it could be if an 8/6/9 is really a 0, and pick the value the copies agree on.
   It never changes a number without support from another copy.
2. **QR codes on crumpled paper.** Only 4 of 16 real photos decode: the paper bends the QR grid
   ("checksum error") and creases make white dots inside the corner squares. More preprocessing can't fix
   physical damage, so the system falls back to OCR for those fields (picture: `reports/figures/problems.png`).
3. **Sideways photos.** 7 photos were taken sideways; I added an orientation step
   (a receipt is long and narrow, so if it's wider than tall it's lying sideways; Tesseract OSD checks upside-down).

## My numbers (test set: shops never seen while tuning)

- Field accuracy: **~10 % → 45 %** (baseline → full pipeline); **56–60 % on the real photos**, lower on the synthetic hard ones.
- CER: **95 % → 50 %** with preprocessing (Tesseract). Raw photos contain the table, keyboard, sideways text.
- Best fields: receipt number 67–71 %, fiscal sign 62–71 %, payment 81 % (Tesseract).
- QR decoded: 52 % on the first try → 57 % after retries.
- Speed on CPU: Tesseract ~6 s / receipt, EasyOCR ~17 s → I chose Tesseract as default.
- Honest weak spot: VAT and total are still low, because of the dotted-zero font and bent receipts.

## Metrics in one line each

- **CER** = character edits needed to turn my output into the correct text ÷ length of the correct text.
- **WER** = the same with words.
- **Field accuracy** = correct fields ÷ all fields (a missing field must be predicted as missing).
- **Item F1** = an item counts only if name, quantity, price and total are all correct.
- **QR plain / final** = decoded on the first try / after retries.
- **Consistent receipt** = items add up to the total and no check fails.

## Likely questions

- *Why is accuracy not higher?* → crumpled thermal paper, the dotted-zero font, and only 15 receipts for rules. The errors are listed and classified in `reports/errors.csv`.
- *How would you improve it?* → (1) more receipts, (2) fine-tune an OCR model on this font, (3) a layout model instead of regex rules, (4) ask users to photograph the receipt flat.
- *Why is EasyOCR slower?* → it's a neural network (detector + recognizer) running on CPU; Tesseract is a classic engine.
- *How did you protect personal data?* → cardholder and staff names are blacked out by a script that finds them with OCR, and I checked every image by eye.
- *How do you know your labels are right?* → I typed them from the paper receipts; the QR text I rebuilt from the printed fields matched the 4 decodable codes exactly.
