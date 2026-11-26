# Results (holdout2 split, 14 images, 7 receipts, 5 sellers)

## Engines × configurations

|                           |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:--------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('tesseract', 'baseline') |     14.0 |     nan |     nan |           4.3 |         0.0 |         42.9 |         42.9 |            0.0 |          27.7 |
| ('tesseract', 'pre')      |     14.0 |     nan |     nan |          15.7 |         0.0 |         42.9 |         42.9 |            0.0 |          28.0 |
| ('tesseract', 'pre_post') |     14.0 |     nan |     nan |          28.6 |         0.0 |         42.9 |         42.9 |            0.0 |          20.8 |
| ('easyocr', 'baseline')   |     14.0 |     nan |     nan |           5.7 |         0.0 |         42.9 |         42.9 |            0.0 |          40.1 |
| ('easyocr', 'pre')        |     14.0 |     nan |     nan |          37.1 |         0.0 |         42.9 |         42.9 |            0.0 |          37.3 |
| ('easyocr', 'pre_post')   |     14.0 |     nan |     nan |          48.6 |         0.0 |         42.9 |         42.9 |            0.0 |          36.5 |
| ('rapidocr', 'baseline')  |     14.0 |     nan |     nan |          42.9 |         0.0 |         42.9 |         42.9 |            0.0 |          10.4 |
| ('rapidocr', 'pre')       |     14.0 |     nan |     nan |          67.1 |        14.8 |         42.9 |         42.9 |           28.6 |          26.0 |
| ('rapidocr', 'pre_post')  |     14.0 |     nan |     nan |          71.4 |        14.8 |         42.9 |         42.9 |           28.6 |          12.1 |
| ('hybrid', 'baseline')    |     14.0 |     nan |     nan |          42.9 |         0.0 |         42.9 |         42.9 |            0.0 |          17.7 |
| ('hybrid', 'pre')         |     14.0 |     nan |     nan |          65.7 |        14.8 |         42.9 |         42.9 |           28.6 |          20.7 |
| ('hybrid', 'pre_post')    |     14.0 |     nan |     nan |          68.6 |        14.8 |         42.9 |         42.9 |           28.6 |          25.7 |


## Field accuracy, %

|                           |   seller_name |   seller_tin |   address |   datetime |   receipt_number |   fiscal_module |   fiscal_sign |   vat |   total |   payment |
|:--------------------------|--------------:|-------------:|----------:|-----------:|-----------------:|----------------:|--------------:|------:|--------:|----------:|
| ('tesseract', 'baseline') |           0.0 |         14.3 |      28.6 |        0.0 |              0.0 |             0.0 |           0.0 |   0.0 |     0.0 |       0.0 |
| ('tesseract', 'pre')      |           0.0 |         28.6 |      28.6 |        0.0 |             14.3 |            28.6 |          14.3 |   0.0 |    14.3 |      28.6 |
| ('tesseract', 'pre_post') |           0.0 |         28.6 |      28.6 |       28.6 |             28.6 |            42.9 |          42.9 |   0.0 |    42.9 |      42.9 |
| ('easyocr', 'baseline')   |          14.3 |         14.3 |      28.6 |        0.0 |              0.0 |             0.0 |           0.0 |   0.0 |     0.0 |       0.0 |
| ('easyocr', 'pre')        |          14.3 |         71.4 |      28.6 |        0.0 |             71.4 |            57.1 |          57.1 |  14.3 |     0.0 |      57.1 |
| ('easyocr', 'pre_post')   |          28.6 |         71.4 |      28.6 |       28.6 |             57.1 |            71.4 |          85.7 |  14.3 |    42.9 |      57.1 |
| ('rapidocr', 'baseline')  |           0.0 |         42.9 |      28.6 |       42.9 |             42.9 |           100.0 |          57.1 |  14.3 |     0.0 |     100.0 |
| ('rapidocr', 'pre')       |          14.3 |        100.0 |      28.6 |       57.1 |             71.4 |            85.7 |          85.7 |  57.1 |    71.4 |     100.0 |
| ('rapidocr', 'pre_post')  |          42.9 |        100.0 |      28.6 |       71.4 |             71.4 |            85.7 |          85.7 |  57.1 |    71.4 |     100.0 |
| ('hybrid', 'baseline')    |           0.0 |         42.9 |      28.6 |       42.9 |             42.9 |           100.0 |          57.1 |  14.3 |     0.0 |     100.0 |
| ('hybrid', 'pre')         |           0.0 |        100.0 |      28.6 |       57.1 |             71.4 |            85.7 |          85.7 |  57.1 |    71.4 |     100.0 |
| ('hybrid', 'pre_post')    |          14.3 |        100.0 |      28.6 |       71.4 |             71.4 |            85.7 |          85.7 |  57.1 |    71.4 |     100.0 |


