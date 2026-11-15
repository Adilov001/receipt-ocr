# Results (test split, 53 images, 16 receipts, 3 sellers)

## Engines × configurations

|                           |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:--------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('tesseract', 'baseline') |     53.0 |    93.3 |    96.2 |           4.6 |         0.0 |         47.2 |         58.5 |            0.0 |           7.1 |
| ('tesseract', 'pre')      |     53.0 |    45.3 |    79.1 |          17.3 |         3.1 |         47.2 |         58.5 |            2.7 |           8.2 |
| ('tesseract', 'pre_post') |     53.0 |    45.3 |    79.1 |          50.5 |         9.4 |         47.2 |         58.5 |            5.4 |           8.2 |
| ('easyocr', 'baseline')   |     53.0 |    72.9 |    93.8 |          18.9 |         0.0 |         47.2 |         58.5 |            0.0 |          33.9 |
| ('easyocr', 'pre')        |     53.0 |    42.8 |    80.2 |          24.9 |         0.0 |         47.2 |         58.5 |            2.7 |          18.4 |
| ('easyocr', 'pre_post')   |     53.0 |    42.8 |    80.2 |          47.8 |         0.0 |         47.2 |         58.5 |            0.0 |          16.4 |
| ('rapidocr', 'baseline')  |     53.0 |    63.1 |    77.2 |          45.4 |        26.1 |         47.2 |         58.5 |           21.6 |           7.3 |
| ('rapidocr', 'pre')       |     53.0 |    33.7 |    61.3 |          48.4 |        45.7 |         47.2 |         58.5 |           37.8 |           7.6 |
| ('rapidocr', 'pre_post')  |     53.0 |    33.7 |    61.3 |          70.5 |        65.7 |         47.2 |         58.5 |           48.6 |           8.0 |
| ('hybrid', 'baseline')    |     53.0 |    63.1 |    77.2 |          45.4 |        26.1 |         47.2 |         58.5 |           21.6 |           9.4 |
| ('hybrid', 'pre')         |     53.0 |    33.7 |    61.3 |          48.9 |        45.7 |         47.2 |         58.5 |           37.8 |          10.5 |
| ('hybrid', 'pre_post')    |     53.0 |    33.7 |    61.3 |          71.4 |        65.7 |         47.2 |         58.5 |           48.6 |          10.3 |


## Field accuracy, %

|                           |   seller_name |   seller_tin |   address |   datetime |   receipt_number |   fiscal_module |   fiscal_sign |   vat |   total |   payment |
|:--------------------------|--------------:|-------------:|----------:|-----------:|-----------------:|----------------:|--------------:|------:|--------:|----------:|
| ('tesseract', 'baseline') |           0.0 |          2.7 |       0.0 |        2.7 |              8.1 |             0.0 |           2.7 |   2.7 |    10.8 |      16.2 |
| ('tesseract', 'pre')      |           0.0 |         29.7 |       5.4 |       24.3 |             43.2 |             0.0 |          16.2 |   5.4 |    10.8 |      37.8 |
| ('tesseract', 'pre_post') |          29.7 |         29.7 |       5.4 |       64.9 |             73.0 |            54.1 |          64.9 |  56.8 |    54.1 |      73.0 |
| ('easyocr', 'baseline')   |           0.0 |         24.3 |       0.0 |        0.0 |             32.4 |            10.8 |          27.0 |  27.0 |    29.7 |      37.8 |
| ('easyocr', 'pre')        |           0.0 |         48.6 |       0.0 |        5.4 |             45.9 |            27.0 |          24.3 |  32.4 |    16.2 |      48.6 |
| ('easyocr', 'pre_post')   |          21.6 |         48.6 |       0.0 |       62.2 |             73.0 |            64.9 |          62.2 |  56.8 |    40.5 |      48.6 |
| ('rapidocr', 'baseline')  |           0.0 |         45.9 |      21.6 |       64.9 |             48.6 |            75.7 |          40.5 |  43.2 |    62.2 |      51.4 |
| ('rapidocr', 'pre')       |           0.0 |         56.8 |      21.6 |       56.8 |             70.3 |            59.5 |          45.9 |  35.1 |    67.6 |      70.3 |
| ('rapidocr', 'pre_post')  |          78.4 |         56.8 |      21.6 |       81.1 |             83.8 |            78.4 |          73.0 |  70.3 |    83.8 |      78.4 |
| ('hybrid', 'baseline')    |           0.0 |         45.9 |      21.6 |       64.9 |             48.6 |            75.7 |          40.5 |  43.2 |    62.2 |      51.4 |
| ('hybrid', 'pre')         |           0.0 |         56.8 |      21.6 |       56.8 |             73.0 |            59.5 |          45.9 |  35.1 |    67.6 |      73.0 |
| ('hybrid', 'pre_post')    |          78.4 |         56.8 |      21.6 |       81.1 |             83.8 |            78.4 |          73.0 |  73.0 |    86.5 |      81.1 |


## By shooting condition

