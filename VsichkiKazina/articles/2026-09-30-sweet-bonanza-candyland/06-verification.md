# 06-VERIFICATION — Всички Казина · 2026-09-30-sweet-bonanza-candyland
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Type: guide (live game-show explainer) · byline: Георги Тодоров · gate: PASS 93/100 · humanisation: HUMAN-LIKE (external check offline) · run date: 30.09.2026

## Surviving [VERIFY] flags (stay in body)
**1** in-text [VERIFY]: `[VERIFY: RTP по отделни залози не е официално оповестен]` — точната RTP таблица по всяка позиция. Диапазонът (91.59%–96.83%) и посоката (числа най-високо, features ~91%) са потвърдени от няколко бази; точните проценти по отделните залози не са публикувани открито (вероятно само в gated Client Hub на Pragmatic). 0 [CONFLICT]/[DATA NEEDED].

Хеджирани (не bare [VERIFY]): горната RTP граница (дадена като „91.59% до 96.83%, някои източници до ~96.95%" — разминаване обяснено); волатилност (маркетингов термин → пропуснат, не твърдян); версия на колелото (използвано ТЕКУЩОТО, старото launch-колело с „10" изрично не се ползва). 96.48% е изрично отделено като RTP на СЛОТА, не на шоуто.

## EVERY SPECIFIC FIGURE → SOURCE
| Figure in body | Source | Note |
|---|---|---|
| Provider **Pragmatic Play Live** | pragmaticplay.com/live-casino | |
| Release **24 ноември 2021** | livecasinocomparer | „2019" = слотът, не шоуто. |
| **54 сегмента** | официален; livecasinocomparer; casino.org; casinobloke; monkeytilt | Единодушно. |
| **Число 1: 23 сегм., 1:1, 42.59%** | casino.org; livecasinocomparer stats; monkeytilt | 23/54 = 42.59%. |
| **Число 2: 15 сегм., 2:1, 27.78%** | същите | 15/54 = 27.78%. |
| **Число 5: 7 сегм., 5:1, 12.96%** | същите | 7/54 = 12.96%. |
| **Sugar Bomb: 3 сегм., 5.56% (НЕ bettable)** | casino.org (не bettable); stats | 3/54 = 5.56%. |
| **Bubble Surprise: 3 сегм., 5x/10x/25x, 5.56%** | официален (бонус кръг); casino.org; stats | post-launch feature. |
| **Candy Drop: 2 сегм., до 1000x, 3.70%** | официален (до 1000x); stats | 2/54 = 3.70%. |
| **Sweet Spins: 1 сегм., до 20 000x, 1.85%** | casinobloke (20000x); stats | 1/54 = 1.85%. |
| **6 bettable позиции** | casino.org | Sugar Bomb извън тях. |
| **Sugar Bomb множител 2x–10x + преспин** | официален (до 10x); livecasinocomparer | |
| **Sugar Bomb Booster +25% залог → удвоява множителя** | livecasinocomparer; casinobloke | |
| **Max win 20 000×, таван 500 000 евро** | casinobloke (20000×); официален + livecasinocomparer (€500k cap) | Sweet Spins е пътят. |
| **RTP 91.59%–96.83%** | casino.org/CasinoScores; livecasinocomparer | Зависи и от Booster. |
| **Горна граница ~96.95% (някои източници)** | mrq; fluffyspins | Разминаване → хеджирано. |
| **96.48% = RTP на СЛОТА, не на шоуто** | контекст (слот vk-0018) | Често бъркано. |
| Точна RTP таблица по позиции → [VERIFY] | не публикувана | Виж флаг. |

## RECALCULATION (segment probabilities + SVG numbers ⊂ body)
- Сума: 23+15+7+3+3+2+1 = **54**. ✓
- 23/54 = 0.4259 = **42.59%**; 15/54 = **27.78%**; 7/54 = **12.96%**; 3/54 = **5.56%**; 2/54 = **3.70%**; 1/54 = **1.85%**. ✓ съвпадат с текст/инфографика/източници.
- SVG барове (scale 7.23 px/%): 1 → 308 px; 2 → 201; 5 → 94; SB/BS → 40; CD → 27; SS → 13; всички вътре в 380..688. ✓
- Всички числа/етикети в SVG ⊂ тяло (grep-verbatim, проверено): 54 сегмента, 23, 42.59%, 15, 27.78%, 12.96%, 5.56%, 3.70%, 1.85%, „20 000x", „500 000 евро", 91.59%, 96.83%, 1:1, 2:1, 5:1, „до 1000x", „до 20 000x", „2x до 10x", „5x, 10x или 25x". ✓

## COMPLIANCE SPOT-CHECK (verbatim untouchables)
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — тяло + footer. ✓
- RG signposting: /otgovorna-igra/ + регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 август 2026, ДВ бр. 69), pending-application, БЕЗ issued-licence, БЕЗ измислен №. ✓
- НЯМА BG оператор, НЯМА НАП лиценз №, НЯМА данъчна секция, НЯМА бонус условия на оператор, НЯМА афилиейт линк. ✓
- Byline Георги Тодоров; brand „Всички Казина"; дати 30.09.2026; € / евро. ✓
- Em-dashes (—): 0 в тяло/ALT/caption/SVG. En-dash само числов/времеви. Кавички „..." нормализирани. ✓
- Internal links: 5 от одобрения жив набор (/blog/live-game-shows/, /kazino-igri/kazino-na-zhivo/, /blog/sweet-bonanza/, /kak-ocenyavame/, /otgovorna-igra/). ✓

## ANTI-CANNIBALIZATION note
НОВ live game-show pillar. Distinct primary kw „sweet bonanza candyland / свит бонанза кендиленд". РАЗЛИЧЕН продукт от слота Sweet Bonanza (vk-0018, RNG барабани, RTP 96.48%, 2019) и от game-shows overview (vk-0025, hub) — тази статия е spoke, покрива само колелото, шестте залога, Sugar Bomb и трите бонус кръга. Game-show explainer → без афилиейт линк.

## HUMAN-ACTION LIST (owned by you, Step 6 / Step 8)
1. Попълни „[About Всички Казина boilerplate]" слота.
2. Resolve in-text [VERIFY]: ако имаш достъп до Pragmatic Client Hub, добави точната RTP таблица по позиции; иначе остави диапазона.
3. Потвърди при публикуване, че текущото колело при целевия оператор съвпада с описаното разпределение (54 сегмента, 6 залога, Bubble Surprise вкл.).
4. Потвърди тавана (20 000× / 500 000 евро) и Sugar Bomb Booster механиката спрямо live версията.
5. Потвърди афилиейт-лиценз статуса при публикуване (footer казва подадено/очаква; никога „издаден").
