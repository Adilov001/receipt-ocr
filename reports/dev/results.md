# Results (dev split, 27 images, 8 receipts, 1 sellers)

## Engines × configurations

|                           |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:--------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('tesseract', 'baseline') |     27.0 |     nan |     nan |           2.2 |         0.0 |          0.0 |          0.0 |            0.0 |           6.0 |
| ('tesseract', 'pre')      |     27.0 |     nan |     nan |           9.6 |         0.0 |          0.0 |          0.0 |            0.0 |           9.5 |
| ('tesseract', 'pre_post') |     27.0 |     nan |     nan |          17.0 |        10.5 |          0.0 |          0.0 |           14.8 |          10.2 |


## Field accuracy, %

|                           |   seller_name |   seller_tin |   address |   datetime |   receipt_number |   fiscal_module |   fiscal_sign |   vat |   total |   payment |
|:--------------------------|--------------:|-------------:|----------:|-----------:|-----------------:|----------------:|--------------:|------:|--------:|----------:|
| ('tesseract', 'baseline') |           7.4 |          0.0 |       0.0 |        0.0 |              3.7 |             0.0 |           3.7 |   0.0 |     3.7 |       3.7 |
| ('tesseract', 'pre')      |          14.8 |          3.7 |       3.7 |        7.4 |             22.2 |             0.0 |           7.4 |   0.0 |     7.4 |      29.6 |
| ('tesseract', 'pre_post') |          18.5 |          3.7 |       3.7 |       25.9 |             22.2 |             0.0 |           7.4 |  14.8 |    29.6 |      44.4 |


## By shooting condition

|                                          |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:-----------------------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('tesseract', 'baseline', 'crumpled')    |     24.0 |     nan |     nan |           1.2 |         0.0 |          0.0 |          0.0 |            0.0 |           6.1 |
| ('tesseract', 'baseline', 'shadow')      |     11.0 |     nan |     nan |           3.6 |         0.0 |          0.0 |          0.0 |            0.0 |           5.8 |
| ('tesseract', 'baseline', 'handheld')    |      9.0 |     nan |     nan |           3.3 |         0.0 |          0.0 |          0.0 |            0.0 |           5.5 |
| ('tesseract', 'baseline', 'tilted')      |     13.0 |     nan |     nan |           3.1 |         0.0 |          0.0 |          0.0 |            0.0 |           5.9 |
| ('tesseract', 'baseline', 'sideways')    |      9.0 |     nan |     nan |           0.0 |         0.0 |          0.0 |          0.0 |            0.0 |           5.8 |
| ('tesseract', 'baseline', 'clean')       |      1.0 |     nan |     nan |          20.0 |         0.0 |          0.0 |          0.0 |            0.0 |           5.4 |
| ('tesseract', 'baseline', 'synthetic')   |     18.0 |     nan |     nan |           0.6 |         0.0 |          0.0 |          0.0 |            0.0 |           5.3 |
| ('tesseract', 'baseline', 'faded')       |      9.0 |     nan |     nan |           0.0 |         0.0 |          0.0 |          0.0 |            0.0 |           4.8 |
| ('tesseract', 'baseline', 'perspective') |      9.0 |     nan |     nan |           0.0 |         0.0 |          0.0 |          0.0 |            0.0 |           4.8 |
| ('tesseract', 'pre', 'crumpled')         |     24.0 |     nan |     nan |           8.8 |         0.0 |          0.0 |          0.0 |            0.0 |           9.6 |
| ('tesseract', 'pre', 'shadow')           |     11.0 |     nan |     nan |          10.0 |         0.0 |          0.0 |          0.0 |            0.0 |           7.4 |
| ('tesseract', 'pre', 'handheld')         |      9.0 |     nan |     nan |           8.9 |         0.0 |          0.0 |          0.0 |            0.0 |           8.1 |
| ('tesseract', 'pre', 'tilted')           |     13.0 |     nan |     nan |           9.2 |         0.0 |          0.0 |          0.0 |            0.0 |           8.1 |
| ('tesseract', 'pre', 'sideways')         |      9.0 |     nan |     nan |          12.2 |         0.0 |          0.0 |          0.0 |            0.0 |           9.2 |
| ('tesseract', 'pre', 'clean')            |      1.0 |     nan |     nan |          30.0 |         0.0 |          0.0 |          0.0 |            0.0 |          11.8 |
| ('tesseract', 'pre', 'synthetic')        |     18.0 |     nan |     nan |           7.2 |         0.0 |          0.0 |          0.0 |            0.0 |           8.0 |
| ('tesseract', 'pre', 'faded')            |      9.0 |     nan |     nan |           5.6 |         0.0 |          0.0 |          0.0 |            0.0 |           8.6 |
| ('tesseract', 'pre', 'perspective')      |      9.0 |     nan |     nan |           5.6 |         0.0 |          0.0 |          0.0 |            0.0 |           8.6 |
| ('tesseract', 'pre_post', 'crumpled')    |     24.0 |     nan |     nan |          14.6 |         6.1 |          0.0 |          0.0 |           12.5 |          10.2 |
| ('tesseract', 'pre_post', 'shadow')      |     11.0 |     nan |     nan |          13.6 |         0.0 |          0.0 |          0.0 |            0.0 |           8.0 |
| ('tesseract', 'pre_post', 'handheld')    |      9.0 |     nan |     nan |          13.3 |         0.0 |          0.0 |          0.0 |           11.1 |           8.8 |
| ('tesseract', 'pre_post', 'tilted')      |     13.0 |     nan |     nan |          13.1 |         0.0 |          0.0 |          0.0 |            7.7 |           8.7 |
| ('tesseract', 'pre_post', 'sideways')    |      9.0 |     nan |     nan |          23.3 |        16.7 |          0.0 |          0.0 |           22.2 |           9.8 |
| ('tesseract', 'pre_post', 'clean')       |      1.0 |     nan |     nan |          60.0 |       100.0 |          0.0 |          0.0 |          100.0 |          13.0 |
| ('tesseract', 'pre_post', 'synthetic')   |     18.0 |     nan |     nan |           9.4 |         0.0 |          0.0 |          0.0 |            5.6 |           8.9 |
| ('tesseract', 'pre_post', 'faded')       |      9.0 |     nan |     nan |           5.6 |         0.0 |          0.0 |          0.0 |           11.1 |           9.5 |
| ('tesseract', 'pre_post', 'perspective') |      9.0 |     nan |     nan |           5.6 |         0.0 |          0.0 |          0.0 |           11.1 |           9.5 |