|                                          |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:-----------------------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('tesseract', 'baseline', 'sideways')    |     16.0 |    99.4 |    99.9 |           0.0 |         0.0 |         62.5 |         62.5 |            0.0 |           4.1 |
| ('tesseract', 'baseline', 'crumpled')    |     15.0 |    97.4 |    98.7 |           0.0 |         0.0 |         20.0 |         40.0 |            0.0 |           6.4 |
| ('tesseract', 'baseline', 'handheld')    |      6.0 |    96.3 |    97.5 |           0.0 |         0.0 |         50.0 |         50.0 |            0.0 |           4.8 |
| ('tesseract', 'baseline', 'clean')       |     15.0 |    66.0 |    80.2 |          10.7 |         0.0 |         46.7 |         60.0 |            0.0 |           9.2 |
| ('tesseract', 'baseline', 'partial')     |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           5.7 |
| ('tesseract', 'baseline', 'synthetic')   |     14.0 |    97.8 |    98.8 |           0.7 |         0.0 |         28.6 |         42.9 |            0.0 |           7.3 |
| ('tesseract', 'baseline', 'shadow')      |      7.0 |    97.7 |    98.5 |           0.0 |         0.0 |         28.6 |         42.9 |            0.0 |           7.5 |
| ('tesseract', 'baseline', 'tilted')      |      7.0 |    97.7 |    98.5 |           0.0 |         0.0 |         28.6 |         42.9 |            0.0 |           7.5 |
| ('tesseract', 'baseline', 'faded')       |      7.0 |    97.8 |    99.2 |           1.4 |         0.0 |         28.6 |         42.9 |            0.0 |           7.2 |
| ('tesseract', 'baseline', 'perspective') |      7.0 |    97.8 |    99.2 |           1.4 |         0.0 |         28.6 |         42.9 |            0.0 |           7.2 |
| ('tesseract', 'pre', 'sideways')         |     16.0 |    38.9 |    71.6 |          14.3 |         0.0 |         62.5 |         62.5 |            0.0 |           6.6 |
| ('tesseract', 'pre', 'crumpled')         |     15.0 |    48.5 |    82.2 |          12.7 |         0.0 |         20.0 |         40.0 |            0.0 |           9.1 |
| ('tesseract', 'pre', 'handheld')         |      6.0 |    59.7 |    96.9 |           6.7 |         0.0 |         50.0 |         50.0 |            0.0 |           8.2 |
| ('tesseract', 'pre', 'clean')            |     15.0 |    46.9 |    80.9 |          21.3 |         8.3 |         46.7 |         60.0 |            6.7 |           9.9 |
| ('tesseract', 'pre', 'partial')          |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           5.7 |
| ('tesseract', 'pre', 'synthetic')        |     14.0 |    57.2 |    90.5 |          12.1 |         0.0 |         28.6 |         42.9 |            0.0 |           9.5 |
| ('tesseract', 'pre', 'shadow')           |      7.0 |    56.2 |    78.8 |          11.4 |         0.0 |         28.6 |         42.9 |            0.0 |           8.7 |
| ('tesseract', 'pre', 'tilted')           |      7.0 |    56.2 |    78.8 |          11.4 |         0.0 |         28.6 |         42.9 |            0.0 |           8.7 |
| ('tesseract', 'pre', 'faded')            |      7.0 |    58.3 |   102.2 |          12.9 |         0.0 |         28.6 |         42.9 |            0.0 |          10.3 |
| ('tesseract', 'pre', 'perspective')      |      7.0 |    58.3 |   102.2 |          12.9 |         0.0 |         28.6 |         42.9 |            0.0 |          10.3 |
| ('tesseract', 'pre_post', 'sideways')    |     16.0 |    38.9 |    71.6 |          47.1 |         7.7 |         62.5 |         62.5 |            0.0 |           6.6 |
| ('tesseract', 'pre_post', 'crumpled')    |     15.0 |    48.5 |    82.2 |          36.0 |         0.0 |         20.0 |         40.0 |            0.0 |           9.1 |
| ('tesseract', 'pre_post', 'handheld')    |      6.0 |    59.7 |    96.9 |          38.3 |        22.2 |         50.0 |         50.0 |            0.0 |           8.2 |
| ('tesseract', 'pre_post', 'clean')       |     15.0 |    46.9 |    80.9 |          60.7 |        16.7 |         46.7 |         60.0 |            6.7 |           9.8 |
| ('tesseract', 'pre_post', 'partial')     |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           5.6 |
| ('tesseract', 'pre_post', 'synthetic')   |     14.0 |    57.2 |    90.5 |          35.0 |         0.0 |         28.6 |         42.9 |            7.1 |           9.5 |
| ('tesseract', 'pre_post', 'shadow')      |      7.0 |    56.2 |    78.8 |          34.3 |         0.0 |         28.6 |         42.9 |           14.3 |           8.7 |
| ('tesseract', 'pre_post', 'tilted')      |      7.0 |    56.2 |    78.8 |          34.3 |         0.0 |         28.6 |         42.9 |           14.3 |           8.7 |
| ('tesseract', 'pre_post', 'faded')       |      7.0 |    58.3 |   102.2 |          35.7 |         0.0 |         28.6 |         42.9 |            0.0 |          10.4 |
| ('tesseract', 'pre_post', 'perspective') |      7.0 |    58.3 |   102.2 |          35.7 |         0.0 |         28.6 |         42.9 |            0.0 |          10.4 |
| ('easyocr', 'baseline', 'sideways')      |     16.0 |    88.7 |   101.7 |           0.0 |         0.0 |         62.5 |         62.5 |            0.0 |          39.8 |
| ('easyocr', 'baseline', 'crumpled')      |     15.0 |    80.3 |    98.8 |           4.7 |         0.0 |         20.0 |         40.0 |            0.0 |          47.3 |
| ('easyocr', 'baseline', 'handheld')      |      6.0 |    73.2 |    92.6 |           6.7 |         0.0 |         50.0 |         50.0 |            0.0 |          42.9 |
| ('easyocr', 'baseline', 'clean')         |     15.0 |    16.6 |    65.6 |          40.0 |         0.0 |         46.7 |         60.0 |            0.0 |          42.7 |
| ('easyocr', 'baseline', 'partial')       |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           8.6 |
| ('easyocr', 'baseline', 'synthetic')     |     14.0 |    85.2 |   100.5 |           5.0 |         0.0 |         28.6 |         42.9 |            0.0 |          45.4 |
| ('easyocr', 'baseline', 'shadow')        |      7.0 |    76.9 |   102.5 |           2.9 |         0.0 |         28.6 |         42.9 |            0.0 |          47.4 |
| ('easyocr', 'baseline', 'tilted')        |      7.0 |    76.9 |   102.5 |           2.9 |         0.0 |         28.6 |         42.9 |            0.0 |          47.4 |
| ('easyocr', 'baseline', 'faded')         |      7.0 |    93.5 |    98.5 |           7.1 |         0.0 |         28.6 |         42.9 |            0.0 |          43.4 |
| ('easyocr', 'baseline', 'perspective')   |      7.0 |    93.5 |    98.5 |           7.1 |         0.0 |         28.6 |         42.9 |            0.0 |          43.4 |
| ('easyocr', 'pre', 'sideways')           |     16.0 |    40.2 |    78.6 |          21.4 |         0.0 |         62.5 |         62.5 |            7.1 |          17.0 |
| ('easyocr', 'pre', 'crumpled')           |     15.0 |    46.8 |    81.3 |          16.0 |         0.0 |         20.0 |         40.0 |            6.7 |          21.7 |
| ('easyocr', 'pre', 'handheld')           |      6.0 |    55.8 |    87.2 |          10.0 |         0.0 |         50.0 |         50.0 |            0.0 |          18.5 |
| ('easyocr', 'pre', 'clean')              |     15.0 |    36.0 |    79.6 |          34.0 |         0.0 |         46.7 |         60.0 |            0.0 |          24.6 |
| ('easyocr', 'pre', 'partial')            |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           8.4 |
| ('easyocr', 'pre', 'synthetic')          |     14.0 |    62.1 |    91.1 |          10.7 |         0.0 |         28.6 |         42.9 |            0.0 |          22.5 |
| ('easyocr', 'pre', 'shadow')             |      7.0 |    52.6 |    85.3 |          15.7 |         0.0 |         28.6 |         42.9 |            0.0 |          25.4 |
| ('easyocr', 'pre', 'tilted')             |      7.0 |    52.6 |    85.3 |          15.7 |         0.0 |         28.6 |         42.9 |            0.0 |          25.4 |
| ('easyocr', 'pre', 'faded')              |      7.0 |    71.5 |    96.9 |           5.7 |         0.0 |         28.6 |         42.9 |            0.0 |          19.6 |
| ('easyocr', 'pre', 'perspective')        |      7.0 |    71.5 |    96.9 |           5.7 |         0.0 |         28.6 |         42.9 |            0.0 |          19.6 |
| ('easyocr', 'pre_post', 'sideways')      |     16.0 |    40.2 |    78.6 |          45.7 |         0.0 |         62.5 |         62.5 |            0.0 |          16.3 |
| ('easyocr', 'pre_post', 'crumpled')      |     15.0 |    46.8 |    81.3 |          34.0 |         0.0 |         20.0 |         40.0 |            0.0 |          20.6 |
| ('easyocr', 'pre_post', 'handheld')      |      6.0 |    55.8 |    87.2 |          30.0 |         0.0 |         50.0 |         50.0 |            0.0 |          17.6 |
| ('easyocr', 'pre_post', 'clean')         |     15.0 |    36.0 |    79.6 |          58.7 |         0.0 |         46.7 |         60.0 |            0.0 |          21.6 |
| ('easyocr', 'pre_post', 'partial')       |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           5.6 |
| ('easyocr', 'pre_post', 'synthetic')     |     14.0 |    62.1 |    91.1 |          28.6 |         0.0 |         28.6 |         42.9 |            0.0 |          22.5 |
| ('easyocr', 'pre_post', 'shadow')        |      7.0 |    52.7 |    85.3 |          34.3 |         0.0 |         28.6 |         42.9 |            0.0 |          25.4 |
| ('easyocr', 'pre_post', 'tilted')        |      7.0 |    52.7 |    85.3 |          34.3 |         0.0 |         28.6 |         42.9 |            0.0 |          25.4 |
| ('easyocr', 'pre_post', 'faded')         |      7.0 |    71.6 |    96.9 |          22.9 |         0.0 |         28.6 |         42.9 |            0.0 |          19.7 |
| ('easyocr', 'pre_post', 'perspective')   |      7.0 |    71.6 |    96.9 |          22.9 |         0.0 |         28.6 |         42.9 |            0.0 |          19.7 |
| ('rapidocr', 'baseline', 'sideways')     |     16.0 |    77.4 |    85.2 |          17.1 |         0.0 |         62.5 |         62.5 |            0.0 |           5.1 |
| ('rapidocr', 'baseline', 'crumpled')     |     15.0 |    71.5 |    83.2 |          27.3 |         7.1 |         20.0 |         40.0 |            6.7 |           7.2 |
| ('rapidocr', 'baseline', 'handheld')     |      6.0 |    64.8 |    80.8 |          28.3 |        20.0 |         50.0 |         50.0 |           16.7 |           5.7 |
| ('rapidocr', 'baseline', 'clean')        |     15.0 |     8.9 |    43.8 |          70.0 |        53.3 |         46.7 |         60.0 |           40.0 |           8.8 |
| ('rapidocr', 'baseline', 'partial')      |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           5.7 |
| ('rapidocr', 'baseline', 'synthetic')    |     14.0 |    78.4 |    88.5 |          25.7 |         8.3 |         28.6 |         42.9 |           14.3 |           7.9 |
| ('rapidocr', 'baseline', 'shadow')       |      7.0 |    65.3 |    80.8 |          31.4 |        14.3 |         28.6 |         42.9 |           28.6 |           8.1 |
| ('rapidocr', 'baseline', 'tilted')       |      7.0 |    65.3 |    80.8 |          31.4 |        14.3 |         28.6 |         42.9 |           28.6 |           8.1 |
| ('rapidocr', 'baseline', 'faded')        |      7.0 |    91.4 |    96.2 |          20.0 |         0.0 |         28.6 |         42.9 |            0.0 |           7.6 |
| ('rapidocr', 'baseline', 'perspective')  |      7.0 |    91.4 |    96.2 |          20.0 |         0.0 |         28.6 |         42.9 |            0.0 |           7.6 |
| ('rapidocr', 'pre', 'sideways')          |     16.0 |    30.4 |    58.7 |          46.4 |        58.3 |         62.5 |         62.5 |           21.4 |           5.2 |
| ('rapidocr', 'pre', 'crumpled')          |     15.0 |    37.0 |    64.4 |          36.7 |        38.5 |         20.0 |         40.0 |           13.3 |           7.3 |
| ('rapidocr', 'pre', 'handheld')          |      6.0 |    47.4 |    75.2 |          23.3 |         0.0 |         50.0 |         50.0 |            0.0 |           6.2 |
| ('rapidocr', 'pre', 'clean')             |     15.0 |    29.0 |    54.5 |          58.7 |        51.6 |         46.7 |         60.0 |           66.7 |           9.6 |
| ('rapidocr', 'pre', 'partial')           |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           5.7 |
| ('rapidocr', 'pre', 'synthetic')         |     14.0 |    50.5 |    76.6 |          26.4 |        27.3 |         28.6 |         42.9 |            7.1 |           8.3 |
| ('rapidocr', 'pre', 'shadow')            |      7.0 |    48.2 |    69.0 |          30.0 |        33.3 |         28.6 |         42.9 |            0.0 |           8.2 |
| ('rapidocr', 'pre', 'tilted')            |      7.0 |    48.2 |    69.0 |          30.0 |        33.3 |         28.6 |         42.9 |            0.0 |           8.2 |
| ('rapidocr', 'pre', 'faded')             |      7.0 |    52.9 |    84.2 |          22.9 |        20.0 |         28.6 |         42.9 |           14.3 |           8.4 |
| ('rapidocr', 'pre', 'perspective')       |      7.0 |    52.9 |    84.2 |          22.9 |        20.0 |         28.6 |         42.9 |           14.3 |           8.4 |
| ('rapidocr', 'pre_post', 'sideways')     |     16.0 |    30.4 |    58.7 |          68.6 |        66.7 |         62.5 |         62.5 |           28.6 |           5.6 |
| ('rapidocr', 'pre_post', 'crumpled')     |     15.0 |    37.0 |    64.4 |          57.3 |        53.8 |         20.0 |         40.0 |           33.3 |           7.8 |
| ('rapidocr', 'pre_post', 'handheld')     |      6.0 |    47.4 |    75.2 |          43.3 |        22.2 |         50.0 |         50.0 |           16.7 |           6.5 |
| ('rapidocr', 'pre_post', 'clean')        |     15.0 |    29.1 |    54.5 |          82.0 |        77.4 |         46.7 |         60.0 |           73.3 |           9.8 |
| ('rapidocr', 'pre_post', 'partial')      |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           6.0 |
| ('rapidocr', 'pre_post', 'synthetic')    |     14.0 |    50.5 |    76.6 |          50.7 |        36.4 |         28.6 |         42.9 |           21.4 |           9.2 |
| ('rapidocr', 'pre_post', 'shadow')       |      7.0 |    48.2 |    69.0 |          57.1 |        50.0 |         28.6 |         42.9 |           28.6 |           9.1 |
| ('rapidocr', 'pre_post', 'tilted')       |      7.0 |    48.2 |    69.0 |          57.1 |        50.0 |         28.6 |         42.9 |           28.6 |           9.1 |
| ('rapidocr', 'pre_post', 'faded')        |      7.0 |    52.9 |    84.2 |          44.3 |        20.0 |         28.6 |         42.9 |           14.3 |           9.3 |
| ('rapidocr', 'pre_post', 'perspective')  |      7.0 |    52.9 |    84.2 |          44.3 |        20.0 |         28.6 |         42.9 |           14.3 |           9.3 |
| ('hybrid', 'baseline', 'sideways')       |     16.0 |    77.4 |    85.2 |          17.1 |         0.0 |         62.5 |         62.5 |            0.0 |           6.7 |
| ('hybrid', 'baseline', 'crumpled')       |     15.0 |    71.5 |    83.2 |          27.3 |         7.1 |         20.0 |         40.0 |            6.7 |           9.3 |
| ('hybrid', 'baseline', 'handheld')       |      6.0 |    64.8 |    80.8 |          28.3 |        20.0 |         50.0 |         50.0 |           16.7 |           7.2 |
| ('hybrid', 'baseline', 'clean')          |     15.0 |     8.9 |    43.8 |          70.0 |        53.3 |         46.7 |         60.0 |           40.0 |          12.8 |
| ('hybrid', 'baseline', 'partial')        |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           6.0 |
| ('hybrid', 'baseline', 'synthetic')      |     14.0 |    78.4 |    88.5 |          25.7 |         8.3 |         28.6 |         42.9 |           14.3 |           9.7 |
| ('hybrid', 'baseline', 'shadow')         |      7.0 |    65.3 |    80.8 |          31.4 |        14.3 |         28.6 |         42.9 |           28.6 |          10.2 |
| ('hybrid', 'baseline', 'tilted')         |      7.0 |    65.3 |    80.8 |          31.4 |        14.3 |         28.6 |         42.9 |           28.6 |          10.2 |
| ('hybrid', 'baseline', 'faded')          |      7.0 |    91.4 |    96.2 |          20.0 |         0.0 |         28.6 |         42.9 |            0.0 |           9.2 |
| ('hybrid', 'baseline', 'perspective')    |      7.0 |    91.4 |    96.2 |          20.0 |         0.0 |         28.6 |         42.9 |            0.0 |           9.2 |
| ('hybrid', 'pre', 'sideways')            |     16.0 |    30.4 |    58.7 |          47.9 |        58.3 |         62.5 |         62.5 |           21.4 |           9.0 |
| ('hybrid', 'pre', 'crumpled')            |     15.0 |    37.0 |    64.4 |          37.3 |        38.5 |         20.0 |         40.0 |           20.0 |          11.6 |
| ('hybrid', 'pre', 'handheld')            |      6.0 |    47.4 |    75.2 |          25.0 |         0.0 |         50.0 |         50.0 |           16.7 |          10.7 |
| ('hybrid', 'pre', 'clean')               |     15.0 |    29.0 |    54.5 |          58.7 |        51.6 |         46.7 |         60.0 |           60.0 |          13.6 |
| ('hybrid', 'pre', 'partial')             |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           5.9 |
| ('hybrid', 'pre', 'synthetic')           |     14.0 |    50.5 |    76.6 |          27.9 |        27.3 |         28.6 |         42.9 |            7.1 |          12.1 |
| ('hybrid', 'pre', 'shadow')              |      7.0 |    48.2 |    69.0 |          30.0 |        33.3 |         28.6 |         42.9 |            0.0 |          11.3 |
| ('hybrid', 'pre', 'tilted')              |      7.0 |    48.2 |    69.0 |          30.0 |        33.3 |         28.6 |         42.9 |            0.0 |          11.3 |
| ('hybrid', 'pre', 'faded')               |      7.0 |    52.9 |    84.2 |          25.7 |        20.0 |         28.6 |         42.9 |           14.3 |          12.9 |
| ('hybrid', 'pre', 'perspective')         |      7.0 |    52.9 |    84.2 |          25.7 |        20.0 |         28.6 |         42.9 |           14.3 |          12.9 |
| ('hybrid', 'pre_post', 'sideways')       |     16.0 |    30.4 |    58.7 |          70.0 |        66.7 |         62.5 |         62.5 |           28.6 |           8.9 |
| ('hybrid', 'pre_post', 'crumpled')       |     15.0 |    37.0 |    64.4 |          58.0 |        53.8 |         20.0 |         40.0 |           33.3 |          11.5 |
| ('hybrid', 'pre_post', 'handheld')       |      6.0 |    47.4 |    75.2 |          45.0 |        22.2 |         50.0 |         50.0 |           16.7 |          10.6 |
| ('hybrid', 'pre_post', 'clean')          |     15.0 |    29.1 |    54.5 |          82.0 |        77.4 |         46.7 |         60.0 |           66.7 |          13.3 |
| ('hybrid', 'pre_post', 'partial')        |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           5.7 |
| ('hybrid', 'pre_post', 'synthetic')      |     14.0 |    50.5 |    76.6 |          52.9 |        36.4 |         28.6 |         42.9 |           28.6 |          11.9 |
| ('hybrid', 'pre_post', 'shadow')         |      7.0 |    48.2 |    69.0 |          58.6 |        50.0 |         28.6 |         42.9 |           42.9 |          11.1 |
| ('hybrid', 'pre_post', 'tilted')         |      7.0 |    48.2 |    69.0 |          58.6 |        50.0 |         28.6 |         42.9 |           42.9 |          11.1 |
| ('hybrid', 'pre_post', 'faded')          |      7.0 |    52.9 |    84.2 |          47.1 |        20.0 |         28.6 |         42.9 |           14.3 |          12.7 |
| ('hybrid', 'pre_post', 'perspective')    |      7.0 |    52.9 |    84.2 |          47.1 |        20.0 |         28.6 |         42.9 |           14.3 |          12.7 |


