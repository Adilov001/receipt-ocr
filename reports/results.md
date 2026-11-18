# Results (test split, 53 images, 16 receipts, 3 sellers)

## Engines × configurations

|                           |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:--------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('tesseract', 'baseline') |     53.0 |    93.4 |    96.5 |           4.6 |         0.0 |         47.2 |         58.5 |            0.0 |           7.4 |
| ('tesseract', 'pre')      |     53.0 |    45.4 |    81.3 |          17.8 |         3.1 |         47.2 |         58.5 |            2.7 |           8.5 |
| ('tesseract', 'pre_post') |     53.0 |    45.1 |    80.3 |          51.6 |         9.4 |         47.2 |         58.5 |            5.4 |           8.5 |
| ('easyocr', 'baseline')   |     53.0 |    73.1 |    95.4 |          20.0 |         0.0 |         47.2 |         58.5 |            0.0 |          36.0 |
| ('easyocr', 'pre')        |     53.0 |    41.8 |    82.3 |          25.1 |         0.0 |         47.2 |         58.5 |            2.7 |          19.1 |
| ('easyocr', 'pre_post')   |     53.0 |    41.0 |    78.3 |          51.4 |         0.0 |         47.2 |         58.5 |            0.0 |          18.4 |
| ('rapidocr', 'baseline')  |     53.0 |    62.1 |    72.3 |          48.6 |        41.3 |         47.2 |         58.5 |           29.7 |           8.8 |
| ('rapidocr', 'pre')       |     53.0 |    28.2 |    48.6 |          51.9 |        58.8 |         47.2 |         58.5 |           37.8 |           8.2 |
| ('rapidocr', 'pre_post')  |     53.0 |    27.8 |    46.0 |          77.3 |        70.6 |         47.2 |         58.5 |           54.1 |           8.0 |
| ('hybrid', 'baseline')    |     53.0 |    62.1 |    72.3 |          48.6 |        41.3 |         47.2 |         58.5 |           29.7 |          10.8 |
| ('hybrid', 'pre')         |     53.0 |    28.2 |    48.6 |          52.4 |        58.8 |         47.2 |         58.5 |           35.1 |          11.7 |
| ('hybrid', 'pre_post')    |     53.0 |    27.8 |    46.0 |          78.1 |        70.6 |         47.2 |         58.5 |           51.4 |          11.0 |


## Field accuracy, %

|                           |   seller_name |   seller_tin |   address |   datetime |   receipt_number |   fiscal_module |   fiscal_sign |   vat |   total |   payment |
|:--------------------------|--------------:|-------------:|----------:|-----------:|-----------------:|----------------:|--------------:|------:|--------:|----------:|
| ('tesseract', 'baseline') |           0.0 |          2.7 |       0.0 |        2.7 |              8.1 |             0.0 |           2.7 |   2.7 |    10.8 |      16.2 |
| ('tesseract', 'pre')      |           0.0 |         29.7 |      10.8 |       24.3 |             43.2 |             0.0 |          16.2 |   5.4 |    10.8 |      37.8 |
| ('tesseract', 'pre_post') |          32.4 |         29.7 |      10.8 |       64.9 |             73.0 |            54.1 |          64.9 |  56.8 |    54.1 |      75.7 |
| ('easyocr', 'baseline')   |           0.0 |         24.3 |       0.0 |        0.0 |             37.8 |            10.8 |          27.0 |  27.0 |    29.7 |      43.2 |
| ('easyocr', 'pre')        |           0.0 |         48.6 |       0.0 |        5.4 |             45.9 |            27.0 |          24.3 |  35.1 |    16.2 |      48.6 |
| ('easyocr', 'pre_post')   |          32.4 |         48.6 |       0.0 |       62.2 |             73.0 |            64.9 |          64.9 |  67.6 |    40.5 |      59.5 |
| ('rapidocr', 'baseline')  |           0.0 |         45.9 |      37.8 |       62.2 |             45.9 |            62.2 |          51.4 |  54.1 |    70.3 |      56.8 |
| ('rapidocr', 'pre')       |           0.0 |         59.5 |      32.4 |       56.8 |             62.2 |            59.5 |          45.9 |  56.8 |    67.6 |      78.4 |
| ('rapidocr', 'pre_post')  |          89.2 |         59.5 |      45.9 |       81.1 |             83.8 |            81.1 |          75.7 |  86.5 |    83.8 |      86.5 |
| ('hybrid', 'baseline')    |           0.0 |         45.9 |      37.8 |       62.2 |             45.9 |            62.2 |          51.4 |  54.1 |    70.3 |      56.8 |
| ('hybrid', 'pre')         |           0.0 |         59.5 |      32.4 |       56.8 |             64.9 |            59.5 |          45.9 |  56.8 |    67.6 |      81.1 |
| ('hybrid', 'pre_post')    |          89.2 |         59.5 |      45.9 |       81.1 |             83.8 |            81.1 |          75.7 |  86.5 |    86.5 |      91.9 |


## By shooting condition