## By shooting condition

|                                          |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:-----------------------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('tesseract', 'baseline', 'long')        |      5.0 |     nan |     nan |           2.0 |         0.0 |         40.0 |         40.0 |            0.0 |          24.0 |
| ('tesseract', 'baseline', 'upside_down') |      8.0 |     nan |     nan |           0.0 |         0.0 |         37.5 |         37.5 |            0.0 |          24.8 |
| ('tesseract', 'baseline', 'partial')     |      7.0 |     nan |     nan |         nan   |       nan   |         42.9 |         42.9 |          nan   |          29.5 |
| ('tesseract', 'baseline', 'crumpled')    |      7.0 |     nan |     nan |           4.0 |         0.0 |         28.6 |         28.6 |            0.0 |          25.4 |
| ('tesseract', 'baseline', 'sideways')    |      5.0 |     nan |     nan |          10.0 |         0.0 |         40.0 |         40.0 |            0.0 |          38.0 |
| ('tesseract', 'baseline', 'shadow')      |      7.0 |     nan |     nan |           7.5 |         0.0 |         71.4 |         71.4 |            0.0 |          27.1 |
| ('tesseract', 'pre', 'long')             |      5.0 |     nan |     nan |          18.0 |         0.0 |         40.0 |         40.0 |            0.0 |          20.7 |
| ('tesseract', 'pre', 'upside_down')      |      8.0 |     nan |     nan |          10.0 |         0.0 |         37.5 |         37.5 |            0.0 |          17.2 |
| ('tesseract', 'pre', 'partial')          |      7.0 |     nan |     nan |         nan   |       nan   |         42.9 |         42.9 |          nan   |          31.7 |
| ('tesseract', 'pre', 'crumpled')         |      7.0 |     nan |     nan |           6.0 |         0.0 |         28.6 |         28.6 |            0.0 |          26.2 |
| ('tesseract', 'pre', 'sideways')         |      5.0 |     nan |     nan |          23.3 |         0.0 |         40.0 |         40.0 |            0.0 |          50.7 |
| ('tesseract', 'pre', 'shadow')           |      7.0 |     nan |     nan |          17.5 |         0.0 |         71.4 |         71.4 |            0.0 |          32.2 |
| ('tesseract', 'pre_post', 'long')        |      5.0 |     nan |     nan |          28.0 |         0.0 |         40.0 |         40.0 |            0.0 |          21.6 |
| ('tesseract', 'pre_post', 'upside_down') |      8.0 |     nan |     nan |          27.5 |         0.0 |         37.5 |         37.5 |            0.0 |          23.2 |
| ('tesseract', 'pre_post', 'partial')     |      7.0 |     nan |     nan |         nan   |       nan   |         42.9 |         42.9 |          nan   |          20.4 |
| ('tesseract', 'pre_post', 'crumpled')    |      7.0 |     nan |     nan |          18.0 |         0.0 |         28.6 |         28.6 |            0.0 |          19.7 |
| ('tesseract', 'pre_post', 'sideways')    |      5.0 |     nan |     nan |          30.0 |         0.0 |         40.0 |         40.0 |            0.0 |          21.2 |
| ('tesseract', 'pre_post', 'shadow')      |      7.0 |     nan |     nan |          32.5 |         0.0 |         71.4 |         71.4 |            0.0 |          14.4 |
| ('easyocr', 'baseline', 'long')          |      5.0 |     nan |     nan |           2.0 |         0.0 |         40.0 |         40.0 |            0.0 |          70.6 |
| ('easyocr', 'baseline', 'upside_down')   |      8.0 |     nan |     nan |           0.0 |         0.0 |         37.5 |         37.5 |            0.0 |          39.8 |
| ('easyocr', 'baseline', 'partial')       |      7.0 |     nan |     nan |         nan   |       nan   |         42.9 |         42.9 |          nan   |          12.8 |
| ('easyocr', 'baseline', 'crumpled')      |      7.0 |     nan |     nan |           6.0 |         0.0 |         28.6 |         28.6 |            0.0 |          45.0 |
| ('easyocr', 'baseline', 'sideways')      |      5.0 |     nan |     nan |          13.3 |         0.0 |         40.0 |         40.0 |            0.0 |          48.6 |
| ('easyocr', 'baseline', 'shadow')        |      7.0 |     nan |     nan |          10.0 |         0.0 |         71.4 |         71.4 |            0.0 |          41.2 |
| ('easyocr', 'pre', 'long')               |      5.0 |     nan |     nan |          46.0 |         0.0 |         40.0 |         40.0 |            0.0 |          63.9 |
| ('easyocr', 'pre', 'upside_down')        |      8.0 |     nan |     nan |          40.0 |         0.0 |         37.5 |         37.5 |            0.0 |          31.8 |
| ('easyocr', 'pre', 'partial')            |      7.0 |     nan |     nan |         nan   |       nan   |         42.9 |         42.9 |          nan   |          11.2 |
| ('easyocr', 'pre', 'crumpled')           |      7.0 |     nan |     nan |          34.0 |         0.0 |         28.6 |         28.6 |            0.0 |          52.6 |
| ('easyocr', 'pre', 'sideways')           |      5.0 |     nan |     nan |          33.3 |         0.0 |         40.0 |         40.0 |            0.0 |          53.6 |
| ('easyocr', 'pre', 'shadow')             |      7.0 |     nan |     nan |          25.0 |         0.0 |         71.4 |         71.4 |            0.0 |          43.2 |
| ('easyocr', 'pre_post', 'long')          |      5.0 |     nan |     nan |          54.0 |         0.0 |         40.0 |         40.0 |            0.0 |          63.1 |
| ('easyocr', 'pre_post', 'upside_down')   |      8.0 |     nan |     nan |          52.5 |         0.0 |         37.5 |         37.5 |            0.0 |          31.7 |
| ('easyocr', 'pre_post', 'partial')       |      7.0 |     nan |     nan |         nan   |       nan   |         42.9 |         42.9 |          nan   |          10.6 |
| ('easyocr', 'pre_post', 'crumpled')      |      7.0 |     nan |     nan |          44.0 |         0.0 |         28.6 |         28.6 |            0.0 |          51.1 |
| ('easyocr', 'pre_post', 'sideways')      |      5.0 |     nan |     nan |          43.3 |         0.0 |         40.0 |         40.0 |            0.0 |          51.5 |
| ('easyocr', 'pre_post', 'shadow')        |      7.0 |     nan |     nan |          42.5 |         0.0 |         71.4 |         71.4 |            0.0 |          42.2 |
| ('rapidocr', 'baseline', 'long')         |      5.0 |     nan |     nan |          36.0 |         0.0 |         40.0 |         40.0 |            0.0 |           7.9 |
| ('rapidocr', 'baseline', 'upside_down')  |      8.0 |     nan |     nan |          37.5 |         0.0 |         37.5 |         37.5 |            0.0 |           8.8 |
| ('rapidocr', 'baseline', 'partial')      |      7.0 |     nan |     nan |         nan   |       nan   |         42.9 |         42.9 |          nan   |          11.9 |
| ('rapidocr', 'baseline', 'crumpled')     |      7.0 |     nan |     nan |          48.0 |         0.0 |         28.6 |         28.6 |            0.0 |          10.3 |
| ('rapidocr', 'baseline', 'sideways')     |      5.0 |     nan |     nan |          50.0 |         0.0 |         40.0 |         40.0 |            0.0 |          14.9 |
| ('rapidocr', 'baseline', 'shadow')       |      7.0 |     nan |     nan |          52.5 |         0.0 |         71.4 |         71.4 |            0.0 |           8.2 |
| ('rapidocr', 'pre', 'long')              |      5.0 |     nan |     nan |          72.0 |        16.0 |         40.0 |         40.0 |           40.0 |          29.3 |
| ('rapidocr', 'pre', 'upside_down')       |      8.0 |     nan |     nan |          62.5 |        10.5 |         37.5 |         37.5 |           25.0 |          27.1 |
| ('rapidocr', 'pre', 'partial')           |      7.0 |     nan |     nan |         nan   |       nan   |         42.9 |         42.9 |          nan   |          18.7 |
| ('rapidocr', 'pre', 'crumpled')          |      7.0 |     nan |     nan |          66.0 |        33.3 |         28.6 |         28.6 |           40.0 |          30.4 |
| ('rapidocr', 'pre', 'sideways')          |      5.0 |     nan |     nan |          73.3 |        25.0 |         40.0 |         40.0 |           33.3 |          29.3 |
| ('rapidocr', 'pre', 'shadow')            |      7.0 |     nan |     nan |          67.5 |        22.2 |         71.4 |         71.4 |           25.0 |          19.8 |
| ('rapidocr', 'pre_post', 'long')         |      5.0 |     nan |     nan |          74.0 |        16.0 |         40.0 |         40.0 |           40.0 |          17.3 |
| ('rapidocr', 'pre_post', 'upside_down')  |      8.0 |     nan |     nan |          65.0 |        10.5 |         37.5 |         37.5 |           25.0 |          12.2 |
| ('rapidocr', 'pre_post', 'partial')      |      7.0 |     nan |     nan |         nan   |       nan   |         42.9 |         42.9 |          nan   |           8.3 |
| ('rapidocr', 'pre_post', 'crumpled')     |      7.0 |     nan |     nan |          70.0 |        33.3 |         28.6 |         28.6 |           40.0 |          13.1 |
| ('rapidocr', 'pre_post', 'sideways')     |      5.0 |     nan |     nan |          80.0 |        25.0 |         40.0 |         40.0 |           33.3 |          14.4 |
| ('rapidocr', 'pre_post', 'shadow')       |      7.0 |     nan |     nan |          75.0 |        22.2 |         71.4 |         71.4 |           25.0 |           9.2 |
| ('hybrid', 'baseline', 'long')           |      5.0 |     nan |     nan |          36.0 |         0.0 |         40.0 |         40.0 |            0.0 |          23.8 |
| ('hybrid', 'baseline', 'upside_down')    |      8.0 |     nan |     nan |          37.5 |         0.0 |         37.5 |         37.5 |            0.0 |          18.2 |
| ('hybrid', 'baseline', 'partial')        |      7.0 |     nan |     nan |         nan   |       nan   |         42.9 |         42.9 |          nan   |          10.8 |
| ('hybrid', 'baseline', 'crumpled')       |      7.0 |     nan |     nan |          48.0 |         0.0 |         28.6 |         28.6 |            0.0 |          20.6 |
| ('hybrid', 'baseline', 'sideways')       |      5.0 |     nan |     nan |          50.0 |         0.0 |         40.0 |         40.0 |            0.0 |          20.3 |
| ('hybrid', 'baseline', 'shadow')         |      7.0 |     nan |     nan |          52.5 |         0.0 |         71.4 |         71.4 |            0.0 |          16.7 |
| ('hybrid', 'pre', 'long')                |      5.0 |     nan |     nan |          70.0 |        16.0 |         40.0 |         40.0 |           40.0 |          29.7 |
| ('hybrid', 'pre', 'upside_down')         |      8.0 |     nan |     nan |          62.5 |        10.5 |         37.5 |         37.5 |           25.0 |          17.8 |
| ('hybrid', 'pre', 'partial')             |      7.0 |     nan |     nan |         nan   |       nan   |         42.9 |         42.9 |          nan   |          12.9 |
| ('hybrid', 'pre', 'crumpled')            |      7.0 |     nan |     nan |          64.0 |        33.3 |         28.6 |         28.6 |           40.0 |          23.3 |
| ('hybrid', 'pre', 'sideways')            |      5.0 |     nan |     nan |          70.0 |        25.0 |         40.0 |         40.0 |           33.3 |          29.4 |
| ('hybrid', 'pre', 'shadow')              |      7.0 |     nan |     nan |          65.0 |        22.2 |         71.4 |         71.4 |           25.0 |          20.1 |
| ('hybrid', 'pre_post', 'long')           |      5.0 |     nan |     nan |          72.0 |        16.0 |         40.0 |         40.0 |           40.0 |          30.0 |
| ('hybrid', 'pre_post', 'upside_down')    |      8.0 |     nan |     nan |          65.0 |        10.5 |         37.5 |         37.5 |           25.0 |          18.8 |
| ('hybrid', 'pre_post', 'partial')        |      7.0 |     nan |     nan |         nan   |       nan   |         42.9 |         42.9 |          nan   |          22.8 |
| ('hybrid', 'pre_post', 'crumpled')       |      7.0 |     nan |     nan |          66.0 |        33.3 |         28.6 |         28.6 |           40.0 |          27.6 |
| ('hybrid', 'pre_post', 'sideways')       |      5.0 |     nan |     nan |          73.3 |        25.0 |         40.0 |         40.0 |           33.3 |          41.9 |
| ('hybrid', 'pre_post', 'shadow')         |      7.0 |     nan |     nan |          70.0 |        22.2 |         71.4 |         71.4 |           25.0 |          25.0 |


