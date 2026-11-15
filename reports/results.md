# Results (test split, 53 images, 16 receipts, 3 sellers)

## Engines × configurations

|                           |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:--------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('tesseract', 'baseline') |     53.0 |    93.3 |    96.2 |           4.6 |         0.0 |         47.2 |         58.5 |            0.0 |           5.5 |
| ('tesseract', 'pre')      |     53.0 |    47.6 |    81.7 |          15.1 |         3.1 |         47.2 |         58.5 |            2.7 |           6.9 |
| ('tesseract', 'pre_post') |     53.0 |    47.6 |    81.7 |          46.8 |         9.4 |         47.2 |         58.5 |            2.7 |           7.0 |
| ('easyocr', 'baseline')   |     53.0 |    72.9 |    93.8 |          18.9 |         0.0 |         47.2 |         58.5 |            0.0 |          30.4 |
| ('easyocr', 'pre')        |     53.0 |    45.7 |    82.5 |          21.9 |         0.0 |         47.2 |         58.5 |            2.7 |          14.9 |
| ('easyocr', 'pre_post')   |     53.0 |    45.7 |    82.5 |          44.6 |         0.0 |         47.2 |         58.5 |            0.0 |          15.2 |
| ('rapidocr', 'baseline')  |     53.0 |    63.1 |    77.2 |          45.4 |        26.1 |         47.2 |         58.5 |           21.6 |           5.7 |
| ('rapidocr', 'pre')       |     53.0 |    36.4 |    63.4 |          45.9 |        42.9 |         47.2 |         58.5 |           35.1 |           6.1 |
| ('rapidocr', 'pre_post')  |     53.0 |    36.4 |    63.4 |          67.8 |        57.1 |         47.2 |         58.5 |           45.9 |           5.9 |
| ('hybrid', 'baseline')    |     53.0 |    63.1 |    77.2 |          45.4 |        26.1 |         47.2 |         58.5 |           21.6 |           7.6 |
| ('hybrid', 'pre')         |     53.0 |    36.4 |    63.4 |          46.5 |        42.9 |         47.2 |         58.5 |           35.1 |           9.0 |
| ('hybrid', 'pre_post')    |     53.0 |    36.4 |    63.4 |          68.4 |        57.1 |         47.2 |         58.5 |           43.2 |           9.1 |


## Field accuracy, %

|                           |   seller_name |   seller_tin |   address |   datetime |   receipt_number |   fiscal_module |   fiscal_sign |   vat |   total |   payment |
|:--------------------------|--------------:|-------------:|----------:|-----------:|-----------------:|----------------:|--------------:|------:|--------:|----------:|
| ('tesseract', 'baseline') |           0.0 |          2.7 |       0.0 |        2.7 |              8.1 |             0.0 |           2.7 |   2.7 |    10.8 |      16.2 |
| ('tesseract', 'pre')      |           0.0 |         24.3 |       5.4 |       18.9 |             37.8 |             0.0 |          16.2 |   5.4 |    10.8 |      32.4 |
| ('tesseract', 'pre_post') |          27.0 |         24.3 |       5.4 |       62.2 |             70.3 |            54.1 |          64.9 |  48.6 |    45.9 |      64.9 |
| ('easyocr', 'baseline')   |           0.0 |         24.3 |       0.0 |        0.0 |             32.4 |            10.8 |          27.0 |  27.0 |    29.7 |      37.8 |
| ('easyocr', 'pre')        |           0.0 |         43.2 |       0.0 |        5.4 |             40.5 |            21.6 |          21.6 |  32.4 |    10.8 |      43.2 |
| ('easyocr', 'pre_post')   |          16.2 |         43.2 |       0.0 |       62.2 |             70.3 |            64.9 |          62.2 |  48.6 |    35.1 |      43.2 |
| ('rapidocr', 'baseline')  |           0.0 |         45.9 |      21.6 |       64.9 |             48.6 |            75.7 |          40.5 |  43.2 |    62.2 |      51.4 |
| ('rapidocr', 'pre')       |           0.0 |         51.4 |      16.2 |       54.1 |             64.9 |            59.5 |          45.9 |  37.8 |    59.5 |      70.3 |
| ('rapidocr', 'pre_post')  |          67.6 |         51.4 |      16.2 |       81.1 |             81.1 |            78.4 |          73.0 |  67.6 |    83.8 |      78.4 |
| ('hybrid', 'baseline')    |           0.0 |         45.9 |      21.6 |       64.9 |             48.6 |            75.7 |          40.5 |  43.2 |    62.2 |      51.4 |
| ('hybrid', 'pre')         |           0.0 |         51.4 |      16.2 |       54.1 |             67.6 |            59.5 |          45.9 |  37.8 |    59.5 |      73.0 |
| ('hybrid', 'pre_post')    |          67.6 |         51.4 |      16.2 |       81.1 |             81.1 |            78.4 |          73.0 |  70.3 |    83.8 |      81.1 |


