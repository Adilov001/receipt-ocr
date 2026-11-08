# Results (test split, 21 images, 7 receipts, 2 sellers)

## Engines × configurations

|                           |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:--------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('tesseract', 'baseline') |     21.0 |    94.7 |    96.9 |           9.5 |         0.0 |         52.4 |         57.1 |            0.0 |           3.9 |
| ('tesseract', 'pre')      |     21.0 |    50.2 |    83.6 |          17.6 |         0.0 |         52.4 |         57.1 |            0.0 |           6.1 |
| ('tesseract', 'pre_post') |     21.0 |    50.2 |    83.6 |          44.8 |         4.1 |         52.4 |         57.1 |            0.0 |           6.2 |
| ('easyocr', 'baseline')   |     21.0 |    79.8 |    97.3 |          10.5 |         0.0 |         52.4 |         57.1 |            0.0 |          43.0 |
| ('easyocr', 'pre')        |     21.0 |    52.7 |    84.1 |          20.5 |         0.0 |         52.4 |         57.1 |            4.8 |          17.3 |
| ('easyocr', 'pre_post')   |     21.0 |    52.7 |    84.1 |          44.3 |         0.0 |         52.4 |         57.1 |            0.0 |          17.5 |


## Field accuracy, %

|                           |   seller_name |   seller_tin |   address |   datetime |   receipt_number |   fiscal_module |   fiscal_sign |   vat |   total |   payment |
|:--------------------------|--------------:|-------------:|----------:|-----------:|-----------------:|----------------:|--------------:|------:|--------:|----------:|
| ('tesseract', 'baseline') |           4.8 |         28.6 |      28.6 |        0.0 |              0.0 |             4.8 |           0.0 |   0.0 |     0.0 |      28.6 |
| ('tesseract', 'pre')      |           4.8 |         38.1 |      23.8 |        4.8 |             23.8 |             9.5 |          14.3 |   0.0 |     0.0 |      57.1 |
| ('tesseract', 'pre_post') |          23.8 |         38.1 |      23.8 |       57.1 |             66.7 |            57.1 |          71.4 |   4.8 |    23.8 |      81.0 |
| ('easyocr', 'baseline')   |           0.0 |         28.6 |      28.6 |        0.0 |              0.0 |             4.8 |           0.0 |   0.0 |    14.3 |      28.6 |
| ('easyocr', 'pre')        |           0.0 |         47.6 |      28.6 |        4.8 |             28.6 |             9.5 |           9.5 |  23.8 |     0.0 |      52.4 |
| ('easyocr', 'pre_post')   |           9.5 |         47.6 |      28.6 |       66.7 |             71.4 |            61.9 |          61.9 |  23.8 |    19.0 |      52.4 |


## By shooting condition

