# Results (holdout split, 12 images, 6 receipts, 6 sellers)

## Engines × configurations

|                           |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:--------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('tesseract', 'baseline') |     12.0 |     nan |     nan |          21.7 |         0.0 |         50.0 |         66.7 |            0.0 |          10.6 |
| ('tesseract', 'pre')      |     12.0 |     nan |     nan |          25.0 |        33.3 |         50.0 |         66.7 |            0.0 |           8.6 |
| ('tesseract', 'pre_post') |     12.0 |     nan |     nan |          40.0 |        33.3 |         50.0 |         66.7 |            0.0 |           8.7 |
| ('rapidocr', 'baseline')  |     12.0 |     nan |     nan |          65.0 |        50.0 |         50.0 |         66.7 |           50.0 |           8.1 |
| ('rapidocr', 'pre')       |     12.0 |     nan |     nan |          53.3 |        53.3 |         50.0 |         66.7 |           33.3 |           8.3 |
| ('rapidocr', 'pre_post')  |     12.0 |     nan |     nan |          63.3 |        53.3 |         50.0 |         66.7 |           33.3 |           8.2 |


## Field accuracy, %

|                           |   seller_name |   seller_tin |   address |   datetime |   receipt_number |   fiscal_module |   fiscal_sign |   vat |   total |   payment |
|:--------------------------|--------------:|-------------:|----------:|-----------:|-----------------:|----------------:|--------------:|------:|--------:|----------:|
| ('tesseract', 'baseline') |           0.0 |         33.3 |      50.0 |       33.3 |             16.7 |             0.0 |           0.0 |  33.3 |    16.7 |      33.3 |
| ('tesseract', 'pre')      |           0.0 |         16.7 |      50.0 |       16.7 |             33.3 |            16.7 |           0.0 |  33.3 |    33.3 |      50.0 |
| ('tesseract', 'pre_post') |           0.0 |         16.7 |      50.0 |       50.0 |             83.3 |            50.0 |          50.0 |  33.3 |    16.7 |      50.0 |
| ('rapidocr', 'baseline')  |          16.7 |         83.3 |      50.0 |       50.0 |             50.0 |           100.0 |          83.3 |  66.7 |    66.7 |      83.3 |
| ('rapidocr', 'pre')       |          16.7 |         83.3 |      50.0 |       50.0 |             33.3 |           100.0 |          50.0 |  50.0 |    50.0 |      50.0 |
| ('rapidocr', 'pre_post')  |          50.0 |         83.3 |      50.0 |       50.0 |             83.3 |           100.0 |          83.3 |  50.0 |    33.3 |      50.0 |


## By shooting condition

|                                      |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:-------------------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('tesseract', 'baseline', 'clean')   |      6.0 |     nan |     nan |          21.7 |         0.0 |         50.0 |         50.0 |            0.0 |          14.4 |
| ('tesseract', 'baseline', 'partial') |      6.0 |     nan |     nan |         nan   |       nan   |         50.0 |         83.3 |          nan   |           6.8 |
| ('tesseract', 'pre', 'clean')        |      6.0 |     nan |     nan |          25.0 |        33.3 |         50.0 |         50.0 |            0.0 |          11.1 |
| ('tesseract', 'pre', 'partial')      |      6.0 |     nan |     nan |         nan   |       nan   |         50.0 |         83.3 |          nan   |           6.0 |
| ('tesseract', 'pre_post', 'clean')   |      6.0 |     nan |     nan |          40.0 |        33.3 |         50.0 |         50.0 |            0.0 |          11.4 |
| ('tesseract', 'pre_post', 'partial') |      6.0 |     nan |     nan |         nan   |       nan   |         50.0 |         83.3 |          nan   |           6.1 |
| ('rapidocr', 'baseline', 'clean')    |      6.0 |     nan |     nan |          65.0 |        50.0 |         50.0 |         50.0 |           50.0 |          10.1 |
| ('rapidocr', 'baseline', 'partial')  |      6.0 |     nan |     nan |         nan   |       nan   |         50.0 |         83.3 |          nan   |           6.2 |
| ('rapidocr', 'pre', 'clean')         |      6.0 |     nan |     nan |          53.3 |        53.3 |         50.0 |         50.0 |           33.3 |          10.3 |
| ('rapidocr', 'pre', 'partial')       |      6.0 |     nan |     nan |         nan   |       nan   |         50.0 |         83.3 |          nan   |           6.3 |
| ('rapidocr', 'pre_post', 'clean')    |      6.0 |     nan |     nan |          63.3 |        53.3 |         50.0 |         50.0 |           33.3 |          10.0 |
| ('rapidocr', 'pre_post', 'partial')  |      6.0 |     nan |     nan |         nan   |       nan   |         50.0 |         83.3 |          nan   |           6.4 |