## By language

|                                    |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:-----------------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('tesseract', 'baseline', 'mixed') |     14.0 |     nan |     nan |           4.3 |         0.0 |         42.9 |         42.9 |            0.0 |          27.7 |
| ('tesseract', 'pre', 'mixed')      |     14.0 |     nan |     nan |          15.7 |         0.0 |         42.9 |         42.9 |            0.0 |          28.0 |
| ('tesseract', 'pre_post', 'mixed') |     14.0 |     nan |     nan |          28.6 |         0.0 |         42.9 |         42.9 |            0.0 |          20.8 |
| ('easyocr', 'baseline', 'mixed')   |     14.0 |     nan |     nan |           5.7 |         0.0 |         42.9 |         42.9 |            0.0 |          40.1 |
| ('easyocr', 'pre', 'mixed')        |     14.0 |     nan |     nan |          37.1 |         0.0 |         42.9 |         42.9 |            0.0 |          37.3 |
| ('easyocr', 'pre_post', 'mixed')   |     14.0 |     nan |     nan |          48.6 |         0.0 |         42.9 |         42.9 |            0.0 |          36.5 |
| ('rapidocr', 'baseline', 'mixed')  |     14.0 |     nan |     nan |          42.9 |         0.0 |         42.9 |         42.9 |            0.0 |          10.4 |
| ('rapidocr', 'pre', 'mixed')       |     14.0 |     nan |     nan |          67.1 |        14.8 |         42.9 |         42.9 |           28.6 |          26.0 |
| ('rapidocr', 'pre_post', 'mixed')  |     14.0 |     nan |     nan |          71.4 |        14.8 |         42.9 |         42.9 |           28.6 |          12.1 |
| ('hybrid', 'baseline', 'mixed')    |     14.0 |     nan |     nan |          42.9 |         0.0 |         42.9 |         42.9 |            0.0 |          17.7 |
| ('hybrid', 'pre', 'mixed')         |     14.0 |     nan |     nan |          65.7 |        14.8 |         42.9 |         42.9 |           28.6 |          20.7 |
| ('hybrid', 'pre_post', 'mixed')    |     14.0 |     nan |     nan |          68.6 |        14.8 |         42.9 |         42.9 |           28.6 |          25.7 |