## By shooting condition

|                                          |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:-----------------------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('tesseract', 'baseline', 'sideways')    |     16.0 |    99.4 |    99.9 |           0.0 |         0.0 |         62.5 |         62.5 |            0.0 |           3.6 |
| ('tesseract', 'baseline', 'crumpled')    |     15.0 |    97.4 |    98.7 |           0.0 |         0.0 |         20.0 |         40.0 |            0.0 |           5.6 |
| ('tesseract', 'baseline', 'handheld')    |      6.0 |    96.3 |    97.5 |           0.0 |         0.0 |         50.0 |         50.0 |            0.0 |           4.0 |
| ('tesseract', 'baseline', 'clean')       |     15.0 |    66.0 |    80.2 |          10.7 |         0.0 |         46.7 |         60.0 |            0.0 |           7.6 |
| ('tesseract', 'baseline', 'partial')     |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           3.8 |
| ('tesseract', 'baseline', 'synthetic')   |     14.0 |    97.8 |    98.8 |           0.7 |         0.0 |         28.6 |         42.9 |            0.0 |           5.4 |
| ('tesseract', 'baseline', 'shadow')      |      7.0 |    97.7 |    98.5 |           0.0 |         0.0 |         28.6 |         42.9 |            0.0 |           5.6 |
| ('tesseract', 'baseline', 'tilted')      |      7.0 |    97.7 |    98.5 |           0.0 |         0.0 |         28.6 |         42.9 |            0.0 |           5.6 |
| ('tesseract', 'baseline', 'faded')       |      7.0 |    97.8 |    99.2 |           1.4 |         0.0 |         28.6 |         42.9 |            0.0 |           5.2 |
| ('tesseract', 'baseline', 'perspective') |      7.0 |    97.8 |    99.2 |           1.4 |         0.0 |         28.6 |         42.9 |            0.0 |           5.2 |
| ('tesseract', 'pre', 'sideways')         |     16.0 |    38.9 |    71.6 |          14.3 |         0.0 |         62.5 |         62.5 |            0.0 |           6.0 |
| ('tesseract', 'pre', 'crumpled')         |     15.0 |    48.5 |    82.2 |          12.7 |         0.0 |         20.0 |         40.0 |            0.0 |           7.9 |
| ('tesseract', 'pre', 'handheld')         |      6.0 |    59.7 |    96.9 |           6.7 |         0.0 |         50.0 |         50.0 |            0.0 |           7.2 |
| ('tesseract', 'pre', 'clean')            |     15.0 |    62.7 |    98.0 |          18.0 |         8.3 |         46.7 |         60.0 |            6.7 |           8.9 |
| ('tesseract', 'pre', 'partial')          |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           3.8 |
| ('tesseract', 'pre', 'synthetic')        |     14.0 |    57.2 |    90.5 |          10.0 |         0.0 |         28.6 |         42.9 |            0.0 |           7.8 |
| ('tesseract', 'pre', 'shadow')           |      7.0 |    56.2 |    78.8 |           7.1 |         0.0 |         28.6 |         42.9 |            0.0 |           7.2 |
| ('tesseract', 'pre', 'tilted')           |      7.0 |    56.2 |    78.8 |           7.1 |         0.0 |         28.6 |         42.9 |            0.0 |           7.2 |
| ('tesseract', 'pre', 'faded')            |      7.0 |    58.3 |   102.2 |          12.9 |         0.0 |         28.6 |         42.9 |            0.0 |           8.4 |
| ('tesseract', 'pre', 'perspective')      |      7.0 |    58.3 |   102.2 |          12.9 |         0.0 |         28.6 |         42.9 |            0.0 |           8.4 |
| ('tesseract', 'pre_post', 'sideways')    |     16.0 |    38.9 |    71.6 |          47.1 |         7.7 |         62.5 |         62.5 |            0.0 |           6.0 |
| ('tesseract', 'pre_post', 'crumpled')    |     15.0 |    48.5 |    82.2 |          36.0 |         0.0 |         20.0 |         40.0 |            0.0 |           7.9 |
| ('tesseract', 'pre_post', 'handheld')    |      6.0 |    59.7 |    96.9 |          38.3 |        22.2 |         50.0 |         50.0 |            0.0 |           7.2 |
| ('tesseract', 'pre_post', 'clean')       |     15.0 |    62.7 |    98.0 |          54.0 |        16.7 |         46.7 |         60.0 |            6.7 |           9.0 |
| ('tesseract', 'pre_post', 'partial')     |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           3.9 |
| ('tesseract', 'pre_post', 'synthetic')   |     14.0 |    57.2 |    90.5 |          32.1 |         0.0 |         28.6 |         42.9 |            0.0 |           8.2 |
| ('tesseract', 'pre_post', 'shadow')      |      7.0 |    56.2 |    78.8 |          28.6 |         0.0 |         28.6 |         42.9 |            0.0 |           7.6 |
| ('tesseract', 'pre_post', 'tilted')      |      7.0 |    56.2 |    78.8 |          28.6 |         0.0 |         28.6 |         42.9 |            0.0 |           7.6 |
| ('tesseract', 'pre_post', 'faded')       |      7.0 |    58.3 |   102.2 |          35.7 |         0.0 |         28.6 |         42.9 |            0.0 |           8.7 |
| ('tesseract', 'pre_post', 'perspective') |      7.0 |    58.3 |   102.2 |          35.7 |         0.0 |         28.6 |         42.9 |            0.0 |           8.7 |
| ('easyocr', 'baseline', 'sideways')      |     16.0 |    88.7 |   101.7 |           0.0 |         0.0 |         62.5 |         62.5 |            0.0 |          38.0 |
| ('easyocr', 'baseline', 'crumpled')      |     15.0 |    80.3 |    98.8 |           4.7 |         0.0 |         20.0 |         40.0 |            0.0 |          44.3 |
| ('easyocr', 'baseline', 'handheld')      |      6.0 |    73.2 |    92.6 |           6.7 |         0.0 |         50.0 |         50.0 |            0.0 |          40.3 |
| ('easyocr', 'baseline', 'clean')         |     15.0 |    16.6 |    65.6 |          40.0 |         0.0 |         46.7 |         60.0 |            0.0 |          39.9 |
| ('easyocr', 'baseline', 'partial')       |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           4.5 |
| ('easyocr', 'baseline', 'synthetic')     |     14.0 |    85.2 |   100.5 |           5.0 |         0.0 |         28.6 |         42.9 |            0.0 |          40.5 |
| ('easyocr', 'baseline', 'shadow')        |      7.0 |    76.9 |   102.5 |           2.9 |         0.0 |         28.6 |         42.9 |            0.0 |          42.8 |
| ('easyocr', 'baseline', 'tilted')        |      7.0 |    76.9 |   102.5 |           2.9 |         0.0 |         28.6 |         42.9 |            0.0 |          42.8 |
| ('easyocr', 'baseline', 'faded')         |      7.0 |    93.5 |    98.5 |           7.1 |         0.0 |         28.6 |         42.9 |            0.0 |          38.2 |
| ('easyocr', 'baseline', 'perspective')   |      7.0 |    93.5 |    98.5 |           7.1 |         0.0 |         28.6 |         42.9 |            0.0 |          38.2 |
| ('easyocr', 'pre', 'sideways')           |     16.0 |    40.2 |    78.6 |          21.4 |         0.0 |         62.5 |         62.5 |            7.1 |          15.9 |
| ('easyocr', 'pre', 'crumpled')           |     15.0 |    46.8 |    81.3 |          16.0 |         0.0 |         20.0 |         40.0 |            6.7 |          19.8 |
| ('easyocr', 'pre', 'handheld')           |      6.0 |    55.8 |    87.2 |          10.0 |         0.0 |         50.0 |         50.0 |            0.0 |          16.8 |
| ('easyocr', 'pre', 'clean')              |     15.0 |    55.1 |    94.9 |          28.0 |         0.0 |         46.7 |         60.0 |            0.0 |          19.1 |
| ('easyocr', 'pre', 'partial')            |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           4.1 |
| ('easyocr', 'pre', 'synthetic')          |     14.0 |    62.1 |    91.1 |           9.3 |         0.0 |         28.6 |         42.9 |            0.0 |          21.2 |
| ('easyocr', 'pre', 'shadow')             |      7.0 |    52.6 |    85.3 |          12.9 |         0.0 |         28.6 |         42.9 |            0.0 |          24.1 |
| ('easyocr', 'pre', 'tilted')             |      7.0 |    52.6 |    85.3 |          12.9 |         0.0 |         28.6 |         42.9 |            0.0 |          24.1 |
| ('easyocr', 'pre', 'faded')              |      7.0 |    71.5 |    96.9 |           5.7 |         0.0 |         28.6 |         42.9 |            0.0 |          18.4 |
| ('easyocr', 'pre', 'perspective')        |      7.0 |    71.5 |    96.9 |           5.7 |         0.0 |         28.6 |         42.9 |            0.0 |          18.4 |
| ('easyocr', 'pre_post', 'sideways')      |     16.0 |    40.2 |    78.6 |          45.7 |         0.0 |         62.5 |         62.5 |            0.0 |          16.1 |
| ('easyocr', 'pre_post', 'crumpled')      |     15.0 |    46.8 |    81.3 |          34.0 |         0.0 |         20.0 |         40.0 |            0.0 |          20.0 |
| ('easyocr', 'pre_post', 'handheld')      |      6.0 |    55.8 |    87.2 |          30.0 |         0.0 |         50.0 |         50.0 |            0.0 |          16.9 |
| ('easyocr', 'pre_post', 'clean')         |     15.0 |    55.1 |    94.9 |          52.7 |         0.0 |         46.7 |         60.0 |            0.0 |          19.8 |
| ('easyocr', 'pre_post', 'partial')       |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           4.4 |
| ('easyocr', 'pre_post', 'synthetic')     |     14.0 |    62.1 |    91.1 |          26.4 |         0.0 |         28.6 |         42.9 |            0.0 |          21.1 |
| ('easyocr', 'pre_post', 'shadow')        |      7.0 |    52.7 |    85.3 |          30.0 |         0.0 |         28.6 |         42.9 |            0.0 |          24.1 |
| ('easyocr', 'pre_post', 'tilted')        |      7.0 |    52.7 |    85.3 |          30.0 |         0.0 |         28.6 |         42.9 |            0.0 |          24.1 |
| ('easyocr', 'pre_post', 'faded')         |      7.0 |    71.6 |    96.9 |          22.9 |         0.0 |         28.6 |         42.9 |            0.0 |          18.1 |
| ('easyocr', 'pre_post', 'perspective')   |      7.0 |    71.6 |    96.9 |          22.9 |         0.0 |         28.6 |         42.9 |            0.0 |          18.1 |
| ('rapidocr', 'baseline', 'sideways')     |     16.0 |    77.4 |    85.2 |          17.1 |         0.0 |         62.5 |         62.5 |            0.0 |           4.3 |
| ('rapidocr', 'baseline', 'crumpled')     |     15.0 |    71.5 |    83.2 |          27.3 |         7.1 |         20.0 |         40.0 |            6.7 |           5.9 |
| ('rapidocr', 'baseline', 'handheld')     |      6.0 |    64.8 |    80.8 |          28.3 |        20.0 |         50.0 |         50.0 |           16.7 |           4.5 |
| ('rapidocr', 'baseline', 'clean')        |     15.0 |     8.9 |    43.8 |          70.0 |        53.3 |         46.7 |         60.0 |           40.0 |           7.2 |
| ('rapidocr', 'baseline', 'partial')      |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           4.0 |
| ('rapidocr', 'baseline', 'synthetic')    |     14.0 |    78.4 |    88.5 |          25.7 |         8.3 |         28.6 |         42.9 |           14.3 |           6.0 |
| ('rapidocr', 'baseline', 'shadow')       |      7.0 |    65.3 |    80.8 |          31.4 |        14.3 |         28.6 |         42.9 |           28.6 |           6.4 |
| ('rapidocr', 'baseline', 'tilted')       |      7.0 |    65.3 |    80.8 |          31.4 |        14.3 |         28.6 |         42.9 |           28.6 |           6.4 |
| ('rapidocr', 'baseline', 'faded')        |      7.0 |    91.4 |    96.2 |          20.0 |         0.0 |         28.6 |         42.9 |            0.0 |           5.7 |
| ('rapidocr', 'baseline', 'perspective')  |      7.0 |    91.4 |    96.2 |          20.0 |         0.0 |         28.6 |         42.9 |            0.0 |           5.7 |
| ('rapidocr', 'pre', 'sideways')          |     16.0 |    30.4 |    58.7 |          46.4 |        58.3 |         62.5 |         62.5 |           21.4 |           4.8 |
| ('rapidocr', 'pre', 'crumpled')          |     15.0 |    37.0 |    64.4 |          36.7 |        38.5 |         20.0 |         40.0 |           13.3 |           6.4 |
| ('rapidocr', 'pre', 'handheld')          |      6.0 |    47.4 |    75.2 |          23.3 |         0.0 |         50.0 |         50.0 |            0.0 |           5.4 |
| ('rapidocr', 'pre', 'clean')             |     15.0 |    46.7 |    68.2 |          54.7 |        45.2 |         46.7 |         60.0 |           60.0 |           7.9 |
| ('rapidocr', 'pre', 'partial')           |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           4.0 |
| ('rapidocr', 'pre', 'synthetic')         |     14.0 |    50.5 |    76.6 |          24.3 |        27.3 |         28.6 |         42.9 |            7.1 |           6.7 |
| ('rapidocr', 'pre', 'shadow')            |      7.0 |    48.2 |    69.0 |          25.7 |        33.3 |         28.6 |         42.9 |            0.0 |           6.6 |
| ('rapidocr', 'pre', 'tilted')            |      7.0 |    48.2 |    69.0 |          25.7 |        33.3 |         28.6 |         42.9 |            0.0 |           6.6 |
| ('rapidocr', 'pre', 'faded')             |      7.0 |    52.9 |    84.2 |          22.9 |        20.0 |         28.6 |         42.9 |           14.3 |           6.8 |
| ('rapidocr', 'pre', 'perspective')       |      7.0 |    52.9 |    84.2 |          22.9 |        20.0 |         28.6 |         42.9 |           14.3 |           6.8 |
| ('rapidocr', 'pre_post', 'sideways')     |     16.0 |    30.4 |    58.7 |          68.6 |        66.7 |         62.5 |         62.5 |           28.6 |           4.7 |
| ('rapidocr', 'pre_post', 'crumpled')     |     15.0 |    37.0 |    64.4 |          57.3 |        53.8 |         20.0 |         40.0 |           33.3 |           6.2 |
| ('rapidocr', 'pre_post', 'handheld')     |      6.0 |    47.4 |    75.2 |          43.3 |        22.2 |         50.0 |         50.0 |           16.7 |           5.2 |
| ('rapidocr', 'pre_post', 'clean')        |     15.0 |    46.8 |    68.2 |          78.0 |        58.1 |         46.7 |         60.0 |           66.7 |           7.8 |
| ('rapidocr', 'pre_post', 'partial')      |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           3.9 |
| ('rapidocr', 'pre_post', 'synthetic')    |     14.0 |    50.5 |    76.6 |          47.9 |        36.4 |         28.6 |         42.9 |           21.4 |           6.4 |
| ('rapidocr', 'pre_post', 'shadow')       |      7.0 |    48.2 |    69.0 |          51.4 |        50.0 |         28.6 |         42.9 |           28.6 |           6.2 |
| ('rapidocr', 'pre_post', 'tilted')       |      7.0 |    48.2 |    69.0 |          51.4 |        50.0 |         28.6 |         42.9 |           28.6 |           6.2 |
| ('rapidocr', 'pre_post', 'faded')        |      7.0 |    52.9 |    84.2 |          44.3 |        20.0 |         28.6 |         42.9 |           14.3 |           6.5 |
| ('rapidocr', 'pre_post', 'perspective')  |      7.0 |    52.9 |    84.2 |          44.3 |        20.0 |         28.6 |         42.9 |           14.3 |           6.5 |
| ('hybrid', 'baseline', 'sideways')       |     16.0 |    77.4 |    85.2 |          17.1 |         0.0 |         62.5 |         62.5 |            0.0 |           5.6 |
| ('hybrid', 'baseline', 'crumpled')       |     15.0 |    71.5 |    83.2 |          27.3 |         7.1 |         20.0 |         40.0 |            6.7 |           7.7 |
| ('hybrid', 'baseline', 'handheld')       |      6.0 |    64.8 |    80.8 |          28.3 |        20.0 |         50.0 |         50.0 |           16.7 |           5.8 |
| ('hybrid', 'baseline', 'clean')          |     15.0 |     8.9 |    43.8 |          70.0 |        53.3 |         46.7 |         60.0 |           40.0 |          11.0 |
| ('hybrid', 'baseline', 'partial')        |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           4.4 |
| ('hybrid', 'baseline', 'synthetic')      |     14.0 |    78.4 |    88.5 |          25.7 |         8.3 |         28.6 |         42.9 |           14.3 |           7.7 |
| ('hybrid', 'baseline', 'shadow')         |      7.0 |    65.3 |    80.8 |          31.4 |        14.3 |         28.6 |         42.9 |           28.6 |           8.3 |
| ('hybrid', 'baseline', 'tilted')         |      7.0 |    65.3 |    80.8 |          31.4 |        14.3 |         28.6 |         42.9 |           28.6 |           8.3 |
| ('hybrid', 'baseline', 'faded')          |      7.0 |    91.4 |    96.2 |          20.0 |         0.0 |         28.6 |         42.9 |            0.0 |           7.0 |
| ('hybrid', 'baseline', 'perspective')    |      7.0 |    91.4 |    96.2 |          20.0 |         0.0 |         28.6 |         42.9 |            0.0 |           7.0 |
| ('hybrid', 'pre', 'sideways')            |     16.0 |    30.4 |    58.7 |          47.9 |        58.3 |         62.5 |         62.5 |           21.4 |           8.5 |
| ('hybrid', 'pre', 'crumpled')            |     15.0 |    37.0 |    64.4 |          37.3 |        38.5 |         20.0 |         40.0 |           20.0 |          10.5 |
| ('hybrid', 'pre', 'handheld')            |      6.0 |    47.4 |    75.2 |          25.0 |         0.0 |         50.0 |         50.0 |           16.7 |           9.8 |
| ('hybrid', 'pre', 'clean')               |     15.0 |    46.7 |    68.2 |          54.7 |        45.2 |         46.7 |         60.0 |           53.3 |          12.2 |
| ('hybrid', 'pre', 'partial')             |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           4.1 |
| ('hybrid', 'pre', 'synthetic')           |     14.0 |    50.5 |    76.6 |          25.7 |        27.3 |         28.6 |         42.9 |            7.1 |          10.1 |
| ('hybrid', 'pre', 'shadow')              |      7.0 |    48.2 |    69.0 |          25.7 |        33.3 |         28.6 |         42.9 |            0.0 |           9.3 |
| ('hybrid', 'pre', 'tilted')              |      7.0 |    48.2 |    69.0 |          25.7 |        33.3 |         28.6 |         42.9 |            0.0 |           9.3 |
| ('hybrid', 'pre', 'faded')               |      7.0 |    52.9 |    84.2 |          25.7 |        20.0 |         28.6 |         42.9 |           14.3 |          10.9 |
| ('hybrid', 'pre', 'perspective')         |      7.0 |    52.9 |    84.2 |          25.7 |        20.0 |         28.6 |         42.9 |           14.3 |          10.9 |
| ('hybrid', 'pre_post', 'sideways')       |     16.0 |    30.4 |    58.7 |          70.0 |        66.7 |         62.5 |         62.5 |           28.6 |           8.5 |
| ('hybrid', 'pre_post', 'crumpled')       |     15.0 |    37.0 |    64.4 |          58.0 |        53.8 |         20.0 |         40.0 |           33.3 |          10.8 |
| ('hybrid', 'pre_post', 'handheld')       |      6.0 |    47.4 |    75.2 |          45.0 |        22.2 |         50.0 |         50.0 |           16.7 |           9.9 |
| ('hybrid', 'pre_post', 'clean')          |     15.0 |    46.8 |    68.2 |          78.0 |        58.1 |         46.7 |         60.0 |           60.0 |          11.8 |
| ('hybrid', 'pre_post', 'partial')        |     16.0 |   nan   |   nan   |         nan   |       nan   |         62.5 |         68.8 |          nan   |           4.2 |
| ('hybrid', 'pre_post', 'synthetic')      |     14.0 |    50.5 |    76.6 |          49.3 |        36.4 |         28.6 |         42.9 |           21.4 |          10.9 |
| ('hybrid', 'pre_post', 'shadow')         |      7.0 |    48.2 |    69.0 |          51.4 |        50.0 |         28.6 |         42.9 |           28.6 |          10.2 |
| ('hybrid', 'pre_post', 'tilted')         |      7.0 |    48.2 |    69.0 |          51.4 |        50.0 |         28.6 |         42.9 |           28.6 |          10.2 |
| ('hybrid', 'pre_post', 'faded')          |      7.0 |    52.9 |    84.2 |          47.1 |        20.0 |         28.6 |         42.9 |           14.3 |          11.5 |
| ('hybrid', 'pre_post', 'perspective')    |      7.0 |    52.9 |    84.2 |          47.1 |        20.0 |         28.6 |         42.9 |           14.3 |          11.5 |


