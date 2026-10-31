# 06 — VERIFICATION · Lightning Dice (Evolution): как се играе, множители и RTP

STATUS: for human sign-off before publish. FLAGS STAY IN THE TEXT — this file only helps you verify fast.
Type: guide (live game explainer) · byline: Георги Тодоров · gate: PASS 93/100 · humanisation: HUMAN-LIKE (external check offline) · run date: 28.09.2026
Surviving flags (as in-text version-dependence cautions): [VERIFY] 3 · [DATA NEEDED] 0 · [CONFLICT] 0.

## Surviving flags (left IN the body as prose cautions per house rules)
1. [VERIFY] Базова таблица за изплащания (3/18=149:1 … 10/11=4:1) — зависи от версията/масата. §„Какво плаща всяко число" + caption.
2. [VERIFY] Светкавични множители 5x–1000x, 1000x само на 3/18, 500x на 4/17, върху 2–4 числа/рунд. §„Как работят светкавиците" + caption.
3. [VERIFY] RTP ≈ 96,21% (залог 3/18) / ≈ 96,03% (останалите); домашно предимство ≈ 3,8–4% — провери в информацията на играта. §„RTP и реалната цена".

Note: launch year deliberately OMITTED (sources conflict: LCC „May 2023" vs други) — not fabricated, not flagged.

## External checks (finalized by orchestrator)
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402, probed live 28.09). gemini=skipped. Initial draft stands as final 05b. See 07-gemini-check-1.md.
- Images (Step 8): 1 hand-authored SVG infographic (payout ladder + lightning multipliers + RTP; numbers verbatim to 05b). AI hero SKIPPED (402). Image review SKIPPED (402); manual integrity PASSED. images: 1. See 08-image-review-1.md.

Body word count: ~1014 (prose, excluding Title/Meta, ALT/caption, footer). Within the 1000–1800 guide band.

## SOURCES REACHED (28.09.2026)
- LiveCasinoComparer — Lightning Dice (три зара/кула, базова таблица, светкавици 2–4 числа, RTP 96,21%): https://www.livecasinocomparer.com/live-casino-software/evolution-live-casino-software/live-lightning-dice/
- casinos.com — Lightning Dice (multipliers up to 1000x on 3/18, 500x on 4/17, RTP 96,21% / 96,03%): https://www.casinos.com/games/lightning-dice
- SlotCatalog — Lightning Dice (Evolution Gaming) game info: https://slotcatalog.com/en/slots/Lightning-Dice

## EVERY SPECIFIC FIGURE → SOURCE
| Figure in body | Value | Source / status |
|---|---|---|
| Диапазон на залога | сбор 3–18, 16 опции | livecasinocomparer.com; casinos.com |
| Базови изплащания | 149:1 / 49:1 / 24:1 / 14:1 / 9:1 / 6:1 / 5:1 / 4:1 | livecasinocomparer.com — [VERIFY] version-dependent |
| Светкавици/рунд | 2–4 числа | livecasinocomparer.com |
| Множители | 5x–1000x; 1000x на 3/18; 500x на 4/17 | casinos.com; livecasinocomparer.com — [VERIFY] |
| RTP | ≈ 96,21% (3/18); ≈ 96,03% (останалите) | casinos.com — [VERIFY] |
| Домашно предимство | ≈ 3,8–4% | derived from RTP — [VERIFY] |
| Комбинаторика | 216 общо; 3 и 18 по 1 начин (≈0,46%); 10 и 11 по 27 начина (12,5%) | computed (basic combinatorics) — verifiable, not flagged |

## NOT USED (avoid fabrication)
- Точен min/max лимит на залога → операторо-зависим, не се твърди.
- Launch year → conflicting sources → omitted.
- „Стратегии по горещи числа" от таблото → изрично оборени в текста (заровете нямат памет), не се представят като работещи.

## RECALCULATION (with working)
- RTP на €100 (3/18): 100 × 0,9621 = €96,21 връщане; загуба €3,79 (= домашно предимство 3,79%). ✓ Body казва „около €96 … около €4". ✓
- Комбинаторика: 3 дав. 216 равновероятни изхода. Сбор 3 = {1,1,1} = 1 начин; сбор 18 = {6,6,6} = 1 начин → 1/216 ≈ 0,463%. Сбор 10 = 27 начина, сбор 11 = 27 начина → 27/216 = 12,5%. ✓ Стълбицата на изплащанията е монотонна спрямо рядкостта (най-редките плащат най-много). ✓
- SVG numbers ⊂ body numbers: 149:1 / 49:1 / 24:1 / 14:1 / 9:1 / 6:1 / 5:1 / 4:1 / 5x / 500x / 1000x / 96,21% / 96,03% / 3,8–4%. Verified programmatically. ✓

## COMPLIANCE SPOT-CHECK
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-text + footer). ✓
- RG signposting: /otgovorna-igra/ + регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66. ✓
- Афилиейт footer (1 август 2026 режим), заявление подадено/очаква — БЕЗ издаден лиценз, БЕЗ измислен №. ✓
- Game explainer: NO BG operator names, NO НАП licence №, NO tax, NO bonus terms, NO affiliate links. Evolution само като maker. ✓
- Byline Георги Тодоров; „Всички Казина" правилно. ✓ Zero em-dashes. ✓
- Internal links (live in sitemap): /kazino-igri/kazino-na-zhivo/, /blog/live-game-shows/, /kak-ocenyavame/, /otgovorna-igra/. ✓

## ANTI-CANNIBALIZATION (Step-6 human check)
Lightning Dice live game-show spoke. Distinct primary kw (lightning dice / лайтнинг дайс) от Super Sic Bo (богато меню + множители по позиции), от Сик Бо правила пилар (vk-0174, непубликуван), от Bac Bo (vk-0197, зарова бакара), Lightning Roulette (vk-0186), Lightning Baccarat (vk-0199). Един вид залог (сборът) — механично различна.

## HUMAN-ACTION LIST
1. Попълни „[About Всички Казина boilerplate]" слота.
2. Разреши 3-те [VERIFY]: базова таблица, множители, RTP/предимство (провери в информацията на конкретната маса/версия на Evolution).
3. Потвърди афилиейт-лицензния статус на сайта при публикуване (подадено/очаква; никога „издаден").
