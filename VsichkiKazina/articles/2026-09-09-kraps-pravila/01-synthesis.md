# 01-SYNTHESIS — vk-0029 · Крапс (зарове)

Sources: Wizard of Odds craps appendix (house-edge table, authoritative), PokerNews (odds bet + true-odds payouts), Venetian/WinStar (rules). Всяка house-edge стойност от една вътрешно консистентна таблица (WoO); правилата потвърдени ≥2 източника.

## Seed thesis
Крапс изглежда хаотичен, но опира до един рунд (come-out → точка → 7-или-точка) и няколко залога. Честният ъгъл: изборът на залог мести предимството от <1% (pass/don't pass + odds) до >15% (Any 7). Разясни кой е добрият избор и защо центърът на масата е капан.

## Verified constants
- Pass 1.414% · Don't pass 1.364% (bar 12) · Come 1.414 / Don't Come 1.364.
- Odds bet 0.00%; true odds 4/10=2:1, 5/9=3:2, 6/8=6:5; pass+2x ~0.57%, don't pass+2x ~0.46%.
- Place 6/8 1.515% · 5/9 4.0% · 4/10 6.667%.
- Field 2.778% (12 @3:1) / 5.556% (12 @2:1).
- Any 7 16.667% · Any Craps 11.111% · hard 4/10 11.111% · hard 6/8 9.091%.

## Flags
0 in-text blocking. Всички числа публична игрална математика (WoO), не оператор-специфични → 0 [VERIFY] в текста. Don't pass двойна конвенция (1.36% vs 1.40%) отбелязана честно в 06.
