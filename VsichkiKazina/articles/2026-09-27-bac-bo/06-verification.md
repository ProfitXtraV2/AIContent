# 06 — VERIFICATION · Bac Bo (Evolution): как се играе, множители и RTP

STATUS: for human sign-off before publish. FLAGS STAY IN THE TEXT — this file only helps you verify fast.
Type: guide (live game explainer) · byline: Георги Тодоров · gate: PASS 92/100 · humanisation: HUMAN-LIKE (external check offline) · run date: 27.09.2026
Surviving flags: [VERIFY] 4 · [DATA NEEDED] 0 · [CONFLICT] 0.

## Surviving flags (left IN the body per house rules)
1. [VERIFY] Прозорец за залагане ≈ 15 сек — зависи от версия/маса. §„Как протича един рунд".
2. [VERIFY] Третиране на залога Player/Banker при равенство (връща се ≈90%, губи се ≈10%; изплащане 0,9:1). §„Залозите и изплащанията".
3. [VERIFY] RTP на Player/Banker ≈ 98,87% / домашно предимство ≈ 1,13% — провери в информацията на играта. §„RTP и домашно предимство".
4. [VERIFY] Lightning Bac Bo (отделна версия): RTP ≈ 97,53% и такса ≈ 50% върху залога. §„Bac Bo и класическата бакара".

## External checks (finalized by orchestrator)
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402, probed live). gemini=skipped. Initial draft stands as final 05b. See 07-gemini-check-1.md.
- Images (Step 8): 1 hand-authored SVG infographic (залози + изплащания + Tie таблица + RTP/предимство; numbers verbatim to 05b). AI hero SKIPPED (402). Image review SKIPPED (402); manual integrity PASSED. images: 1. See 08-image-review-1.md.

Body word count: ~1086 (prose, excluding Title/Meta, ALT/caption, footer). Within the 1000–1800 guide band.

## SOURCES REACHED (27.09.2026)
- Evolution — пускане на Bac Bo (2022; „up to 88 to 1"; дизайн): https://www.evolution.com/news/evolution-launches-bac-bo-its-unique-dice-baccarat-game
- Wizard of Odds — Bac Bo (таблица за Tie, домашно предимство P/B 1,13%, Tie 4,48%): https://wizardofodds.com/games/bac-bo/
- LiveCasinoComparer — Bac Bo (2 зара всяка страна, 1:1 без комисиона, 0,9:1 при равенство, overall RTP 98,87%, ~15 сек): https://www.livecasinocomparer.com/live-casino-software/evolution-live-casino-software/evolution-live-baccarat/bac-bo/
- casinos.com — Lightning Bac Bo (RTP 97,53%, max 2000x) — контекст за вариацията: https://www.casinos.com/games/lightning-bac-bo

## EVERY SPECIFIC FIGURE → SOURCE
| Figure in body | Value | Source / status |
|---|---|---|
| Пусната | 2022 | evolution.com (26.01.2022) |
| Зарове | 2 за Player + 2 за Banker; суми 2–12 | evolution.com; livecasinocomparer.com |
| Player / Banker изплащане | 1:1; Banker без комисиона | livecasinocomparer.com |
| Равенство за P/B | 0,9:1 (губи се ≈10%) | livecasinocomparer.com; wizardofodds.com — [VERIFY] |
| Tie таблица | 2/12=88:1, 3/11=25:1, 4/10=10:1, 5/9=6:1, 6/7/8=4:1 | wizardofodds.com; livecasinocomparer.com (Evolution „up to 88:1") |
| RTP P/B | ≈ 98,87% (домашно предимство ≈ 1,13%) | livecasinocomparer.com; wizardofodds.com — [VERIFY] |
| Домашно предимство Tie | ≈ 4,48% (RTP ≈ 95,52%) | wizardofodds.com |
| Прозорец за залагане | ≈ 15 сек | livecasinocomparer.com — [VERIFY] |
| Lightning Bac Bo | RTP ≈ 97,53%; такса ≈ 50% | casinos.com — [VERIFY] |

## NOT USED (avoid fabrication)
- Конкретни min/max лимити на залога → операторо-зависими, не се твърдят.
- Wizard of Odds „7:1 / 79:1" прозаична бележка → противоречи на собствената му таблица + Evolution + LCC (88:1 стълбица); ИЗКЛЮЧЕНА като грешка.
- Blended „all-bets" RTP → не се твърди; 98,87% е за оптимална игра P/B.

## RECALCULATION (with working)
- P/B на €100: 100 × 0,9887 = €98,87 връщане; загуба €1,13 (= домашно предимство 1,13%). ✓
- Tie на €100: 100 × (1 − 0,0448) = €95,52 връщане; загуба €4,48. ✓ (≈ 4× спрямо 1,13%). ✓
- Tie стълбица: 88:1 само при 2/12 (по 1-1 или 6-6, най-редки); 4:1 при 6/7/8 (най-чести) — низходящ множител спрямо честотата. ✓
- SVG numbers ⊂ body numbers: 98,87 / 1,13 / 4,48 / 88:1 / 25:1 / 10:1 / 6:1 / 4:1 / 1:1 / „2 или 12"…„6, 7 или 8". Verified programmatically. ✓

## COMPLIANCE SPOT-CHECK
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-text + footer). ✓
- RG signposting: /otgovorna-igra/ + регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66. ✓
- Афилиейт footer (1 август 2026 режим), заявление подадено/очаква — БЕЗ издаден лиценз, БЕЗ измислен №. ✓
- Game explainer: NO BG operator names, NO НАП licence №, NO tax, NO bonus terms, NO affiliate links. Evolution само като maker. ✓
- Byline Георги Тодоров; „Всички Казина" правилно. ✓ Zero em-dashes. ✓
- Internal links (live in sitemap): /blog/live-game-shows/, /kazino-igri/kazino-na-zhivo/, /blog/bakara-pravila/, /kak-ocenyavame/, /otgovorna-igra/. ✓

## ANTI-CANNIBALIZATION (Step-6 human check)
Bac Bo live game-show spoke. Distinct primary kw (bac bo / бак бо) от card-бакара (vk-0012 /blog/bakara-pravila/), колелата (Dream Catcher/Crazy Time/Funky/Monopoly), лото (Mega Ball vk-0193), case (Deal or No Deal vk-0194) и стълба (Cash or Crash vk-0191). Зарова механика, различна от всички.

## HUMAN-ACTION LIST
1. Попълни „[About Всички Казина boilerplate]" слота.
2. Разреши 4-те [VERIFY]: време за залагане, третиране при равенство, RTP P/B, Lightning-параметри.
3. Потвърди афилиейт-лицензния статус на сайта при публикуване (подадено/очаква; никога „издаден").