|                                          |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:-----------------------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('tesseract', 'baseline', 'sideways')    |     12.0 |    99.3 |    99.9 |           0.0 |         0.0 |         50.0 |         50.0 |            0.0 |           4.5 |
| ('tesseract', 'baseline', 'crumpled')    |     12.0 |    97.4 |    98.7 |           0.0 |         0.0 |         25.0 |         25.0 |            0.0 |           5.5 |
| ('tesseract', 'baseline', 'clean')       |      2.0 |    70.0 |    82.2 |          35.0 |         0.0 |         50.0 |        100.0 |            0.0 |           2.4 |
| ('tesseract', 'baseline', 'handheld')    |      6.0 |    96.3 |    97.5 |           0.0 |         0.0 |         50.0 |         50.0 |            0.0 |           3.4 |
| ('tesseract', 'baseline', 'synthetic')   |     14.0 |    96.1 |    98.0 |           9.3 |         0.0 |         57.1 |         57.1 |            0.0 |           3.8 |
| ('tesseract', 'baseline', 'shadow')      |      7.0 |    94.2 |    96.6 |          10.0 |         0.0 |         57.1 |         57.1 |            0.0 |           4.4 |
| ('tesseract', 'baseline', 'tilted')      |      7.0 |    94.2 |    96.6 |          10.0 |         0.0 |         57.1 |         57.1 |            0.0 |           4.4 |
| ('tesseract', 'baseline', 'faded')       |      7.0 |    98.0 |    99.4 |           8.6 |         0.0 |         57.1 |         57.1 |            0.0 |           3.1 |
| ('tesseract', 'baseline', 'perspective') |      7.0 |    98.0 |    99.4 |           8.6 |         0.0 |         57.1 |         57.1 |            0.0 |           3.1 |
| ('tesseract', 'pre', 'sideways')         |     12.0 |    42.1 |    74.8 |          12.5 |         0.0 |         50.0 |         50.0 |            0.0 |           6.4 |
| ('tesseract', 'pre', 'crumpled')         |     12.0 |    48.5 |    82.2 |          12.5 |         0.0 |         25.0 |         25.0 |            0.0 |           7.2 |
| ('tesseract', 'pre', 'clean')            |      2.0 |    31.3 |    68.5 |          45.0 |         0.0 |         50.0 |        100.0 |            0.0 |           5.3 |
| ('tesseract', 'pre', 'handheld')         |      6.0 |    59.7 |    96.9 |           6.7 |         0.0 |         50.0 |         50.0 |            0.0 |           6.4 |
| ('tesseract', 'pre', 'synthetic')        |     14.0 |    60.1 |    92.1 |          14.3 |         0.0 |         57.1 |         57.1 |            0.0 |           5.7 |
| ('tesseract', 'pre', 'shadow')           |      7.0 |    58.9 |    81.1 |          14.3 |         0.0 |         57.1 |         57.1 |            0.0 |           5.0 |
| ('tesseract', 'pre', 'tilted')           |      7.0 |    58.9 |    81.1 |          14.3 |         0.0 |         57.1 |         57.1 |            0.0 |           5.0 |
| ('tesseract', 'pre', 'faded')            |      7.0 |    61.2 |   103.0 |          14.3 |         0.0 |         57.1 |         57.1 |            0.0 |           6.4 |
| ('tesseract', 'pre', 'perspective')      |      7.0 |    61.2 |   103.0 |          14.3 |         0.0 |         57.1 |         57.1 |            0.0 |           6.4 |
| ('tesseract', 'pre_post', 'sideways')    |     12.0 |    42.1 |    74.8 |          40.8 |         9.5 |         50.0 |         50.0 |            0.0 |           6.6 |
| ('tesseract', 'pre_post', 'crumpled')    |     12.0 |    48.5 |    82.2 |          28.3 |         0.0 |         25.0 |         25.0 |            0.0 |           7.4 |
| ('tesseract', 'pre_post', 'clean')       |      2.0 |    31.3 |    68.5 |          75.0 |         0.0 |         50.0 |        100.0 |            0.0 |           5.3 |
| ('tesseract', 'pre_post', 'handheld')    |      6.0 |    59.7 |    96.9 |          35.0 |        22.2 |         50.0 |         50.0 |            0.0 |           6.5 |
| ('tesseract', 'pre_post', 'synthetic')   |     14.0 |    60.1 |    92.1 |          39.3 |         0.0 |         57.1 |         57.1 |            0.0 |           5.8 |
| ('tesseract', 'pre_post', 'shadow')      |      7.0 |    58.9 |    81.1 |          40.0 |         0.0 |         57.1 |         57.1 |            0.0 |           5.1 |
| ('tesseract', 'pre_post', 'tilted')      |      7.0 |    58.9 |    81.1 |          40.0 |         0.0 |         57.1 |         57.1 |            0.0 |           5.1 |
| ('tesseract', 'pre_post', 'faded')       |      7.0 |    61.2 |   103.0 |          38.6 |         0.0 |         57.1 |         57.1 |            0.0 |           6.5 |
| ('tesseract', 'pre_post', 'perspective') |      7.0 |    61.2 |   103.0 |          38.6 |         0.0 |         57.1 |         57.1 |            0.0 |           6.5 |
| ('easyocr', 'baseline', 'sideways')      |     12.0 |    88.9 |   102.2 |           0.0 |         0.0 |         50.0 |         50.0 |            0.0 |          44.9 |
| ('easyocr', 'baseline', 'crumpled')      |     12.0 |    80.3 |    98.8 |           3.3 |         0.0 |         25.0 |         25.0 |            0.0 |          44.9 |
| ('easyocr', 'baseline', 'clean')         |      2.0 |    53.1 |    83.1 |          30.0 |         0.0 |         50.0 |        100.0 |            0.0 |          57.0 |
| ('easyocr', 'baseline', 'handheld')      |      6.0 |    73.2 |    92.6 |           6.7 |         0.0 |         50.0 |         50.0 |            0.0 |          39.7 |
| ('easyocr', 'baseline', 'synthetic')     |     14.0 |    84.2 |    99.7 |          10.7 |         0.0 |         57.1 |         57.1 |            0.0 |          36.8 |
| ('easyocr', 'baseline', 'shadow')        |      7.0 |    76.2 |   101.6 |          11.4 |         0.0 |         57.1 |         57.1 |            0.0 |          39.9 |
| ('easyocr', 'baseline', 'tilted')        |      7.0 |    76.2 |   101.6 |          11.4 |         0.0 |         57.1 |         57.1 |            0.0 |          39.9 |
| ('easyocr', 'baseline', 'faded')         |      7.0 |    92.1 |    97.7 |          10.0 |         0.0 |         57.1 |         57.1 |            0.0 |          33.7 |
| ('easyocr', 'baseline', 'perspective')   |      7.0 |    92.1 |    97.7 |          10.0 |         0.0 |         57.1 |         57.1 |            0.0 |          33.7 |
| ('easyocr', 'pre', 'sideways')           |     12.0 |    44.0 |    81.0 |          19.2 |         0.0 |         50.0 |         50.0 |            8.3 |          17.7 |
| ('easyocr', 'pre', 'crumpled')           |     12.0 |    46.8 |    81.3 |          17.5 |         0.0 |         25.0 |         25.0 |            8.3 |          17.9 |
| ('easyocr', 'pre', 'clean')              |      2.0 |    51.5 |    81.3 |          30.0 |         0.0 |         50.0 |        100.0 |            0.0 |          17.4 |
| ('easyocr', 'pre', 'handheld')           |      6.0 |    55.8 |    87.2 |          10.0 |         0.0 |         50.0 |         50.0 |            0.0 |          16.2 |
| ('easyocr', 'pre', 'synthetic')          |     14.0 |    66.0 |    91.6 |          13.6 |         0.0 |         57.1 |         57.1 |            0.0 |          17.9 |
| ('easyocr', 'pre', 'shadow')             |      7.0 |    57.2 |    86.8 |          18.6 |         0.0 |         57.1 |         57.1 |            0.0 |          20.4 |
| ('easyocr', 'pre', 'tilted')             |      7.0 |    57.2 |    86.8 |          18.6 |         0.0 |         57.1 |         57.1 |            0.0 |          20.4 |
| ('easyocr', 'pre', 'faded')              |      7.0 |    74.9 |    96.4 |           8.6 |         0.0 |         57.1 |         57.1 |            0.0 |          15.4 |
| ('easyocr', 'pre', 'perspective')        |      7.0 |    74.9 |    96.4 |           8.6 |         0.0 |         57.1 |         57.1 |            0.0 |          15.4 |
| ('easyocr', 'pre_post', 'sideways')      |     12.0 |    44.0 |    81.0 |          40.8 |         0.0 |         50.0 |         50.0 |            0.0 |          18.0 |
| ('easyocr', 'pre_post', 'crumpled')      |     12.0 |    46.8 |    81.3 |          29.2 |         0.0 |         25.0 |         25.0 |            0.0 |          18.2 |
| ('easyocr', 'pre_post', 'clean')         |      2.0 |    51.5 |    81.3 |          70.0 |         0.0 |         50.0 |        100.0 |            0.0 |          17.4 |
| ('easyocr', 'pre_post', 'handheld')      |      6.0 |    55.8 |    87.2 |          30.0 |         0.0 |         50.0 |         50.0 |            0.0 |          16.2 |
| ('easyocr', 'pre_post', 'synthetic')     |     14.0 |    66.1 |    91.6 |          36.4 |         0.0 |         57.1 |         57.1 |            0.0 |          18.1 |
| ('easyocr', 'pre_post', 'shadow')        |      7.0 |    57.2 |    86.7 |          41.4 |         0.0 |         57.1 |         57.1 |            0.0 |          20.7 |
| ('easyocr', 'pre_post', 'tilted')        |      7.0 |    57.2 |    86.7 |          41.4 |         0.0 |         57.1 |         57.1 |            0.0 |          20.7 |
| ('easyocr', 'pre_post', 'faded')         |      7.0 |    74.9 |    96.4 |          31.4 |         0.0 |         57.1 |         57.1 |            0.0 |          15.5 |
| ('easyocr', 'pre_post', 'perspective')   |      7.0 |    74.9 |    96.4 |          31.4 |         0.0 |         57.1 |         57.1 |            0.0 |          15.5 |