## By language

|                                      |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:-------------------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('tesseract', 'baseline', 'uz_latn') |      6.0 |     nan |     nan |          30.0 |         0.0 |         50.0 |         50.0 |            0.0 |          17.4 |
| ('tesseract', 'baseline', 'mixed')   |      6.0 |     nan |     nan |          13.3 |         0.0 |         50.0 |         83.3 |            0.0 |           3.8 |
| ('tesseract', 'pre', 'uz_latn')      |      6.0 |     nan |     nan |          30.0 |         0.0 |         50.0 |         50.0 |            0.0 |          14.8 |
| ('tesseract', 'pre', 'mixed')        |      6.0 |     nan |     nan |          20.0 |        57.1 |         50.0 |         83.3 |            0.0 |           2.3 |
| ('tesseract', 'pre_post', 'uz_latn') |      6.0 |     nan |     nan |          40.0 |         0.0 |         50.0 |         50.0 |            0.0 |          15.1 |
| ('tesseract', 'pre_post', 'mixed')   |      6.0 |     nan |     nan |          40.0 |        57.1 |         50.0 |         83.3 |            0.0 |           2.4 |
| ('rapidocr', 'baseline', 'uz_latn')  |      6.0 |     nan |     nan |          70.0 |        25.0 |         50.0 |         50.0 |           33.3 |          14.2 |
| ('rapidocr', 'baseline', 'mixed')    |      6.0 |     nan |     nan |          60.0 |        75.0 |         50.0 |         83.3 |           66.7 |           2.1 |
| ('rapidocr', 'pre', 'uz_latn')       |      6.0 |     nan |     nan |          66.7 |        25.0 |         50.0 |         50.0 |           33.3 |          14.5 |
| ('rapidocr', 'pre', 'mixed')         |      6.0 |     nan |     nan |          40.0 |        85.7 |         50.0 |         83.3 |           33.3 |           2.1 |
| ('rapidocr', 'pre_post', 'uz_latn')  |      6.0 |     nan |     nan |          66.7 |        25.0 |         50.0 |         50.0 |           33.3 |          14.3 |
| ('rapidocr', 'pre_post', 'mixed')    |      6.0 |     nan |     nan |          60.0 |        85.7 |         50.0 |         83.3 |           33.3 |           2.1 |


## QR decoded per photo and per receipt

|                           |   whole photo % |   QR close-up % |   per receipt (any real photo) % |
|:--------------------------|----------------:|----------------:|---------------------------------:|
| ('tesseract', 'baseline') |            50.0 |            83.3 |                             83.3 |
| ('tesseract', 'pre')      |            50.0 |            83.3 |                             83.3 |
| ('tesseract', 'pre_post') |            50.0 |            83.3 |                             83.3 |
| ('rapidocr', 'baseline')  |            50.0 |            83.3 |                             83.3 |
| ('rapidocr', 'pre')       |            50.0 |            83.3 |                             83.3 |
| ('rapidocr', 'pre_post')  |            50.0 |            83.3 |                             83.3 |


## 95 % confidence intervals (bootstrap over receipts, real whole-receipt photos, pre + post)

| engine    |   receipts | field acc %      | item F1 %       | consistent %    |
|:----------|-----------:|:-----------------|:----------------|:----------------|
| tesseract |          6 | 40.0 [25.0–53.3] | 33.3 [0.0–60.0] | 0.0 [0.0–0.0]   |
| rapidocr  |          6 | 63.3 [48.3–78.3] | 53.3 [0.0–94.7] | 33.3 [0.0–66.7] |


## Per seller (real whole-receipt photos, pre + post)