|                                          |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:-----------------------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('tesseract', 'baseline', 'sideways')    |     16.0 |    99.4 |    99.9 |           0.0 |         0.0 |         62.5 |         62.5 |            0.0 |           4.4 |
| ('tesseract', 'baseline', 'crumpled')    |     15.0 |    97.4 |    98.9 |           0.0 |         0.0 |         20.0 |         40.0 |            0.0 |           7.0 |
| ('tesseract', 'baseline', 'handheld')    |      6.0 |    96.4 |    97.9 |           0.0 |         0.0 |         50.0 |         50.0 |            0.0 |           5.3 |
| ('tesseract', 'baseline', 'clean')       |     15.0 |    66.2 |    81.5 |          10.7 |         0.0 |         46.7 |         60.0 |            0.0 |           9.2 |
| ('tesseract', 'baseline', 'partial')     |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           5.9 |
| ('tesseract', 'baseline', 'synthetic')   |     14.0 |    97.8 |    99.0 |           0.7 |         0.0 |         28.6 |         42.9 |            0.0 |           8.1 |
| ('tesseract', 'baseline', 'shadow')      |      7.0 |    97.8 |    98.6 |           0.0 |         0.0 |         28.6 |         42.9 |            0.0 |           8.2 |
| ('tesseract', 'baseline', 'tilted')      |      7.0 |    97.8 |    98.6 |           0.0 |         0.0 |         28.6 |         42.9 |            0.0 |           8.2 |
| ('tesseract', 'baseline', 'faded')       |      7.0 |    97.8 |    99.4 |           1.4 |         0.0 |         28.6 |         42.9 |            0.0 |           7.9 |
| ('tesseract', 'baseline', 'perspective') |      7.0 |    97.8 |    99.4 |           1.4 |         0.0 |         28.6 |         42.9 |            0.0 |           7.9 |
| ('tesseract', 'pre', 'sideways')         |     16.0 |    39.0 |    73.8 |          15.0 |         0.0 |         62.5 |         62.5 |            0.0 |           7.4 |
| ('tesseract', 'pre', 'crumpled')         |     15.0 |    48.6 |    84.0 |          12.7 |         0.0 |         20.0 |         40.0 |            0.0 |          10.0 |
| ('tesseract', 'pre', 'handheld')         |      6.0 |    59.9 |    99.9 |           8.3 |         0.0 |         50.0 |         50.0 |            0.0 |           8.6 |
| ('tesseract', 'pre', 'clean')            |     15.0 |    46.9 |    82.3 |          21.3 |         8.3 |         46.7 |         60.0 |            6.7 |           9.8 |
| ('tesseract', 'pre', 'partial')          |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           5.7 |
| ('tesseract', 'pre', 'synthetic')        |     14.0 |    57.4 |    92.9 |          12.9 |         0.0 |         28.6 |         42.9 |            0.0 |          10.4 |
| ('tesseract', 'pre', 'shadow')           |      7.0 |    56.3 |    80.0 |          11.4 |         0.0 |         28.6 |         42.9 |            0.0 |           9.5 |
| ('tesseract', 'pre', 'tilted')           |      7.0 |    56.3 |    80.0 |          11.4 |         0.0 |         28.6 |         42.9 |            0.0 |           9.5 |
| ('tesseract', 'pre', 'faded')            |      7.0 |    58.4 |   105.8 |          14.3 |         0.0 |         28.6 |         42.9 |            0.0 |          11.3 |
| ('tesseract', 'pre', 'perspective')      |      7.0 |    58.4 |   105.8 |          14.3 |         0.0 |         28.6 |         42.9 |            0.0 |          11.3 |
| ('tesseract', 'pre_post', 'sideways')    |     16.0 |    38.7 |    72.6 |          47.9 |         7.7 |         62.5 |         62.5 |            0.0 |           6.6 |
| ('tesseract', 'pre_post', 'crumpled')    |     15.0 |    48.3 |    82.9 |          36.0 |         0.0 |         20.0 |         40.0 |            0.0 |           9.1 |
| ('tesseract', 'pre_post', 'handheld')    |      6.0 |    59.7 |    99.1 |          40.0 |        22.2 |         50.0 |         50.0 |            0.0 |           8.2 |
| ('tesseract', 'pre_post', 'clean')       |     15.0 |    46.8 |    81.7 |          61.3 |        16.7 |         46.7 |         60.0 |            6.7 |          10.3 |
| ('tesseract', 'pre_post', 'partial')     |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           6.1 |
| ('tesseract', 'pre_post', 'synthetic')   |     14.0 |    57.0 |    91.4 |          36.4 |         0.0 |         28.6 |         42.9 |            7.1 |           9.5 |
| ('tesseract', 'pre_post', 'shadow')      |      7.0 |    56.2 |    79.7 |          35.7 |         0.0 |         28.6 |         42.9 |           14.3 |           8.7 |
| ('tesseract', 'pre_post', 'tilted')      |      7.0 |    56.2 |    79.7 |          35.7 |         0.0 |         28.6 |         42.9 |           14.3 |           8.7 |
| ('tesseract', 'pre_post', 'faded')       |      7.0 |    57.9 |   103.0 |          37.1 |         0.0 |         28.6 |         42.9 |            0.0 |          10.4 |
| ('tesseract', 'pre_post', 'perspective') |      7.0 |    57.9 |   103.0 |          37.1 |         0.0 |         28.6 |         42.9 |            0.0 |          10.4 |
| ('easyocr', 'baseline', 'sideways')      |     16.0 |    88.9 |   102.7 |           0.0 |         0.0 |         62.5 |         62.5 |            0.0 |          41.0 |
| ('easyocr', 'baseline', 'crumpled')      |     15.0 |    80.6 |   100.5 |           6.0 |         0.0 |         20.0 |         40.0 |            0.0 |          49.7 |
| ('easyocr', 'baseline', 'handheld')      |      6.0 |    73.5 |    94.7 |           6.7 |         0.0 |         50.0 |         50.0 |            0.0 |          52.7 |
| ('easyocr', 'baseline', 'clean')         |     15.0 |    16.6 |    68.5 |          40.0 |         0.0 |         46.7 |         60.0 |            0.0 |          47.6 |
| ('easyocr', 'baseline', 'partial')       |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           6.9 |
| ('easyocr', 'baseline', 'synthetic')     |     14.0 |    85.4 |   102.3 |           7.9 |         0.0 |         28.6 |         42.9 |            0.0 |          51.5 |
| ('easyocr', 'baseline', 'shadow')        |      7.0 |    77.2 |   105.9 |           8.6 |         0.0 |         28.6 |         42.9 |            0.0 |          53.3 |
| ('easyocr', 'baseline', 'tilted')        |      7.0 |    77.2 |   105.9 |           8.6 |         0.0 |         28.6 |         42.9 |            0.0 |          53.3 |
| ('easyocr', 'baseline', 'faded')         |      7.0 |    93.5 |    98.7 |           7.1 |         0.0 |         28.6 |         42.9 |            0.0 |          49.7 |
| ('easyocr', 'baseline', 'perspective')   |      7.0 |    93.5 |    98.7 |           7.1 |         0.0 |         28.6 |         42.9 |            0.0 |          49.7 |
| ('easyocr', 'pre', 'sideways')           |     16.0 |    40.2 |    81.4 |          21.4 |         0.0 |         62.5 |         62.5 |            7.1 |          19.3 |
| ('easyocr', 'pre', 'crumpled')           |     15.0 |    46.7 |    83.7 |          16.0 |         0.0 |         20.0 |         40.0 |            6.7 |          24.2 |
| ('easyocr', 'pre', 'handheld')           |      6.0 |    56.0 |    90.0 |          10.0 |         0.0 |         50.0 |         50.0 |            0.0 |          23.1 |
| ('easyocr', 'pre', 'clean')              |     15.0 |    29.2 |    78.8 |          34.7 |         0.0 |         46.7 |         60.0 |            0.0 |          24.1 |
| ('easyocr', 'pre', 'partial')            |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           7.3 |
| ('easyocr', 'pre', 'synthetic')          |     14.0 |    62.0 |    93.2 |          10.7 |         0.0 |         28.6 |         42.9 |            0.0 |          26.9 |
| ('easyocr', 'pre', 'shadow')             |      7.0 |    52.8 |    87.7 |          15.7 |         0.0 |         28.6 |         42.9 |            0.0 |          30.9 |
| ('easyocr', 'pre', 'tilted')             |      7.0 |    52.8 |    87.7 |          15.7 |         0.0 |         28.6 |         42.9 |            0.0 |          30.9 |
| ('easyocr', 'pre', 'faded')              |      7.0 |    71.1 |    98.7 |           5.7 |         0.0 |         28.6 |         42.9 |            0.0 |          22.9 |
| ('easyocr', 'pre', 'perspective')        |      7.0 |    71.1 |    98.7 |           5.7 |         0.0 |         28.6 |         42.9 |            0.0 |          22.9 |
| ('easyocr', 'pre_post', 'sideways')      |     16.0 |    39.4 |    77.4 |          46.4 |         0.0 |         62.5 |         62.5 |            0.0 |          18.9 |
| ('easyocr', 'pre_post', 'crumpled')      |     15.0 |    46.0 |    80.3 |          36.7 |         0.0 |         20.0 |         40.0 |            0.0 |          23.4 |
| ('easyocr', 'pre_post', 'handheld')      |      6.0 |    55.3 |    85.8 |          31.7 |         0.0 |         50.0 |         50.0 |            0.0 |          22.2 |
| ('easyocr', 'pre_post', 'clean')         |     15.0 |    28.3 |    73.8 |          64.0 |         0.0 |         46.7 |         60.0 |            0.0 |          23.0 |
| ('easyocr', 'pre_post', 'partial')       |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           6.2 |
| ('easyocr', 'pre_post', 'synthetic')     |     14.0 |    61.5 |    90.7 |          32.1 |         0.0 |         28.6 |         42.9 |            0.0 |          26.9 |
| ('easyocr', 'pre_post', 'shadow')        |      7.0 |    52.3 |    84.5 |          40.0 |         0.0 |         28.6 |         42.9 |            0.0 |          30.8 |
| ('easyocr', 'pre_post', 'tilted')        |      7.0 |    52.3 |    84.5 |          40.0 |         0.0 |         28.6 |         42.9 |            0.0 |          30.8 |
| ('easyocr', 'pre_post', 'faded')         |      7.0 |    70.6 |    96.8 |          24.3 |         0.0 |         28.6 |         42.9 |            0.0 |          22.9 |
| ('easyocr', 'pre_post', 'perspective')   |      7.0 |    70.6 |    96.8 |          24.3 |         0.0 |         28.6 |         42.9 |            0.0 |          22.9 |
| ('rapidocr', 'baseline', 'sideways')     |     16.0 |    78.0 |    86.6 |          15.7 |         0.0 |         62.5 |         62.5 |            0.0 |           6.3 |
| ('rapidocr', 'baseline', 'crumpled')     |     15.0 |    70.1 |    80.4 |          29.3 |         0.0 |         20.0 |         40.0 |            0.0 |           8.9 |
| ('rapidocr', 'baseline', 'handheld')     |      6.0 |    62.5 |    73.4 |          16.7 |         0.0 |         50.0 |         50.0 |            0.0 |           7.1 |
| ('rapidocr', 'baseline', 'clean')        |     15.0 |     5.9 |    19.6 |          76.7 |        82.8 |         46.7 |         60.0 |           66.7 |          10.6 |
| ('rapidocr', 'baseline', 'partial')      |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           7.0 |
| ('rapidocr', 'baseline', 'synthetic')    |     14.0 |    76.8 |    85.9 |          28.6 |        10.0 |         28.6 |         42.9 |            7.1 |           9.2 |
| ('rapidocr', 'baseline', 'shadow')       |      7.0 |    62.9 |    76.0 |          40.0 |        16.7 |         28.6 |         42.9 |           14.3 |           9.6 |
| ('rapidocr', 'baseline', 'tilted')       |      7.0 |    62.9 |    76.0 |          40.0 |        16.7 |         28.6 |         42.9 |           14.3 |           9.6 |
| ('rapidocr', 'baseline', 'faded')        |      7.0 |    90.7 |    95.7 |          17.1 |         0.0 |         28.6 |         42.9 |            0.0 |           8.7 |
| ('rapidocr', 'baseline', 'perspective')  |      7.0 |    90.7 |    95.7 |          17.1 |         0.0 |         28.6 |         42.9 |            0.0 |           8.7 |
| ('rapidocr', 'pre', 'sideways')          |     16.0 |    26.8 |    47.9 |          47.1 |        50.0 |         62.5 |         62.5 |           28.6 |           6.1 |
| ('rapidocr', 'pre', 'crumpled')          |     15.0 |    34.6 |    56.5 |          39.3 |        24.0 |         20.0 |         40.0 |           20.0 |           8.7 |
| ('rapidocr', 'pre', 'handheld')          |      6.0 |    44.3 |    66.8 |          21.7 |        22.2 |         50.0 |         50.0 |            0.0 |           7.5 |
| ('rapidocr', 'pre', 'clean')             |     15.0 |     9.9 |    25.4 |          66.0 |        86.7 |         46.7 |         60.0 |           66.7 |           9.6 |
| ('rapidocr', 'pre', 'partial')           |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           6.2 |
| ('rapidocr', 'pre', 'synthetic')         |     14.0 |    46.7 |    70.8 |          25.0 |        18.2 |         28.6 |         42.9 |            0.0 |           9.3 |
| ('rapidocr', 'pre', 'shadow')            |      7.0 |    47.1 |    63.3 |          28.6 |        18.2 |         28.6 |         42.9 |            0.0 |           8.9 |
| ('rapidocr', 'pre', 'tilted')            |      7.0 |    47.1 |    63.3 |          28.6 |        18.2 |         28.6 |         42.9 |            0.0 |           8.9 |
| ('rapidocr', 'pre', 'faded')             |      7.0 |    46.2 |    78.4 |          21.4 |        18.2 |         28.6 |         42.9 |            0.0 |           9.7 |
| ('rapidocr', 'pre', 'perspective')       |      7.0 |    46.2 |    78.4 |          21.4 |        18.2 |         28.6 |         42.9 |            0.0 |           9.7 |
| ('rapidocr', 'pre_post', 'sideways')     |     16.0 |    26.3 |    45.4 |          75.7 |        58.3 |         62.5 |         62.5 |           35.7 |           5.9 |
| ('rapidocr', 'pre_post', 'crumpled')     |     15.0 |    34.1 |    53.6 |          65.3 |        40.0 |         20.0 |         40.0 |           46.7 |           8.1 |
| ('rapidocr', 'pre_post', 'handheld')     |      6.0 |    43.9 |    64.3 |          51.7 |        44.4 |         50.0 |         50.0 |           16.7 |           6.5 |
| ('rapidocr', 'pre_post', 'clean')        |     15.0 |     9.6 |    23.0 |          88.0 |        93.3 |         46.7 |         60.0 |           73.3 |           9.5 |
| ('rapidocr', 'pre_post', 'partial')      |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           6.2 |
| ('rapidocr', 'pre_post', 'synthetic')    |     14.0 |    46.1 |    67.8 |          57.1 |        36.4 |         28.6 |         42.9 |           21.4 |           8.6 |
| ('rapidocr', 'pre_post', 'shadow')       |      7.0 |    46.7 |    61.2 |          65.7 |        54.5 |         28.6 |         42.9 |           28.6 |           8.3 |
| ('rapidocr', 'pre_post', 'tilted')       |      7.0 |    46.7 |    61.2 |          65.7 |        54.5 |         28.6 |         42.9 |           28.6 |           8.3 |
| ('rapidocr', 'pre_post', 'faded')        |      7.0 |    45.5 |    74.4 |          48.6 |        18.2 |         28.6 |         42.9 |           14.3 |           9.0 |
| ('rapidocr', 'pre_post', 'perspective')  |      7.0 |    45.5 |    74.4 |          48.6 |        18.2 |         28.6 |         42.9 |           14.3 |           9.0 |
| ('hybrid', 'baseline', 'sideways')       |     16.0 |    78.0 |    86.6 |          15.7 |         0.0 |         62.5 |         62.5 |            0.0 |           7.7 |
| ('hybrid', 'baseline', 'crumpled')       |     15.0 |    70.1 |    80.4 |          29.3 |         0.0 |         20.0 |         40.0 |            0.0 |          10.8 |
| ('hybrid', 'baseline', 'handheld')       |      6.0 |    62.5 |    73.4 |          16.7 |         0.0 |         50.0 |         50.0 |            0.0 |           8.7 |
| ('hybrid', 'baseline', 'clean')          |     15.0 |     5.9 |    19.6 |          76.7 |        82.8 |         46.7 |         60.0 |           66.7 |          14.4 |
| ('hybrid', 'baseline', 'partial')        |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           7.2 |
| ('hybrid', 'baseline', 'synthetic')      |     14.0 |    76.8 |    85.9 |          28.6 |        10.0 |         28.6 |         42.9 |            7.1 |          11.3 |
| ('hybrid', 'baseline', 'shadow')         |      7.0 |    62.9 |    76.0 |          40.0 |        16.7 |         28.6 |         42.9 |           14.3 |          12.0 |
| ('hybrid', 'baseline', 'tilted')         |      7.0 |    62.9 |    76.0 |          40.0 |        16.7 |         28.6 |         42.9 |           14.3 |          12.0 |
| ('hybrid', 'baseline', 'faded')          |      7.0 |    90.7 |    95.7 |          17.1 |         0.0 |         28.6 |         42.9 |            0.0 |          10.6 |
| ('hybrid', 'baseline', 'perspective')    |      7.0 |    90.7 |    95.7 |          17.1 |         0.0 |         28.6 |         42.9 |            0.0 |          10.6 |
| ('hybrid', 'pre', 'sideways')            |     16.0 |    26.8 |    47.9 |          47.9 |        50.0 |         62.5 |         62.5 |           28.6 |          10.1 |
| ('hybrid', 'pre', 'crumpled')            |     15.0 |    34.6 |    56.5 |          39.3 |        24.0 |         20.0 |         40.0 |           20.0 |          13.3 |
| ('hybrid', 'pre', 'handheld')            |      6.0 |    44.3 |    66.8 |          23.3 |        22.2 |         50.0 |         50.0 |            0.0 |          11.9 |
| ('hybrid', 'pre', 'clean')               |     15.0 |     9.9 |    25.4 |          66.7 |        86.7 |         46.7 |         60.0 |           60.0 |          14.2 |
| ('hybrid', 'pre', 'partial')             |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           7.1 |
| ('hybrid', 'pre', 'synthetic')           |     14.0 |    46.7 |    70.8 |          25.7 |        18.2 |         28.6 |         42.9 |            0.0 |          13.4 |
| ('hybrid', 'pre', 'shadow')              |      7.0 |    47.1 |    63.3 |          28.6 |        18.2 |         28.6 |         42.9 |            0.0 |          12.3 |
| ('hybrid', 'pre', 'tilted')              |      7.0 |    47.1 |    63.3 |          28.6 |        18.2 |         28.6 |         42.9 |            0.0 |          12.3 |
| ('hybrid', 'pre', 'faded')               |      7.0 |    46.2 |    78.4 |          22.9 |        18.2 |         28.6 |         42.9 |            0.0 |          14.5 |
| ('hybrid', 'pre', 'perspective')         |      7.0 |    46.2 |    78.4 |          22.9 |        18.2 |         28.6 |         42.9 |            0.0 |          14.5 |
| ('hybrid', 'pre_post', 'sideways')       |     16.0 |    26.3 |    45.4 |          77.1 |        58.3 |         62.5 |         62.5 |           35.7 |          10.0 |
| ('hybrid', 'pre_post', 'crumpled')       |     15.0 |    34.1 |    53.6 |          66.0 |        40.0 |         20.0 |         40.0 |           46.7 |          12.9 |
| ('hybrid', 'pre_post', 'handheld')       |      6.0 |    43.9 |    64.3 |          53.3 |        44.4 |         50.0 |         50.0 |           16.7 |          11.3 |
| ('hybrid', 'pre_post', 'clean')          |     15.0 |     9.6 |    23.0 |          88.0 |        93.3 |         46.7 |         60.0 |           66.7 |          13.4 |
| ('hybrid', 'pre_post', 'partial')        |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           5.9 |
| ('hybrid', 'pre_post', 'synthetic')      |     14.0 |    46.1 |    67.8 |          59.3 |        36.4 |         28.6 |         42.9 |           21.4 |          13.4 |
| ('hybrid', 'pre_post', 'shadow')         |      7.0 |    46.7 |    61.2 |          67.1 |        54.5 |         28.6 |         42.9 |           28.6 |          12.2 |
| ('hybrid', 'pre_post', 'tilted')         |      7.0 |    46.7 |    61.2 |          67.1 |        54.5 |         28.6 |         42.9 |           28.6 |          12.2 |
| ('hybrid', 'pre_post', 'faded')          |      7.0 |    45.5 |    74.4 |          51.4 |        18.2 |         28.6 |         42.9 |           14.3 |          14.5 |
| ('hybrid', 'pre_post', 'perspective')    |      7.0 |    45.5 |    74.4 |          51.4 |        18.2 |         28.6 |         42.9 |           14.3 |          14.5 |


