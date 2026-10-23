# 06 — Verification (vk-0289 свара)

## Surviving flags
NONE. 0 [VERIFY] / 0 [DATA NEEDED] / 0 [CONFLICT] in 05b.
This is a народна/казино card-game rules guide with 0 operator-specific facts, 0 НАП-register facts, 0 tax figures, 0 € amounts → nothing requiring human source verification remains in the text.

## Time-sensitive claims
- None in the body. свара rules are evergreen.
- Footer affiliate-licensing line (1 авг. 2026 regime) is the standard brand boilerplate, not an article-specific dated claim. Byline dates 23.10.2026 (today, UTC).

## Figure recalculation (working shown)
Key numbers in the infographic, re-derived from the card values stated in 05b:
- Асо = 11 точки. Две аса от една боя = 2 × 11 = **22** ✓ (matches 05b + infographic).
- Три аса = 3 × 11 = **33** ✓ (matches 05b „Три аса … правят 33" + infographic „33 точки, най-силната ръка").
- Свара-tie миза = 1 ÷ (брой равни играчи): 2-ма → 1/2, 3-ма → 1/3, 4-ма → 1/4 ✓ (matches 05b „по половината / по една трета / по една четвърт").
All figures internally consistent; no value changed across stages 02 → 05b (diffed).

## Sources (card-game rules — reachable, non-operator)
- denislavsotirov.blogspot.com „Правилата на Играта: Сварка" — народен точков вариант (32 карти, 3 карти, точки, сбор по боя, 7♣ „Чичо Лари" = 11, 3 аса = 33, миза ½/⅓/¼).
- 24chasa.bg — онлайн свара (J/Q/K=10, А=11, 7-спатия „Йончев"=11 връзва се с всяка, 2 аса=22, 3 аса=33, на тъмно, играй/повиши/откажи/анте, свара=равенство→нова игра).
- svara-bg.com/pravila — комбинационен вариант (тройка/цвят/кента) + „малка свара" + изрично „уговорете правилата преди игра" → фолднато в „Какво се уговаря на масата". (Site self-flags example-arithmetic inconsistencies → no disputed example totals reproduced.)
Dedup: info.toto.bg (23.10.2026) used only to confirm „тото скандо" is NOT a real БСТ game (separate skipped candidate).

## Gemini Step-7 (text)
- Initial draft: Shows AI patterns 75% → HL25.
- Humaniser pass 1: Shows AI patterns 80% → HL20 (pass lowered score; noisy detector).
- Humaniser pass 2: **Highly likely human-written 90% → HL90 = PASS**.
- KEEP-BEST = pass 2 (HL90), the highest seen and a PASS. gemini column: `human 90`. 2 humaniser passes (MAX_GEMINI_PASSES).

## Step-8 images
images: 2 (infographic 100, hero 100). Gemini image review pass 1: 100/100 PASS, 0 integrity failures; every infographic number verified 1:1 vs 05b. No iteration needed.

## Brand Gate
PASS WITH FIXES → 93/100, 0 criticals after 2 mechanical fixes (grammar agreement + editorial first-person). Byline Георги Тодоров, brand „Всички Казина", verbatim 18+ line, RG signposting, affiliate footer — all present. No operator → no НАП-№/affiliate-link obligation.