## QR decoded per photo and per receipt

|                           |   whole photo % |   QR close-up % |   per receipt (any real photo) % |
|:--------------------------|----------------:|----------------:|---------------------------------:|
| ('tesseract', 'baseline') |            42.9 |            42.9 |                             57.1 |
| ('tesseract', 'pre')      |            42.9 |            42.9 |                             57.1 |
| ('tesseract', 'pre_post') |            42.9 |            42.9 |                             57.1 |
| ('easyocr', 'baseline')   |            42.9 |            42.9 |                             57.1 |
| ('easyocr', 'pre')        |            42.9 |            42.9 |                             57.1 |
| ('easyocr', 'pre_post')   |            42.9 |            42.9 |                             57.1 |
| ('rapidocr', 'baseline')  |            42.9 |            42.9 |                             57.1 |
| ('rapidocr', 'pre')       |            42.9 |            42.9 |                             57.1 |
| ('rapidocr', 'pre_post')  |            42.9 |            42.9 |                             57.1 |
| ('hybrid', 'baseline')    |            42.9 |            42.9 |                             57.1 |
| ('hybrid', 'pre')         |            42.9 |            42.9 |                             57.1 |
| ('hybrid', 'pre_post')    |            42.9 |            42.9 |                             57.1 |


## 95 % confidence intervals (bootstrap over receipts, real whole-receipt photos, pre + post)

