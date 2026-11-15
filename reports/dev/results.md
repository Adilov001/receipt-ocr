# Results (dev split, 65 images, 13 receipts, 4 sellers)

## Engines × configurations

|                           |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:--------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('tesseract', 'baseline') |     65.0 |    80.1 |    90.3 |          13.5 |         2.2 |         29.2 |         40.0 |            1.9 |           6.4 |
| ('tesseract', 'pre')      |     65.0 |    50.9 |    83.6 |          22.1 |        10.2 |         29.2 |         40.0 |            5.8 |           8.3 |
| ('tesseract', 'pre_post') |     65.0 |    50.9 |    83.6 |          40.8 |        16.9 |         29.2 |         40.0 |           17.3 |           9.3 |
| ('rapidocr', 'baseline')  |     65.0 |    66.4 |    95.7 |          46.2 |        13.2 |         29.2 |         40.0 |           15.4 |           7.9 |
| ('rapidocr', 'pre')       |     65.0 |    63.2 |    95.5 |          46.3 |        26.8 |         29.2 |         40.0 |           23.1 |           8.2 |
| ('rapidocr', 'pre_post')  |     65.0 |    63.2 |    95.7 |          58.1 |        26.8 |         29.2 |         40.0 |           36.5 |           8.1 |
| ('hybrid', 'baseline')    |     65.0 |    66.4 |    95.7 |          46.9 |        16.4 |         29.2 |         40.0 |           17.3 |           9.3 |
| ('hybrid', 'pre')         |     65.0 |    63.2 |    95.5 |          46.7 |        35.7 |         29.2 |         40.0 |           25.0 |          11.1 |
| ('hybrid', 'pre_post')    |     65.0 |    63.2 |    95.7 |          58.8 |        35.9 |         29.2 |         40.0 |           40.4 |          10.9 |


## Field accuracy, %

|                           |   seller_name |   seller_tin |   address |   datetime |   receipt_number |   fiscal_module |   fiscal_sign |   vat |   total |   payment |
|:--------------------------|--------------:|-------------:|----------:|-----------:|-----------------:|----------------:|--------------:|------:|--------:|----------:|
| ('tesseract', 'baseline') |           9.6 |         25.0 |      23.1 |        5.8 |              9.6 |             1.9 |           5.8 |   1.9 |    15.4 |      36.5 |
| ('tesseract', 'pre')      |          15.4 |         26.9 |      21.2 |       13.5 |             34.6 |             7.7 |          17.3 |  11.5 |    19.2 |      53.8 |
| ('tesseract', 'pre_post') |          21.2 |         26.9 |      21.2 |       53.8 |             57.7 |            32.7 |          42.3 |  48.1 |    38.5 |      65.4 |
| ('rapidocr', 'baseline')  |          28.8 |         67.3 |      26.9 |       51.9 |             55.8 |            25.0 |          48.1 |  40.4 |    55.8 |      61.5 |
| ('rapidocr', 'pre')       |          48.1 |         67.3 |      26.9 |       48.1 |             53.8 |            25.0 |          38.5 |  36.5 |    48.1 |      71.2 |
| ('rapidocr', 'pre_post')  |          50.0 |         67.3 |      26.9 |       69.2 |             73.1 |            44.2 |          55.8 |  48.1 |    71.2 |      75.0 |
| ('hybrid', 'baseline')    |          32.7 |         67.3 |      26.9 |       51.9 |             57.7 |            25.0 |          48.1 |  40.4 |    57.7 |      61.5 |
| ('hybrid', 'pre')         |          51.9 |         67.3 |      23.1 |       48.1 |             53.8 |            25.0 |          38.5 |  36.5 |    48.1 |      75.0 |
| ('hybrid', 'pre_post')    |          55.8 |         67.3 |      23.1 |       71.2 |             73.1 |            44.2 |          55.8 |  48.1 |    71.2 |      78.8 |


## By shooting condition