|                                        |   photos |   field acc % |   item F1 % |   consistent % |
|:---------------------------------------|---------:|--------------:|------------:|---------------:|
| ('tesseract', 'dxb_benefit')           |      1.0 |          50.0 |         0.0 |            0.0 |
| ('tesseract', 'bon_chimgan')           |      1.0 |          10.0 |        66.7 |            0.0 |
| ('tesseract', 'supermarket_305645847') |      1.0 |          20.0 |         0.0 |            0.0 |
| ('tesseract', 'kfc_chimgan')           |      1.0 |          60.0 |         0.0 |            0.0 |
| ('tesseract', 'pharm_t13')             |      1.0 |          50.0 |       100.0 |            0.0 |
| ('tesseract', 'era_aro_bread')         |      1.0 |          50.0 |         0.0 |            0.0 |
| ('rapidocr', 'dxb_benefit')            |      1.0 |          70.0 |         0.0 |            0.0 |
| ('rapidocr', 'bon_chimgan')            |      1.0 |          80.0 |       100.0 |          100.0 |
| ('rapidocr', 'supermarket_305645847')  |      1.0 |          40.0 |         0.0 |            0.0 |
| ('rapidocr', 'kfc_chimgan')            |      1.0 |          60.0 |         0.0 |            0.0 |
| ('rapidocr', 'pharm_t13')              |      1.0 |          40.0 |       100.0 |            0.0 |
| ('rapidocr', 'era_aro_bread')          |      1.0 |          90.0 |       100.0 |          100.0 |


## Error causes (pre_post)

|                                            |   count |
|:-------------------------------------------|--------:|
| ('rapidocr', 'date/time misread')          |       2 |
| ('rapidocr', 'digits missing/extra')       |       1 |
| ('rapidocr', 'digits/amounts misread')     |       1 |
| ('rapidocr', 'not found')                  |      13 |
| ('rapidocr', 'spurious value')             |       3 |
| ('rapidocr', 'text misread / wrong span')  |       2 |
| ('tesseract', 'date/time misread')         |       1 |
| ('tesseract', 'digits misread')            |       1 |
| ('tesseract', 'digits/amounts misread')    |       2 |
| ('tesseract', 'not found')                 |      25 |
| ('tesseract', 'spurious value')            |       2 |
| ('tesseract', 'text misread / wrong span') |       5 |


## Error examples