| engine    |   receipts | field acc %      | item F1 %       | consistent %    |
|:----------|-----------:|:-----------------|:----------------|:----------------|
| tesseract |          7 | 28.6 [14.3–42.9] | 0.0 [0.0–0.0]   | 0.0 [0.0–0.0]   |
| easyocr   |          7 | 48.6 [35.7–62.9] | 0.0 [0.0–0.0]   | 0.0 [0.0–0.0]   |
| rapidocr  |          7 | 71.4 [58.6–81.4] | 14.8 [0.0–53.3] | 28.6 [0.0–57.1] |
| hybrid    |          7 | 68.6 [57.1–78.6] | 14.8 [0.0–53.5] | 28.6 [0.0–57.1] |


## Per seller (real whole-receipt photos, pre + post)

|                                              |   photos |   field acc % |   item F1 % |   consistent % |
|:---------------------------------------------|---------:|--------------:|------------:|---------------:|
| ('tesseract', 'burger_king_chimgan')         |      2.0 |          25.0 |         0.0 |            0.0 |
| ('tesseract', 'era_omad_dengiz')             |      1.0 |          20.0 |         0.0 |            0.0 |
| ('tesseract', 'papa_johns_alexander_brands') |      1.0 |          60.0 |         0.0 |            0.0 |
| ('tesseract', 'oka_market')                  |      1.0 |          20.0 |         0.0 |            0.0 |
| ('tesseract', 'korzinka_markaz6')            |      2.0 |          25.0 |         0.0 |            0.0 |
| ('easyocr', 'burger_king_chimgan')           |      2.0 |          45.0 |         0.0 |            0.0 |
| ('easyocr', 'era_omad_dengiz')               |      1.0 |          80.0 |         0.0 |            0.0 |
| ('easyocr', 'papa_johns_alexander_brands')   |      1.0 |          70.0 |         0.0 |            0.0 |
| ('easyocr', 'oka_market')                    |      1.0 |          30.0 |         0.0 |            0.0 |
| ('easyocr', 'korzinka_markaz6')              |      2.0 |          35.0 |         0.0 |            0.0 |
| ('rapidocr', 'burger_king_chimgan')          |      2.0 |          55.0 |         0.0 |            0.0 |
| ('rapidocr', 'era_omad_dengiz')              |      1.0 |          90.0 |       100.0 |          100.0 |
| ('rapidocr', 'papa_johns_alexander_brands')  |      1.0 |          80.0 |         0.0 |            0.0 |
| ('rapidocr', 'oka_market')                   |      1.0 |          70.0 |         0.0 |            0.0 |
| ('rapidocr', 'korzinka_markaz6')             |      2.0 |          75.0 |        66.7 |           50.0 |
| ('hybrid', 'burger_king_chimgan')            |      2.0 |          55.0 |         0.0 |            0.0 |
| ('hybrid', 'era_omad_dengiz')                |      1.0 |          90.0 |       100.0 |          100.0 |
| ('hybrid', 'papa_johns_alexander_brands')    |      1.0 |          80.0 |         0.0 |            0.0 |
| ('hybrid', 'oka_market')                     |      1.0 |          60.0 |         0.0 |            0.0 |
| ('hybrid', 'korzinka_markaz6')               |      2.0 |          70.0 |        66.7 |           50.0 |


