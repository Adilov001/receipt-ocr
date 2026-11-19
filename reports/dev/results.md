# Results (dev split, 65 images, 13 receipts, 4 sellers)

## Engines × configurations

|                          |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:-------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('rapidocr', 'baseline') |     65.0 |    37.0 |    54.9 |          57.3 |        36.6 |         29.2 |         43.1 |           44.2 |          14.9 |
| ('rapidocr', 'pre')      |     65.0 |    30.4 |    51.8 |          53.8 |        43.6 |         29.2 |         43.1 |           36.5 |          14.5 |
| ('rapidocr', 'pre_post') |     65.0 |    29.8 |    49.4 |          69.4 |        52.6 |         29.2 |         43.1 |           50.0 |          11.7 |


## Field accuracy, %

|                          |   seller_name |   seller_tin |   address |   datetime |   receipt_number |   fiscal_module |   fiscal_sign |   vat |   total |   payment |
|:-------------------------|--------------:|-------------:|----------:|-----------:|-----------------:|----------------:|--------------:|------:|--------:|----------:|
| ('rapidocr', 'baseline') |          40.4 |         53.8 |      38.5 |       51.9 |             63.5 |            59.6 |          53.8 |  67.3 |    73.1 |      71.2 |
| ('rapidocr', 'pre')      |          57.7 |         55.8 |      28.8 |       50.0 |             55.8 |            51.9 |          42.3 |  57.7 |    57.7 |      80.8 |
| ('rapidocr', 'pre_post') |          73.1 |         55.8 |      38.5 |       76.9 |             78.8 |            67.3 |          67.3 |  73.1 |    78.8 |      84.6 |


## By shooting condition