## By language

|                                      |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:-------------------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('tesseract', 'baseline', 'uz_latn') |     15.0 |    97.9 |    98.9 |           0.0 |         0.0 |         40.0 |         40.0 |            0.0 |           4.7 |
| ('tesseract', 'baseline', 'mixed')   |      6.0 |    83.7 |    91.0 |          33.3 |         0.0 |         83.3 |        100.0 |            0.0 |           1.8 |
| ('tesseract', 'pre', 'uz_latn')      |     15.0 |    48.2 |    82.3 |          11.3 |         0.0 |         40.0 |         40.0 |            0.0 |           6.7 |
| ('tesseract', 'pre', 'mixed')        |      6.0 |    56.9 |    87.4 |          33.3 |         0.0 |         83.3 |        100.0 |            0.0 |           4.5 |
| ('tesseract', 'pre_post', 'uz_latn') |     15.0 |    48.2 |    82.3 |          34.7 |         8.0 |         40.0 |         40.0 |            0.0 |           6.9 |
| ('tesseract', 'pre_post', 'mixed')   |      6.0 |    56.9 |    87.4 |          70.0 |         0.0 |         83.3 |        100.0 |            0.0 |           4.5 |
| ('easyocr', 'baseline', 'uz_latn')   |     15.0 |    82.3 |    98.9 |           2.7 |         0.0 |         40.0 |         40.0 |            0.0 |          43.9 |
| ('easyocr', 'baseline', 'mixed')     |      6.0 |    71.6 |    92.5 |          30.0 |         0.0 |         83.3 |        100.0 |            0.0 |          40.9 |
| ('easyocr', 'pre', 'uz_latn')        |     15.0 |    47.5 |    82.4 |          16.7 |         0.0 |         40.0 |         40.0 |            6.7 |          17.4 |
| ('easyocr', 'pre', 'mixed')          |      6.0 |    70.1 |    89.2 |          30.0 |         0.0 |         83.3 |        100.0 |            0.0 |          17.0 |
| ('easyocr', 'pre_post', 'uz_latn')   |     15.0 |    47.5 |    82.4 |          34.0 |         0.0 |         40.0 |         40.0 |            0.0 |          17.7 |
| ('easyocr', 'pre_post', 'mixed')     |      6.0 |    70.1 |    89.0 |          70.0 |         0.0 |         83.3 |        100.0 |            0.0 |          17.1 |