## By language

|                                      |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:-------------------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('tesseract', 'baseline', 'uz_latn') |     27.0 |     nan |     nan |           2.2 |         0.0 |          0.0 |          0.0 |            0.0 |           6.0 |
| ('tesseract', 'pre', 'uz_latn')      |     27.0 |     nan |     nan |           9.6 |         0.0 |          0.0 |          0.0 |            0.0 |           9.5 |
| ('tesseract', 'pre_post', 'uz_latn') |     27.0 |     nan |     nan |          17.0 |        10.5 |          0.0 |          0.0 |           14.8 |          10.2 |


## Preprocessing ablation (tesseract, dev split, post-processing on)

|                              |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:-----------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| none (raw image)             |     27.0 |     nan |     nan |           1.9 |         0.0 |          0.0 |          0.0 |            0.0 |           5.6 |
| + crop                       |     27.0 |     nan |     nan |           7.4 |         0.0 |          0.0 |          0.0 |            3.7 |           6.7 |
| + orient                     |     27.0 |     nan |     nan |           7.4 |         0.0 |          0.0 |          0.0 |            3.7 |           7.0 |
| + deskew                     |     27.0 |     nan |     nan |          10.0 |         0.0 |          0.0 |          0.0 |            3.7 |           6.3 |
| + illumination               |     27.0 |     nan |     nan |          12.6 |        10.8 |          0.0 |          0.0 |            7.4 |           6.7 |
| + clahe                      |     27.0 |     nan |     nan |          17.0 |        10.5 |          0.0 |          0.0 |           14.8 |           9.0 |
| + binarize                   |     27.0 |     nan |     nan |           7.4 |         0.0 |          0.0 |          0.0 |            0.0 |           7.6 |
| default without crop         |     27.0 |     nan |     nan |          15.2 |         0.0 |          0.0 |          0.0 |            0.0 |           6.0 |
| default without orient       |     27.0 |     nan |     nan |          15.6 |        10.5 |          0.0 |          0.0 |           14.8 |           6.4 |
| default without deskew       |     27.0 |     nan |     nan |          12.2 |         6.1 |          0.0 |          0.0 |            7.4 |           6.4 |
| default without illumination |     27.0 |     nan |     nan |           7.4 |         5.6 |          0.0 |          0.0 |           11.1 |           5.8 |
| default without clahe        |     27.0 |     nan |     nan |          12.6 |        10.8 |          0.0 |          0.0 |            7.4 |           6.9 |