## By language

|                                      |   images |   CER % |   WER % |   field acc % |   item F1 % |   QR plain % |   QR final % |   consistent % |   sec/receipt |
|:-------------------------------------|---------:|--------:|--------:|--------------:|------------:|-------------:|-------------:|---------------:|--------------:|
| ('tesseract', 'baseline', 'uz_latn') |     51.0 |    93.3 |    96.2 |           3.6 |         0.0 |         45.1 |         56.9 |            0.0 |           5.7 |
| ('tesseract', 'baseline', 'mixed')   |      2.0 |   nan   |   nan   |          40.0 |         0.0 |        100.0 |        100.0 |            0.0 |           1.7 |
| ('tesseract', 'pre', 'uz_latn')      |     51.0 |    47.6 |    81.7 |          14.2 |         0.0 |         45.1 |         56.9 |            0.0 |           7.1 |
| ('tesseract', 'pre', 'mixed')        |      2.0 |   nan   |   nan   |          50.0 |       100.0 |        100.0 |        100.0 |          100.0 |           1.9 |
| ('tesseract', 'pre_post', 'uz_latn') |     51.0 |    47.6 |    81.7 |          46.1 |         6.5 |         45.1 |         56.9 |            0.0 |           7.2 |
| ('tesseract', 'pre_post', 'mixed')   |      2.0 |   nan   |   nan   |          70.0 |       100.0 |        100.0 |        100.0 |          100.0 |           1.8 |
| ('easyocr', 'baseline', 'uz_latn')   |     51.0 |    72.9 |    93.8 |          18.3 |         0.0 |         45.1 |         56.9 |            0.0 |          30.9 |
| ('easyocr', 'baseline', 'mixed')     |      2.0 |   nan   |   nan   |          40.0 |         0.0 |        100.0 |        100.0 |            0.0 |          16.3 |
| ('easyocr', 'pre', 'uz_latn')        |     51.0 |    45.7 |    82.5 |          21.1 |         0.0 |         45.1 |         56.9 |            2.8 |          15.2 |
| ('easyocr', 'pre', 'mixed')          |      2.0 |   nan   |   nan   |          50.0 |         0.0 |        100.0 |        100.0 |            0.0 |           8.3 |
| ('easyocr', 'pre_post', 'uz_latn')   |     51.0 |    45.7 |    82.5 |          43.9 |         0.0 |         45.1 |         56.9 |            0.0 |          15.5 |
| ('easyocr', 'pre_post', 'mixed')     |      2.0 |   nan   |   nan   |          70.0 |         0.0 |        100.0 |        100.0 |            0.0 |           8.4 |
| ('rapidocr', 'baseline', 'uz_latn')  |     51.0 |    63.1 |    77.2 |          44.7 |        26.9 |         45.1 |         56.9 |           19.4 |           5.8 |
| ('rapidocr', 'baseline', 'mixed')    |      2.0 |   nan   |   nan   |          70.0 |         0.0 |        100.0 |        100.0 |          100.0 |           1.4 |
| ('rapidocr', 'pre', 'uz_latn')       |     51.0 |    36.4 |    63.4 |          45.6 |        44.1 |         45.1 |         56.9 |           33.3 |           6.2 |
| ('rapidocr', 'pre', 'mixed')         |      2.0 |   nan   |   nan   |          60.0 |         0.0 |        100.0 |        100.0 |          100.0 |           1.9 |
| ('rapidocr', 'pre_post', 'uz_latn')  |     51.0 |    36.4 |    63.4 |          67.8 |        58.8 |         45.1 |         56.9 |           44.4 |           6.1 |
| ('rapidocr', 'pre_post', 'mixed')    |      2.0 |   nan   |   nan   |          70.0 |         0.0 |        100.0 |        100.0 |          100.0 |           1.9 |
| ('hybrid', 'baseline', 'uz_latn')    |     51.0 |    63.1 |    77.2 |          44.7 |        26.9 |         45.1 |         56.9 |           19.4 |           7.8 |
| ('hybrid', 'baseline', 'mixed')      |      2.0 |   nan   |   nan   |          70.0 |         0.0 |        100.0 |        100.0 |          100.0 |           2.9 |
| ('hybrid', 'pre', 'uz_latn')         |     51.0 |    36.4 |    63.4 |          46.1 |        44.1 |         45.1 |         56.9 |           33.3 |           9.3 |
| ('hybrid', 'pre', 'mixed')           |      2.0 |   nan   |   nan   |          60.0 |         0.0 |        100.0 |        100.0 |          100.0 |           3.1 |
| ('hybrid', 'pre_post', 'uz_latn')    |     51.0 |    36.4 |    63.4 |          68.3 |        58.8 |         45.1 |         56.9 |           41.7 |           9.3 |
| ('hybrid', 'pre_post', 'mixed')      |      2.0 |   nan   |   nan   |          70.0 |         0.0 |        100.0 |        100.0 |          100.0 |           3.1 |