## By language

|                                      |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:-------------------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('tesseract', 'baseline', 'uz_latn') |     51.0 |    93.4 |    96.5 |           3.6 |         0.0 |         45.1 |         56.9 |            0.0 |           7.6 |
| ('tesseract', 'baseline', 'mixed')   |      2.0 |   nan   |   nan   |          40.0 |         0.0 |        100.0 |        100.0 |            0.0 |           1.7 |
| ('tesseract', 'pre', 'uz_latn')      |     51.0 |    45.4 |    81.3 |          16.9 |         0.0 |         45.1 |         56.9 |            0.0 |           8.8 |
| ('tesseract', 'pre', 'mixed')        |      2.0 |   nan   |   nan   |          50.0 |       100.0 |        100.0 |        100.0 |          100.0 |           1.4 |
| ('tesseract', 'pre_post', 'uz_latn') |     51.0 |    45.1 |    80.3 |          51.1 |         6.5 |         45.1 |         56.9 |            2.8 |           8.8 |
| ('tesseract', 'pre_post', 'mixed')   |      2.0 |   nan   |   nan   |          70.0 |       100.0 |        100.0 |        100.0 |          100.0 |           1.5 |
| ('easyocr', 'baseline', 'uz_latn')   |     51.0 |    73.1 |    95.4 |          19.4 |         0.0 |         45.1 |         56.9 |            0.0 |          36.7 |
| ('easyocr', 'baseline', 'mixed')     |      2.0 |   nan   |   nan   |          40.0 |         0.0 |        100.0 |        100.0 |            0.0 |          17.9 |
| ('easyocr', 'pre', 'uz_latn')        |     51.0 |    41.8 |    82.3 |          24.4 |         0.0 |         45.1 |         56.9 |            2.8 |          19.4 |
| ('easyocr', 'pre', 'mixed')          |      2.0 |   nan   |   nan   |          50.0 |         0.0 |        100.0 |        100.0 |            0.0 |          10.0 |
| ('easyocr', 'pre_post', 'uz_latn')   |     51.0 |    41.0 |    78.3 |          50.8 |         0.0 |         45.1 |         56.9 |            0.0 |          18.7 |
| ('easyocr', 'pre_post', 'mixed')     |      2.0 |   nan   |   nan   |          70.0 |         0.0 |        100.0 |        100.0 |            0.0 |           9.9 |
| ('rapidocr', 'baseline', 'uz_latn')  |     51.0 |    62.1 |    72.3 |          48.6 |        39.3 |         45.1 |         56.9 |           30.6 |           9.1 |
| ('rapidocr', 'baseline', 'mixed')    |      2.0 |   nan   |   nan   |          50.0 |       100.0 |        100.0 |        100.0 |            0.0 |           1.5 |
| ('rapidocr', 'pre', 'uz_latn')       |     51.0 |    28.2 |    48.6 |          51.7 |        57.6 |         45.1 |         56.9 |           38.9 |           8.4 |
| ('rapidocr', 'pre', 'mixed')         |      2.0 |   nan   |   nan   |          60.0 |       100.0 |        100.0 |        100.0 |            0.0 |           1.4 |
| ('rapidocr', 'pre_post', 'uz_latn')  |     51.0 |    27.8 |    46.0 |          77.2 |        69.7 |         45.1 |         56.9 |           55.6 |           8.2 |
| ('rapidocr', 'pre_post', 'mixed')    |      2.0 |   nan   |   nan   |          80.0 |       100.0 |        100.0 |        100.0 |            0.0 |           1.4 |
| ('hybrid', 'baseline', 'uz_latn')    |     51.0 |    62.1 |    72.3 |          48.6 |        39.3 |         45.1 |         56.9 |           30.6 |          11.1 |
| ('hybrid', 'baseline', 'mixed')      |      2.0 |   nan   |   nan   |          50.0 |       100.0 |        100.0 |        100.0 |            0.0 |           3.0 |
| ('hybrid', 'pre', 'uz_latn')         |     51.0 |    28.2 |    48.6 |          52.2 |        57.6 |         45.1 |         56.9 |           36.1 |          12.0 |
| ('hybrid', 'pre', 'mixed')           |      2.0 |   nan   |   nan   |          60.0 |       100.0 |        100.0 |        100.0 |            0.0 |           2.7 |
| ('hybrid', 'pre_post', 'uz_latn')    |     51.0 |    27.8 |    46.0 |          78.1 |        69.7 |         45.1 |         56.9 |           52.8 |          11.3 |
| ('hybrid', 'pre_post', 'mixed')      |      2.0 |   nan   |   nan   |          80.0 |       100.0 |        100.0 |        100.0 |            0.0 |           2.7 |


