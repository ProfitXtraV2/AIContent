# 06 — VERIFICATION · Side Bet City (Evolution): как се играе и RTP

STATUS: for human sign-off before publish. FLAGS STAY IN THE TEXT — this file only helps you verify fast.
Type: guide (live game explainer) · byline: Георги Тодоров · gate: PASS 93/100 · humanisation: HUMAN-LIKE (external check offline) · run date: 29.09.2026
Surviving flags (as in-text version-dependence cautions): [VERIFY] 2 · [DATA NEEDED] 0 · [CONFLICT] 0.

## Surviving flags (left IN the body as prose cautions per house rules)
1. [VERIFY] Изплащания по ръка (3/5/7 карти) и „All Lose" 0,70:1 — version/operator-dependent, дадени примерно (WoO + LiveCasinoComparer съвпадат). §„Трите залога и какво плащат" + §„Как протича един рунд" + caption.
2. [VERIFY] RTP по вид залог ≈ 96,69% (3 карти) / ≈ 96,29% (All Lose) / ≈ 95,21% (5 карти) / ≈ 94,34% (7 карти) — провери в информацията на играта. §„RTP: кой залог връща най-много".

Note: „All Lucky Ladies" НЕ съществува в тази игра (то е блекджек страничен залог) → НЕ се споменава; четвъртият залог е „All Lose". Launch 2019 (Evolution PR 27.06.2019) → stated, not flagged. Operator max-bet → NOT stated (max win multiplier 1000x чрез 5-картов роял флош).

## External checks (finalized by orchestrator)
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402, probed live 29.09). gemini=skipped. Initial draft stands as final 05b. See 07-gemini-check-1.md.
- Images (Step 8): 1 hand-authored SVG infographic (RTP by bet + headline payouts + All Lose; numbers verbatim to 05b). AI hero SKIPPED (402). Image review SKIPPED (402); manual integrity PASSED. images: 1. See 08-image-review-1.md.

Body word count: ~1010 (prose, excluding Title/Meta, ALT/caption, footer). Within the 1000–1800 guide band.

## SOURCES REACHED (29.09.2026)
- Wizard of Odds — Side Bet City (paytables 3/5/7, house edge → RTP 96,69% / 95,21% / 94,34%, All Lose 96,29%): https://wizardofodds.com/games/side-bet-city/
- LiveCasinoComparer — Side Bet City (paytables, RTP by bet, single deck reshuffled each round, release Jun 2019): https://www.livecasinocomparer.com/live-casino-software/evolution-live-casino-software/evolution-side-bet-city/
- Evolution official press release — Side Bet City (3/5/7 + All Lose bet structure; launch 27 Jun 2019): https://www.evolution.com/investors/financial-publications/press-releases/evolutions-80s-themed-side-bet-city-extends-live-poker-line-up-c15fffd0
- Casinobloke — Side Bet City (RTP, single deck reshuffled, "no separate side bets"): https://www.casinobloke.com/live-dealer/live-poker-side-bet-city/

## EVERY SPECIFIC FIGURE → SOURCE
| Figure in body | Value | Source / status |
|---|---|---|
| Тесте / раздаване | 1 тесте (52), 7 карти, reshuffle всеки рунд | WoO; LiveCasinoComparer; Casinobloke |
| Залози | 3 / 5 / 7 карти + All Lose (0,70:1) | Evolution PR; WoO |
| 3-card paytable | чифт 1:1, флош 4:1, кент 5:1, тройка 35:1, стрейт флош 40:1, роял флош 100:1 | WoO; LiveCasinoComparer — [VERIFY] |
| 5-card paytable | JJ+ 1:1, два чифта 4:1, тройка 7:1, кент 25:1, флош 40:1, фул хаус 50:1, каре 100:1, стрейт флош 250:1, роял флош 1000:1 | WoO; LiveCasinoComparer — [VERIFY] |
| 7-card paytable | тройка 3:1, кент 4:1, флош 5:1, фул хаус 7:1, каре 50:1, стрейт флош 100:1, роял флош 500:1 | WoO; LiveCasinoComparer — [VERIFY] |
| RTP по залог | 96,69% / 96,29% / 95,21% / 94,34% | WoO; LiveCasinoComparer; Casinobloke — [VERIFY] |
| Най-голямо изплащане | роял флош 1000:1 (5 карти) = 1000x | LiveCasinoComparer; WoO |
| Launch | 2019 (27.06.2019) | Evolution PR; LiveCasinoComparer — corroborated |

## NOT USED (avoid fabrication)
- „All Lucky Ladies" → НЕ съществува в Side Bet City (блекджек страничен залог) → не се споменава.
- Operator max-bet (напр. €10 000) → operator-dependent → не се твърди.
- Пълните таблици не се представят като „официални фиксирани" → маркирани version-dependent.
- „Стратегия/система" → изрично оборена (залог преди раздаването, случайно тесте), не като работеща.

## RECALCULATION (with working)
- RTP ordering: 96,69% (3) > 96,29% (All Lose) > 95,21% (5) > 94,34% (7) → монотонно намаляващ с броя карти, които залогът трябва да подреди. ✓ Body твърди същото.
- 3-card логика: в 3 карти кентът е по-рядък от флоша → плаща повече (5:1 > 4:1). ✓
- Най-голямо изплащане: 5-картов роял флош 1000:1 > 7-картов роял флош 500:1 > 3-картов роял флош 100:1. ✓ Body казва „1000:1 … най-голямото изплащане в играта".
- Worked-€: €100 × 0,9669 ≈ €96,69 (3 карти); €100 × 0,9434 ≈ €94,34 (7 карти); разлика ≈ €2,35 на €100 само от избора на залог. ✓ Body: „над €2 на всеки €100".
- SVG numbers ⊂ body numbers: 52, 7, 3/5/7, 0,70:1, 96,69%, 96,29%, 95,21%, 94,34%, 1000:1, 500:1, 100:1. Verified programmatically. ✓

## COMPLIANCE SPOT-CHECK
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-text + footer). ✓
- RG signposting: /otgovorna-igra/ + регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66. ✓
- Афилиейт footer (1 август 2026 режим), заявление подадено/очаква — БЕЗ издаден лиценз, БЕЗ измислен №. ✓
- Game explainer: NO BG operator names, NO НАП licence №, NO tax, NO bonus terms, NO affiliate links. Evolution само като maker. ✓
- Byline Георги Тодоров; „Всички Казина" правилно. ✓ Zero em-dashes. ✓
- Internal links (live in sitemap): /kazino-igri/kazino-na-zhivo/, /blog/live-game-shows/, /kak-ocenyavame/, /otgovorna-igra/. ✓

## ANTI-CANNIBALIZATION (Step-6 human check)
Side Bet City live game-show spoke. Distinct primary kw (side bet city / сайд бет сити) и различна механика от покер пиларите Casino Hold'em (vk-0189), Three Card Poker (vk-0176), Ultimate Texas Hold'em (vk-0178), Teen Patti (vk-0184) — там срещу дилър с решения; тук залог преди раздаването, без дилър/решения. Distinct и от останалите живи формати (колела/зарове/лото/case/стълба).

## HUMAN-ACTION LIST
1. Попълни „[About Всички Казина boilerplate]" слота.
2. Разреши 2-те [VERIFY]: изплащания по ръка + RTP по вид залог — провери в информацията на конкретната маса/версия на Evolution.
3. Потвърди афилиейт-лицензния статус на сайта при публикуване (подадено/очаква; никога „издаден").