## By language

|                                      |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:-------------------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('tesseract', 'baseline', 'uz_latn') |     51.0 |    93.3 |    96.2 |           3.6 |         0.0 |         45.1 |         56.9 |            0.0 |           7.3 |
| ('tesseract', 'baseline', 'mixed')   |      2.0 |   nan   |   nan   |          40.0 |         0.0 |        100.0 |        100.0 |            0.0 |           1.7 |
| ('tesseract', 'pre', 'uz_latn')      |     51.0 |    45.3 |    79.1 |          16.4 |         0.0 |         45.1 |         56.9 |            0.0 |           8.5 |
| ('tesseract', 'pre', 'mixed')        |      2.0 |   nan   |   nan   |          50.0 |       100.0 |        100.0 |        100.0 |          100.0 |           1.4 |
| ('tesseract', 'pre_post', 'uz_latn') |     51.0 |    45.3 |    79.1 |          50.0 |         6.5 |         45.1 |         56.9 |            2.8 |           8.5 |
| ('tesseract', 'pre_post', 'mixed')   |      2.0 |   nan   |   nan   |          70.0 |       100.0 |        100.0 |        100.0 |          100.0 |           1.5 |
| ('easyocr', 'baseline', 'uz_latn')   |     51.0 |    72.9 |    93.8 |          18.3 |         0.0 |         45.1 |         56.9 |            0.0 |          34.5 |
| ('easyocr', 'baseline', 'mixed')     |      2.0 |   nan   |   nan   |          40.0 |         0.0 |        100.0 |        100.0 |            0.0 |          16.4 |
| ('easyocr', 'pre', 'uz_latn')        |     51.0 |    42.8 |    80.2 |          24.2 |         0.0 |         45.1 |         56.9 |            2.8 |          18.9 |
| ('easyocr', 'pre', 'mixed')          |      2.0 |   nan   |   nan   |          50.0 |         0.0 |        100.0 |        100.0 |            0.0 |           7.8 |
| ('easyocr', 'pre_post', 'uz_latn')   |     51.0 |    42.8 |    80.2 |          47.2 |         0.0 |         45.1 |         56.9 |            0.0 |          16.7 |
| ('easyocr', 'pre_post', 'mixed')     |      2.0 |   nan   |   nan   |          70.0 |         0.0 |        100.0 |        100.0 |            0.0 |           7.8 |
| ('rapidocr', 'baseline', 'uz_latn')  |     51.0 |    63.1 |    77.2 |          44.7 |        26.9 |         45.1 |         56.9 |           19.4 |           7.5 |
| ('rapidocr', 'baseline', 'mixed')    |      2.0 |   nan   |   nan   |          70.0 |         0.0 |        100.0 |        100.0 |          100.0 |           1.4 |
| ('rapidocr', 'pre', 'uz_latn')       |     51.0 |    33.7 |    61.3 |          48.1 |        47.1 |         45.1 |         56.9 |           36.1 |           7.8 |
| ('rapidocr', 'pre', 'mixed')         |      2.0 |   nan   |   nan   |          60.0 |         0.0 |        100.0 |        100.0 |          100.0 |           1.5 |
| ('rapidocr', 'pre_post', 'uz_latn')  |     51.0 |    33.7 |    61.3 |          70.6 |        67.6 |         45.1 |         56.9 |           47.2 |           8.2 |
| ('rapidocr', 'pre_post', 'mixed')    |      2.0 |   nan   |   nan   |          70.0 |         0.0 |        100.0 |        100.0 |          100.0 |           1.5 |
| ('hybrid', 'baseline', 'uz_latn')    |     51.0 |    63.1 |    77.2 |          44.7 |        26.9 |         45.1 |         56.9 |           19.4 |           9.6 |
| ('hybrid', 'baseline', 'mixed')      |      2.0 |   nan   |   nan   |          70.0 |         0.0 |        100.0 |        100.0 |          100.0 |           2.9 |
| ('hybrid', 'pre', 'uz_latn')         |     51.0 |    33.7 |    61.3 |          48.6 |        47.1 |         45.1 |         56.9 |           36.1 |          10.8 |
| ('hybrid', 'pre', 'mixed')           |      2.0 |   nan   |   nan   |          60.0 |         0.0 |        100.0 |        100.0 |          100.0 |           2.7 |
| ('hybrid', 'pre_post', 'uz_latn')    |     51.0 |    33.7 |    61.3 |          71.4 |        67.6 |         45.1 |         56.9 |           47.2 |          10.6 |
| ('hybrid', 'pre_post', 'mixed')      |      2.0 |   nan   |   nan   |          70.0 |         0.0 |        100.0 |        100.0 |          100.0 |           2.7 |