## QR decoded per photo and per receipt

|                           |   whole photo % |   QR close-up % |   per receipt (any real photo) % |
|:--------------------------|----------------:|----------------:|---------------------------------:|
| ('tesseract', 'baseline') |            60.9 |            68.8 |                             81.2 |
| ('tesseract', 'pre')      |            60.9 |            68.8 |                             81.2 |
| ('tesseract', 'pre_post') |            60.9 |            68.8 |                             81.2 |
| ('easyocr', 'baseline')   |            60.9 |            68.8 |                             81.2 |
| ('easyocr', 'pre')        |            60.9 |            68.8 |                             81.2 |
| ('easyocr', 'pre_post')   |            60.9 |            68.8 |                             81.2 |
| ('rapidocr', 'baseline')  |            60.9 |            68.8 |                             81.2 |
| ('rapidocr', 'pre')       |            60.9 |            68.8 |                             81.2 |
| ('rapidocr', 'pre_post')  |            60.9 |            68.8 |                             81.2 |
| ('hybrid', 'baseline')    |            60.9 |            68.8 |                             81.2 |
| ('hybrid', 'pre')         |            60.9 |            68.8 |                             81.2 |
| ('hybrid', 'pre_post')    |            60.9 |            68.8 |                             81.2 |


## 95 % confidence intervals (bootstrap over receipts, real whole-receipt photos, pre + post)

