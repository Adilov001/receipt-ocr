# Roadmap (v2, 19 Nov 2026): following the technical specification

The plan follows the specification section by section: first close what it requires, then the
"будет плюсом" items, then deeper improvements. Rules for every step: tune on **dev** only, measure on
**test**, keep the holdout untouched until a new one is collected, add a test for every new rule,
keep the time ≤ 10 s per receipt.

## Where we are (test, real photos, RapidOCR + pre + post)

| target (HR) | now | status |
|---|---:|---|
| field accuracy ≥ 85 % | 89.6 % [82.9–95.0] | reached (holdout of 6 new shops: 63.3 %) |
| item F1 ≥ 75 % | 87.0 % | reached |
| CER ≤ 10 % | 9.4 % | reached |
| WER ≤ 20 % | 24.3 % | not reached |
| QR ≥ 95 % | 60.9 % per photo, 81.2 % per receipt | not reached |
| arithmetic checks 100 % | 100 % | reached |
| ≤ 10 s per receipt | 6–8 s (also in Docker) | reached |

Done in the first part of the internship (17–18 Nov): recognizer chosen among 5 (`cyrillic_PP-OCRv5`),
address block, line grouping on curved paper, label vocabulary, confidence intervals, QR check on 150
public receipts, 6-shop holdout, REST API + Docker.

## Phase 1 — close the gaps the specification requires

| # | spec | task | who | time |
|---|---|---|---|---|
| 1.1 | §3 | **Full text labelled for every receipt** (now 15 of 35): drafts from OCR, corrected against the paper | Claude + you | 2–3 h |
| 1.2 | §3 | **Real photos for missing conditions**: uneven light, perspective (shot at an angle), faded old receipt, long receipt in one shot (now only synthetic) — ~10 photos, names masked, labelled | you + Claude | 1–2 h |
| 1.3 | §4.1 | **Contribution of each preprocessing step by shooting condition** (ablation split by condition) in the README | Claude | 30 min |
| 1.4 | §5 | **CER / WER by language and alphabet** (Uzbek Latin, Cyrillic, Russian) once 1.1 is done | Claude | 20 min |
| 1.5 | §4.6 | **Recheck the web UI** with the new default engine (boxes, QR area, checks, GT diff, engine comparison) | Claude | 15 min |

## Phase 2 — "будет плюсом" (bonus points, §7)

| # | task | time |
|---|---|---|
| 2.1 | **Quantization of the recognizer (FP32 → INT8 ONNX)** with a table: size, OCR time, CER / field accuracy before vs after | 1–2 h |
| 2.2 | **Full Uzbek Cyrillic support**: 2–3 receipts printed in Uzbek Cyrillic (ў, қ, ғ, ҳ), labelled and measured; add Cyrillic label words | 2 h + photos |
| 2.3 | **Long receipt from several photos**: stitch overlapping frames (feature matching), then the normal pipeline | ~1 day |

## Phase 3 — accuracy on new layouts and remaining targets

| # | task | why | time |
|---|---|---|---|
| 3.1 | **Label words of new layouts** (`Umumiy to'lov`, `Kassa raqami`, `Savdo Cheki`, `Check raqami`, `Fiskal belgi`, `JAMI =`) + TIN reliability | holdout 63 % on new shops: most errors are "not found" | 1 day |
| 3.2 | **New holdout** (5–10 receipts from new shops), measured once | the old holdout has been seen | photos + 1 h |
| 3.3 | **QR tuning on the public Russian train set** (~850 receipts): retry order, scales, time budget; confirm on own photos | QR 81 % per receipt | 2–3 h |
| 3.4 | **API hint**: when a QR is found but unreadable, the response asks for a close-up | practical QR fix for users | 30 min |

## Phase 4 — model training (later in the internship)

| # | task | time |
|---|---|---|
| 4.1 | More receipts with full-text labels (target 60+ receipts, 12+ shops) | ongoing |
| 4.2 | **Fine-tune the recognizer** on line crops of dev receipts (Colab GPU, allowed by §6), export to ONNX | 2–3 days |
| 4.3 | Compare with the current model on test + new holdout; keep it only if better | 2 h |

## Order

1. **Now:** 1.5 → 1.3 → 2.1 (Claude, alone) — meanwhile **you** take the photos for 1.2 and look for
   Uzbek Cyrillic receipts (2.2).
2. **Together:** 1.1 full-text labels, then 1.4.
3. **Next:** 3.1 → 3.2 → 3.4 → 3.3.
4. **Later:** 2.3, Phase 4.

Integration requests from the web team always come first.