|                                         |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:----------------------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('rapidocr', 'baseline', 'crumpled')    |     27.0 |    46.1 |    63.9 |          41.9 |        24.5 |          0.0 |         18.5 |           29.6 |          18.5 |
| ('rapidocr', 'baseline', 'shadow')      |     15.0 |    32.4 |    50.4 |          62.7 |        43.2 |         13.3 |         40.0 |           46.7 |          16.9 |
| ('rapidocr', 'baseline', 'handheld')    |      9.0 |    50.8 |    69.0 |          31.1 |        35.3 |          0.0 |         33.3 |           44.4 |          17.4 |
| ('rapidocr', 'baseline', 'tilted')      |     17.0 |    29.7 |    49.4 |          61.2 |        39.0 |         11.8 |         35.3 |           41.2 |          16.5 |
| ('rapidocr', 'baseline', 'clean')       |     14.0 |     8.5 |    23.8 |          87.9 |        57.1 |         42.9 |         64.3 |           71.4 |          11.9 |
| ('rapidocr', 'baseline', 'sideways')    |     13.0 |    77.1 |    89.3 |           8.2 |         0.0 |          7.7 |         30.8 |           18.2 |          15.9 |
| ('rapidocr', 'baseline', 'partial')     |     13.0 |   nan   |   nan   |         nan   |       nan   |         69.2 |         76.9 |          nan   |           9.2 |
| ('rapidocr', 'baseline', 'blur')        |      1.0 |    33.2 |    64.5 |          80.0 |         0.0 |          0.0 |          0.0 |          100.0 |          29.3 |
| ('rapidocr', 'baseline', 'synthetic')   |     26.0 |    45.5 |    65.2 |          45.8 |        28.6 |         15.4 |         30.8 |           26.9 |          18.0 |
| ('rapidocr', 'baseline', 'faded')       |     13.0 |    58.1 |    80.0 |          27.7 |        12.9 |         15.4 |         30.8 |            7.7 |          17.7 |
| ('rapidocr', 'baseline', 'perspective') |     13.0 |    58.1 |    80.0 |          27.7 |        12.9 |         15.4 |         30.8 |            7.7 |          17.7 |
| ('rapidocr', 'pre', 'crumpled')         |     27.0 |    35.4 |    57.4 |          46.3 |        49.0 |          0.0 |         18.5 |           29.6 |          18.1 |
| ('rapidocr', 'pre', 'shadow')           |     15.0 |    46.8 |    62.1 |          38.0 |        29.4 |         13.3 |         40.0 |            0.0 |          15.6 |
| ('rapidocr', 'pre', 'handheld')         |      9.0 |    44.2 |    64.1 |          34.4 |        47.1 |          0.0 |         33.3 |           22.2 |          15.6 |
| ('rapidocr', 'pre', 'tilted')           |     17.0 |    43.2 |    60.0 |          40.6 |        26.3 |         11.8 |         35.3 |            0.0 |          15.7 |
| ('rapidocr', 'pre', 'clean')            |     14.0 |    12.6 |    31.3 |          71.4 |        61.9 |         42.9 |         64.3 |           50.0 |          12.7 |
| ('rapidocr', 'pre', 'sideways')         |     13.0 |    26.7 |    49.2 |          50.0 |        52.6 |          7.7 |         30.8 |           45.5 |          14.2 |
| ('rapidocr', 'pre', 'partial')          |     13.0 |   nan   |   nan   |         nan   |       nan   |         69.2 |         76.9 |          nan   |           8.8 |
| ('rapidocr', 'pre', 'blur')             |      1.0 |    31.2 |    63.4 |          60.0 |         0.0 |          0.0 |          0.0 |            0.0 |          29.3 |
| ('rapidocr', 'pre', 'synthetic')        |     26.0 |    46.9 |    69.8 |          34.2 |        19.0 |         15.4 |         30.8 |           15.4 |          15.7 |
| ('rapidocr', 'pre', 'faded')            |     13.0 |    43.7 |    75.4 |          30.8 |        12.1 |         15.4 |         30.8 |           30.8 |          15.6 |
| ('rapidocr', 'pre', 'perspective')      |     13.0 |    43.7 |    75.4 |          30.8 |        12.1 |         15.4 |         30.8 |           30.8 |          15.6 |
| ('rapidocr', 'pre_post', 'crumpled')    |     27.0 |    35.0 |    55.0 |          58.1 |        61.2 |          0.0 |         18.5 |           51.9 |          14.3 |
| ('rapidocr', 'pre_post', 'shadow')      |     15.0 |    46.4 |    60.1 |          57.3 |        41.2 |         13.3 |         40.0 |           26.7 |          12.5 |
| ('rapidocr', 'pre_post', 'handheld')    |      9.0 |    43.8 |    61.8 |          46.7 |        47.1 |          0.0 |         33.3 |           44.4 |          12.5 |
| ('rapidocr', 'pre_post', 'tilted')      |     17.0 |    42.7 |    57.5 |          58.8 |        42.1 |         11.8 |         35.3 |           29.4 |          12.5 |
| ('rapidocr', 'pre_post', 'clean')       |     14.0 |    11.9 |    28.9 |          89.3 |        71.4 |         42.9 |         64.3 |           50.0 |          10.7 |
| ('rapidocr', 'pre_post', 'sideways')    |     13.0 |    26.3 |    47.0 |          60.9 |        63.2 |          7.7 |         30.8 |           54.5 |          12.5 |
| ('rapidocr', 'pre_post', 'partial')     |     13.0 |   nan   |   nan   |         nan   |       nan   |         69.2 |         76.9 |          nan   |           6.7 |
| ('rapidocr', 'pre_post', 'blur')        |      1.0 |    31.1 |    63.4 |          60.0 |         0.0 |          0.0 |          0.0 |            0.0 |          22.4 |
| ('rapidocr', 'pre_post', 'synthetic')   |     26.0 |    46.5 |    67.6 |          51.9 |        28.6 |         15.4 |         30.8 |           34.6 |          12.6 |
| ('rapidocr', 'pre_post', 'faded')       |     13.0 |    43.1 |    72.9 |          47.7 |        18.2 |         15.4 |         30.8 |           38.5 |          12.4 |
| ('rapidocr', 'pre_post', 'perspective') |     13.0 |    43.1 |    72.9 |          47.7 |        18.2 |         15.4 |         30.8 |           38.5 |          12.4 |