| engine    |   receipts | field acc %      | item F1 %         | consistent %     | CER %            | WER %            |
|:----------|-----------:|:-----------------|:------------------|:-----------------|:-----------------|:-----------------|
| tesseract |         16 | 60.9 [50.0–71.0] | 15.0 [0.0–33.3]   | 4.3 [0.0–15.0]   | 33.3 [20.1–52.3] | 69.2 [53.9–90.5] |
| easyocr   |         16 | 63.0 [53.9–71.7] | 0.0 [0.0–0.0]     | 0.0 [0.0–0.0]    | 20.6 [15.1–28.3] | 65.9 [57.9–75.1] |
| rapidocr  |         16 | 89.6 [82.9–95.0] | 87.0 [72.7–100.0] | 73.9 [55.0–90.5] | 9.4 [4.5–16.0]   | 24.3 [18.0–31.8] |
| hybrid    |         16 | 89.6 [83.2–95.0] | 87.0 [73.9–100.0] | 69.6 [50.0–84.6] | 9.4 [4.3–16.0]   | 24.3 [17.6–32.4] |


## Per seller (real whole-receipt photos, pre + post)

|                                   |   photos |   field acc % |   item F1 % |   consistent % |   CER % |   WER % |
|:----------------------------------|---------:|--------------:|------------:|---------------:|--------:|--------:|
| ('tesseract', 'era_barkamol')     |     21.0 |          59.5 |        10.8 |            0.0 |    33.3 |    69.2 |
| ('tesseract', 'diyor_neft')       |      1.0 |          70.0 |       100.0 |          100.0 |   nan   |   nan   |
| ('tesseract', 'era_avtomobilist') |      1.0 |          80.0 |         0.0 |            0.0 |   nan   |   nan   |
| ('easyocr', 'era_barkamol')       |     21.0 |          62.4 |         0.0 |            0.0 |    20.6 |    65.9 |
| ('easyocr', 'diyor_neft')         |      1.0 |          70.0 |         0.0 |            0.0 |   nan   |   nan   |
| ('easyocr', 'era_avtomobilist')   |      1.0 |          70.0 |         0.0 |            0.0 |   nan   |   nan   |
| ('rapidocr', 'era_barkamol')      |     21.0 |          89.5 |        85.7 |           76.2 |     9.4 |    24.3 |
| ('rapidocr', 'diyor_neft')        |      1.0 |          80.0 |       100.0 |            0.0 |   nan   |   nan   |
| ('rapidocr', 'era_avtomobilist')  |      1.0 |         100.0 |       100.0 |          100.0 |   nan   |   nan   |
| ('hybrid', 'era_barkamol')        |     21.0 |          89.5 |        85.7 |           71.4 |     9.4 |    24.3 |
| ('hybrid', 'diyor_neft')          |      1.0 |          80.0 |       100.0 |            0.0 |   nan   |   nan   |
| ('hybrid', 'era_avtomobilist')    |      1.0 |         100.0 |       100.0 |          100.0 |   nan   |   nan   |


