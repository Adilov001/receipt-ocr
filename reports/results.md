# Results (test split, 53 images, 16 receipts, 3 sellers)

## Engines × configurations

|                           |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:--------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('tesseract', 'baseline') |     53.0 |    93.4 |    96.5 |           4.6 |         0.0 |         47.2 |         58.5 |            0.0 |           7.4 |
| ('tesseract', 'pre')      |     53.0 |    49.1 |    88.1 |          23.8 |         0.0 |         47.2 |         58.5 |            0.0 |          10.5 |
| ('tesseract', 'pre_post') |     53.0 |    49.0 |    87.5 |          54.3 |        12.1 |         47.2 |         58.5 |           18.9 |          10.1 |
| ('easyocr', 'baseline')   |     53.0 |    73.1 |    95.4 |          20.0 |         0.0 |         47.2 |         58.5 |            0.0 |          35.5 |
| ('easyocr', 'pre')        |     53.0 |    35.3 |    75.8 |          31.1 |         5.3 |         47.2 |         58.5 |            0.0 |          40.2 |
| ('easyocr', 'pre_post')   |     53.0 |    34.5 |    71.7 |          55.7 |         7.9 |         47.2 |         58.5 |            8.1 |          39.0 |
| ('rapidocr', 'baseline')  |     53.0 |    62.1 |    72.3 |          48.6 |        41.3 |         47.2 |         58.5 |           29.7 |           8.3 |
| ('rapidocr', 'pre')       |     53.0 |    17.6 |    37.9 |          67.3 |        60.3 |         47.2 |         58.5 |           62.2 |           8.8 |
| ('rapidocr', 'pre_post')  |     53.0 |    17.2 |    35.7 |          85.9 |        71.2 |         47.2 |         58.5 |           70.3 |           9.0 |
| ('hybrid', 'baseline')    |     53.0 |    62.1 |    72.3 |          48.6 |        41.3 |         47.2 |         58.5 |           29.7 |          10.0 |
| ('hybrid', 'pre')         |     53.0 |    17.6 |    37.9 |          68.1 |        60.3 |         47.2 |         58.5 |           62.2 |          13.6 |
| ('hybrid', 'pre_post')    |     53.0 |    17.2 |    35.7 |          86.2 |        71.2 |         47.2 |         58.5 |           70.3 |          12.5 |


## Field accuracy, %

|                           |   seller_name |   seller_tin |   address |   datetime |   receipt_number |   fiscal_module |   fiscal_sign |   vat |   total |   payment |
|:--------------------------|--------------:|-------------:|----------:|-----------:|-----------------:|----------------:|--------------:|------:|--------:|----------:|
| ('tesseract', 'baseline') |           0.0 |          2.7 |       0.0 |        2.7 |              8.1 |             0.0 |           2.7 |   2.7 |    10.8 |      16.2 |
| ('tesseract', 'pre')      |           0.0 |         35.1 |      10.8 |       18.9 |             45.9 |             2.7 |          32.4 |   2.7 |    29.7 |      59.5 |
| ('tesseract', 'pre_post') |          21.6 |         35.1 |      10.8 |       73.0 |             73.0 |            56.8 |          73.0 |  48.6 |    67.6 |      83.8 |
| ('easyocr', 'baseline')   |           0.0 |         24.3 |       0.0 |        0.0 |             37.8 |            10.8 |          27.0 |  27.0 |    29.7 |      43.2 |
| ('easyocr', 'pre')        |           0.0 |         40.5 |       0.0 |       10.8 |             67.6 |            35.1 |          37.8 |  40.5 |    27.0 |      51.4 |
| ('easyocr', 'pre_post')   |          35.1 |         40.5 |       0.0 |       59.5 |             83.8 |            73.0 |          78.4 |  75.7 |    56.8 |      54.1 |
| ('rapidocr', 'baseline')  |           0.0 |         45.9 |      37.8 |       62.2 |             45.9 |            62.2 |          51.4 |  54.1 |    70.3 |      56.8 |
| ('rapidocr', 'pre')       |           2.7 |         75.7 |      32.4 |       67.6 |             81.1 |            75.7 |          78.4 |  83.8 |    91.9 |      83.8 |
| ('rapidocr', 'pre_post')  |          89.2 |         75.7 |      56.8 |       86.5 |             94.6 |            91.9 |          89.2 |  89.2 |    94.6 |      91.9 |
| ('hybrid', 'baseline')    |           0.0 |         45.9 |      37.8 |       62.2 |             45.9 |            62.2 |          51.4 |  54.1 |    70.3 |      56.8 |
| ('hybrid', 'pre')         |           2.7 |         75.7 |      32.4 |       67.6 |             83.8 |            75.7 |          81.1 |  83.8 |    94.6 |      83.8 |
| ('hybrid', 'pre_post')    |          89.2 |         75.7 |      56.8 |       86.5 |             94.6 |            91.9 |          91.9 |  89.2 |    94.6 |      91.9 |


## By shooting condition

