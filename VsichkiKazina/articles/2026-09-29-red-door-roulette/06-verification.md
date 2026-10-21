# 06 — VERIFICATION · Red Door Roulette (Evolution): как работи бонусът и какъв е RTP

STATUS: for human sign-off before publish. FLAGS STAY IN THE TEXT — this file only helps you verify fast.
Type: guide (live roulette explainer) · byline: Георги Тодоров · gate: PASS 93/100 · humanisation: HUMAN-LIKE (external check offline) · run date: 29.09.2026
Surviving flags (as in-text version-dependence cautions): [VERIFY] 1 · [DATA NEEDED] 0 · [CONFLICT] 0.

## Surviving flags (left IN the body as prose cautions per house rules)
1. [VERIFY] Съставът на 64-сегментното бонус колело и точните множители / таванът 4000x са
   version-dependent (provider snippet + DBs). §„Бонус колелото" + caption („Примерни стойности;
   съставът на сегментите и точните множители зависят от версията и масата").

Deferred / not claimed (kept OUT of the body to avoid a fabricated fact):
- Release date OMITTED: casino.org / SlotCatalog / Evolution point to Nov 2023, LiveCasinoComparer
  says June 2023 (conflict). Not stated in the body → no unresolved claim reaches publish.
- Stake-multiple max-win NOT stated: SlotCatalog conflicts (2000x vs 20000x). Only the robust
  4000x multiplier + €500 000 cash cap are claimed.
- Betting-window length NOT FOUND on reachable sources → omitted (not claimed).

## External checks (finalized by orchestrator)
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402, probed live 29.09). gemini=skipped. Initial draft stands as final 05b. See 07-gemini-check-1.md.
- Images (Step 8): 1 hand-authored SVG infographic (cut payout + keys + bonus wheel + RTP; numbers verbatim to 05b). AI hero SKIPPED (402). Image review SKIPPED (402); manual integrity PASSED. images: 1. See 08-image-review-1.md.

Body word count: ~1040 (prose, excluding Title/Meta, ALT/caption, footer). Within the 1000–1800 guide band.

## SOURCES REACHED (29.09.2026)
- Evolution official — Red Door Roulette (single-zero European; Keys with 2x–20x; Crazy Time-style bonus wheel; up to 4000x): https://games.evolution.com/live-casino/live-roulette/red-door-roulette/
- LiveCasinoComparer — Red Door Roulette (37 pockets; straight-up 19:1; other bets standard 17:1/2:1/1:1; 3–15 bonus numbers with Keys; RTP 97,09%/97,30%; max 4000x; cap 500,000): https://www.livecasinocomparer.com/live-casino-software/evolution-live-casino-software/evolution-roulette/red-door-roulette/
- casino.org / CasinoScores — Red Door Roulette (RTP 97,09%/97,30%; straight-up 19:1; cap €500,000; 4000x): https://www.casino.org/casinoscores/red-door-roulette/
- SlotCatalog — Red Door Roulette (single-zero; 19:1; release 2023; conflicting stake-multiple max-win): https://slotcatalog.com/en/slots/Red-Door-Roulette