## Error causes (pre_post)

|                                                 |   count |
|:------------------------------------------------|--------:|
| ('easyocr', 'date/time misread')                |       6 |
| ('easyocr', 'digits misread')                   |      10 |
| ('easyocr', 'digits missing/extra')             |       4 |
| ('easyocr', 'digits/amounts misread')           |      11 |
| ('easyocr', 'not found')                        |      90 |
| ('easyocr', 'text misread / wrong span')        |      67 |
| ('easyocr', 'wrong line picked (value of vat)') |       5 |
| ('hybrid', 'date/time misread')                 |       3 |
| ('hybrid', 'digits misread')                    |       6 |
| ('hybrid', 'digits missing/extra')              |       4 |
| ('hybrid', 'digits/amounts misread')            |       6 |
| ('hybrid', 'not found')                         |      49 |
| ('hybrid', 'text misread / wrong span')         |      38 |
| ('rapidocr', 'date/time misread')               |       3 |
| ('rapidocr', 'digits misread')                  |       6 |
| ('rapidocr', 'digits missing/extra')            |       3 |
| ('rapidocr', 'digits/amounts misread')          |       5 |
| ('rapidocr', 'not found')                       |      57 |
| ('rapidocr', 'text misread / wrong span')       |      35 |
| ('tesseract', 'date/time misread')              |       6 |
| ('tesseract', 'digits misread')                 |       6 |
| ('tesseract', 'digits missing/extra')           |       3 |
| ('tesseract', 'digits/amounts misread')         |       9 |
| ('tesseract', 'not found')                      |      98 |
| ('tesseract', 'text misread / wrong span')      |      61 |