## Error causes (pre_post)

|                                                 |   count |
|:------------------------------------------------|--------:|
| ('easyocr', 'date/time misread')                |       5 |
| ('easyocr', 'digits misread')                   |      10 |
| ('easyocr', 'digits missing/extra')             |       4 |
| ('easyocr', 'digits/amounts misread')           |      10 |
| ('easyocr', 'not found')                        |     106 |
| ('easyocr', 'text misread / wrong span')        |      65 |
| ('easyocr', 'wrong line picked (value of vat)') |       5 |
| ('hybrid', 'date/time misread')                 |       3 |
| ('hybrid', 'digits misread')                    |       6 |
| ('hybrid', 'digits missing/extra')              |       4 |
| ('hybrid', 'digits/amounts misread')            |       6 |
| ('hybrid', 'not found')                         |      58 |
| ('hybrid', 'text misread / wrong span')         |      40 |
| ('rapidocr', 'date/time misread')               |       3 |
| ('rapidocr', 'digits misread')                  |       6 |
| ('rapidocr', 'digits missing/extra')            |       3 |
| ('rapidocr', 'digits/amounts misread')          |       5 |
| ('rapidocr', 'not found')                       |      65 |
| ('rapidocr', 'text misread / wrong span')       |      37 |
| ('tesseract', 'date/time misread')              |       6 |
| ('tesseract', 'digits misread')                 |       6 |
| ('tesseract', 'digits missing/extra')           |       3 |
| ('tesseract', 'digits/amounts misread')         |       8 |
| ('tesseract', 'not found')                      |     116 |
| ('tesseract', 'text misread / wrong span')      |      58 |


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
| r17_a.jpg | pre_post | tesseract | clean             | seller_name    | ERA                                                                            | = 00" 02,                                                                                                                                                                      | text misread / wrong span |
| r17_a.jpg | pre_post | tesseract | clean             | seller_tin     | 31802964140017                                                                 |                                                                                                                                                                                | not found                 |
| r17_a.jpg | pre_post | tesseract | clean             | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy |                                                                                                                                                                                | not found                 |
| r17_a.jpg | pre_post | tesseract | clean             | vat            | 0.0                                                                            |                                                                                                                                                                                | not found                 |
| r17_a.jpg | pre_post | tesseract | clean             | total          | 24000.0                                                                        |                                                                                                                                                                                | not found                 |
| r17_a.jpg | pre_post | tesseract | clean             | payment        | card                                                                           |                                                                                                                                                                                | not found                 |
| r18_a.jpg | pre_post | tesseract | crumpled          | seller_name    | ERA                                                                            | ANVARSON MAXMUDOV DILMUROD OʻGʻLI т                                                                                                                                            | text misread / wrong span |
| r18_a.jpg | pre_post | tesseract | crumpled          | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | Fargʻona viloyati. >, Fargʻona shahri.                                                                                                                                         | text misread / wrong span |
| r02_c.jpg | pre_post | tesseract | sideways          | seller_tin     | 31802964140017                                                                 |                                                                                                                                                                                | not found                 |
| r02_c.jpg | pre_post | tesseract | sideways          | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | Fargʻona viloyati, Fargʻona shahri                                                                                                                                             | text misread / wrong span |
| r02_c.jpg | pre_post | tesseract | sideways          | vat            | 0.0                                                                            | 6.68                                                                                                                                                                           | digits/amounts misread    |
| r03_c.jpg | pre_post | tesseract | sideways          | seller_name    | ERA                                                                            | ЕВА:                                                                                                                                                                           | text misread / wrong span |
| r03_c.jpg | pre_post | tesseract | sideways          | address        | Farg'ona viloyati, Farg'ona shahri, Barkamol MFY, Yangi asr ko'chasi, 118 b uy | Fargʻona viloyati, Fargʻona shahri, Barkamol MFY, Yangi asi, koʻchasi, 118 b uy, Yur. Mana il Fargʻona viloyati, Fargʻona shahri., Barkamol MFY, Yangi asr, koʻchasi. 118 b uy | text misread / wrong span |
| r03_c.jpg | pre_post | tesseract | sideways          | payment        | card                                                                           | other                                                                                                                                                                          | text misread / wrong span |
| r11_c.jpg | pre_post | tesseract | clean             | seller_name    | ERA                                                                            | вртлорб1                                                                                                                                                                       | text misread / wrong span |