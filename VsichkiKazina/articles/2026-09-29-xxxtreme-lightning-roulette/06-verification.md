# 06 — VERIFICATION · XXXtreme Lightning Roulette (Evolution): как се играе, множители и RTP

STATUS: for human sign-off before publish. FLAGS STAY IN THE TEXT — this file only helps you verify fast.
Type: guide (live game explainer) · byline: Георги Тодоров · gate: PASS 93/100 · humanisation: HUMAN-LIKE (external check offline) · run date: 29.09.2026
Surviving flags (as in-text version-dependence cautions): [VERIFY] 3 · [DATA NEEDED] 0 · [CONFLICT] 0.

## Surviving flags (left IN the body as prose cautions per house rules)
1. [VERIFY] Базови множители 50x–500x и таван 2000x само чрез Double Strike (лента 600x–2000x) — точните дискретни стойности зависят от версията. §„Множителите и орязаното изплащане" + §„Chain Lightning и Double Strikes" + caption.
2. [VERIFY] Печеливш стрейт-ъп на нещастливо число плаща 19:1 (спрямо 29:1 при базовата Lightning Roulette и 35:1 нормално) — source/version-dependent. §„Множителите и орязаното изплащане".
3. [VERIFY] RTP ≈ 97,10% (стрейт-ъп, множител-eligible) / ≈ 97,30% (останалите залози) — провери в информацията на играта. §„RTP: зависи от залога".

Note: max-win € cap и точна дължина на прозореца за залагане НЕ бяха намерени в достъпните източници → deliberately НЕ се твърдят. Launch 2022 corroborated (research corrected assumed 2021) → stated, not flagged.

## External checks (finalized by orchestrator)
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402, probed live 29.09). gemini=skipped. Initial draft stands as final 05b. See 07-gemini-check-1.md.
- Images (Step 8): 1 hand-authored SVG infographic (Lightning numbers + multipliers + reduced payout + RTP; numbers verbatim to 05b). AI hero SKIPPED (402). Image review SKIPPED (402); manual integrity PASSED. images: 1. See 08-image-review-1.md.

Body word count: ~1030 (prose, excluding Title/Meta, ALT/caption, footer). Within the 1000–1800 guide band.

## SOURCES REACHED (29.09.2026)
- LiveCasinoComparer — XXXtreme Lightning Roulette (1–5 Lightning Numbers, Chain Lightning ≤10, Double Strikes 600x–2000x, multipliers 50x–500x, straight-up 19:1, RTP 97,10% straight-up / 97,30% other): https://www.livecasinocomparer.com/live-casino-software/evolution-live-casino-software/evolution-roulette/xxxtreme-lightning-roulette/
- Casino.org / CasinoScores — how to play XXXtreme Lightning Roulette (Chain Lightning, Double Strikes, 19:1, RTP 97,10%): https://www.casino.org/casinoscores/blog/how-to-play-xxxtreme-lightning-roulette/
- Evolution official — XXXtreme Lightning Roulette (single-zero, Lightning + Chain Lightning ≤10, Double Strikes до 2000x): https://games.evolution.com/live-casino/live-roulette/xxxtreme-lightning-roulette/
- SlotCatalog — XXXtreme Lightning Roulette (release 2022, max multiplier 2000x, RTP 97,30% other bets): https://slotcatalog.com/en/slots/Xxxtreme-Lightning-Roulette

## EVERY SPECIFIC FIGURE → SOURCE
| Figure in body | Value | Source / status |
|---|---|---|
| Маса | европейска рулетка, 1–36 + една нула | Evolution; LiveCasinoComparer |
| Щастливи числа/рунд | 1–5; Chain Lightning общо ≤10 | Evolution; LiveCasinoComparer; Casino.org |
| Базови множители | 50x–500x | LiveCasinoComparer; Casino.org — [VERIFY] точни стойности |
| Double Strikes / таван | повторен удар → 600x–2000x; таван 2000x | всичките 4 източника — [VERIFY] band |
| Стрейт-ъп базово изплащане | 19:1 (база LR 29:1; нормално 35:1) | LiveCasinoComparer; Casino.org — [VERIFY] |
| RTP стрейт-ъп | ≈ 97,10% | LiveCasinoComparer; Casino.org — [VERIFY] |
| RTP други залози | ≈ 97,30% (стандартна европейска) | LiveCasinoComparer; SlotCatalog — [VERIFY] |
| Launch | 2022 | SlotCatalog; LiveCasinoComparer — corroborated |

## NOT USED (avoid fabrication)
- Max-win € cap → NOT FOUND → не се твърди.
- Дължина на прозореца за залагане → NOT FOUND → не се твърди.
- Точен дискретен списък с всички множителни стойности → представен като стъпки 50x–500x + лента 600x–2000x, не като фиксирана таблица.
- „Проследяване на горещи числа/система" → изрично оборено в текста, не като работещо.

## RECALCULATION (with working)
- RTP на €100 (стрейт-ъп): 100 × 0,9710 = €97,10 връщане; загуба €2,90. ✓ Body: „към €97".
- Посока на RTP: множител-eligible стрейт-ъп 97,10% < външен залог 97,30% → залогът с шанс за множител връща по-малко. ✓ Логично, защото орязаното 19:1 тежи повече от рядкия множител.
- Монотонност на разреза: 19:1 (XXXtreme) < 29:1 (база LR) < 35:1 (нормално) → по-висок таван (2000x vs 500x) е платен от по-дълбок разрез. ✓
- SVG numbers ⊂ body numbers: 1–36, една нула, 1–5, 10, 50x, 500x, 600x, 2000x, 35:1, 29:1, 19:1, 97,10%, 97,30%. Verified programmatically. ✓

## COMPLIANCE SPOT-CHECK
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-text + footer). ✓
- RG signposting: /otgovorna-igra/ + регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66. ✓
- Афилиейт footer (1 август 2026 режим), заявление подадено/очаква — БЕЗ издаден лиценз, БЕЗ измислен №. ✓
- Game explainer: NO BG operator names, NO НАП licence №, NO tax, NO bonus terms, NO affiliate links. Evolution само като maker. ✓
- Byline Георги Тодоров; „Всички Казина" правилно. ✓ Zero em-dashes. ✓
- Internal links (live in sitemap): /kazino-igri/kazino-na-zhivo/, /blog/live-game-shows/, /kak-ocenyavame/, /otgovorna-igra/. ✓

## ANTI-CANNIBALIZATION (Step-6 human check)
XXXtreme Lightning Roulette live game-show spoke. Distinct primary kw (xxxtreme lightning roulette / екстрийм лайтнинг рулетка) и по-високи множители (до 2000x чрез Chain Lightning + Double Strikes) от базовата Lightning Roulette (vk-0186, до 500x, стрейт-ъп 29:1). Базовата = fold-in / вътрешна връзка, не конкурент. Distinct и от Lightning Baccarat (vk-0199), Lightning Dice (vk-0202), Lightning Blackjack (vk-0208).

## HUMAN-ACTION LIST
1. Попълни „[About Всички Казина boilerplate]" слота.
2. Разреши 3-те [VERIFY]: множители/таван, стрейт-ъп изплащане 19:1, RTP по вид залог — провери в информацията на конкретната маса/версия на Evolution.
3. Потвърди афилиейт-лицензния статус на сайта при публикуване (подадено/очаква; никога „издаден").