|                                          |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:-----------------------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('tesseract', 'baseline', 'sideways')    |     16.0 |    99.4 |    99.9 |           0.0 |         0.0 |         62.5 |         62.5 |            0.0 |           4.2 |
| ('tesseract', 'baseline', 'crumpled')    |     15.0 |    97.4 |    98.9 |           0.0 |         0.0 |         20.0 |         40.0 |            0.0 |           6.6 |
| ('tesseract', 'baseline', 'handheld')    |      6.0 |    96.4 |    97.9 |           0.0 |         0.0 |         50.0 |         50.0 |            0.0 |           4.9 |
| ('tesseract', 'baseline', 'clean')       |     15.0 |    66.2 |    81.5 |          10.7 |         0.0 |         46.7 |         60.0 |            0.0 |           9.7 |
| ('tesseract', 'baseline', 'partial')     |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           6.1 |
| ('tesseract', 'baseline', 'synthetic')   |     14.0 |    97.8 |    99.0 |           0.7 |         0.0 |         28.6 |         42.9 |            0.0 |           7.7 |
| ('tesseract', 'baseline', 'shadow')      |      7.0 |    97.8 |    98.6 |           0.0 |         0.0 |         28.6 |         42.9 |            0.0 |           7.8 |
| ('tesseract', 'baseline', 'tilted')      |      7.0 |    97.8 |    98.6 |           0.0 |         0.0 |         28.6 |         42.9 |            0.0 |           7.8 |
| ('tesseract', 'baseline', 'faded')       |      7.0 |    97.8 |    99.4 |           1.4 |         0.0 |         28.6 |         42.9 |            0.0 |           7.5 |
| ('tesseract', 'baseline', 'perspective') |      7.0 |    97.8 |    99.4 |           1.4 |         0.0 |         28.6 |         42.9 |            0.0 |           7.5 |
| ('tesseract', 'pre', 'sideways')         |     16.0 |    43.0 |    80.2 |          20.7 |         0.0 |         62.5 |         62.5 |            0.0 |           6.5 |
| ('tesseract', 'pre', 'crumpled')         |     15.0 |    45.0 |    75.7 |          19.3 |         0.0 |         20.0 |         40.0 |            0.0 |           8.4 |
| ('tesseract', 'pre', 'handheld')         |      6.0 |    58.3 |    77.0 |          13.3 |         0.0 |         50.0 |         50.0 |            0.0 |           6.4 |
| ('tesseract', 'pre', 'clean')            |     15.0 |    59.6 |   124.9 |          27.3 |         0.0 |         46.7 |         60.0 |            0.0 |          16.8 |
| ('tesseract', 'pre', 'partial')          |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           6.7 |
| ('tesseract', 'pre', 'synthetic')        |     14.0 |    55.8 |    84.1 |          20.0 |         0.0 |         28.6 |         42.9 |            0.0 |           9.3 |
| ('tesseract', 'pre', 'shadow')           |      7.0 |    31.0 |    54.6 |          25.7 |         0.0 |         28.6 |         42.9 |            0.0 |           9.4 |
| ('tesseract', 'pre', 'tilted')           |      7.0 |    31.0 |    54.6 |          25.7 |         0.0 |         28.6 |         42.9 |            0.0 |           9.4 |
| ('tesseract', 'pre', 'faded')            |      7.0 |    80.6 |   113.6 |          14.3 |         0.0 |         28.6 |         42.9 |            0.0 |           9.2 |
| ('tesseract', 'pre', 'perspective')      |      7.0 |    80.6 |   113.6 |          14.3 |         0.0 |         28.6 |         42.9 |            0.0 |           9.2 |
| ('tesseract', 'pre_post', 'sideways')    |     16.0 |    42.9 |    79.6 |          51.4 |         8.7 |         62.5 |         62.5 |            7.1 |           6.6 |
| ('tesseract', 'pre_post', 'crumpled')    |     15.0 |    44.9 |    75.3 |          44.0 |         7.4 |         20.0 |         40.0 |            6.7 |           8.4 |
| ('tesseract', 'pre_post', 'handheld')    |      6.0 |    58.2 |    76.0 |          36.7 |         0.0 |         50.0 |         50.0 |            0.0 |           6.4 |
| ('tesseract', 'pre_post', 'clean')       |     15.0 |    59.5 |   124.1 |          60.7 |        21.4 |         46.7 |         60.0 |           40.0 |          15.8 |
| ('tesseract', 'pre_post', 'partial')     |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           6.1 |
| ('tesseract', 'pre_post', 'synthetic')   |     14.0 |    55.7 |    83.6 |          46.4 |         0.0 |         28.6 |         42.9 |            0.0 |           9.4 |
| ('tesseract', 'pre_post', 'shadow')      |      7.0 |    30.9 |    54.0 |          60.0 |         0.0 |         28.6 |         42.9 |            0.0 |           9.5 |
| ('tesseract', 'pre_post', 'tilted')      |      7.0 |    30.9 |    54.0 |          60.0 |         0.0 |         28.6 |         42.9 |            0.0 |           9.5 |
| ('tesseract', 'pre_post', 'faded')       |      7.0 |    80.6 |   113.3 |          32.9 |         0.0 |         28.6 |         42.9 |            0.0 |           9.3 |
| ('tesseract', 'pre_post', 'perspective') |      7.0 |    80.6 |   113.3 |          32.9 |         0.0 |         28.6 |         42.9 |            0.0 |           9.3 |
| ('easyocr', 'baseline', 'sideways')      |     16.0 |    88.9 |   102.7 |           0.0 |         0.0 |         62.5 |         62.5 |            0.0 |          40.3 |
| ('easyocr', 'baseline', 'crumpled')      |     15.0 |    80.6 |   100.5 |           6.0 |         0.0 |         20.0 |         40.0 |            0.0 |          48.4 |
| ('easyocr', 'baseline', 'handheld')      |      6.0 |    73.5 |    94.7 |           6.7 |         0.0 |         50.0 |         50.0 |            0.0 |          51.6 |
| ('easyocr', 'baseline', 'clean')         |     15.0 |    16.6 |    68.5 |          40.0 |         0.0 |         46.7 |         60.0 |            0.0 |          47.6 |
| ('easyocr', 'baseline', 'partial')       |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           6.6 |
| ('easyocr', 'baseline', 'synthetic')     |     14.0 |    85.4 |   102.3 |           7.9 |         0.0 |         28.6 |         42.9 |            0.0 |          50.1 |
| ('easyocr', 'baseline', 'shadow')        |      7.0 |    77.2 |   105.9 |           8.6 |         0.0 |         28.6 |         42.9 |            0.0 |          52.0 |
| ('easyocr', 'baseline', 'tilted')        |      7.0 |    77.2 |   105.9 |           8.6 |         0.0 |         28.6 |         42.9 |            0.0 |          52.0 |
| ('easyocr', 'baseline', 'faded')         |      7.0 |    93.5 |    98.7 |           7.1 |         0.0 |         28.6 |         42.9 |            0.0 |          48.1 |
| ('easyocr', 'baseline', 'perspective')   |      7.0 |    93.5 |    98.7 |           7.1 |         0.0 |         28.6 |         42.9 |            0.0 |          48.1 |
| ('easyocr', 'pre', 'sideways')           |     16.0 |    31.5 |    73.4 |          30.0 |         6.9 |         62.5 |         62.5 |            0.0 |          45.7 |
| ('easyocr', 'pre', 'crumpled')           |     15.0 |    34.1 |    73.9 |          23.3 |         7.1 |         20.0 |         40.0 |            0.0 |          52.7 |
| ('easyocr', 'pre', 'handheld')           |      6.0 |    44.7 |    81.6 |          21.7 |         0.0 |         50.0 |         50.0 |            0.0 |          51.8 |
| ('easyocr', 'pre', 'clean')              |     15.0 |    39.4 |    81.5 |          37.3 |         5.9 |         46.7 |         60.0 |            0.0 |          54.5 |
| ('easyocr', 'pre', 'partial')            |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           7.4 |
| ('easyocr', 'pre', 'synthetic')          |     14.0 |    44.5 |    81.9 |          22.1 |         8.0 |         28.6 |         42.9 |            0.0 |          59.8 |
| ('easyocr', 'pre', 'shadow')             |      7.0 |    18.0 |    65.7 |          38.6 |        15.4 |         28.6 |         42.9 |            0.0 |          63.6 |
| ('easyocr', 'pre', 'tilted')             |      7.0 |    18.0 |    65.7 |          38.6 |        15.4 |         28.6 |         42.9 |            0.0 |          63.6 |
| ('easyocr', 'pre', 'faded')              |      7.0 |    70.9 |    98.1 |           5.7 |         0.0 |         28.6 |         42.9 |            0.0 |          56.1 |
| ('easyocr', 'pre', 'perspective')        |      7.0 |    70.9 |    98.1 |           5.7 |         0.0 |         28.6 |         42.9 |            0.0 |          56.1 |
| ('easyocr', 'pre_post', 'sideways')      |     16.0 |    30.7 |    68.8 |          55.0 |        13.8 |         62.5 |         62.5 |           14.3 |          44.9 |
| ('easyocr', 'pre_post', 'crumpled')      |     15.0 |    33.4 |    69.6 |          46.0 |        14.3 |         20.0 |         40.0 |           13.3 |          51.3 |
| ('easyocr', 'pre_post', 'handheld')      |      6.0 |    44.0 |    78.5 |          38.3 |         0.0 |         50.0 |         50.0 |            0.0 |          50.9 |
| ('easyocr', 'pre_post', 'clean')         |     15.0 |    38.8 |    77.8 |          61.3 |         5.9 |         46.7 |         60.0 |            0.0 |          53.6 |
| ('easyocr', 'pre_post', 'partial')       |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           6.2 |
| ('easyocr', 'pre_post', 'synthetic')     |     14.0 |    43.8 |    78.0 |          45.0 |         8.0 |         28.6 |         42.9 |           14.3 |          57.9 |
| ('easyocr', 'pre_post', 'shadow')        |      7.0 |    17.1 |    60.4 |          62.9 |        15.4 |         28.6 |         42.9 |           14.3 |          61.9 |
| ('easyocr', 'pre_post', 'tilted')        |      7.0 |    17.1 |    60.4 |          62.9 |        15.4 |         28.6 |         42.9 |           14.3 |          61.9 |
| ('easyocr', 'pre_post', 'faded')         |      7.0 |    70.4 |    95.5 |          27.1 |         0.0 |         28.6 |         42.9 |           14.3 |          53.9 |
| ('easyocr', 'pre_post', 'perspective')   |      7.0 |    70.4 |    95.5 |          27.1 |         0.0 |         28.6 |         42.9 |           14.3 |          53.9 |
| ('rapidocr', 'baseline', 'sideways')     |     16.0 |    78.0 |    86.6 |          15.7 |         0.0 |         62.5 |         62.5 |            0.0 |           5.8 |
| ('rapidocr', 'baseline', 'crumpled')     |     15.0 |    70.1 |    80.4 |          29.3 |         0.0 |         20.0 |         40.0 |            0.0 |           8.2 |
| ('rapidocr', 'baseline', 'handheld')     |      6.0 |    62.5 |    73.4 |          16.7 |         0.0 |         50.0 |         50.0 |            0.0 |           6.3 |
| ('rapidocr', 'baseline', 'clean')        |     15.0 |     5.9 |    19.6 |          76.7 |        82.8 |         46.7 |         60.0 |           66.7 |          10.5 |
| ('rapidocr', 'baseline', 'partial')      |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           6.5 |
| ('rapidocr', 'baseline', 'synthetic')    |     14.0 |    76.8 |    85.9 |          28.6 |        10.0 |         28.6 |         42.9 |            7.1 |           9.0 |
| ('rapidocr', 'baseline', 'shadow')       |      7.0 |    62.9 |    76.0 |          40.0 |        16.7 |         28.6 |         42.9 |           14.3 |           9.3 |
| ('rapidocr', 'baseline', 'tilted')       |      7.0 |    62.9 |    76.0 |          40.0 |        16.7 |         28.6 |         42.9 |           14.3 |           9.3 |
| ('rapidocr', 'baseline', 'faded')        |      7.0 |    90.7 |    95.7 |          17.1 |         0.0 |         28.6 |         42.9 |            0.0 |           8.6 |
| ('rapidocr', 'baseline', 'perspective')  |      7.0 |    90.7 |    95.7 |          17.1 |         0.0 |         28.6 |         42.9 |            0.0 |           8.6 |
| ('rapidocr', 'pre', 'sideways')          |     16.0 |    14.9 |    36.5 |          60.0 |        50.0 |         62.5 |         62.5 |           50.0 |           6.5 |
| ('rapidocr', 'pre', 'crumpled')          |     15.0 |    20.9 |    41.5 |          53.3 |        34.5 |         20.0 |         40.0 |           46.7 |           9.4 |
| ('rapidocr', 'pre', 'handheld')          |      6.0 |    30.7 |    53.9 |          40.0 |        18.2 |         50.0 |         50.0 |           16.7 |           7.9 |
| ('rapidocr', 'pre', 'clean')             |     15.0 |     8.1 |    23.3 |          81.3 |        86.7 |         46.7 |         60.0 |           86.7 |          10.5 |
| ('rapidocr', 'pre', 'partial')           |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           6.5 |
| ('rapidocr', 'pre', 'synthetic')         |     14.0 |    25.3 |    51.2 |          51.4 |        37.0 |         28.6 |         42.9 |           42.9 |          10.0 |
| ('rapidocr', 'pre', 'shadow')            |      7.0 |    12.4 |    26.5 |          75.7 |        57.1 |         28.6 |         42.9 |           71.4 |           9.8 |
| ('rapidocr', 'pre', 'tilted')            |      7.0 |    12.4 |    26.5 |          75.7 |        57.1 |         28.6 |         42.9 |           71.4 |           9.8 |
| ('rapidocr', 'pre', 'faded')             |      7.0 |    38.3 |    75.9 |          27.1 |        15.4 |         28.6 |         42.9 |           14.3 |          10.2 |
| ('rapidocr', 'pre', 'perspective')       |      7.0 |    38.3 |    75.9 |          27.1 |        15.4 |         28.6 |         42.9 |           14.3 |          10.2 |
| ('rapidocr', 'pre_post', 'sideways')     |     16.0 |    14.5 |    34.1 |          82.1 |        57.1 |         62.5 |         62.5 |           50.0 |           6.7 |
| ('rapidocr', 'pre_post', 'crumpled')     |     15.0 |    20.5 |    39.2 |          73.3 |        48.3 |         20.0 |         40.0 |           60.0 |           9.7 |
| ('rapidocr', 'pre_post', 'handheld')     |      6.0 |    30.0 |    51.2 |          61.7 |        36.4 |         50.0 |         50.0 |           16.7 |           8.4 |
| ('rapidocr', 'pre_post', 'clean')        |     15.0 |     7.9 |    21.7 |          97.3 |        93.3 |         46.7 |         60.0 |           93.3 |          10.7 |
| ('rapidocr', 'pre_post', 'partial')      |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           6.8 |
| ('rapidocr', 'pre_post', 'synthetic')    |     14.0 |    24.7 |    47.9 |          71.4 |        44.4 |         28.6 |         42.9 |           50.0 |          10.3 |
| ('rapidocr', 'pre_post', 'shadow')       |      7.0 |    12.0 |    24.9 |          90.0 |        71.4 |         28.6 |         42.9 |           85.7 |          10.4 |
| ('rapidocr', 'pre_post', 'tilted')       |      7.0 |    12.0 |    24.9 |          90.0 |        71.4 |         28.6 |         42.9 |           85.7 |          10.4 |
| ('rapidocr', 'pre_post', 'faded')        |      7.0 |    37.3 |    70.9 |          52.9 |        15.4 |         28.6 |         42.9 |           14.3 |          10.2 |
| ('rapidocr', 'pre_post', 'perspective')  |      7.0 |    37.3 |    70.9 |          52.9 |        15.4 |         28.6 |         42.9 |           14.3 |          10.2 |
| ('hybrid', 'baseline', 'sideways')       |     16.0 |    78.0 |    86.6 |          15.7 |         0.0 |         62.5 |         62.5 |            0.0 |           7.2 |
| ('hybrid', 'baseline', 'crumpled')       |     15.0 |    70.1 |    80.4 |          29.3 |         0.0 |         20.0 |         40.0 |            0.0 |          10.0 |
| ('hybrid', 'baseline', 'handheld')       |      6.0 |    62.5 |    73.4 |          16.7 |         0.0 |         50.0 |         50.0 |            0.0 |           7.7 |
| ('hybrid', 'baseline', 'clean')          |     15.0 |     5.9 |    19.6 |          76.7 |        82.8 |         46.7 |         60.0 |           66.7 |          13.6 |
| ('hybrid', 'baseline', 'partial')        |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           6.3 |
| ('hybrid', 'baseline', 'synthetic')      |     14.0 |    76.8 |    85.9 |          28.6 |        10.0 |         28.6 |         42.9 |            7.1 |          10.7 |
| ('hybrid', 'baseline', 'shadow')         |      7.0 |    62.9 |    76.0 |          40.0 |        16.7 |         28.6 |         42.9 |           14.3 |          11.4 |
| ('hybrid', 'baseline', 'tilted')         |      7.0 |    62.9 |    76.0 |          40.0 |        16.7 |         28.6 |         42.9 |           14.3 |          11.4 |
| ('hybrid', 'baseline', 'faded')          |      7.0 |    90.7 |    95.7 |          17.1 |         0.0 |         28.6 |         42.9 |            0.0 |          10.1 |
| ('hybrid', 'baseline', 'perspective')    |      7.0 |    90.7 |    95.7 |          17.1 |         0.0 |         28.6 |         42.9 |            0.0 |          10.1 |
| ('hybrid', 'pre', 'sideways')            |     16.0 |    14.9 |    36.5 |          61.4 |        50.0 |         62.5 |         62.5 |           50.0 |           9.6 |
| ('hybrid', 'pre', 'crumpled')            |     15.0 |    20.9 |    41.5 |          54.7 |        34.5 |         20.0 |         40.0 |           46.7 |          12.4 |
| ('hybrid', 'pre', 'handheld')            |      6.0 |    30.7 |    53.9 |          40.0 |        18.2 |         50.0 |         50.0 |           16.7 |          10.7 |
| ('hybrid', 'pre', 'clean')               |     15.0 |     8.1 |    23.3 |          82.0 |        86.7 |         46.7 |         60.0 |           86.7 |          20.3 |
| ('hybrid', 'pre', 'partial')             |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           7.9 |
| ('hybrid', 'pre', 'synthetic')           |     14.0 |    25.3 |    51.2 |          52.9 |        37.0 |         28.6 |         42.9 |           42.9 |          13.5 |
| ('hybrid', 'pre', 'shadow')              |      7.0 |    12.4 |    26.5 |          75.7 |        57.1 |         28.6 |         42.9 |           71.4 |          13.8 |
| ('hybrid', 'pre', 'tilted')              |      7.0 |    12.4 |    26.5 |          75.7 |        57.1 |         28.6 |         42.9 |           71.4 |          13.8 |
| ('hybrid', 'pre', 'faded')               |      7.0 |    38.3 |    75.9 |          30.0 |        15.4 |         28.6 |         42.9 |           14.3 |          13.3 |
| ('hybrid', 'pre', 'perspective')         |      7.0 |    38.3 |    75.9 |          30.0 |        15.4 |         28.6 |         42.9 |           14.3 |          13.3 |
| ('hybrid', 'pre_post', 'sideways')       |     16.0 |    14.5 |    34.1 |          82.9 |        57.1 |         62.5 |         62.5 |           50.0 |           9.6 |
| ('hybrid', 'pre_post', 'crumpled')       |     15.0 |    20.5 |    39.2 |          74.0 |        48.3 |         20.0 |         40.0 |           60.0 |          11.9 |
| ('hybrid', 'pre_post', 'handheld')       |      6.0 |    30.0 |    51.2 |          61.7 |        36.4 |         50.0 |         50.0 |           16.7 |           9.6 |
| ('hybrid', 'pre_post', 'clean')          |     15.0 |     7.9 |    21.7 |          97.3 |        93.3 |         46.7 |         60.0 |           93.3 |          19.1 |
| ('hybrid', 'pre_post', 'partial')        |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           6.5 |
| ('hybrid', 'pre_post', 'synthetic')      |     14.0 |    24.7 |    47.9 |          72.1 |        44.4 |         28.6 |         42.9 |           50.0 |          12.3 |
| ('hybrid', 'pre_post', 'shadow')         |      7.0 |    12.0 |    24.9 |          90.0 |        71.4 |         28.6 |         42.9 |           85.7 |          12.4 |
| ('hybrid', 'pre_post', 'tilted')         |      7.0 |    12.0 |    24.9 |          90.0 |        71.4 |         28.6 |         42.9 |           85.7 |          12.4 |
| ('hybrid', 'pre_post', 'faded')          |      7.0 |    37.3 |    70.9 |          54.3 |        15.4 |         28.6 |         42.9 |           14.3 |          12.1 |
| ('hybrid', 'pre_post', 'perspective')    |      7.0 |    37.3 |    70.9 |          54.3 |        15.4 |         28.6 |         42.9 |           14.3 |          12.1 |