## EVERY SPECIFIC FIGURE → SOURCE
| Figure in body | Value | Source / status |
|---|---|---|
| Колело / джобове | 37, една зелена нула (европейска) | Evolution; LiveCasinoComparer; SlotCatalog |
| Стрейт-ъп изплащане | 19:1 (вместо 35:1) | Evolution; LiveCasinoComparer; casino.org; SlotCatalog |
| Останали залози | сплит 17:1; ред/черно 1:1; дузини/колони 2:1 (стандартни) | LiveCasinoComparer |
| Worked-€ пример | €10 стрейт-ъп → €190 при 19:1 (vs €350 при 35:1) | derived: 10×19 и 10×35 |
| Бонус числа / ключове | 3–15 на рунд; влизане само със стрейт-ъп на печелившото число с ключ | Evolution; LiveCasinoComparer; casino.org |
| Базов множител на ключ | 2x–20x | Evolution; LiveCasinoComparer; SlotCatalog |
| Бонус колело | 64 сегмента (стил Crazy Time); Double удвоява всичко + въртене отново | Evolution; LiveCasinoComparer; casino.org — [VERIFY] точен състав/версия |
| Таван множител | до 4000x | Evolution; LiveCasinoComparer; casino.org — [VERIFY] версия |
| Паричен таван | €500 000 на рунд | LiveCasinoComparer; casino.org |
| RTP | 97,09% (стрейт-ъп) / 97,30% (останалите залози) | LiveCasinoComparer; casino.org |
| Домашно предимство | ≈2,9% (стрейт-ъп) / ≈2,7% (други) | derived: 100 − RTP |
| Lightning Roulette (сравнение) | множители 50x–500x; стрейт-ъп 29:1 | internal (vk-0186) |
| XXXtreme Lightning Roulette (сравнение) | таван 2000x | internal (vk-0209) |

## NOT USED (avoid fabrication)
- Точна дата на пускане → conflict (Nov 2023 vs June 2023) → омитната.
- Stake-multiple максимален изход (напр. „2000x/20000x залога") → sources conflict → не се твърди; дадени само 4000x множител + €500 000 паричен таван.
- Прозорец за залагане → NOT FOUND → омитнат.
- „Стратегия за печелене" → изрично оборена (колелото е случайно, изплащането фиксирано).

## RECALCULATION (with working)
- Домашно предимство стрейт-ъп: 100 − 97,09 = 2,91 ≈ „около 2,9%". ✓ Body.
- Домашно предимство други залози: 100 − 97,30 = 2,70 ≈ „около 2,7%". ✓ Body.
- Орязване: стандарт 35:1 → 19:1; играчът получава 20/36 ≈ 55% от нормалната печалба на единично число („почти наполовина по-малко"). ✓ Body.
- Worked-€: €10 × 19 = €190 (19:1) vs €10 × 35 = €350 (35:1). ✓ Body.
- SVG numbers ⊂ body numbers: 37, 19:1, 35:1, 17:1, 1:1, 3–15, 2x–20x, 64, Double, 4000x, €500 000, 97,09%, 97,30%, 2,9%, 2,7% — all present in 05b. Verified programmatically. ✓

## COMPLIANCE SPOT-CHECK
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-text + footer). ✓
- RG signposting: /otgovorna-igra/ + регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66. ✓
- Афилиейт footer (1 август 2026 режим), заявление подадено/очаква — БЕЗ издаден лиценз, БЕЗ измислен №. ✓
- Game explainer: NO BG operator names, NO НАП licence №, NO tax, NO bonus terms, NO affiliate links. Evolution само като maker. ✓
- Byline Георги Тодоров; „Всички Казина" правилно. ✓ Zero em-dashes. ✓
- Internal links (live in sitemap): /kazino-igri/kazino-na-zhivo/, /blog/live-game-shows/, /kak-ocenyavame/, /otgovorna-igra/. ✓

## ANTI-CANNIBALIZATION (Step-6 human check)
Distinct branded live roulette spoke. Различен primary kw (red door roulette / ред дор рулетка) и
механика от Lightning Roulette (vk-0186, множители 50x–500x по числа, стрейт-ъп 29:1) и XXXtreme
Lightning Roulette (vk-0209, таван 2000x). Тук: ключ-условие + отделно Crazy Time-style бонус
колело, най-дълбоко орязан стрейт-ъп (19:1). Различен от рулетка-правила (vk-0024).

## HUMAN-ACTION LIST
1. Попълни „[About Всички Казина boilerplate]" слота.
2. Разреши 1-вия [VERIFY]: точен състав на бонус колелото / таван 4000x — провери в информацията на конкретната маса/версия на Evolution.
3. Потвърди датата на пускане, ако решиш да я добавиш (Nov 2023 vs June 2023 — сега омитната).
4. Потвърди афилиейт-лицензния статус на сайта при публикуване (подадено/очаква; никога „издаден").
