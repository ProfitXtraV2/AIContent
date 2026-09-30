# 06 — VERIFICATION · vk-0180 · Casino War (Казино война)

STATUS: for human sign-off before publish.
Surviving flags: [VERIFY] 0 · [DATA NEEDED] 0 · [CONFLICT] 0.

## External checks (finalized by orchestrator)
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402, prepayment credits depleted). gemini=skipped. Initial draft stands as final 05b. See 07-gemini-check-1.md.
- Images (Step 8): 1 hand-authored SVG infographic (house edge by strategy + tie side bet; numbers verbatim to 05b). AI hero SKIPPED (402). Image review SKIPPED (402); manual integrity PASSED. images: 1 (infographic, review skipped — API down). See 08-image-review-1.md.

Body word count: 1014 (prose, excluding the image ALT and caption; excludes footer blocks). Within the 1000–1500 guide band.

## EVERY SPECIFIC FIGURE → PRIMARY SOURCE
Both sources reached and read on 25.09.2026.
Source A (game-math + edge table + side bet): Wizard of Odds — Casino War — https://wizardofodds.com/games/casino-war/
Source B (rules corroboration): Wikipedia — Casino War — https://en.wikipedia.org/wiki/Casino_War

| Figure in body | Value | Source |
|---|---|---|
| Тестета | обикновено 6 | A, B |
| Механика | по една карта на играч и дилър, по-високата печели 1:1 | A, B |
| Асо | най-високо; боята няма значение | A, B |
| Печалба на първа карта (всеки) | ≈46.3% (6 тестета) | B |
| Равенство на първа карта | ≈7.4% | B |
| При равенство — предаване | губиш половината залог | A, B |
| При равенство — война | втори залог = първоначалния; дилърът изгаря 3 карти, по 1 нова на всеки | A, B |
| Изход на войната | твоята ≥ дилъра → вторият залог печели 1:1, първоначалният се връща (push); дилърът по-висок → губиш и двата | A |
| Домашно предимство — винаги война (без бонус, 6 тестета) | 2.88% (спрямо първоначалния залог) | A |
| Element of risk — война (6 тестета) | 2.70% (спрямо реално рискуваното) | A |
| Домашно предимство — винаги предаване (6 тестета) | 3.70% | A |
| Домашно предимство — с бонус 1x за второ равенство | 2.33% | A |
| Домашно предимство — супер-либерален бонус 3x | ≈1.24% | A |
| Ефект от броя тестета | повече тестета → леко по-високо основно предимство, по-ниско предимство на залога за равенство | A |
| Страничен залог за равенство — изплащане | 10:1 | A, B |
| Страничен залог за равенство — домашно предимство (6 тестета) | 18.65% | A |
| Страничен залог за равенство — вариант 11:1 | предимство ≈11.25% | A |
| RTP — война | ≈97.12% (= 100% − 2.88%) | derived from A |
| RTP — предаване | ≈96.30% (= 100% − 3.70%) | derived from A |

Note: the €10 example is labelled примерни. Bonus rules (1x / 3x) VARY by casino; the body states this and tells the reader to check the felt.

## RECALCULATION — RTP from house edge (with working)
War: RTP = 100% − 2.88% = 97.12%. ✓ Body states ≈97.12% over the long run (thousands of hands), not a session promise.
Surrender: RTP = 100% − 3.70% = 96.30%. ✓ Body states surrender lowers return to ≈96.30%.
1x bonus: RTP = 100% − 2.33% = 97.67% (context; not stated as RTP in body).
Label distinction preserved: 2.88% = house edge per initial wager; 2.70% = element of risk (per money actually at risk, accounting for the doubled war bet). These measure different denominators — not mixed.

## INTERNAL LINKS USED (4, all live in sitemap 25.09.2026)
1. /kazino-igri/ — anchor „казиното"
2. /kazino-igri/blakdzhak/ — anchor „блекджек" (contrast: blackjack has strategy, war has none)
3. /otgovorna-igra/ — anchor „инструментите за отговорна игра" (RG touch)
4. /kak-ocenyavame/ — anchor „публична методика, а не през усещане"

## HUMAN CHECK BEFORE PUBLISH
- Confirm the 6-deck edges (war 2.88% / element of risk 2.70% / surrender 3.70% / 1x bonus 2.33% / tie bet 18.65%) vs the live Wizard of Odds page; confirm the target operator's deck count and whether a tie-after-tie bonus applies (it changes the edge).
- War outcome wording follows Wizard of Odds (raise wins even money, original pushes) where Wikipedia differs — confirm against the operator's own rules.
- No operator named, no НАП/tax claim, no affiliate — correct for an educational guide.
- Fill [About Всички Казина boilerplate] + [author-bio] at publish.