## Error causes (pre_post)

|                                                 |   count |
|:------------------------------------------------|--------:|
| ('easyocr', 'apostrophe')                       |       2 |
| ('easyocr', 'date/time misread')                |       6 |
| ('easyocr', 'digits misread')                   |      10 |
| ('easyocr', 'digits missing/extra')             |       4 |
| ('easyocr', 'digits/amounts misread')           |       9 |
| ('easyocr', 'not found')                        |      78 |
| ('easyocr', 'text misread / wrong span')        |      63 |
| ('easyocr', 'wrong line picked (value of vat)') |       8 |
| ('hybrid', 'date/time misread')                 |       3 |
| ('hybrid', 'digits misread')                    |       4 |
| ('hybrid', 'digits missing/extra')              |       5 |
| ('hybrid', 'digits/amounts misread')            |       1 |
| ('hybrid', 'not found')                         |      45 |
| ('hybrid', 'text misread / wrong span')         |      23 |
| ('rapidocr', 'date/time misread')               |       3 |
| ('rapidocr', 'digits misread')                  |       4 |
| ('rapidocr', 'digits missing/extra')            |       4 |
| ('rapidocr', 'digits/amounts misread')          |       1 |
| ('rapidocr', 'not found')                       |      50 |
| ('rapidocr', 'text misread / wrong span')       |      22 |
| ('tesseract', 'date/time misread')              |       6 |
| ('tesseract', 'digits misread')                 |       6 |
| ('tesseract', 'digits missing/extra')           |       3 |
| ('tesseract', 'digits/amounts misread')         |       9 |
| ('tesseract', 'not found')                      |      96 |
| ('tesseract', 'text misread / wrong span')      |      59 |