## Error causes (pre_post)

|                                             |   count |
|:--------------------------------------------|--------:|
| ('tesseract', 'date/time misread')          |       6 |
| ('tesseract', 'digits misread')             |       9 |
| ('tesseract', 'digits missing/extra')       |       2 |
| ('tesseract', 'digits/amounts misread')     |      11 |
| ('tesseract', 'not found')                  |     153 |
| ('tesseract', 'text misread / wrong span')  |      42 |
| ('tesseract', 'thousand/decimal separator') |       1 |


## Error examples

| image     | config   | engine    | conditions                      | field          | gt                                                                            | pred                                                                                                                             | cause                     |
|:----------|:---------|:----------|:--------------------------------|:---------------|:------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------|:--------------------------|
| r01_a.jpg | pre_post | tesseract | crumpled;shadow;handheld;tilted | seller_name    | Tinda                                                                         |                                                                                                                                  | not found                 |
| r01_a.jpg | pre_post | tesseract | crumpled;shadow;handheld;tilted | seller_tin     | 31709886970015                                                                | 41709886970015                                                                                                                   | digits misread            |
| r01_a.jpg | pre_post | tesseract | crumpled;shadow;handheld;tilted | address        | Farg'ona viloyati, Farg'ona shahar, 64-Barkamol MFY Yangi asr ko'chasi 130-uy | koʻchasi 13, Yur. Mane) FARGʻONA VILOYATI, ) FARGʻONA SHAHRI                                                                     | text misread / wrong span |
| r01_a.jpg | pre_post | tesseract | crumpled;shadow;handheld;tilted | receipt_number | 36785                                                                         |                                                                                                                                  | not found                 |
| r01_a.jpg | pre_post | tesseract | crumpled;shadow;handheld;tilted | fiscal_module  | NA000000006920                                                                |                                                                                                                                  | not found                 |
| r01_a.jpg | pre_post | tesseract | crumpled;shadow;handheld;tilted | vat            | 0.0                                                                           |                                                                                                                                  | not found                 |
| r01_a.jpg | pre_post | tesseract | crumpled;shadow;handheld;tilted | total          | 32000.0                                                                       | 80.0                                                                                                                             | digits/amounts misread    |
| r01_a.jpg | pre_post | tesseract | crumpled;shadow;handheld;tilted | payment        | card                                                                          |                                                                                                                                  | not found                 |
| r01_b.jpg | pre_post | tesseract | crumpled                        | seller_name    | Tinda                                                                         | LIYEV ASKARALIYEVICH                                                                                                             | text misread / wrong span |
| r01_b.jpg | pre_post | tesseract | crumpled                        | seller_tin     | 31709886970015                                                                |                                                                                                                                  | not found                 |
| r01_b.jpg | pre_post | tesseract | crumpled                        | address        | Farg'ona viloyati, Farg'ona shahar, 64-Barkamol MFY Yangi asr ko'chasi 130-uy | Fargʻona viloyati, Fargʻona shahar ‚ 64-                                                                                         | text misread / wrong span |
| r01_b.jpg | pre_post | tesseract | crumpled                        | receipt_number | 36785                                                                         |                                                                                                                                  | not found                 |
| r01_b.jpg | pre_post | tesseract | crumpled                        | fiscal_module  | NA000000006920                                                                |                                                                                                                                  | not found                 |
| r01_b.jpg | pre_post | tesseract | crumpled                        | fiscal_sign    | 352606397030                                                                  |                                                                                                                                  | not found                 |
| r01_b.jpg | pre_post | tesseract | crumpled                        | vat            | 0.0                                                                           |                                                                                                                                  | not found                 |
| r01_b.jpg | pre_post | tesseract | crumpled                        | total          | 32000.0                                                                       | 32009.0                                                                                                                          | digits/amounts misread    |
| r01_b.jpg | pre_post | tesseract | crumpled                        | payment        | card                                                                          |                                                                                                                                  | not found                 |
| r05_a.jpg | pre_post | tesseract | crumpled                        | seller_name    | Tinda                                                                         | turasan MAMADALIYIN АКА ЕК                                                                                                       | text misread / wrong span |
| r05_a.jpg | pre_post | tesseract | crumpled                        | seller_tin     | 31709886970015                                                                |                                                                                                                                  | not found                 |
| r05_a.jpg | pre_post | tesseract | crumpled                        | address        | Farg'ona viloyati, Farg'ona shahar, 64-Barkamol MFY Yangi asr ko'chasi 130-uy | Fargʻona) viloyt |                                                                                                               | text misread / wrong span |
| r05_a.jpg | pre_post | tesseract | crumpled                        | datetime       | 2026-11-04T18:07:47                                                           | 2026-11-04T18:07:00                                                                                                              | date/time misread         |
| r05_a.jpg | pre_post | tesseract | crumpled                        | receipt_number | 36800                                                                         | 36802                                                                                                                            | digits misread            |
| r05_a.jpg | pre_post | tesseract | crumpled                        | fiscal_module  | NA000000006920                                                                |                                                                                                                                  | not found                 |
| r05_a.jpg | pre_post | tesseract | crumpled                        | fiscal_sign    | 861532066154                                                                  | 861532866154                                                                                                                     | digits misread            |
| r05_a.jpg | pre_post | tesseract | crumpled                        | vat            | 0.0                                                                           |                                                                                                                                  | not found                 |
| r06_a.jpg | pre_post | tesseract | crumpled;tilted                 | seller_name    | Tinda                                                                         | ADHAMJON MAMADALIYEV ^ Te ati                                                                                                    | text misread / wrong span |
| r06_a.jpg | pre_post | tesseract | crumpled;tilted                 | seller_tin     | 31709886970015                                                                |                                                                                                                                  | not found                 |
| r06_a.jpg | pre_post | tesseract | crumpled;tilted                 | address        | Farg'ona viloyati, Farg'ona shahar, 64-Barkamol MFY Yangi asr ko'chasi 130-uy | fargʻona Уз У 64-, papgʻona Shahar + 7                                                                                           | text misread / wrong span |
| r06_a.jpg | pre_post | tesseract | crumpled;tilted                 | datetime       | 2026-11-04T18:04:00                                                           | 2026-11-04T18:03:00                                                                                                              | date/time misread         |
| r06_a.jpg | pre_post | tesseract | crumpled;tilted                 | receipt_number | 36799                                                                         | 3                                                                                                                                | digits missing/extra      |
| r06_a.jpg | pre_post | tesseract | crumpled;tilted                 | fiscal_module  | NA000000006920                                                                |                                                                                                                                  | not found                 |
| r06_a.jpg | pre_post | tesseract | crumpled;tilted                 | fiscal_sign    | 559055341237                                                                  |                                                                                                                                  | not found                 |
| r06_a.jpg | pre_post | tesseract | crumpled;tilted                 | total          | 10000.0                                                                       | 10080.0                                                                                                                          | digits/amounts misread    |
| r07_a.jpg | pre_post | tesseract | sideways;crumpled               | seller_name    | Tinda                                                                         | ADHAMION MAMADAL.                                                                                                                | text misread / wrong span |
| r07_a.jpg | pre_post | tesseract | sideways;crumpled               | seller_tin     | 31709886970015                                                                |                                                                                                                                  | not found                 |
| r07_a.jpg | pre_post | tesseract | sideways;crumpled               | address        | Farg'ona viloyati, Farg'ona shahar, 64-Barkamol MFY Yangi asr ko'chasi 130-uy | Fargʻona viloyati, Fargʻona shahar 5, 199, Barkamol MFY Yanyi ast, koʻchasi 139-МУ, Yur Manet FARGʻONA VILOYATI, FARGʻONA SHAHRI | text misread / wrong span |
| r07_a.jpg | pre_post | tesseract | sideways;crumpled               | datetime       | 2026-11-04T20:33:07                                                           | 2026-11-04T20:35:07                                                                                                              | date/time misread         |
| r07_a.jpg | pre_post | tesseract | sideways;crumpled               | fiscal_module  | NA000000006920                                                                |                                                                                                                                  | not found                 |
| r07_a.jpg | pre_post | tesseract | sideways;crumpled               | fiscal_sign    | 570122841671                                                                  |                                                                                                                                  | not found                 |
| r07_a.jpg | pre_post | tesseract | sideways;crumpled               | payment        | card                                                                          | other                                                                                                                            | text misread / wrong span |