## By language

|                                      |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:-------------------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('tesseract', 'baseline', 'uz_latn') |     51.0 |    93.4 |    96.5 |           3.6 |         0.0 |         45.1 |         56.9 |            0.0 |           7.6 |
| ('tesseract', 'baseline', 'mixed')   |      2.0 |   nan   |   nan   |          40.0 |         0.0 |        100.0 |        100.0 |            0.0 |           1.7 |
| ('tesseract', 'pre', 'uz_latn')      |     51.0 |    49.1 |    88.1 |          23.6 |         0.0 |         45.1 |         56.9 |            0.0 |          10.7 |
| ('tesseract', 'pre', 'mixed')        |      2.0 |   nan   |   nan   |          30.0 |         0.0 |        100.0 |        100.0 |            0.0 |           7.1 |
| ('tesseract', 'pre_post', 'uz_latn') |     51.0 |    49.0 |    87.5 |          54.2 |        12.5 |         45.1 |         56.9 |           19.4 |          10.2 |
| ('tesseract', 'pre_post', 'mixed')   |      2.0 |   nan   |   nan   |          60.0 |         0.0 |        100.0 |        100.0 |            0.0 |           7.0 |
| ('easyocr', 'baseline', 'uz_latn')   |     51.0 |    73.1 |    95.4 |          19.4 |         0.0 |         45.1 |         56.9 |            0.0 |          36.1 |
| ('easyocr', 'baseline', 'mixed')     |      2.0 |   nan   |   nan   |          40.0 |         0.0 |        100.0 |        100.0 |            0.0 |          17.8 |
| ('easyocr', 'pre', 'uz_latn')        |     51.0 |    35.3 |    75.8 |          30.8 |         5.4 |         45.1 |         56.9 |            0.0 |          40.8 |
| ('easyocr', 'pre', 'mixed')          |      2.0 |   nan   |   nan   |          40.0 |         0.0 |        100.0 |        100.0 |            0.0 |          25.4 |
| ('easyocr', 'pre_post', 'uz_latn')   |     51.0 |    34.5 |    71.7 |          55.6 |         8.1 |         45.1 |         56.9 |            8.3 |          39.6 |
| ('easyocr', 'pre_post', 'mixed')     |      2.0 |   nan   |   nan   |          60.0 |         0.0 |        100.0 |        100.0 |            0.0 |          25.3 |
| ('rapidocr', 'baseline', 'uz_latn')  |     51.0 |    62.1 |    72.3 |          48.6 |        39.3 |         45.1 |         56.9 |           30.6 |           8.6 |
| ('rapidocr', 'baseline', 'mixed')    |      2.0 |   nan   |   nan   |          50.0 |       100.0 |        100.0 |        100.0 |            0.0 |           1.7 |
| ('rapidocr', 'pre', 'uz_latn')       |     51.0 |    17.6 |    37.9 |          66.9 |        59.2 |         45.1 |         56.9 |           63.9 |           9.1 |
| ('rapidocr', 'pre', 'mixed')         |      2.0 |   nan   |   nan   |          80.0 |       100.0 |        100.0 |        100.0 |            0.0 |           1.6 |
| ('rapidocr', 'pre_post', 'uz_latn')  |     51.0 |    17.2 |    35.7 |          85.6 |        70.4 |         45.1 |         56.9 |           72.2 |           9.3 |
| ('rapidocr', 'pre_post', 'mixed')    |      2.0 |   nan   |   nan   |         100.0 |       100.0 |        100.0 |        100.0 |            0.0 |           1.6 |
| ('hybrid', 'baseline', 'uz_latn')    |     51.0 |    62.1 |    72.3 |          48.6 |        39.3 |         45.1 |         56.9 |           30.6 |          10.3 |
| ('hybrid', 'baseline', 'mixed')      |      2.0 |   nan   |   nan   |          50.0 |       100.0 |        100.0 |        100.0 |            0.0 |           3.2 |
| ('hybrid', 'pre', 'uz_latn')         |     51.0 |    17.6 |    37.9 |          67.8 |        59.2 |         45.1 |         56.9 |           63.9 |          13.8 |
| ('hybrid', 'pre', 'mixed')           |      2.0 |   nan   |   nan   |          80.0 |       100.0 |        100.0 |        100.0 |            0.0 |           8.3 |
| ('hybrid', 'pre_post', 'uz_latn')    |     51.0 |    17.2 |    35.7 |          85.8 |        70.4 |         45.1 |         56.9 |           72.2 |          12.7 |
| ('hybrid', 'pre_post', 'mixed')      |      2.0 |   nan   |   nan   |         100.0 |       100.0 |        100.0 |        100.0 |            0.0 |           8.3 |


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

