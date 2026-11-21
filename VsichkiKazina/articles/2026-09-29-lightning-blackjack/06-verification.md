# 06 — VERIFICATION · Lightning Blackjack (Evolution): как се играе, множители и RTP

STATUS: for human sign-off before publish. FLAGS STAY IN THE TEXT — this file only helps you verify fast.
Type: guide (live game explainer) · byline: Георги Тодоров · gate: PASS 93/100 · humanisation: HUMAN-LIKE (external check offline) · run date: 29.09.2026
Surviving flags (as in-text version-dependence cautions): [VERIFY] 3 · [DATA NEEDED] 0 · [CONFLICT] 0.

## Surviving flags (left IN the body as prose cautions per house rules)
1. [VERIFY] Множители 2x–25x, по-високите ръце/блекджек дават по-едрите — точните дискретни стойности се разминават по версии, затова са дадени като диапазон. §„Множителите" + caption ("Примерни стойности").
2. [VERIFY] RTP 99,56% е за оптимална стратегия и само първа ръка; ефективно връщане ≈82% / домашно предимство ≈17,6% (спрямо залога) / ≈9% (спрямо залог+такса) — външна аналитична оценка, не оператор-публикувана. §„RTP: рекламното число срещу реалната цена".
3. [VERIFY] Прозорец за залагане ≈15 секунди — single-source/version-dependent. §„Как протича една ръка".

Note: precise operator stake caps (напр. €1–€5000) и точен максимален изход (напр. €187 500) деликатно ОМИТНАТИ (operator/version-dependent, single-source) — не се твърдят.

## External checks (finalized by orchestrator)
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402, probed live 29.09). gemini=skipped. Initial draft stands as final 05b. See 07-gemini-check-1.md.
- Images (Step 8): 1 hand-authored SVG infographic (fee + multipliers + RTP; numbers verbatim to 05b). AI hero SKIPPED (402). Image review SKIPPED (402); manual integrity PASSED. images: 1. See 08-image-review-1.md.

Body word count: ~1010 (prose, excluding Title/Meta, ALT/caption, footer). Within the 1000–1800 guide band.

## SOURCES REACHED (29.09.2026)
- LiveCasinoComparer — Lightning Blackjack (100% Lightning Fee, множители 2x–25x, RTP 99,56% optimal, ефективно ~82,4%, 3:2, betting window ~15s): https://www.livecasinocomparer.com/live-casino-software/evolution-live-casino-software/evolution-live-blackjack/lightning-blackjack/
- Wizard of Odds — Lightning Blackjack (fee = 100% на залога; множител се пренася към следваща печеливша ръка само до размера на предишния залог; house edge 17,63% спрямо залога / 8,82% спрямо всичко заложено): https://wizardofodds.com/games/lightning-blackjack/
- Evolution official — Lightning Blackjack (100% Lightning Fee; множител валиден до 180 дни): https://games.evolution.com/live-casino/live-blackjack/lightning-blackjack/
- casinos.com — Lightning Blackjack (8 тестета, 2x–25x, RTP 99,56%): https://www.casinos.com/games/lightning-blackjack

## EVERY SPECIFIC FIGURE → SOURCE
| Figure in body | Value | Source / status |
|---|---|---|
| Lightning такса | 100% от залога, не се връща | Evolution; Wizard of Odds; LiveCasinoComparer |
| Пример залог | €10 → €20 | derived from 100% fee |
| Множители | 2x–25x; по-високи ръце/блекджек → по-едри | Evolution; LiveCasinoComparer; casinos.com — [VERIFY] точни дискретни стойности |
| Пренос на множителя | само следваща печеливша ръка, до размера на предишния залог; удвояване/разделяне | Wizard of Odds; LiveCasinoComparer |
| Валидност на множителя | до 180 дни | Evolution official |
| Основни правила | 8 тестета; блекджек 3:2 | casinos.com; LiveCasinoComparer |
| Прозорец за залагане | ≈15 секунди | LiveCasinoComparer — [VERIFY] |
| RTP (реклама) | до 99,56% (optimal, първа ръка) | LiveCasinoComparer; casinos.com — [VERIFY] контекст |
| Ефективно връщане | ≈82% (edge ≈17,6% спрямо залога; ≈9% спрямо залог+такса) | Wizard of Odds (17,63%/8,82%) — [VERIFY] analyst calc |
| Класически блекджек | задържа под €1 на €100 (edge ~0,72%) | Wizard of Odds |

## NOT USED (avoid fabrication)
- Точен дискретен списък с множители → sources conflict → представен като диапазон 2x–25x.
- Точни оператор-лимити на залога / максимален изход → operator/version-dependent, не се твърдят.
- „Стратегия/прогресия за печелене" → изрично оборена в текста (раздаването е случайно, таксата фиксирана), не се представя като работеща.

## RECALCULATION (with working)
- Такса: €10 залог × 100% = €10 такса → €20 внесени за рунда. ✓ Body: „Заложиш ли €10, плащаш €20".
- Ефективен RTP/edge: WoO house edge = 17,63% спрямо оригиналния залог → връщане 100 − 17,63 ≈ 82,4% ≈ „около 82%". ✓ Спрямо всичко заложено (залог + равна такса): 17,63% / 2 ≈ 8,82% ≈ „около 9%". ✓
- €-израз: на €100 залог+такса, задържани ≈ 8,82% × 100 ≈ €8,8 ≈ „към €9". ✓ Спрямо само залога: ≈ €17–18. ✓
- Класика: house edge ~0,72% → под €1 на €100. ✓
- SVG numbers ⊂ body numbers: 100%, €10, €20, 2x, 25x, 3:2, 8 тестета, 180 дни, 99,56%, 82%, 17,6%, 9%, €1, €100, €9, €17–18. Verified programmatically. ✓

## COMPLIANCE SPOT-CHECK
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-text + footer). ✓
- RG signposting: /otgovorna-igra/ + регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66. ✓
- Афилиейт footer (1 август 2026 режим), заявление подадено/очаква — БЕЗ издаден лиценз, БЕЗ измислен №. ✓
- Game explainer: NO BG operator names, NO НАП licence №, NO tax, NO bonus terms, NO affiliate links. Evolution само като maker. ✓
- Byline Георги Тодоров; „Всички Казина" правилно. ✓ Zero em-dashes. ✓
- Internal links (live in sitemap): /kazino-igri/kazino-na-zhivo/, /blog/live-game-shows/, /kak-ocenyavame/, /otgovorna-igra/. ✓

## ANTI-CANNIBALIZATION (Step-6 human check)
Lightning Blackjack live game-show spoke. Distinct primary kw (lightning blackjack / лайтнинг блекджек) и механика от Lightning Baccarat (vk-0199, 20% такса върху бакара), Lightning Dice (vk-0202, светкавици по числа за сбор), Lightning Roulette (vk-0186, множители по числа). Тук: 100%-ова такса върху блекджек с непроменени базови правила.

## HUMAN-ACTION LIST
1. Попълни „[About Всички Казина boilerplate]" слота.
2. Разреши 3-те [VERIFY]: множители (точни стойности по версия), ефективен RTP/edge, прозорец за залагане — провери в информацията на конкретната маса/версия на Evolution.
3. Потвърди афилиейт-лицензния статус на сайта при публикуване (подадено/очаква; никога „издаден").