## By language

|                                     |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:------------------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('rapidocr', 'baseline', 'uz_latn') |     50.0 |    38.2 |    55.2 |          51.5 |        34.7 |         22.0 |         38.0 |           45.0 |          15.3 |
| ('rapidocr', 'baseline', 'mixed')   |     15.0 |    30.1 |    53.3 |          76.7 |        39.3 |         53.3 |         60.0 |           41.7 |          13.5 |
| ('rapidocr', 'pre', 'uz_latn')      |     50.0 |    29.1 |    50.5 |          51.0 |        64.0 |         22.0 |         38.0 |           40.0 |          15.2 |
| ('rapidocr', 'pre', 'mixed')        |     15.0 |    37.6 |    58.4 |          63.3 |        17.2 |         53.3 |         60.0 |           25.0 |          12.4 |
| ('rapidocr', 'pre_post', 'uz_latn') |     50.0 |    28.6 |    47.7 |          65.0 |        72.0 |         22.0 |         38.0 |           57.5 |          12.2 |
| ('rapidocr', 'pre_post', 'mixed')   |     15.0 |    37.1 |    57.8 |          84.2 |        27.6 |         53.3 |         60.0 |           25.0 |           9.9 |


## QR decoded per photo and per receipt

|                          |   whole photo % |   QR close-up % |   per receipt (any real photo) % |
|:-------------------------|----------------:|----------------:|---------------------------------:|
| ('rapidocr', 'baseline') |            38.5 |            76.9 |                             84.6 |
| ('rapidocr', 'pre')      |            38.5 |            76.9 |                             84.6 |
| ('rapidocr', 'pre_post') |            38.5 |            76.9 |                             84.6 |


## 95 % confidence intervals (bootstrap over receipts, real whole-receipt photos, pre + post)

| engine   |   receipts | field acc %      | item F1 %        | consistent %     | CER %           | WER %            |
|:---------|-----------:|:-----------------|:-----------------|:-----------------|:----------------|:-----------------|
| rapidocr |         13 | 86.9 [82.1–91.5] | 74.3 [58.1–93.5] | 65.4 [46.4–85.2] | 12.3 [8.0–16.9] | 30.2 [24.0–36.3] |


## Per seller (real whole-receipt photos, pre + post)

|                               |   photos |   field acc % |   item F1 % |   consistent % |   CER % |   WER % |
|:------------------------------|---------:|--------------:|------------:|---------------:|--------:|--------:|
| ('rapidocr', 'era_tinda')     |     17.0 |          85.3 |       100.0 |           76.5 |    11.8 |    28.5 |
| ('rapidocr', 'akmal_farm')    |      6.0 |          93.3 |        40.0 |           33.3 |    15.0 |    38.8 |
| ('rapidocr', 'era_hamkorlik') |      2.0 |          85.0 |       100.0 |           50.0 |   nan   |   nan   |
| ('rapidocr', 'era_avtogaz')   |      1.0 |          80.0 |       100.0 |          100.0 |   nan   |   nan   |


## Preprocessing ablation (rapidocr, dev split, post-processing on)