|                                          |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:-----------------------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('tesseract', 'baseline', 'crumpled')    |     27.0 |   nan   |   nan   |           1.9 |         0.0 |          0.0 |         11.1 |            0.0 |           7.9 |
| ('tesseract', 'baseline', 'shadow')      |     15.0 |    82.3 |    90.9 |          10.7 |         0.0 |         13.3 |         33.3 |            0.0 |           6.9 |
| ('tesseract', 'baseline', 'handheld')    |      9.0 |   nan   |   nan   |           3.3 |         0.0 |          0.0 |         22.2 |            0.0 |           6.5 |
| ('tesseract', 'baseline', 'tilted')      |     17.0 |    82.3 |    90.9 |           9.4 |         0.0 |         11.8 |         29.4 |            0.0 |           7.0 |
| ('tesseract', 'baseline', 'clean')       |     14.0 |    63.7 |    81.6 |          28.6 |         5.3 |         42.9 |         64.3 |            7.1 |           6.5 |
| ('tesseract', 'baseline', 'sideways')    |     13.0 |   nan   |   nan   |           0.0 |         0.0 |          7.7 |         23.1 |            0.0 |           6.6 |
| ('tesseract', 'baseline', 'partial')     |     13.0 |   nan   |   nan   |         nan   |       nan   |         69.2 |         76.9 |          nan   |           3.1 |
| ('tesseract', 'baseline', 'blur')        |      1.0 |    88.1 |    97.0 |          30.0 |         0.0 |          0.0 |          0.0 |            0.0 |          12.0 |
| ('tesseract', 'baseline', 'synthetic')   |     26.0 |    90.5 |    95.4 |           8.8 |         0.0 |         15.4 |         26.9 |            0.0 |           6.5 |
| ('tesseract', 'baseline', 'faded')       |     13.0 |    98.7 |   100.0 |           7.7 |         0.0 |         15.4 |         23.1 |            0.0 |           6.0 |
| ('tesseract', 'baseline', 'perspective') |     13.0 |    98.7 |   100.0 |           7.7 |         0.0 |         15.4 |         23.1 |            0.0 |           6.0 |
| ('tesseract', 'pre', 'crumpled')         |     27.0 |   nan   |   nan   |          11.1 |         0.0 |          0.0 |         11.1 |            0.0 |          10.9 |
| ('tesseract', 'pre', 'shadow')           |     15.0 |    68.3 |    88.1 |          15.3 |         6.7 |         13.3 |         33.3 |            0.0 |           7.9 |
| ('tesseract', 'pre', 'handheld')         |      9.0 |   nan   |   nan   |           8.9 |         0.0 |          0.0 |         22.2 |            0.0 |           9.0 |
| ('tesseract', 'pre', 'tilted')           |     17.0 |    68.3 |    88.1 |          14.1 |         5.9 |         11.8 |         29.4 |            0.0 |           8.5 |
| ('tesseract', 'pre', 'clean')            |     14.0 |    28.2 |    64.7 |          36.4 |        20.5 |         42.9 |         64.3 |           14.3 |           8.1 |
| ('tesseract', 'pre', 'sideways')         |     13.0 |   nan   |   nan   |          13.6 |         0.0 |          7.7 |         23.1 |            0.0 |           9.2 |
| ('tesseract', 'pre', 'partial')          |     13.0 |   nan   |   nan   |         nan   |       nan   |         69.2 |         76.9 |          nan   |           3.1 |
| ('tesseract', 'pre', 'blur')             |      1.0 |    44.3 |    89.1 |          50.0 |         0.0 |          0.0 |          0.0 |            0.0 |          13.0 |
| ('tesseract', 'pre', 'synthetic')        |     26.0 |    69.7 |    96.8 |          16.2 |         7.4 |         15.4 |         26.9 |            3.8 |           8.6 |
| ('tesseract', 'pre', 'faded')            |     13.0 |    71.1 |   105.5 |          16.9 |         7.7 |         15.4 |         23.1 |            7.7 |           9.3 |
| ('tesseract', 'pre', 'perspective')      |     13.0 |    71.1 |   105.5 |          16.9 |         7.7 |         15.4 |         23.1 |            7.7 |           9.3 |
| ('tesseract', 'pre_post', 'crumpled')    |     27.0 |   nan   |   nan   |          24.1 |         9.5 |          0.0 |         11.1 |           11.1 |          12.1 |
| ('tesseract', 'pre_post', 'shadow')      |     15.0 |    68.3 |    88.1 |          35.3 |         6.7 |         13.3 |         33.3 |            0.0 |           9.2 |
| ('tesseract', 'pre_post', 'handheld')    |      9.0 |   nan   |   nan   |          23.3 |        14.3 |          0.0 |         22.2 |           11.1 |           9.5 |
| ('tesseract', 'pre_post', 'tilted')      |     17.0 |    68.3 |    88.1 |          32.4 |         5.9 |         11.8 |         29.4 |            5.9 |           9.8 |
| ('tesseract', 'pre_post', 'clean')       |     14.0 |    28.2 |    64.7 |          63.6 |        25.6 |         42.9 |         64.3 |           28.6 |           8.9 |
| ('tesseract', 'pre_post', 'sideways')    |     13.0 |   nan   |   nan   |          30.9 |        37.5 |          7.7 |         23.1 |           27.3 |          10.5 |
| ('tesseract', 'pre_post', 'partial')     |     13.0 |   nan   |   nan   |         nan   |       nan   |         69.2 |         76.9 |          nan   |           3.6 |
| ('tesseract', 'pre_post', 'blur')        |      1.0 |    44.3 |    89.1 |          50.0 |         0.0 |          0.0 |          0.0 |            0.0 |          13.5 |
| ('tesseract', 'pre_post', 'synthetic')   |     26.0 |    69.7 |    96.8 |          31.9 |         7.4 |         15.4 |         26.9 |            7.7 |          10.2 |
| ('tesseract', 'pre_post', 'faded')       |     13.0 |    71.1 |   105.5 |          28.5 |         7.7 |         15.4 |         23.1 |           15.4 |          10.9 |
| ('tesseract', 'pre_post', 'perspective') |     13.0 |    71.1 |   105.5 |          28.5 |         7.7 |         15.4 |         23.1 |           15.4 |          10.9 |
| ('rapidocr', 'baseline', 'crumpled')     |     27.0 |   nan   |   nan   |          33.3 |        17.0 |          0.0 |         11.1 |           18.5 |           9.7 |
| ('rapidocr', 'baseline', 'shadow')       |     15.0 |    70.0 |    94.5 |          41.3 |        11.4 |         13.3 |         33.3 |           20.0 |           8.8 |
| ('rapidocr', 'baseline', 'handheld')     |      9.0 |   nan   |   nan   |          21.1 |        12.5 |          0.0 |         22.2 |           22.2 |           7.3 |
| ('rapidocr', 'baseline', 'tilted')       |     17.0 |    70.0 |    94.5 |          43.5 |        10.0 |         11.8 |         29.4 |           17.6 |           8.9 |
| ('rapidocr', 'baseline', 'clean')        |     14.0 |    55.1 |    95.0 |          74.3 |        20.5 |         42.9 |         64.3 |           14.3 |           7.3 |
| ('rapidocr', 'baseline', 'sideways')     |     13.0 |   nan   |   nan   |           9.1 |         0.0 |          7.7 |         23.1 |            9.1 |           9.2 |
| ('rapidocr', 'baseline', 'partial')      |     13.0 |   nan   |   nan   |         nan   |       nan   |         69.2 |         76.9 |          nan   |           4.0 |
| ('rapidocr', 'baseline', 'blur')         |      1.0 |    60.4 |    94.1 |          80.0 |         0.0 |          0.0 |          0.0 |            0.0 |          12.3 |
| ('rapidocr', 'baseline', 'synthetic')    |     26.0 |    76.4 |    96.6 |          34.2 |         3.4 |         15.4 |         26.9 |            7.7 |           9.0 |
| ('rapidocr', 'baseline', 'faded')        |     13.0 |    82.8 |    98.6 |          23.8 |         0.0 |         15.4 |         23.1 |            7.7 |           9.1 |
| ('rapidocr', 'baseline', 'perspective')  |     13.0 |    82.8 |    98.6 |          23.8 |         0.0 |         15.4 |         23.1 |            7.7 |           9.1 |
| ('rapidocr', 'pre', 'crumpled')          |     27.0 |   nan   |   nan   |          38.1 |        38.5 |          0.0 |         11.1 |           22.2 |           9.2 |
| ('rapidocr', 'pre', 'shadow')            |     15.0 |    68.0 |    96.3 |          33.3 |        23.5 |         13.3 |         33.3 |            0.0 |           7.7 |
| ('rapidocr', 'pre', 'handheld')          |      9.0 |   nan   |   nan   |          24.4 |        44.4 |          0.0 |         22.2 |           11.1 |           7.8 |
| ('rapidocr', 'pre', 'tilted')            |     17.0 |    68.0 |    96.3 |          34.7 |        25.6 |         11.8 |         29.4 |            5.9 |           7.8 |
| ('rapidocr', 'pre', 'clean')             |     14.0 |    50.8 |    93.2 |          62.1 |        25.0 |         42.9 |         64.3 |           14.3 |           9.2 |
| ('rapidocr', 'pre', 'sideways')          |     13.0 |   nan   |   nan   |          40.9 |        27.3 |          7.7 |         23.1 |           27.3 |           8.1 |
| ('rapidocr', 'pre', 'partial')           |     13.0 |   nan   |   nan   |         nan   |       nan   |         69.2 |         76.9 |          nan   |           4.3 |
| ('rapidocr', 'pre', 'blur')              |      1.0 |    55.7 |    95.0 |          60.0 |         0.0 |          0.0 |          0.0 |            0.0 |          17.0 |
| ('rapidocr', 'pre', 'synthetic')         |     26.0 |    74.3 |    97.5 |          31.5 |         9.7 |         15.4 |         26.9 |           11.5 |           7.9 |
| ('rapidocr', 'pre', 'faded')             |     13.0 |    80.6 |    98.6 |          30.0 |         0.0 |         15.4 |         23.1 |           23.1 |           8.3 |
| ('rapidocr', 'pre', 'perspective')       |     13.0 |    80.6 |    98.6 |          30.0 |         0.0 |         15.4 |         23.1 |           23.1 |           8.3 |
| ('rapidocr', 'pre_post', 'crumpled')     |     27.0 |   nan   |   nan   |          45.2 |        34.6 |          0.0 |         11.1 |           37.0 |           9.8 |
| ('rapidocr', 'pre_post', 'shadow')       |     15.0 |    68.2 |    96.8 |          48.7 |        17.6 |         13.3 |         33.3 |           20.0 |           8.2 |
| ('rapidocr', 'pre_post', 'handheld')     |      9.0 |   nan   |   nan   |          34.4 |        44.4 |          0.0 |         22.2 |           33.3 |           8.5 |
| ('rapidocr', 'pre_post', 'tilted')       |     17.0 |    68.2 |    96.8 |          48.2 |        20.5 |         11.8 |         29.4 |           23.5 |           8.5 |
| ('rapidocr', 'pre_post', 'clean')        |     14.0 |    50.9 |    93.2 |          80.7 |        30.0 |         42.9 |         64.3 |           35.7 |           8.2 |
| ('rapidocr', 'pre_post', 'sideways')     |     13.0 |   nan   |   nan   |          46.4 |        36.4 |          7.7 |         23.1 |           36.4 |           8.8 |
| ('rapidocr', 'pre_post', 'partial')      |     13.0 |   nan   |   nan   |         nan   |       nan   |         69.2 |         76.9 |          nan   |           3.6 |
| ('rapidocr', 'pre_post', 'blur')         |      1.0 |    55.7 |    95.0 |          60.0 |         0.0 |          0.0 |          0.0 |            0.0 |          14.5 |
| ('rapidocr', 'pre_post', 'synthetic')    |     26.0 |    74.4 |    97.7 |          42.7 |         6.5 |         15.4 |         26.9 |           23.1 |           8.7 |
| ('rapidocr', 'pre_post', 'faded')        |     13.0 |    80.6 |    98.6 |          38.5 |         0.0 |         15.4 |         23.1 |           30.8 |           9.1 |
| ('rapidocr', 'pre_post', 'perspective')  |     13.0 |    80.6 |    98.6 |          38.5 |         0.0 |         15.4 |         23.1 |           30.8 |           9.1 |
| ('hybrid', 'baseline', 'crumpled')       |     27.0 |   nan   |   nan   |          33.7 |        17.0 |          0.0 |         11.1 |           18.5 |          11.2 |
| ('hybrid', 'baseline', 'shadow')         |     15.0 |    70.0 |    94.5 |          42.0 |        11.4 |         13.3 |         33.3 |           20.0 |          10.9 |
| ('hybrid', 'baseline', 'handheld')       |      9.0 |   nan   |   nan   |          22.2 |        12.5 |          0.0 |         22.2 |           22.2 |           9.5 |
| ('hybrid', 'baseline', 'tilted')         |     17.0 |    70.0 |    94.5 |          44.1 |        10.0 |         11.8 |         29.4 |           17.6 |          10.9 |
| ('hybrid', 'baseline', 'clean')          |     14.0 |    55.1 |    95.0 |          76.4 |        30.0 |         42.9 |         64.3 |           21.4 |          10.0 |
| ('hybrid', 'baseline', 'sideways')       |     13.0 |   nan   |   nan   |           9.1 |         0.0 |          7.7 |         23.1 |            9.1 |           9.9 |
| ('hybrid', 'baseline', 'partial')        |     13.0 |   nan   |   nan   |         nan   |       nan   |         69.2 |         76.9 |          nan   |           3.4 |
| ('hybrid', 'baseline', 'blur')           |      1.0 |    60.4 |    94.1 |          80.0 |         0.0 |          0.0 |          0.0 |            0.0 |          15.2 |
| ('hybrid', 'baseline', 'synthetic')      |     26.0 |    76.4 |    96.6 |          34.2 |         3.4 |         15.4 |         26.9 |            7.7 |          10.4 |
| ('hybrid', 'baseline', 'faded')          |     13.0 |    82.8 |    98.6 |          23.8 |         0.0 |         15.4 |         23.1 |            7.7 |           9.7 |
| ('hybrid', 'baseline', 'perspective')    |     13.0 |    82.8 |    98.6 |          23.8 |         0.0 |         15.4 |         23.1 |            7.7 |           9.7 |
| ('hybrid', 'pre', 'crumpled')            |     27.0 |   nan   |   nan   |          38.1 |        38.5 |          0.0 |         11.1 |           22.2 |          14.4 |
| ('hybrid', 'pre', 'shadow')              |     15.0 |    68.0 |    96.3 |          33.3 |        29.4 |         13.3 |         33.3 |            0.0 |          10.8 |
| ('hybrid', 'pre', 'handheld')            |      9.0 |   nan   |   nan   |          25.6 |        44.4 |          0.0 |         22.2 |           11.1 |          12.1 |
| ('hybrid', 'pre', 'tilted')              |     17.0 |    68.0 |    96.3 |          34.7 |        30.8 |         11.8 |         29.4 |            5.9 |          11.6 |
| ('hybrid', 'pre', 'clean')               |     14.0 |    50.8 |    93.2 |          63.6 |        42.9 |         42.9 |         64.3 |           21.4 |          11.9 |
| ('hybrid', 'pre', 'sideways')            |     13.0 |   nan   |   nan   |          40.9 |        27.3 |          7.7 |         23.1 |           27.3 |          12.2 |
| ('hybrid', 'pre', 'partial')             |     13.0 |   nan   |   nan   |         nan   |       nan   |         69.2 |         76.9 |          nan   |           3.4 |
| ('hybrid', 'pre', 'blur')                |      1.0 |    55.7 |    95.0 |          60.0 |         0.0 |          0.0 |          0.0 |            0.0 |          17.5 |
| ('hybrid', 'pre', 'synthetic')           |     26.0 |    74.3 |    97.5 |          31.5 |        16.1 |         15.4 |         26.9 |           11.5 |          11.5 |
| ('hybrid', 'pre', 'faded')               |     13.0 |    80.6 |    98.6 |          30.8 |         6.2 |         15.4 |         23.1 |           23.1 |          12.2 |
| ('hybrid', 'pre', 'perspective')         |     13.0 |    80.6 |    98.6 |          30.8 |         6.2 |         15.4 |         23.1 |           23.1 |          12.2 |
| ('hybrid', 'pre_post', 'crumpled')       |     27.0 |   nan   |   nan   |          45.6 |        35.3 |          0.0 |         11.1 |           40.7 |          13.9 |
| ('hybrid', 'pre_post', 'shadow')         |     15.0 |    68.2 |    96.8 |          49.3 |        23.5 |         13.3 |         33.3 |           20.0 |          10.4 |
| ('hybrid', 'pre_post', 'handheld')       |      9.0 |   nan   |   nan   |          36.7 |        47.1 |          0.0 |         22.2 |           44.4 |          11.8 |
| ('hybrid', 'pre_post', 'tilted')         |     17.0 |    68.2 |    96.8 |          48.8 |        25.6 |         11.8 |         29.4 |           23.5 |          11.2 |
| ('hybrid', 'pre_post', 'clean')          |     14.0 |    50.9 |    93.2 |          82.1 |        47.6 |         42.9 |         64.3 |           42.9 |          11.7 |
| ('hybrid', 'pre_post', 'sideways')       |     13.0 |   nan   |   nan   |          47.3 |        38.1 |          7.7 |         23.1 |           45.5 |          11.8 |
| ('hybrid', 'pre_post', 'partial')        |     13.0 |   nan   |   nan   |         nan   |       nan   |         69.2 |         76.9 |          nan   |           3.4 |
| ('hybrid', 'pre_post', 'blur')           |      1.0 |    55.7 |    95.0 |          60.0 |         0.0 |          0.0 |          0.0 |            0.0 |          17.0 |
| ('hybrid', 'pre_post', 'synthetic')      |     26.0 |    74.4 |    97.7 |          43.1 |        12.9 |         15.4 |         26.9 |           23.1 |          11.0 |
| ('hybrid', 'pre_post', 'faded')          |     13.0 |    80.6 |    98.6 |          39.2 |         6.2 |         15.4 |         23.1 |           30.8 |          11.8 |
| ('hybrid', 'pre_post', 'perspective')    |     13.0 |    80.6 |    98.6 |          39.2 |         6.2 |         15.4 |         23.1 |           30.8 |          11.8 |


