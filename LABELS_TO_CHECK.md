# Labels to check against the paper receipts

Take each paper receipt, compare it with its row, and fix any wrong value in `data/gt/<id>.json`.
When a receipt is correct, change `"_status": "draft"` to `"_status": "verified"` in its file.
**Most important:** the two rows marked ⚠️ have a digit I could not read through a crease.

| id | shop | date & time | receipt no. | fiscal sign | total | items |
|---|---|---|---|---|---|---|
| r01 | Tinda | 2026-11-04 13:47:26 | 36785 | 352606397030 | 32000 | Keks pishiriq 1×32000 |
| r02 | ERA | 2026-11-05 16:40:02 | 11993 | 930222273403 | 29000 | Aralashmalar 1×29000 |
| r03 | ERA | 2026-11-08 11:02:29 | 12077 | 514092944266 | 21000 | Aralashmalar 1×21000 |
| r04 | AKMAL FARM | 2026-11-03 17:16:32 | 28616 | 823084923002 | 8933.33 | Омиезо капс 20мг №30 (Комомес) 0.333×16000; Аллохол таб №50 0.2×18000 |
| r05 | Tinda | 2026-11-04 18:07:47 | 36800 | 861532066154 | 15700 | Ikkinchi navli un 1×15700 |
| r06 | Tinda | 2026-11-04 18:04:00 | 36799 | 559055341237 | 10000 | Gilos 1×10000 |
| r07 | Tinda | 2026-11-04 20:33:07 | 36811 | 570122841671 | 8000 | Guruch 1×8000 |
| r08 | Tinda | 2026-11-04 21:03:56 | 36812 | 115903172013 | 24000 | Ikkinchi navli un 1×24000 |
| r09 | AKMAL FARM | 2026-11-04 21:18:15 | 28973 | 760014957255 | 4400 | Шприц 5мл Хелф Лайн 1×500; Перчатки стер.хир №7,5 Дентафил 1×3700; Пакет полиэтилен МАЛЕНЬКИЙ ( Андижон 1×200 |
| r10 ⚠️ | Tinda | 2026-11-04 18:31:36 | 36804 | 740250722957 | 5000 | Margarin 1×5000 |
| r11 | ERA | 2026-11-03 17:12:38 | 11917 | 952988211279 | 20000 | Aralashmalar 1×20000 |
| r12 ⚠️ | Tinda | 2026-11-04 18:14:01 | 36801 | 220956006915 | 15000 | Kofe yanchilgan 1×15000 |
| r13 | ERA | 2026-10-31 18:34:21 | 11814 | 438814874366 | 19800 | Aralashmalar 1×19800 |
| r14 | Tinda | 2026-11-03 17:38:16 | 36762 | 532227412590 | 30000 | Xurmo 1×30000 |
| r15 | ERA | 2026-11-02 17:46:10 | 11881 | 272330013324 | 34000 | Aralashmalar 1×34000 |

Notes:
- ⚠️ r10: fiscal sign, 5th digit (`7402?0722957`, I wrote 5).
- ⚠️ r12: fiscal sign, 1st digit (`?20956006915`, I wrote 2).
- r04, r09 (Akmal Farm): seconds of the time and the receipt number come from the QR code (`RS:` on the paper), not from `Chek:`.
- Akmal Farm receipts print no TIN, address or payment type, so those are `null`.