|                              |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:-----------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| none (raw image)             |     65.0 |    36.4 |    52.9 |          69.6 |        49.6 |         29.2 |         43.1 |           48.1 |          11.6 |
| + crop                       |     65.0 |    33.9 |    49.4 |          67.7 |        58.0 |         29.2 |         43.1 |           50.0 |          11.3 |
| + orient                     |     65.0 |    35.9 |    51.1 |          67.3 |        53.8 |         29.2 |         43.1 |           50.0 |           9.9 |
| + deskew                     |     65.0 |    32.5 |    48.8 |          65.8 |        61.1 |         29.2 |         43.1 |           48.1 |           9.5 |
| + illumination               |     65.0 |    32.8 |    50.8 |          66.9 |        55.4 |         29.2 |         43.1 |           44.2 |          10.0 |
| + clahe                      |     65.0 |    29.8 |    49.4 |          69.4 |        52.6 |         29.2 |         43.1 |           50.0 |          11.5 |
| + binarize                   |     65.0 |    41.2 |    62.6 |          52.9 |        30.5 |         29.2 |         43.1 |           25.0 |           9.5 |
| default without crop         |     65.0 |    18.3 |    39.2 |          77.9 |        56.3 |         29.2 |         43.1 |           65.4 |          10.1 |
| default without orient       |     65.0 |    30.6 |    50.1 |          69.0 |        52.6 |         29.2 |         43.1 |           50.0 |           9.9 |
| default without deskew       |     65.0 |    32.8 |    51.2 |          68.8 |        45.8 |         29.2 |         43.1 |           48.1 |           8.9 |
| default without illumination |     65.0 |    29.0 |    47.1 |          69.6 |        48.5 |         29.2 |         43.1 |           46.2 |           8.3 |
| default without clahe        |     65.0 |    32.8 |    50.8 |          66.9 |        55.4 |         29.2 |         43.1 |           44.2 |           8.6 |


## Error causes (pre_post)

|                                           |   count |
|:------------------------------------------|--------:|
| ('rapidocr', 'date/time misread')         |       7 |
| ('rapidocr', 'digits misread')            |      10 |
| ('rapidocr', 'digits missing/extra')      |       4 |
| ('rapidocr', 'digits/amounts misread')    |       4 |
| ('rapidocr', 'not found')                 |      94 |
| ('rapidocr', 'text misread / wrong span') |      40 |


## Error examples