## By language

|                                      |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:-------------------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('tesseract', 'baseline', 'uz_latn') |     50.0 |   nan   |   nan   |           4.8 |         0.0 |         22.0 |         34.0 |            0.0 |           6.6 |
| ('tesseract', 'baseline', 'mixed')   |     15.0 |    80.1 |    90.3 |          42.5 |         4.9 |         53.3 |         60.0 |            8.3 |           5.5 |
| ('tesseract', 'pre', 'uz_latn')      |     50.0 |   nan   |   nan   |          12.5 |         0.0 |         22.0 |         34.0 |            0.0 |           8.7 |
| ('tesseract', 'pre', 'mixed')        |     15.0 |    50.9 |    83.6 |          54.2 |        22.2 |         53.3 |         60.0 |           25.0 |           6.9 |
| ('tesseract', 'pre_post', 'uz_latn') |     50.0 |   nan   |   nan   |          31.3 |        12.5 |         22.0 |         34.0 |           15.0 |           9.9 |
| ('tesseract', 'pre_post', 'mixed')   |     15.0 |    50.9 |    83.6 |          72.5 |        22.2 |         53.3 |         60.0 |           25.0 |           7.6 |
| ('rapidocr', 'baseline', 'uz_latn')  |     50.0 |   nan   |   nan   |          40.5 |        21.9 |         22.0 |         34.0 |           17.5 |           8.1 |
| ('rapidocr', 'baseline', 'mixed')    |     15.0 |    66.4 |    95.7 |          65.0 |         0.0 |         53.3 |         60.0 |            8.3 |           7.0 |
| ('rapidocr', 'pre', 'uz_latn')       |     50.0 |   nan   |   nan   |          42.5 |        43.6 |         22.0 |         34.0 |           25.0 |           8.3 |
| ('rapidocr', 'pre', 'mixed')         |     15.0 |    63.2 |    95.5 |          59.2 |         0.0 |         53.3 |         60.0 |           16.7 |           7.7 |
| ('rapidocr', 'pre_post', 'uz_latn')  |     50.0 |   nan   |   nan   |          52.8 |        43.6 |         22.0 |         34.0 |           42.5 |           8.4 |
| ('rapidocr', 'pre_post', 'mixed')    |     15.0 |    63.2 |    95.7 |          75.8 |         0.0 |         53.3 |         60.0 |           16.7 |           7.1 |
| ('hybrid', 'baseline', 'uz_latn')    |     50.0 |   nan   |   nan   |          40.8 |        21.9 |         22.0 |         34.0 |           17.5 |           9.7 |
| ('hybrid', 'baseline', 'mixed')      |     15.0 |    66.4 |    95.7 |          67.5 |         8.2 |         53.3 |         60.0 |           16.7 |           8.3 |
| ('hybrid', 'pre', 'uz_latn')         |     50.0 |   nan   |   nan   |          42.7 |        43.6 |         22.0 |         34.0 |           25.0 |          11.7 |
| ('hybrid', 'pre', 'mixed')           |     15.0 |    63.2 |    95.5 |          60.0 |        23.5 |         53.3 |         60.0 |           25.0 |           9.2 |
| ('hybrid', 'pre_post', 'uz_latn')    |     50.0 |   nan   |   nan   |          53.2 |        44.2 |         22.0 |         34.0 |           45.0 |          11.4 |
| ('hybrid', 'pre_post', 'mixed')      |     15.0 |    63.2 |    95.7 |          77.5 |        23.5 |         53.3 |         60.0 |           25.0 |           9.1 |