## Error causes (pre_post)

|                                            |   count |
|:-------------------------------------------|--------:|
| ('easyocr', 'date/time misread')           |       2 |
| ('easyocr', 'digits misread')              |       1 |
| ('easyocr', 'digits missing/extra')        |       2 |
| ('easyocr', 'digits/amounts misread')      |       6 |
| ('easyocr', 'not found')                   |      18 |
| ('easyocr', 'text misread / wrong span')   |       7 |
| ('hybrid', 'date/time misread')            |       2 |
| ('hybrid', 'digits missing/extra')         |       2 |
| ('hybrid', 'digits/amounts misread')       |       3 |
| ('hybrid', 'not found')                    |       5 |
| ('hybrid', 'spurious value')               |       1 |
| ('hybrid', 'text misread / wrong span')    |       9 |
| ('rapidocr', 'date/time misread')          |       2 |
| ('rapidocr', 'digits missing/extra')       |       2 |
| ('rapidocr', 'digits/amounts misread')     |       3 |
| ('rapidocr', 'not found')                  |       5 |
| ('rapidocr', 'text misread / wrong span')  |       8 |
| ('tesseract', 'date/time misread')         |       2 |
| ('tesseract', 'digits misread')            |       1 |
| ('tesseract', 'digits missing/extra')      |       2 |
| ('tesseract', 'digits/amounts misread')    |       2 |
| ('tesseract', 'not found')                 |      33 |
| ('tesseract', 'spurious value')            |       1 |
| ('tesseract', 'text misread / wrong span') |       9 |