| engine    |   receipts | field acc %      | item F1 %         | consistent %     | CER %            | WER %             |
|:----------|-----------:|:-----------------|:------------------|:-----------------|:-----------------|:------------------|
| tesseract |         16 | 59.1 [51.2–66.5] | 19.0 [0.0–39.0]   | 30.4 [11.5–52.4] | 42.3 [34.4–51.1] | 91.3 [71.0–110.4] |
| easyocr   |         16 | 62.2 [54.8–68.6] | 7.8 [0.0–20.4]    | 4.3 [0.0–13.6]   | 25.3 [19.2–30.7] | 65.4 [56.5–73.4]  |
| rapidocr  |         16 | 94.8 [91.4–98.0] | 87.0 [75.0–100.0] | 82.6 [68.0–95.5] | 9.8 [5.6–13.9]   | 23.4 [17.2–29.5]  |
| hybrid    |         16 | 94.8 [91.3–98.0] | 87.0 [75.0–100.0] | 82.6 [68.2–95.7] | 9.8 [5.3–14.3]   | 23.4 [17.2–29.8]  |


## Per seller (real whole-receipt photos, pre + post)

|                                   |   photos |   field acc % |   item F1 % |   consistent % |   CER % |   WER % |
|:----------------------------------|---------:|--------------:|------------:|---------------:|--------:|--------:|
| ('tesseract', 'era_barkamol')     |     21.0 |          58.6 |        20.5 |           33.3 |    42.3 |    91.3 |
| ('tesseract', 'diyor_neft')       |      1.0 |          60.0 |         0.0 |            0.0 |   nan   |   nan   |
| ('tesseract', 'era_avtomobilist') |      1.0 |          70.0 |         0.0 |            0.0 |   nan   |   nan   |
| ('easyocr', 'era_barkamol')       |     21.0 |          61.9 |         4.3 |            4.8 |    25.3 |    65.4 |
| ('easyocr', 'diyor_neft')         |      1.0 |          60.0 |         0.0 |            0.0 |   nan   |   nan   |
| ('easyocr', 'era_avtomobilist')   |      1.0 |          70.0 |       100.0 |            0.0 |   nan   |   nan   |
| ('rapidocr', 'era_barkamol')      |     21.0 |          94.3 |        85.7 |           85.7 |     9.8 |    23.4 |
| ('rapidocr', 'diyor_neft')        |      1.0 |         100.0 |       100.0 |            0.0 |   nan   |   nan   |
| ('rapidocr', 'era_avtomobilist')  |      1.0 |         100.0 |       100.0 |          100.0 |   nan   |   nan   |
| ('hybrid', 'era_barkamol')        |     21.0 |          94.3 |        85.7 |           85.7 |     9.8 |    23.4 |
| ('hybrid', 'diyor_neft')          |      1.0 |         100.0 |       100.0 |            0.0 |   nan   |   nan   |
| ('hybrid', 'era_avtomobilist')    |      1.0 |         100.0 |       100.0 |          100.0 |   nan   |   nan   |