## Preprocessing ablation (tesseract, dev split, post-processing on)

|                              |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:-----------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| none (raw image)             |     65.0 |    81.4 |    86.4 |          27.3 |         8.6 |         29.2 |         40.0 |            0.0 |           5.8 |
| + crop                       |     65.0 |    75.2 |    93.2 |          33.1 |        14.7 |         29.2 |         40.0 |           11.5 |           6.7 |
| + orient                     |     65.0 |    75.2 |    93.2 |          32.9 |        14.9 |         29.2 |         40.0 |           11.5 |           7.1 |
| + deskew                     |     65.0 |    72.7 |    89.7 |          35.2 |         9.7 |         29.2 |         40.0 |            9.6 |           8.9 |
| + illumination               |     65.0 |    72.9 |   108.2 |          37.3 |         9.6 |         29.2 |         40.0 |            9.6 |          10.1 |
| + clahe                      |     65.0 |    50.9 |    83.6 |          40.8 |        16.9 |         29.2 |         40.0 |           17.3 |           8.4 |
| + binarize                   |     65.0 |    78.3 |   158.1 |          29.2 |         1.9 |         29.2 |         40.0 |            1.9 |           7.7 |
| default without crop         |     65.0 |    57.6 |   109.7 |          40.2 |        15.7 |         29.2 |         40.0 |            7.7 |          12.0 |
| default without orient       |     65.0 |    50.9 |    83.6 |          40.0 |        16.9 |         29.2 |         40.0 |           17.3 |           7.1 |
| default without deskew       |     65.0 |    57.0 |    85.0 |          37.9 |        20.6 |         29.2 |         40.0 |           17.3 |           7.1 |
| default without illumination |     65.0 |    55.9 |    84.4 |          35.2 |        11.5 |         29.2 |         40.0 |           13.5 |           6.7 |
| default without clahe        |     65.0 |    72.9 |   108.2 |          37.3 |         9.6 |         29.2 |         40.0 |            9.6 |           8.6 |