| image     | config   | engine    | conditions   | field          | gt                                                        | pred                                                                                                                       | cause                     |
|:----------|:---------|:----------|:-------------|:---------------|:----------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------|:--------------------------|
| h01_a.jpg | pre_post | tesseract | clean        | seller_name    | "DXB BENIFIT GROUP" MCHJ                                  | "DXB ВЕМТЕТТ GROUP" MCHJ a |                                                                                               | text misread / wrong span |
| h01_a.jpg | pre_post | tesseract | clean        | seller_tin     | 310219511                                                 |                                                                                                                            | not found                 |
| h01_a.jpg | pre_post | tesseract | clean        | address        | Toshkent sh. Yunusobod                                    |                                                                                                                            | not found                 |
| h01_a.jpg | pre_post | tesseract | clean        | datetime       | 2026-11-17T21:00:47                                       | 2026-11-17T21:00:43                                                                                                        | date/time misread         |
| h01_a.jpg | pre_post | tesseract | clean        | total          | 19000.0                                                   | 4000.0                                                                                                                     | digits/amounts misread    |
| h02_a.jpg | pre_post | tesseract | clean        | seller_name    | Bon! Atlas Chimgan                                        | Ei || “Жи куки                                                                                                             | text misread / wrong span |
| h02_a.jpg | pre_post | tesseract | clean        | seller_tin     | 200992329                                                 |                                                                                                                            | not found                 |
| h02_a.jpg | pre_post | tesseract | clean        | address        | Toshkent sh., M. Ulugbek tumani koch. T. Malik, 3A-uy     |                                                                                                                            | not found                 |
| h02_a.jpg | pre_post | tesseract | clean        | datetime       | 2026-11-16T16:19:46                                       |                                                                                                                            | not found                 |
| h02_a.jpg | pre_post | tesseract | clean        | receipt_number | 96890                                                     |                                                                                                                            | not found                 |
| h02_a.jpg | pre_post | tesseract | clean        | fiscal_module  | LG420230632412                                            |                                                                                                                            | not found                 |
| h02_a.jpg | pre_post | tesseract | clean        | fiscal_sign    | 441117549441                                              | 441117549447                                                                                                               | digits misread            |
| h02_a.jpg | pre_post | tesseract | clean        | vat            | 6321.43                                                   |                                                                                                                            | not found                 |
| h02_a.jpg | pre_post | tesseract | clean        | total          | 59000.0                                                   |                                                                                                                            | not found                 |
| h03_a.jpg | pre_post | tesseract | clean        | seller_name    |                                                           | ESS i                                                                                                                      | spurious value            |
| h03_a.jpg | pre_post | tesseract | clean        | seller_tin     | 305645847                                                 |                                                                                                                            | not found                 |
| h03_a.jpg | pre_post | tesseract | clean        | datetime       | 2026-11-16T22:19:09                                       |                                                                                                                            | not found                 |
| h03_a.jpg | pre_post | tesseract | clean        | fiscal_module  | LG420211614982                                            |                                                                                                                            | not found                 |
| h03_a.jpg | pre_post | tesseract | clean        | fiscal_sign    | 010301300230                                              |                                                                                                                            | not found                 |
| h03_a.jpg | pre_post | tesseract | clean        | vat            | 862.28                                                    |                                                                                                                            | not found                 |
| h03_a.jpg | pre_post | tesseract | clean        | total          | 8048.0                                                    | 0.0                                                                                                                        | digits/amounts misread    |
| h03_a.jpg | pre_post | tesseract | clean        | payment        | card                                                      |                                                                                                                            | not found                 |
| h04_a.jpg | pre_post | tesseract | clean        | seller_name    | KFC Чимган                                                | Qeratok: 0.00 mica!                                                                                                        | text misread / wrong span |
| h04_a.jpg | pre_post | tesseract | clean        | vat            | 4714.29                                                   |                                                                                                                            | not found                 |
| h04_a.jpg | pre_post | tesseract | clean        | total          | 44000.0                                                   |                                                                                                                            | not found                 |
| h04_a.jpg | pre_post | tesseract | clean        | payment        | card                                                      |                                                                                                                            | not found                 |
| h05_a.jpg | pre_post | tesseract | clean        | seller_name    |                                                           | "ое                                                                                                                        | spurious value            |
| h05_a.jpg | pre_post | tesseract | clean        | seller_tin     | 309263742                                                 |                                                                                                                            | not found                 |
| h05_a.jpg | pre_post | tesseract | clean        | vat            | 1564.29                                                   |                                                                                                                            | not found                 |
| h05_a.jpg | pre_post | tesseract | clean        | total          | 14600.0                                                   |                                                                                                                            | not found                 |
| h05_a.jpg | pre_post | tesseract | clean        | payment        | card                                                      |                                                                                                                            | not found                 |
| h06_a.jpg | pre_post | tesseract | clean        | seller_name    | ERA                                                       | "ARD BREAD" XK                                                                                                             | text misread / wrong span |
| h06_a.jpg | pre_post | tesseract | clean        | seller_tin     | 306263261                                                 |                                                                                                                            | not found                 |
| h06_a.jpg | pre_post | tesseract | clean        | address        | Toshkent sh., M.Ulug'bek tum., Yalang'och bozori hududida | = < tum., Yalangʻoch bozori, SE Sire apy, emcee hududida, —= Yur.Manzil Toshkent sh. , M.Ulugʻbek, tum., Yalangʻoch bozori | text misread / wrong span |
| h06_a.jpg | pre_post | tesseract | clean        | fiscal_module  | VG544170024923                                            |                                                                                                                            | not found                 |
| h06_a.jpg | pre_post | tesseract | clean        | fiscal_sign    | 006628644216                                              |                                                                                                                            | not found                 |
| h01_a.jpg | pre_post | rapidocr  | clean        | address        | Toshkent sh. Yunusobod                                    |                                                                                                                            | not found                 |
| h01_a.jpg | pre_post | rapidocr  | clean        | datetime       | 2026-11-17T21:00:47                                       | 2026-11-17T21:00:43                                                                                                        | date/time misread         |
| h01_a.jpg | pre_post | rapidocr  | clean        | total          | 19000.0                                                   | 15000.0                                                                                                                    | digits/amounts misread    |
| h02_a.jpg | pre_post | rapidocr  | clean        | datetime       | 2026-11-16T16:19:46                                       |                                                                                                                            | not found                 |