## Error causes (pre_post)

|                                                 |   count |
|:------------------------------------------------|--------:|
| ('easyocr', 'apostrophe')                       |       2 |
| ('easyocr', 'date/time misread')                |       8 |
| ('easyocr', 'digits misread')                   |      16 |
| ('easyocr', 'digits missing/extra')             |       3 |
| ('easyocr', 'digits/amounts misread')           |       8 |
| ('easyocr', 'not found')                        |      55 |
| ('easyocr', 'text misread / wrong span')        |      67 |
| ('easyocr', 'wrong line picked (value of vat)') |       5 |
| ('hybrid', 'apostrophe')                        |       2 |
| ('hybrid', 'digits misread')                    |       6 |
| ('hybrid', 'digits missing/extra')              |       1 |
| ('hybrid', 'digits/amounts misread')            |       1 |
| ('hybrid', 'not found')                         |      22 |
| ('hybrid', 'text misread / wrong span')         |      19 |
| ('rapidocr', 'apostrophe')                      |       2 |
| ('rapidocr', 'digits misread')                  |       6 |
| ('rapidocr', 'digits missing/extra')            |       1 |
| ('rapidocr', 'digits/amounts misread')          |       1 |
| ('rapidocr', 'not found')                       |      23 |
| ('rapidocr', 'text misread / wrong span')       |      19 |
| ('tesseract', 'apostrophe')                     |       1 |
| ('tesseract', 'date/time misread')              |       4 |
| ('tesseract', 'digits misread')                 |      11 |
| ('tesseract', 'digits missing/extra')           |       3 |
| ('tesseract', 'digits/amounts misread')         |      15 |
| ('tesseract', 'not found')                      |      86 |
| ('tesseract', 'text misread / wrong span')      |      49 |