## Error causes (pre_post)

|                                                 |   count |
|:------------------------------------------------|--------:|
| ('easyocr', 'date/time misread')                |       2 |
| ('easyocr', 'digits misread')                   |       5 |
| ('easyocr', 'digits/amounts misread')           |       6 |
| ('easyocr', 'not found')                        |      69 |
| ('easyocr', 'text misread / wrong span')        |      32 |
| ('easyocr', 'wrong line picked (value of vat)') |       3 |
| ('tesseract', 'date/time misread')              |       3 |
| ('tesseract', 'digits misread')                 |       2 |
| ('tesseract', 'digits missing/extra')           |       2 |
| ('tesseract', 'digits/amounts misread')         |      14 |
| ('tesseract', 'not found')                      |      65 |
| ('tesseract', 'spurious value')                 |       1 |
| ('tesseract', 'text misread / wrong span')      |      29 |


## Error examples

| image        | config   | engine    | conditions                                    | field          | gt                                                                             | pred                                                                                                                             | cause                     |
|:-------------|:---------|:----------|:----------------------------------------------|:---------------|:-------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------|:--------------------------|
| r02_a.jpg    | pre_post | tesseract | sideways;crumpled                             | seller_name    | ERA                                                                            | ANVARDON м. 7 OILMUROO OʻG /                                                                                                     | text misread / wrong span |
| r02_a.jpg    | pre_post | tesseract | sideways;crumpled                             | seller_tin     | 31802964140017                                                                 |                                                                                                                                  | not found                 |
| r02_a.jpg    | pre_post | tesseract | sideways;crumpled                             | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | Fargʻona viloyati, Fargʻona shahri;, Barkamol MFY, Yangi asr, koʻchagi./118 b uy, Yur, Manzil Fargʻona viloyati, Fargʻona shahri | text misread / wrong span |
| r03_a.jpg    | pre_post | tesseract | sideways;crumpled                             | seller_name    | ERA                                                                            | м ANVARION MAXMUDOV DILMUROD OʻGʻRI                                                                                              | text misread / wrong span |
| r03_a.jpg    | pre_post | tesseract | sideways;crumpled                             | seller_tin     | 31802964140017                                                                 |                                                                                                                                  | not found                 |
| r03_a.jpg    | pre_post | tesseract | sideways;crumpled                             | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | anzil Fargʻona viloyati, Его ʼопа shahri, Barkamol MFY, Yangi asr, ʻ М, A ko! jasi. 118 b uy                                     | text misread / wrong span |
| r03_a.jpg    | pre_post | tesseract | sideways;crumpled                             | datetime       | 2026-11-08T11:02:29                                                            | 2026-11-08T11:02:23                                                                                                              | date/time misread         |
| r03_a.jpg    | pre_post | tesseract | sideways;crumpled                             | receipt_number | 12077                                                                          | 12877                                                                                                                            | digits misread            |
| r03_a.jpg    | pre_post | tesseract | sideways;crumpled                             | fiscal_module  | LG420211609580                                                                 |                                                                                                                                  | not found                 |
| r03_a.jpg    | pre_post | tesseract | sideways;crumpled                             | fiscal_sign    | 514092944266                                                                   | 5149929442665                                                                                                                    | digits missing/extra      |
| r03_a.jpg    | pre_post | tesseract | sideways;crumpled                             | vat            | 0.0                                                                            | 69.0                                                                                                                             | digits/amounts misread    |
| r03_a.jpg    | pre_post | tesseract | sideways;crumpled                             | payment        | card                                                                           |                                                                                                                                  | not found                 |
| r04_a.jpg    | pre_post | tesseract | clean                                         | vat            | 957.14                                                                         | 911.43                                                                                                                           | digits/amounts misread    |
| r04_a.jpg    | pre_post | tesseract | clean                                         | total          | 8933.33                                                                        |                                                                                                                                  | not found                 |
| r09_a.jpg    | pre_post | tesseract | clean                                         | seller_name    | 9-Этажка                                                                       | 9-YATAKKA                                                                                                                        | text misread / wrong span |
| r09_a.jpg    | pre_post | tesseract | clean                                         | vat            | 471.43                                                                         | 3396.0                                                                                                                           | digits/amounts misread    |
| r09_a.jpg    | pre_post | tesseract | clean                                         | total          | 4400.0                                                                         | 3700.0                                                                                                                           | digits/amounts misread    |
| r11_a.jpg    | pre_post | tesseract | sideways;crumpled                             | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | Fargʻona viloyati, Fargʻona shahri, Barkamol MFY, Yarigl asr                                                                     | text misread / wrong span |
| r11_a.jpg    | pre_post | tesseract | sideways;crumpled                             | datetime       | 2026-11-03T17:12:38                                                            |                                                                                                                                  | not found                 |
| r11_a.jpg    | pre_post | tesseract | sideways;crumpled                             | fiscal_module  | LG420211609580                                                                 |                                                                                                                                  | not found                 |
| r11_a.jpg    | pre_post | tesseract | sideways;crumpled                             | vat            | 0.0                                                                            | 20600.69                                                                                                                         | digits/amounts misread    |
| r13_a.jpg    | pre_post | tesseract | handheld;crumpled                             | seller_name    | ERA                                                                            | ERA !                                                                                                                            | text misread / wrong span |
| r13_a.jpg    | pre_post | tesseract | handheld;crumpled                             | seller_tin     | 31802964140017                                                                 |                                                                                                                                  | not found                 |
| r13_a.jpg    | pre_post | tesseract | handheld;crumpled                             | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy |                                                                                                                                  | not found                 |
| r13_a.jpg    | pre_post | tesseract | handheld;crumpled                             | datetime       | 2026-10-31T18:34:21                                                            |                                                                                                                                  | not found                 |
| r13_a.jpg    | pre_post | tesseract | handheld;crumpled                             | receipt_number | 11814                                                                          |                                                                                                                                  | not found                 |
| r13_a.jpg    | pre_post | tesseract | handheld;crumpled                             | fiscal_module  | LG420211609580                                                                 |                                                                                                                                  | not found                 |
| r13_a.jpg    | pre_post | tesseract | handheld;crumpled                             | vat            | 0.0                                                                            |                                                                                                                                  | not found                 |
| r13_a.jpg    | pre_post | tesseract | handheld;crumpled                             | total          | 19800.0                                                                        |                                                                                                                                  | not found                 |
| r15_a.jpg    | pre_post | tesseract | sideways;handheld                             | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | Fargʻona viloyati, Fargʻona shahri, Barkamol MFY, Yangi asr, koʻchasi, 118 b uy, Yur.Manzit Fargʻona viloyati, Fargʻona shahri   | text misread / wrong span |
| r15_a.jpg    | pre_post | tesseract | sideways;handheld                             | vat            | 0.0                                                                            | 8.02                                                                                                                             | digits/amounts misread    |
| r02_a_x1.jpg | pre_post | tesseract | synthetic;crumpled;shadow;sideways;tilted     | seller_name    | ERA                                                                            | ANVARJON MAXHUDOV OʻTLHUROD OʻG/LI                                                                                               | text misread / wrong span |
| r02_a_x1.jpg | pre_post | tesseract | synthetic;crumpled;shadow;sideways;tilted     | seller_tin     | 31802964140017                                                                 | 11802964140017                                                                                                                   | digits misread            |
| r02_a_x1.jpg | pre_post | tesseract | synthetic;crumpled;shadow;sideways;tilted     | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | Fargʻona viloyati.                                                                                                               | text misread / wrong span |
| r02_a_x1.jpg | pre_post | tesseract | synthetic;crumpled;shadow;sideways;tilted     | vat            | 0.0                                                                            |                                                                                                                                  | not found                 |
| r02_a_x1.jpg | pre_post | tesseract | synthetic;crumpled;shadow;sideways;tilted     | total          | 29000.0                                                                        |                                                                                                                                  | not found                 |
| r02_a_x2.jpg | pre_post | tesseract | synthetic;crumpled;faded;perspective;sideways | seller_name    | ERA                                                                            | 1z RA i                                                                                                                          | text misread / wrong span |
| r02_a_x2.jpg | pre_post | tesseract | synthetic;crumpled;faded;perspective;sideways | seller_tin     | 31802964140017                                                                 |                                                                                                                                  | not found                 |
| r02_a_x2.jpg | pre_post | tesseract | synthetic;crumpled;faded;perspective;sideways | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | аа fargʻona viloyati.                                                                                                            | text misread / wrong span |
| r02_a_x2.jpg | pre_post | tesseract | synthetic;crumpled;faded;perspective;sideways | vat            | 0.0                                                                            |                                                                                                                                  | not found                 |