## Error examples

| image     | config   | engine    | conditions        | field          | gt                                                                             | pred                                                                                                                                                     | cause                     |
|:----------|:---------|:----------|:------------------|:---------------|:-------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------|
| r02_a.jpg | pre_post | tesseract | sideways;crumpled | seller_name    | ERA                                                                            | ANVARDON м. 7 OILMUROO OʻG /                                                                                                                             | text misread / wrong span |
| r02_a.jpg | pre_post | tesseract | sideways;crumpled | seller_tin     | 31802964140017                                                                 |                                                                                                                                                          | not found                 |
| r02_a.jpg | pre_post | tesseract | sideways;crumpled | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | Fargʻona viloyati, Fargʻona shahri;, Barkamol MFY, Yangi asr, koʻchasi./118 b uy                                                                         | text misread / wrong span |
| r03_a.jpg | pre_post | tesseract | sideways;crumpled | seller_name    | ERA                                                                            | м ANVARION MAXMUDOV DILMUROD OʻGʻRI                                                                                                                      | text misread / wrong span |
| r03_a.jpg | pre_post | tesseract | sideways;crumpled | seller_tin     | 31802964140017                                                                 |                                                                                                                                                          | not found                 |
| r03_a.jpg | pre_post | tesseract | sideways;crumpled | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | Fargʻona viloyati, Его ʼопа shahri, Barkamol MFY, Yangi asr, ʻ М, A ko! jasi. 118 b uy                                                                   | text misread / wrong span |
| r03_a.jpg | pre_post | tesseract | sideways;crumpled | datetime       | 2026-11-08T11:02:29                                                            | 2026-11-08T11:02:23                                                                                                                                      | date/time misread         |
| r03_a.jpg | pre_post | tesseract | sideways;crumpled | receipt_number | 12077                                                                          | 12877                                                                                                                                                    | digits misread            |
| r03_a.jpg | pre_post | tesseract | sideways;crumpled | fiscal_module  | LG420211609580                                                                 |                                                                                                                                                          | not found                 |
| r03_a.jpg | pre_post | tesseract | sideways;crumpled | fiscal_sign    | 514092944266                                                                   | 5149929442665                                                                                                                                            | digits missing/extra      |
| r03_a.jpg | pre_post | tesseract | sideways;crumpled | vat            | 0.0                                                                            | 69.0                                                                                                                                                     | digits/amounts misread    |
| r03_a.jpg | pre_post | tesseract | sideways;crumpled | total          | 21000.0                                                                        | 21099.09                                                                                                                                                 | digits/amounts misread    |
| r03_a.jpg | pre_post | tesseract | sideways;crumpled | payment        | card                                                                           |                                                                                                                                                          | not found                 |
| r11_a.jpg | pre_post | tesseract | sideways;crumpled | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | Fargʻona viloyati, Fargʻona shahri, Barkamol MFY, Yarigl asr, <., koʻchasi, 118 b uy                                                                     | text misread / wrong span |
| r11_a.jpg | pre_post | tesseract | sideways;crumpled | datetime       | 2026-11-03T17:12:38                                                            |                                                                                                                                                          | not found                 |
| r11_a.jpg | pre_post | tesseract | sideways;crumpled | fiscal_module  | LG420211609580                                                                 |                                                                                                                                                          | not found                 |
| r13_a.jpg | pre_post | tesseract | handheld;crumpled | seller_name    | ERA                                                                            | ERA !                                                                                                                                                    | text misread / wrong span |
| r13_a.jpg | pre_post | tesseract | handheld;crumpled | seller_tin     | 31802964140017                                                                 |                                                                                                                                                          | not found                 |
| r13_a.jpg | pre_post | tesseract | handheld;crumpled | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | farq, ral, Barkamol, koʻch, \ Yur. Май?, Fargʻ, QL                                                                                                       | text misread / wrong span |
| r13_a.jpg | pre_post | tesseract | handheld;crumpled | datetime       | 2026-10-31T18:34:21                                                            |                                                                                                                                                          | not found                 |
| r13_a.jpg | pre_post | tesseract | handheld;crumpled | receipt_number | 11814                                                                          |                                                                                                                                                          | not found                 |
| r13_a.jpg | pre_post | tesseract | handheld;crumpled | fiscal_module  | LG420211609580                                                                 |                                                                                                                                                          | not found                 |
| r13_a.jpg | pre_post | tesseract | handheld;crumpled | vat            | 0.0                                                                            |                                                                                                                                                          | not found                 |
| r13_a.jpg | pre_post | tesseract | handheld;crumpled | total          | 19800.0                                                                        |                                                                                                                                                          | not found                 |
| r17_a.jpg | pre_post | tesseract | clean             | seller_name    | ERA                                                                            | ANVARJON MAXMUDOV DILMUROD OʻGʻLI                                                                                                                        | text misread / wrong span |
| r17_a.jpg | pre_post | tesseract | clean             | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | Fargʻona viloyati, Fargʻona shahri, Barkamol MFY, Yangi asr, koʻchasi, 118 b цу                                                                          | text misread / wrong span |
| r18_a.jpg | pre_post | tesseract | crumpled          | seller_name    | ERA                                                                            | ANVARSON MAXMUDOV DILMUROD OʻGʻLI т                                                                                                                      | text misread / wrong span |
| r18_a.jpg | pre_post | tesseract | crumpled          | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | Fargʻona viloyati. >, Fargʻona shahri., Barkamol МЕРУ. Yangi asr, koʻchasi, 118 b uy                                                                     | text misread / wrong span |
| r02_c.jpg | pre_post | tesseract | sideways          | seller_tin     | 31802964140017                                                                 |                                                                                                                                                          | not found                 |
| r02_c.jpg | pre_post | tesseract | sideways          | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | Fargʻona viloyati, Fargʻona shahri, Barkeral KFY VYargi asr, koʻchasi, 118 b uy, tur Manzil, Fargʻona viloyati, Fargʻona shahri, Barkamol FRY, Yangi asi | text misread / wrong span |
| r02_c.jpg | pre_post | tesseract | sideways          | vat            | 0.0                                                                            | 6.68                                                                                                                                                     | digits/amounts misread    |
| r03_c.jpg | pre_post | tesseract | sideways          | seller_name    | ERA                                                                            | ЕВА:                                                                                                                                                     | text misread / wrong span |
| r03_c.jpg | pre_post | tesseract | sideways          | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | Fargʻona viloyati, Fargʻona shahri, Barkamol MFY, Yangi asi, koʻchasi, 118 b uy                                                                          | text misread / wrong span |
| r03_c.jpg | pre_post | tesseract | sideways          | payment        | card                                                                           | other                                                                                                                                                    | text misread / wrong span |
| r11_c.jpg | pre_post | tesseract | clean             | seller_name    | ERA                                                                            | = Barkamol MEY, Yarigi |                                                                                                                                 | text misread / wrong span |
| r11_c.jpg | pre_post | tesseract | clean             | seller_tin     | 31802964140017                                                                 |                                                                                                                                                          | not found                 |
| r11_c.jpg | pre_post | tesseract | clean             | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | Yur. Нан: | koʻchasi, 118 b, == Fargʻona viloyat                                                                                                         | text misread / wrong span |
| r11_c.jpg | pre_post | tesseract | clean             | total          | 20000.0                                                                        | 20600.0                                                                                                                                                  | digits/amounts misread    |
| r13_c.jpg | pre_post | tesseract | clean             | seller_name    | ERA                                                                            | ROD OʻG on                                                                                                                                               | text misread / wrong span |
| r13_c.jpg | pre_post | tesseract | clean             | seller_tin     | 31802964140017                                                                 |                                                                                                                                                          | not found                 |