## Error examples

| image     | config   | engine    | conditions        | field          | gt                                                                             | pred                                                                                                 | cause                     |
|:----------|:---------|:----------|:------------------|:---------------|:-------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------|:--------------------------|
| r02_a.jpg | pre_post | tesseract | sideways;crumpled | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | Fargʻona ghahrin, Barkamol MFY, Yangi ast, koʻchasi./118 b uy                                        | text misread / wrong span |
| r03_a.jpg | pre_post | tesseract | sideways;crumpled | seller_name    | ERA                                                                            | ʻ ERA                                                                                                | apostrophe                |
| r03_a.jpg | pre_post | tesseract | sideways;crumpled | seller_tin     | 31802964140017                                                                 |                                                                                                      | not found                 |
| r03_a.jpg | pre_post | tesseract | sideways;crumpled | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | Fargʻona viloyati, Fargʻona shahri., Barkamot МЕУ, Yangi ast, coʻqhasi, 118 b uy, Fargʻona viloyati. | text misread / wrong span |
| r03_a.jpg | pre_post | tesseract | sideways;crumpled | datetime       | 2026-11-08T11:02:29                                                            | 2026-11-08T11:02:23                                                                                  | date/time misread         |
| r03_a.jpg | pre_post | tesseract | sideways;crumpled | receipt_number | 12077                                                                          |                                                                                                      | not found                 |
| r03_a.jpg | pre_post | tesseract | sideways;crumpled | fiscal_module  | LG420211609580                                                                 | LG428211689588                                                                                       | digits misread            |
| r03_a.jpg | pre_post | tesseract | sideways;crumpled | fiscal_sign    | 514092944266                                                                   | 514892944266                                                                                         | digits misread            |
| r03_a.jpg | pre_post | tesseract | sideways;crumpled | vat            | 0.0                                                                            | 8.68                                                                                                 | digits/amounts misread    |
| r11_a.jpg | pre_post | tesseract | sideways;crumpled | seller_tin     | 31802964140017                                                                 |                                                                                                      | not found                 |
| r11_a.jpg | pre_post | tesseract | sideways;crumpled | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | Fargʻona viloyati, Fargʻona shahri, Barkamol MEY, Yangi asr, koʻchasi, 118 b uy                      | text misread / wrong span |
| r11_a.jpg | pre_post | tesseract | sideways;crumpled | fiscal_module  | LG420211609580                                                                 |                                                                                                      | not found                 |
| r13_a.jpg | pre_post | tesseract | handheld;crumpled | seller_name    | ERA                                                                            | gʻli                                                                                                 | text misread / wrong span |
| r13_a.jpg | pre_post | tesseract | handheld;crumpled | seller_tin     | 31802964140017                                                                 |                                                                                                      | not found                 |
| r13_a.jpg | pre_post | tesseract | handheld;crumpled | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy |                                                                                                      | not found                 |
| r13_a.jpg | pre_post | tesseract | handheld;crumpled | datetime       | 2026-10-31T18:34:21                                                            |                                                                                                      | not found                 |
| r13_a.jpg | pre_post | tesseract | handheld;crumpled | receipt_number | 11814                                                                          |                                                                                                      | not found                 |
| r13_a.jpg | pre_post | tesseract | handheld;crumpled | fiscal_module  | LG420211609580                                                                 |                                                                                                      | not found                 |
| r13_a.jpg | pre_post | tesseract | handheld;crumpled | vat            | 0.0                                                                            | 0.09                                                                                                 | digits/amounts misread    |
| r13_a.jpg | pre_post | tesseract | handheld;crumpled | total          | 19800.0                                                                        | 8.89                                                                                                 | digits/amounts misread    |
| r15_a.jpg | pre_post | tesseract | sideways;handheld | seller_name    | ERA                                                                            | ЕВА                                                                                                  | text misread / wrong span |
| r15_a.jpg | pre_post | tesseract | sideways;handheld | seller_tin     | 31802964140017                                                                 | 31802964140217                                                                                       | digits misread            |
| r15_a.jpg | pre_post | tesseract | sideways;handheld | vat            | 0.0                                                                            | 8.68                                                                                                 | digits/amounts misread    |
| r15_a.jpg | pre_post | tesseract | sideways;handheld | total          | 34000.0                                                                        | 34009.0                                                                                              | digits/amounts misread    |
| r15_a.jpg | pre_post | tesseract | sideways;handheld | payment        | card                                                                           |                                                                                                      | not found                 |
| r18_a.jpg | pre_post | tesseract | crumpled          | seller_name    | ERA                                                                            | ANVARSON MAXMUDOV DILMUROD OʻGʻLI                                                                    | text misread / wrong span |
| r18_a.jpg | pre_post | tesseract | crumpled          | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | Fargʻona viloyati, Fargʻona shahri, Barkamol MEY Yangi asr, koʻchasi, 118 b uy                       | text misread / wrong span |
| r18_a.jpg | pre_post | tesseract | crumpled          | total          | 26000.0                                                                        | 20000.0                                                                                              | digits/amounts misread    |
| r02_c.jpg | pre_post | tesseract | sideways          | seller_name    | ERA                                                                            | па Fargʻona vile ati                                                                                 | text misread / wrong span |
| r02_c.jpg | pre_post | tesseract | sideways          | seller_tin     | 31802964140017                                                                 |                                                                                                      | not found                 |
| r02_c.jpg | pre_post | tesseract | sideways          | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | Far Ma shahri                                                                                        | text misread / wrong span |
| r02_c.jpg | pre_post | tesseract | sideways          | vat            | 0.0                                                                            |                                                                                                      | not found                 |
| r03_c.jpg | pre_post | tesseract | sideways          | seller_name    | ERA                                                                            | | ERA                                                                                                | text misread / wrong span |
| r03_c.jpg | pre_post | tesseract | sideways          | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | Fargʻona shahri, Barkamol MFY, Yangi asr, A koʻchasi, 118 b uy                                       | text misread / wrong span |
| r03_c.jpg | pre_post | tesseract | sideways          | vat            | 0.0                                                                            |                                                                                                      | not found                 |
| r11_c.jpg | pre_post | tesseract | clean             | seller_name    | ERA                                                                            | ARJON MAXMUDOV DILMUROD OʻG b+                                                                       | text misread / wrong span |
| r11_c.jpg | pre_post | tesseract | clean             | seller_tin     | 31802964140017                                                                 |                                                                                                      | not found                 |
| r11_c.jpg | pre_post | tesseract | clean             | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | shahri, "ona, aa, Farg, riq, yangi ast, Barkamol MFY                                                 | text misread / wrong span |
| r13_c.jpg | pre_post | tesseract | clean             | seller_name    | ERA                                                                            | ря 5 рн И a                                                                                          | text misread / wrong span |
| r13_c.jpg | pre_post | tesseract | clean             | seller_tin     | 31802964140017                                                                 |                                                                                                      | not found                 |