| image        | config   | engine   | conditions                                | field          | gt                                                                            | pred                                                                                                             | cause                     |
|:-------------|:---------|:---------|:------------------------------------------|:---------------|:------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------|:--------------------------|
| r01_a.jpg    | pre_post | rapidocr | crumpled;shadow;handheld;tilted           | seller_name    | Tinda                                                                         |                                                                                                                  | not found                 |
| r01_a.jpg    | pre_post | rapidocr | crumpled;shadow;handheld;tilted           | seller_tin     | 31709886970015                                                                | 31709886978015                                                                                                   | digits misread            |
| r01_a.jpg    | pre_post | rapidocr | crumpled;shadow;handheld;tilted           | address        | Farg'ona viloyati, Farg'ona shahar, 64-Barkamol MFY Yangi asr ko'chasi 130-uy | koʻchasi 130-uy, FARGʻONA VILOYATI., Yur,Manzil FARGʻONA SHAHRI                                                  | text misread / wrong span |
| r01_b.jpg    | pre_post | rapidocr | crumpled                                  | address        | Farg'ona viloyati, Farg'ona shahar, 64-Barkamol MFY Yangi asr ko'chasi 130-uy | Fargʻona viloyati, Fargʻona shahar, 64, Barkamol MFy Yangi asi, koʻchasi 130-uy                                  | text misread / wrong span |
| r07_a.jpg    | pre_post | rapidocr | sideways;crumpled                         | seller_tin     | 31709886970015                                                                |                                                                                                                  | not found                 |
| r08_a.jpg    | pre_post | rapidocr | sideways;crumpled                         | address        | Farg'ona viloyati, Farg'ona shahar, 64-Barkamol MFY Yangi asr ko'chasi 130-uy | Fargʻona viloyati, Fargʻona shahar, 64-, Barkamol MFY YangiasL, koʻchasi 130-uy                                  | text misread / wrong span |
| r08_a.jpg    | pre_post | rapidocr | sideways;crumpled                         | fiscal_module  | NA000000006920                                                                | NA008000006920                                                                                                   | digits misread            |
| r10_a.jpg    | pre_post | rapidocr | sideways;handheld;crumpled                | address        | Farg'ona viloyati, Farg'ona shahar, 64-Barkamol MFY Yangi asr ko'chasi 130-uy | Fa. na viloyati, Fargʻona shahar, 64-, Barkamol MFY Ya i asr, koʻchasi 130-uy                                    | text misread / wrong span |
| r10_a.jpg    | pre_post | rapidocr | sideways;handheld;crumpled                | datetime       | 2026-11-04T18:31:36                                                           |                                                                                                                  | not found                 |
| r12_a.jpg    | pre_post | rapidocr | handheld;crumpled                         | seller_tin     | 31709886970015                                                                |                                                                                                                  | not found                 |
| r12_a.jpg    | pre_post | rapidocr | handheld;crumpled                         | address        | Farg'ona viloyati, Farg'ona shahar, 64-Barkamol MFY Yangi asr ko'chasi 130-uy | anzll Fargʻona shahar, 64-, Barkanol MFY Yangi asr koʻchasi 130-uy, FARG OA VILOYATI., YurManzll FARGʻONA SHAHRI | text misread / wrong span |
| r12_a.jpg    | pre_post | rapidocr | handheld;crumpled                         | payment        | card                                                                          |                                                                                                                  | not found                 |
| r14_a.jpg    | pre_post | rapidocr | clean                                     | address        | Farg'ona viloyati, Farg'ona shahar, 64-Barkamol MFY Yangi asr ko'chasi 130-uy | Fargʻona viloyati, Fargʻona shahar , 64-, Barkamol MFY Yangiasr, koʻchasi 130-uy                                 | text misread / wrong span |
| r19_a.jpg    | pre_post | rapidocr | crumpled                                  | address        | Farg'ona viloyati, Farg'ona shahri, Hamkorlik MFY, Nizomiy ko'chasi, 28 B uy  | Fargʻona viloyati, Fargʻona shahri, Hamkorlik MFy,Nizomiy, koʻchasi, 28 8 uy                                     | text misread / wrong span |
| r01_c.jpg    | pre_post | rapidocr | clean                                     | seller_tin     | 31709886970015                                                                |                                                                                                                  | not found                 |
| r01_c.jpg    | pre_post | rapidocr | clean                                     | address        | Farg'ona viloyati, Farg'ona shahar, 64-Barkamol MFY Yangi asr ko'chasi 130-uy | Fargʻona shahar, Barkamol MFy Yang, koʻchasi13                                                                   | text misread / wrong span |
| r04_c.jpg    | pre_post | rapidocr | blur                                      | seller_name    | 9-Этажка                                                                      | AKMAL                                                                                                            | text misread / wrong span |
| r04_c.jpg    | pre_post | rapidocr | blur                                      | datetime       | 2026-11-03T17:16:32                                                           | 2029-11-03T17:15:00                                                                                              | date/time misread         |
| r04_c.jpg    | pre_post | rapidocr | blur                                      | receipt_number | 28616                                                                         | 65                                                                                                               | digits missing/extra      |
| r04_c.jpg    | pre_post | rapidocr | blur                                      | vat            | 957.14                                                                        |                                                                                                                  | not found                 |
| r05_c.jpg    | pre_post | rapidocr | clean                                     | seller_tin     | 31709886970015                                                                |                                                                                                                  | not found                 |
| r05_c.jpg    | pre_post | rapidocr | clean                                     | address        | Farg'ona viloyati, Farg'ona shahar, 64-Barkamol MFY Yangi asr ko'chasi 130-uy | FARGʻONA SHAHRI                                                                                                  | text misread / wrong span |
| r06_c.jpg    | pre_post | rapidocr | clean                                     | fiscal_sign    | 559055341237                                                                  |                                                                                                                  | not found                 |
| r07_c.jpg    | pre_post | rapidocr | clean                                     | address        | Farg'ona viloyati, Farg'ona shahar, 64-Barkamol MFY Yangi asr ko'chasi 130-uy | Fargʻund viloyati, Fargʻona shahar, 64-, Barkamol MFy Yangi asr, koʻchasi 130-uy                                 | text misread / wrong span |
| r08_c.jpg    | pre_post | rapidocr | clean                                     | seller_tin     | 31709886970015                                                                |                                                                                                                  | not found                 |
| r08_c.jpg    | pre_post | rapidocr | clean                                     | address        | Farg'ona viloyati, Farg'ona shahar, 64-Barkamol MFY Yangi asr ko'chasi 130-uy | Fargʻona viloyat, Fargʻona shahar, Barkamol MFy Yangi, koʻchasi 130-                                             | text misread / wrong span |
| r08_c.jpg    | pre_post | rapidocr | clean                                     | datetime       | 2026-11-04T21:03:56                                                           | 2026-11-04T21:03:00                                                                                              | date/time misread         |
| r08_c.jpg    | pre_post | rapidocr | clean                                     | fiscal_sign    | 115903172013                                                                  |                                                                                                                  | not found                 |
| r10_c.jpg    | pre_post | rapidocr | sideways                                  | address        | Farg'ona viloyati, Farg'ona shahar, 64-Barkamol MFY Yangi asr ko'chasi 130-uy | Fa na viloyati, Fargʻona shahar, 64-, Barkamol MFY Yo l asr, koʻchasi 130-uy                                     | text misread / wrong span |
| r12_c.jpg    | pre_post | rapidocr | sideways                                  | fiscal_module  | NA000000006920                                                                | NA100000006920                                                                                                   | digits misread            |
| r19_c.jpg    | pre_post | rapidocr | clean                                     | seller_tin     | 312599814                                                                     |                                                                                                                  | not found                 |
| r19_c.jpg    | pre_post | rapidocr | clean                                     | address        | Farg'ona viloyati, Farg'ona shahri, Hamkorlik MFY, Nizomiy ko'chasi, 28 B uy  | Fargʻona, Hamkorlik MFY, koʻchasi,2                                                                              | text misread / wrong span |
| r24_a.jpg    | pre_post | rapidocr | clean                                     | seller_tin     | 202647034                                                                     |                                                                                                                  | not found                 |
| r24_a.jpg    | pre_post | rapidocr | clean                                     | address        | Farg'ona viloyat, Bag'dod tumani, Konizar MFY, Konizar qishlo'gi              | Bagʻdod tumani, Koni, MFY, Konizar qishlo                                                                        | text misread / wrong span |
| r01_a_x1.jpg | pre_post | rapidocr | synthetic;crumpled;handheld;shadow;tilted | seller_name    | Tinda                                                                         |                                                                                                                  | not found                 |
| r01_a_x1.jpg | pre_post | rapidocr | synthetic;crumpled;handheld;shadow;tilted | seller_tin     | 31709886970015                                                                | 31709886978815                                                                                                   | digits misread            |
| r01_a_x1.jpg | pre_post | rapidocr | synthetic;crumpled;handheld;shadow;tilted | address        | Farg'ona viloyati, Farg'ona shahar, 64-Barkamol MFY Yangi asr ko'chasi 130-uy | koʻchasi 130-uy, Yur,Manzil FARGʻONA SHAHRI                                                                      | text misread / wrong span |
| r01_a_x1.jpg | pre_post | rapidocr | synthetic;crumpled;handheld;shadow;tilted | datetime       | 2026-11-04T13:47:26                                                           | 2026-11-04T13:47:22                                                                                              | date/time misread         |
| r01_a_x1.jpg | pre_post | rapidocr | synthetic;crumpled;handheld;shadow;tilted | receipt_number | 36785                                                                         |                                                                                                                  | not found                 |
| r01_a_x1.jpg | pre_post | rapidocr | synthetic;crumpled;handheld;shadow;tilted | fiscal_module  | NA000000006920                                                                |                                                                                                                  | not found                 |