## Error examples

| image     | config   | engine    | conditions                  | field          | gt                                                                                                   | pred                                                                                                      | cause                     |
|:----------|:---------|:----------|:----------------------------|:---------------|:-----------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------|:--------------------------|
| h07_a.jpg | pre_post | tesseract | long;upside_down            | seller_name    | FAST FOOD SYSTEM MCHJ                                                                                | oe 000 ЕАЗТ FOOD SYSTEMS                                                                                  | text misread / wrong span |
| h07_a.jpg | pre_post | tesseract | long;upside_down            | address        | Toshkent shahri, Mirzo ulug'bek tumani, Katta Yalang'och-ota MFY, Temur Malik ko'chasi, 3a-uy        |                                                                                                           | not found                 |
| h07_a.jpg | pre_post | tesseract | long;upside_down            | datetime       | 2026-11-24T13:29:18                                                                                  | 2026-11-24T13:29:19                                                                                       | date/time misread         |
| h07_a.jpg | pre_post | tesseract | long;upside_down            | receipt_number | 2000                                                                                                 | 362                                                                                                       | digits missing/extra      |
| h07_a.jpg | pre_post | tesseract | long;upside_down            | vat            | 7607.14                                                                                              |                                                                                                           | not found                 |
| h08_a.jpg | pre_post | tesseract | long;crumpled;upside_down   | seller_name    | FAST FOOD SYSTEM MCHJ                                                                                | Savdogar 000000901349249 ",                                                                               | text misread / wrong span |
| h08_a.jpg | pre_post | tesseract | long;crumpled;upside_down   | seller_tin     | 310839380                                                                                            |                                                                                                           | not found                 |
| h08_a.jpg | pre_post | tesseract | long;crumpled;upside_down   | address        | Toshkent shahri, Mirzo ulug'bek tumani, Katta Yalang'och-ota MFY, Temur Malik ko'chasi, 3a-uy        | MIRZO ULUGBEK TUMANI T MALIK ЗА                                                                           | text misread / wrong span |
| h08_a.jpg | pre_post | tesseract | long;crumpled;upside_down   | datetime       | 2026-11-24T13:28:04                                                                                  |                                                                                                           | not found                 |
| h08_a.jpg | pre_post | tesseract | long;crumpled;upside_down   | receipt_number | 2402                                                                                                 |                                                                                                           | not found                 |
| h08_a.jpg | pre_post | tesseract | long;crumpled;upside_down   | fiscal_module  | VG544170029014                                                                                       |                                                                                                           | not found                 |
| h08_a.jpg | pre_post | tesseract | long;crumpled;upside_down   | fiscal_sign    | 522785144893                                                                                         |                                                                                                           | not found                 |
| h08_a.jpg | pre_post | tesseract | long;crumpled;upside_down   | vat            | 7928.57                                                                                              |                                                                                                           | not found                 |
| h08_a.jpg | pre_post | tesseract | long;crumpled;upside_down   | total          | 74000.0                                                                                              |                                                                                                           | not found                 |
| h08_a.jpg | pre_post | tesseract | long;crumpled;upside_down   | payment        | card                                                                                                 |                                                                                                           | not found                 |
| h09_a.jpg | pre_post | tesseract | long;crumpled;upside_down   | seller_name    | ERA                                                                                                  | ERAS                                                                                                      | text misread / wrong span |
| h09_a.jpg | pre_post | tesseract | long;crumpled;upside_down   | seller_tin     | 312649427                                                                                            |                                                                                                           | not found                 |
| h09_a.jpg | pre_post | tesseract | long;crumpled;upside_down   | address        | Toshkent shahri, Yunusobod tumani, Mirzo Ulug'bek MFY, Amir Temur - Xidirali Ergashev ko'chasi, 1-uy | \ Toshkent shahri, Yunusobod tumani, Mirzo, Ulugʻbek MFY, Amir Temur, - Xidirali Ergashev, koʻchasi, 1-uy | text misread / wrong span |
| h09_a.jpg | pre_post | tesseract | long;crumpled;upside_down   | datetime       | 2026-11-24T20:24:10                                                                                  | 2026-11-24T20:24:05                                                                                       | date/time misread         |
| h09_a.jpg | pre_post | tesseract | long;crumpled;upside_down   | receipt_number | 22028                                                                                                |                                                                                                           | not found                 |
| h09_a.jpg | pre_post | tesseract | long;crumpled;upside_down   | fiscal_module  | LG420211633037                                                                                       |                                                                                                           | not found                 |
| h09_a.jpg | pre_post | tesseract | long;crumpled;upside_down   | fiscal_sign    | 026433429105                                                                                         | 026433429185                                                                                              | digits misread            |
| h09_a.jpg | pre_post | tesseract | long;crumpled;upside_down   | vat            | 6428.57                                                                                              | 69207570.0                                                                                                | digits/amounts misread    |
| h10_a.jpg | pre_post | tesseract | long;sideways;shadow        | seller_name    | OOO "ALEXANDER BRANDS"                                                                               | 000 “ALEXANDER BRANDS” |                                                                                  | text misread / wrong span |
| h10_a.jpg | pre_post | tesseract | long;sideways;shadow        | seller_tin     | 310107872                                                                                            |                                                                                                           | not found                 |
| h10_a.jpg | pre_post | tesseract | long;sideways;shadow        | vat            | 6964.28                                                                                              | 12.0                                                                                                      | digits/amounts misread    |
| h10_a.jpg | pre_post | tesseract | long;sideways;shadow        | payment        | card                                                                                                 | cash                                                                                                      | text misread / wrong span |
| h11_a.jpg | pre_post | tesseract | sideways;crumpled;shadow    | seller_name    |                                                                                                      | у "u                                                                                                      | spurious value            |
| h11_a.jpg | pre_post | tesseract | sideways;crumpled;shadow    | datetime       | 2026-11-25T21:26:00                                                                                  |                                                                                                           | not found                 |
| h11_a.jpg | pre_post | tesseract | sideways;crumpled;shadow    | receipt_number | 2562                                                                                                 |                                                                                                           | not found                 |
| h11_a.jpg | pre_post | tesseract | sideways;crumpled;shadow    | fiscal_module  | UZ210317265020                                                                                       |                                                                                                           | not found                 |
| h11_a.jpg | pre_post | tesseract | sideways;crumpled;shadow    | fiscal_sign    | 140092504709                                                                                         |                                                                                                           | not found                 |
| h11_a.jpg | pre_post | tesseract | sideways;crumpled;shadow    | vat            | 0.0                                                                                                  |                                                                                                           | not found                 |
| h11_a.jpg | pre_post | tesseract | sideways;crumpled;shadow    | total          | 6000.0                                                                                               |                                                                                                           | not found                 |
| h11_a.jpg | pre_post | tesseract | sideways;crumpled;shadow    | payment        | card                                                                                                 |                                                                                                           | not found                 |
| h12_a.jpg | pre_post | tesseract | upside_down;crumpled;shadow | seller_name    | «Anglesey Food» MChJ XK                                                                              |                                                                                                           | not found                 |
| h12_a.jpg | pre_post | tesseract | upside_down;crumpled;shadow | seller_tin     | 202099756                                                                                            |                                                                                                           | not found                 |
| h12_a.jpg | pre_post | tesseract | upside_down;crumpled;shadow | address        | Toshkent, Markaz-6, Osiyo ko'chasi, 85-uy                                                            |                                                                                                           | not found                 |
| h12_a.jpg | pre_post | tesseract | upside_down;crumpled;shadow | vat            | 384.64                                                                                               |                                                                                                           | not found                 |
| h12_a.jpg | pre_post | tesseract | upside_down;crumpled;shadow | total          | 3590.0                                                                                               |                                                                                                           | not found                 |