## Error causes (pre_post)

|                                                    |   count |
|:---------------------------------------------------|--------:|
| ('hybrid', 'date/time misread')                    |       9 |
| ('hybrid', 'digits misread')                       |      23 |
| ('hybrid', 'digits missing/extra')                 |       3 |
| ('hybrid', 'digits/amounts misread')               |      18 |
| ('hybrid', 'not found')                            |      98 |
| ('hybrid', 'spurious value')                       |       2 |
| ('hybrid', 'text misread / wrong span')            |      58 |
| ('hybrid', 'thousand/decimal separator')           |       1 |
| ('hybrid', 'wrong line picked (value of total)')   |       1 |
| ('hybrid', 'wrong line picked (value of vat)')     |       1 |
| ('rapidocr', 'date/time misread')                  |       9 |
| ('rapidocr', 'digits misread')                     |      23 |
| ('rapidocr', 'digits missing/extra')               |       2 |
| ('rapidocr', 'digits/amounts misread')             |      17 |
| ('rapidocr', 'not found')                          |     105 |
| ('rapidocr', 'text misread / wrong span')          |      59 |
| ('rapidocr', 'thousand/decimal separator')         |       1 |
| ('rapidocr', 'wrong line picked (value of total)') |       1 |
| ('rapidocr', 'wrong line picked (value of vat)')   |       1 |
| ('tesseract', 'date/time misread')                 |      10 |
| ('tesseract', 'digits misread')                    |      10 |
| ('tesseract', 'digits missing/extra')              |       4 |
| ('tesseract', 'digits/amounts misread')            |      19 |
| ('tesseract', 'not found')                         |     187 |
| ('tesseract', 'spurious value')                    |       2 |
| ('tesseract', 'text misread / wrong span')         |      74 |
| ('tesseract', 'thousand/decimal separator')        |       1 |
| ('tesseract', 'wrong line picked (value of vat)')  |       1 |


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
| r04_a.jpg | pre_post | tesseract | clean                           | vat            | 957.14                                                                        | 911.43                                                                                                                           | digits/amounts misread    |
| r05_a.jpg | pre_post | tesseract | crumpled                        | seller_name    | Tinda                                                                         | turasan MAMADALIYIN АКА ЕК                                                                                                       | text misread / wrong span |
| r05_a.jpg | pre_post | tesseract | crumpled                        | seller_tin     | 31709886970015                                                                |                                                                                                                                  | not found                 |
| r05_a.jpg | pre_post | tesseract | crumpled                        | address        | Farg'ona viloyati, Farg'ona shahar, 64-Barkamol MFY Yangi asr ko'chasi 130-uy | Fargʻona) viloyt |                                                                                                               | text misread / wrong span |
| r05_a.jpg | pre_post | tesseract | crumpled                        | datetime       | 2026-11-04T18:07:47                                                           | 2026-11-04T18:07:00                                                                                                              | date/time misread         |
| r05_a.jpg | pre_post | tesseract | crumpled                        | receipt_number | 36800                                                                         | 36802                                                                                                                            | digits misread            |
| r05_a.jpg | pre_post | tesseract | crumpled                        | fiscal_module  | NA000000006920                                                                |                                                                                                                                  | not found                 |
| r05_a.jpg | pre_post | tesseract | crumpled                        | fiscal_sign    | 861532066154                                                                  | 861532866154                                                                                                                     | digits misread            |
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