## Error examples

| image     | config   | engine    | conditions        | field          | gt                                                                             | pred                                                                                                                                                                           | cause                     |
|:----------|:---------|:----------|:------------------|:---------------|:-------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------|
| r02_a.jpg | pre_post | tesseract | sideways;crumpled | seller_name    | ERA                                                                            | ANVARDON м. 7 OILMUROO OʻG /                                                                                                                                                   | text misread / wrong span |
| r02_a.jpg | pre_post | tesseract | sideways;crumpled | seller_tin     | 31802964140017                                                                 |                                                                                                                                                                                | not found                 |
| r02_a.jpg | pre_post | tesseract | sideways;crumpled | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | Fargʻona viloyati, Fargʻona shahri;, Barkamol MFY, Yangi asr, koʻchagi./118 b uy, Yur, Manzil Fargʻona viloyati, Fargʻona shahri                                               | text misread / wrong span |
| r03_a.jpg | pre_post | tesseract | sideways;crumpled | seller_name    | ERA                                                                            | м ANVARION MAXMUDOV DILMUROD OʻGʻRI                                                                                                                                            | text misread / wrong span |
| r03_a.jpg | pre_post | tesseract | sideways;crumpled | seller_tin     | 31802964140017                                                                 |                                                                                                                                                                                | not found                 |
| r03_a.jpg | pre_post | tesseract | sideways;crumpled | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | anzil Fargʻona viloyati, Его ʼопа shahri, Barkamol MFY, Yangi asr, ʻ М, A ko! jasi. 118 b uy                                                                                   | text misread / wrong span |
| r03_a.jpg | pre_post | tesseract | sideways;crumpled | datetime       | 2026-11-08T11:02:29                                                            | 2026-11-08T11:02:23                                                                                                                                                            | date/time misread         |
| r03_a.jpg | pre_post | tesseract | sideways;crumpled | receipt_number | 12077                                                                          | 12877                                                                                                                                                                          | digits misread            |
| r03_a.jpg | pre_post | tesseract | sideways;crumpled | fiscal_module  | LG420211609580                                                                 |                                                                                                                                                                                | not found                 |
| r03_a.jpg | pre_post | tesseract | sideways;crumpled | fiscal_sign    | 514092944266                                                                   | 5149929442665                                                                                                                                                                  | digits missing/extra      |
| r03_a.jpg | pre_post | tesseract | sideways;crumpled | vat            | 0.0                                                                            | 69.0                                                                                                                                                                           | digits/amounts misread    |
| r03_a.jpg | pre_post | tesseract | sideways;crumpled | total          | 21000.0                                                                        | 21099.09                                                                                                                                                                       | digits/amounts misread    |
| r03_a.jpg | pre_post | tesseract | sideways;crumpled | payment        | card                                                                           |                                                                                                                                                                                | not found                 |
| r11_a.jpg | pre_post | tesseract | sideways;crumpled | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | Fargʻona viloyati, Fargʻona shahri, Barkamol MFY, Yarigl asr                                                                                                                   | text misread / wrong span |
| r11_a.jpg | pre_post | tesseract | sideways;crumpled | datetime       | 2026-11-03T17:12:38                                                            |                                                                                                                                                                                | not found                 |
| r11_a.jpg | pre_post | tesseract | sideways;crumpled | fiscal_module  | LG420211609580                                                                 |                                                                                                                                                                                | not found                 |
| r13_a.jpg | pre_post | tesseract | handheld;crumpled | seller_name    | ERA                                                                            | ERA !                                                                                                                                                                          | text misread / wrong span |
| r13_a.jpg | pre_post | tesseract | handheld;crumpled | seller_tin     | 31802964140017                                                                 |                                                                                                                                                                                | not found                 |
| r13_a.jpg | pre_post | tesseract | handheld;crumpled | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy |                                                                                                                                                                                | not found                 |
| r13_a.jpg | pre_post | tesseract | handheld;crumpled | datetime       | 2026-10-31T18:34:21                                                            |                                                                                                                                                                                | not found                 |
| r13_a.jpg | pre_post | tesseract | handheld;crumpled | receipt_number | 11814                                                                          |                                                                                                                                                                                | not found                 |
| r13_a.jpg | pre_post | tesseract | handheld;crumpled | fiscal_module  | LG420211609580                                                                 |                                                                                                                                                                                | not found                 |
| r13_a.jpg | pre_post | tesseract | handheld;crumpled | vat            | 0.0                                                                            |                                                                                                                                                                                | not found                 |
| r13_a.jpg | pre_post | tesseract | handheld;crumpled | total          | 19800.0                                                                        |                                                                                                                                                                                | not found                 |
| r15_a.jpg | pre_post | tesseract | sideways;handheld | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | Fargʻona viloyati, Fargʻona shahri, Barkamol MFY, Yangi asr, koʻchasi, 118 b uy, Yur.Manzit Fargʻona viloyati, Fargʻona shahri                                                 | text misread / wrong span |
| r17_a.jpg | pre_post | tesseract | clean             | seller_name    | ERA                                                                            | ANVARJON MAXMUDOV DILMUROD OʻGʻLI                                                                                                                                              | text misread / wrong span |
| r17_a.jpg | pre_post | tesseract | clean             | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | Fargʻona viloyati, Fargʻona shahri, Barkamol MFY, Yangi asr, koʻchasi, 118 b цу, Yur, Manzil Fargʻona viloyati, Fargʻona shahri                                                | text misread / wrong span |
| r18_a.jpg | pre_post | tesseract | crumpled          | seller_name    | ERA                                                                            | ANVARSON MAXMUDOV DILMUROD OʻGʻLI т                                                                                                                                            | text misread / wrong span |
| r18_a.jpg | pre_post | tesseract | crumpled          | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | Fargʻona viloyati. >, Fargʻona shahri.                                                                                                                                         | text misread / wrong span |
| r02_c.jpg | pre_post | tesseract | sideways          | seller_tin     | 31802964140017                                                                 |                                                                                                                                                                                | not found                 |
| r02_c.jpg | pre_post | tesseract | sideways          | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | Fargʻona viloyati, Fargʻona shahri                                                                                                                                             | text misread / wrong span |
| r02_c.jpg | pre_post | tesseract | sideways          | vat            | 0.0                                                                            | 6.68                                                                                                                                                                           | digits/amounts misread    |
| r03_c.jpg | pre_post | tesseract | sideways          | seller_name    | ERA                                                                            | ЕВА:                                                                                                                                                                           | text misread / wrong span |
| r03_c.jpg | pre_post | tesseract | sideways          | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | Fargʻona viloyati, Fargʻona shahri, Barkamol MFY, Yangi asi, koʻchasi, 118 b uy, Yur. Mana il Fargʻona viloyati, Fargʻona shahri., Barkamol MFY, Yangi asr, koʻchasi. 118 b uy | text misread / wrong span |
| r03_c.jpg | pre_post | tesseract | sideways          | payment        | card                                                                           | other                                                                                                                                                                          | text misread / wrong span |
| r11_c.jpg | pre_post | tesseract | clean             | seller_name    | ERA                                                                            | = Barkamol MEY, Yarigi |                                                                                                                                                       | text misread / wrong span |
| r11_c.jpg | pre_post | tesseract | clean             | seller_tin     | 31802964140017                                                                 |                                                                                                                                                                                | not found                 |
| r11_c.jpg | pre_post | tesseract | clean             | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | Yur. Нан: | koʻchasi, 118 b, == Fargʻona viloyat                                                                                                                               | text misread / wrong span |
| r11_c.jpg | pre_post | tesseract | clean             | total          | 20000.0                                                                        | 20600.0                                                                                                                                                                        | digits/amounts misread    |
| r13_c.jpg | pre_post | tesseract | clean             | seller_name    | ERA                                                                            | ROD OʻG on                                                                                                                                                                     | text misread / wrong span |