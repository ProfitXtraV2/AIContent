# 06 — VERIFICATION · vk-0193 · Mega Ball (Evolution)

STATUS: for human sign-off before publish.
Surviving flags: [VERIFY] 3 · [DATA NEEDED] 0 · [CONFLICT] 0.
1. [VERIFY] Обявен RTP по версия: 95,40% (мнозинство) срещу ~95,05% (GMBLRS; LiveCasinoComparer диапазон 95,05–95,40%); една ранна оценка до 94,61%. Тялото сочи 95,40% — §„RTP е 95,40%…".
2. [VERIFY] Пул топки 51 срещу 52 (casinos.com) — §„Как протича един рунд".
3. [VERIFY] Максимум карти 200 срещу 400 (casinos.com) — §„Как протича един рунд".
Трите остават В тялото по правилата (един [VERIFY] не блокира публикация; човек ги решава на Step 6). Никаква Version A/B структура в прозата.

## External checks (finalized by orchestrator)
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402). gemini=skipped. Първоначалният драфт остава като финал 05b. Виж 07-gemini-check-1.md.
- Images (Step 8): 1 ръчно авторска SVG инфографика (карти/линии + топки + множител + RTP/домашно предимство + таван; числа verbatim към 05b).
  AI hero SKIPPED (402). Image review SKIPPED (402); ръчна интегритет-проверка PASS. images: 1. Виж 08-image-review-1.md.

Body word count: ~957 (проза, без Title/Meta, ALT/caption, footer). В целевата guide лента (~950–1300).

## SOURCES REACHED (27.09.2026)
- Evolution — Mega Ball (продуктова страница): https://games.evolution.com/game/mega-ball/
- LiveCasinoComparer — Evolution Mega Ball Review: https://www.livecasinocomparer.com/live-casino-software/evolution-live-casino-software/evolution-live-mega-ball/
- casinos.com — Mega Ball: https://www.casinos.com/games/mega-ball
- casinobloke — Mega Ball (95.40% RTP): https://www.casinobloke.com/game-shows/mega-ball/
- GMBLRS — Mega Ball (RTP 95.05%): https://www.gmblrs.com/game-provider/evolution-gaming/mega-ball
- SlotCatalog / gg.co.uk — First Person Mega Ball (95.40% RTP): вторични потвърждения.

## EVERY SPECIFIC FIGURE → SOURCE
| Figure in body | Value | Source / status |
|---|---|---|
| Производител / година | Evolution, 2020 | Evolution; casinos.com; LiveCasinoComparer (юни 2020) |
| Решетка на картата | 5 на 5, 24 числа + свободен център | LiveCasinoComparer; casinos.com |
| Линии на карта | 12 | LiveCasinoComparer; casinos.com; изведено (5+5+2) |
| Изтеглени топки | 20 | всички източници |
| Пул топки | 51 | LiveCasinoComparer + мнозинство; casinos.com дава 52 → [VERIFY] |
| Максимум карти | 200 | LiveCasinoComparer + мнозинство; casinos.com дава 400 → [VERIFY] |
| Цена на карта | €0,10 – €100 | LiveCasinoComparer |
| Допълнителна Mega Ball | 1 (понякога до 2 бонус) | LiveCasinoComparer; casinos.com |
| Множител | 5x – 100x | всички източници |
| Обявен RTP | ≈ 95,40% | LiveCasinoComparer/casinos.com/casinobloke/gg → [VERIFY] по версия (95,05%) |
| Домашно предимство | ≈ 4,60% | изведено (100 − 95,40) |
| €100 връщане | ≈ €95,40 / масата задържа €4,60 | изведено (100 × RTP) |
| Пример карти | 5×€1=€5 → €0,23; 200×€1=€200 → €9,20 | изведено (залог × 4,60%) |
| Волатилност | висока | LiveCasinoComparer; casinos.com |
| Таван на печалбата | 500 000 € на рунд | LiveCasinoComparer; casinos.com; casinobloke |

## NOT USED (avoid fabrication)
- Коефициенти по брой линии (1x … 10 000x–100 000x при 6+ линии, casinos.com) → не смесени в тялото; източниците се разминават, оставен само твърдият таван 500 000 €.
- Ранната по-ниска RTP оценка (94,61%) → не написана като отделна стойност; обхваната от [VERIFY] предупреждението за версия.
- Оператори/бонуси/НАП/данъци → извън обхвата (provider explainer).

## RECALCULATION (with working)
- Линии: 5 + 5 + 2 = 12. ✓
- Домашно предимство: 100 − 95,40 = 4,60%. ✓
- €100 × 0,9540 = €95,40 върнати; €100 − €95,40 = €4,60 задържани. ✓
- 5 × €1 = €5; €5 × 0,046 = €0,23. 200 × €1 = €200; €200 × 0,046 = €9,20. ✓

## INTERNAL LINKS USED (4 distinct, всички live 27.09.2026)
1. /kazino-igri/kazino-na-zhivo/ — „казино на живо" (§intro и §6)
2. /blog/live-game-shows/ — „живите шоу формати" (§intro) [hub]
3. /otgovorna-igra/ — „инструментите за отговорна игра" (§6, RG)
4. /kak-ocenyavame/ — „публична методика, а не от усещане" (§6, methodology)

## HUMAN CHECK BEFORE PUBLISH
- ПОТВЪРДИ обявения RTP (95,40% срещу 95,05%), пула топки (51/52) и максимума карти (200/400) за конкретната версия/маса — реши трите [VERIFY].
- Без оператор, без НАП/данъчно твърдение, без бонус условия, без афилиейт — коректно за обяснител на игра (Evolution = само производител).
- Спица на /blog/live-game-shows/; различен от Dream Catcher (vk-0189, колело) — тук лотария/бинго.
- Попълни [About Всички Казина boilerplate] + [author-bio] при публикуване.
