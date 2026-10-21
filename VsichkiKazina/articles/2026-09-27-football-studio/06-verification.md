# 06 — VERIFICATION · Football Studio (Evolution): как се играе и RTP

STATUS: for human sign-off before publish. FLAGS STAY IN THE TEXT — this file only helps you verify fast.
Type: guide (live game explainer) · byline: Георги Тодоров · gate: PASS 92/100 · humanisation: HUMAN-LIKE (external check offline) · run date: 27.09.2026
Surviving flags: [VERIFY] 3 · [DATA NEEDED] 0 · [CONFLICT] 0.

## Surviving flags (left IN the body per house rules)
1. [VERIFY] Брой тестета = осем, без жокери — провери за конкретната маса. §„Как протича един рунд".
2. [VERIFY] Продължителност на рунд ≈ 25 сек. §„Как протича един рунд".
3. [VERIFY] RTP на Home/Away ≈ 96,27% — един източник (BetMGM) посочва ≈ 95,27%; провери в информацията на играта. §„RTP…".

## External checks (finalized by orchestrator)
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402, probed live). gemini=skipped. Initial draft stands as final 05b. See 07-gemini-check-1.md.
- Images (Step 8): 1 hand-authored SVG infographic (залози + изплащания + RTP/предимство + честота на равенство; numbers verbatim to 05b). AI hero SKIPPED (402). Image review SKIPPED (402); manual integrity PASSED. images: 1. See 08-image-review-1.md.

Body word count: ~1008 (prose, excluding Title/Meta, ALT/caption, footer). Within the 1000–1800 guide band.

## SOURCES REACHED (27.09.2026)
- CasinoBloke — Evolution Live Football Studio (8 тестета без жокери; 2 най-ниска/асо най-високо; половин залог при равенство; Home/Away 1:1; Draw 11:1; RTP 96,27%/89,64%): https://www.casinobloke.com/live-dealer/evolution-live-football-studio/
- Casinolandia — Football Studio (Home/Away 1:1, Draw 11:1; RTP 96,27% предимство 3,73%; Draw 89,64% предимство 10,36%): https://casinolandia.com/live-games/football-studio-by-evolution-gaming/
- LiveCasinoComparer — Evolution Live Football Studio (разработена за Световното 2018; „същата игра като Дракон Тигър с друга кожа"): https://www.livecasinocomparer.com/news/evolution-live-football-studio/
- BetMGM blog — Football Studio (подредба асо високо/2 ниско; рунд ≈ 25 сек; RTP бележка 95,27% — outlier): https://casino.betmgm.com/en/blog/money-slots/football-studio/

## EVERY SPECIFIC FIGURE → SOURCE
| Figure in body | Value | Source / status |
|---|---|---|
| Пусната | 2018 (за Световното) | livecasinocomparer.com; casinobloke.com |
| Тестета | 8, без жокери | casinobloke.com — [VERIFY] |
| Подредба | 2 най-ниска, асо най-високо | casinobloke.com; betmgm.com |
| Home / Away изплащане | 1:1 | casinolandia.com; casinobloke.com |
| Draw изплащане | 11:1 | casinolandia.com; casinobloke.com; livecasinocomparer.com |
| Равенство за Home/Away | връща се половин залог | casinobloke.com; betmgm.com; livecasinocomparer.com |
| RTP Home/Away | ≈ 96,27% (предимство ≈ 3,73%) | casinolandia.com; casinobloke.com — [VERIFY] (BetMGM 95,27%) |
| RTP Draw | ≈ 89,64% (предимство ≈ 10,36%) | casinolandia.com; casinobloke.com |
| Честота на равенство | ≈ 7,5% | изведено (31/415 при 8 тестета = 0,0747; съвпада с 12×0,0747−1 = −0,1036) |
| Рунд | ≈ 25 сек | betmgm.com — [VERIFY] |
| Семейство | премяна на Дракон Тигър | livecasinocomparer.com |

## NOT USED (avoid fabrication)
- Конкретни min/max лимити → операторо-зависими, не се твърдят.
- „Два водещи" → източниците описват един спортен коментатор; твърди се неутрално „водещ".
- Wizard of Odds числа за „Football Studio DICE" (2,25%/4,32%) → ДРУГА игра; ИЗКЛЮЧЕНИ.
- BetMGM 95,27% → малцинствен outlier; тялото използва доминиращото 96,27% + [VERIFY].

## RECALCULATION (with working)
- Home/Away на €100: 100 × 0,9627 = €96,27 връщане; загуба €3,73 (= домашно предимство 3,73%). ✓
- Draw на €100: 100 × 0,8964 = €89,64 връщане; загуба €10,36 (≈ 2,8× спрямо 3,73%; „близо три пъти"). ✓
- Draw честота: 31/415 ≈ 0,0747 (7,47% ≈ 7,5%). Честна цена ≈ 12:1; предложено 11:1 → 11×0,0747 − 1 = −0,1786 върху залога само-печалба; RTP на Draw = 12×0,0747 = 0,8964 (89,64%). ✓
- Home/Away edge проверка: P(win)=P(lose)=(1−0,0747)/2=0,4627; EV=0,4627−0,4627−0,5×0,0747=−0,0374 → RTP 96,26% ≈ 96,27%. ✓
- SVG numbers ⊂ body numbers: 96,27 / 3,73 / 89,64 / 10,36 / 11:1 / 1:1 / 7,5%. Verified programmatically. ✓

## COMPLIANCE SPOT-CHECK
- RG marker verbatim (in-text + footer). ✓ · RG signposting /otgovorna-igra/ + НАП регистър + „Солидарност". ✓
- Афилиейт footer (1 август 2026), заявление подадено/очаква — БЕЗ издаден лиценз/№. ✓
- Game explainer: NO BG operator, NO НАП №, NO tax, NO bonus terms, NO affiliate links. Evolution само maker. ✓
- Byline Георги Тодоров; „Всички Казина". ✓ Zero em-dashes. ✓
- Internal links (live): /blog/live-game-shows/, /kazino-igri/kazino-na-zhivo/, /kak-ocenyavame/, /otgovorna-igra/. (Дракон Тигър vk-0175 непубликуван → споменат без линк.) ✓

## ANTI-CANNIBALIZATION (Step-6 human check)
Football Studio live game-show spoke. Distinct primary kw (football studio / футбол студио) от Bac Bo (vk-0197), колелата, лото (Mega Ball), case (Deal or No Deal), стълба (Cash or Crash). Семейство висока карта (Дракон Тигър) — споменато като контекст, не дублира (Дракон Тигър е драфт vk-0175, различна тема/keyword).

## HUMAN-ACTION LIST
1. Попълни „[About Всички Казина boilerplate]" слота.
2. Разреши 3-те [VERIFY]: брой тестета, време на рунд, RTP Home/Away (96,27 vs 95,27).
3. Когато Дракон Тигър (vk-0175) се публикува, обмисли добавяне на вътрешен линк от секцията „семейството на високата карта".
4. Потвърди афилиейт-лицензния статус при публикуване (подадено/очаква; никога „издаден").
