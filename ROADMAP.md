# Roadmap: closing the gaps to the target values

Current results (test split, real photos, RapidOCR + pre + post) and targets:

| metric | now | target | gap |
|---|---:|---:|---:|
| field accuracy | 82.6 % | 85 % | −2.4 |
| item F1 | 79.2 % | 75 % | reached |
| CER / WER | 16.9 % / 46.1 % | 10 % / 20 % | −6.9 / −26.1 |
| QR decoded (whole photo / close-up) | 60.9 % / 68.8 % | 95 % | −34 / −26 |
| arithmetic checks correct | 100 % | 100 % | reached |
| time per receipt | 8.3 s | ≤ 10 s | reached (budget: 1.7 s) |

Rules for every step: tune on **dev** only, measure on **test**, keep the old numbers in the README,
add a unit test for every new rule, and check the time stays ≤ 10 s.

## What the failure analysis shows

**QR.** Every failed photo (25 real, 9 close-ups, 26 synthetic) is *located but unreadable*: detection
is solved, decoding damaged codes is not. Clean photos still fail 38 % of the time (18/29 decoded),
crumpled ones 79 % (3/14). Per receipt, 23 of 29 decode from at least one of their photos.
Worst sellers: ERA Tinda 11/25 (printed gaps), Akmal Farm 4/9.

**WER.** RapidOCR's recognizer (a Chinese + English model) drops spaces: the OCR text has 17 % fewer
words than the truth ("DIYORNEFTPETROLEUM", "Kartaturi"). One merged pair counts as 2 wrong words.
This is the main reason WER (46 %) is so much higher than CER (17 %).

**CER.** 7 of 10 labelled photos are at 7.6–12 %; three crumpled / shadowed photos (25–47 %) pull the
average up, mostly through wrong line order (lines merged across a curved receipt).

**Fields.** Of the 40 wrong fields on real test photos, **16 are the address** (lines cut off, words
merged), 7 the TIN (dotted zero 0 → 8, or not found), 3 the seller name (spaces lost).
Fixing half of the address errors alone would bring field accuracy to about 86 %.

## Phase A: quick wins (about 2 days) → fields ≥ 85 %, WER much lower

| # | step | why | expected effect |
|---|---|---|---|
| A1 | **Try a Latin recognition model with spaces** (PP-OCRv4 English / Latin rec model in ONNX, run by RapidOCR) instead of the default Chinese + English one | spaces lost → WER, seller name, address | WER 46 → ~25–30 %, seller name and address up |
| A2 | **Rewrite address extraction**: collect all wrapped lines after `Manzil` until the next label (`Yur.Manzil`, `STIR`) | 16 of 40 field errors | field accuracy 82.6 → ~86 % |
| A3 | **Line grouping for curved receipts**: group RapidOCR boxes into lines with a local (not global) height tolerance and by left-to-right order inside a line | merged lines → CER outliers | CER 17 → ~13 % |
| A4 | **TIN from 9 / 14 digits only** + dotted-zero repair using the second printed TIN (`STIR` and `Yur.` block on some layouts) | TIN 70 % | TIN up where a second copy exists |

## Phase B: QR (about 3 days) → whole photo 75–80 %, close-up 85–90 %

| # | step | why |
|---|---|---|
| B1 | **Module-grid resampling**: use the 3 finder patterns + alignment pattern to fit the code's grid locally (piecewise warp), read every module by majority vote of its pixels, re-draw a clean code and decode it in "pure" mode | all failures are "found but unreadable": the grid is bent or has printed gaps |
| B2 | **Add ZBar** (`pyzbar`) as an independent second decoder on the same crops | different algorithm, different failures |
| B3 | **Receipt-level QR**: when a receipt has several photos (whole + close-up), use any one that decodes; report the per-photo and per-receipt rates separately (now 23/29 = 79 % per receipt) | honest, useful in a real app |
| B4 | **UI hint**: if the QR is found but not read, the app asks for a close-up of the code | practical; the spec's QR target assumes a readable code |

95 % per photo is not realistic on crumpled paper with printing defects; B1–B4 target the codes that are
physically readable.

## Phase C: model and data (1–2 weeks) → CER ≈ 10 %

| # | step | why |
|---|---|---|
| C1 | **More data**: 60+ receipts, 12+ sellers, full-text labels for all receipts (now only 7) | more reliable numbers, enough data for C2 |
| C2 | **Fine-tune the recognizer** (PP-OCRv4 rec) on line crops of our receipts: line labels come from aligning the full-text labels with OCR boxes; export to ONNX | the thermal font (dotted zero, thin strokes) is the root cause of most digit errors |
| C3 | **Shadow-robust receipt mask** (r20_a: a strong shadow cut a hole in the receipt) | hard photos |
| C4 | **Docker image** + ONNX speed table (spec "будет плюсом") | reproducibility, bonus points |

## Order of work

1. A1 (one experiment, decides a lot) → A2 → A3 → A4, re-run `make eval`, update README.
2. B3 + B4 (cheap), then B1 (largest QR gain), B2.
3. C1 runs in parallel all the time (photographing receipts), C2 after C1, then C3, C4.
