# 06-VERIFICATION — Всички Казина · 2026-09-17-cleocatra (vk-0099)
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Cleocatra: RTP, волатилност и как се играе** · type: guide (slot explainer) · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 93/100 (96/100 with footers assembled) · humanisation: HUMAN-LIKE · Gemini Step-7: skipped (unavailable) · images: 2 (infographic + hero; hero is an SVG, AI hero skipped) · run date: 17.09.2026

## Surviving flags
**0 surviving [VERIFY]/[DATA NEEDED]/[CONFLICT] in 05b.** All specific figures were verified against reachable public pages (provider site + international game databases). Two live-detail points are handled by HEDGING in the prose rather than assertion, matching the vk-0022 precedent:
1. Which RTP build a given casino runs (default 96.20% vs the lower 95.50% / 94.50% builds Pragmatic ships) — text says the operator picks and the real value is in the in-game info panel.
2. Whether bonus buy is offered in a given market — text says availability varies by market/operator and to check in the game itself.
Neither is asserted as a settled fact, so no flag reaches publish. Slot explainer: no BG operator, no licence number, no bonus terms. Every € figure is ILLUSTRATIVE.

## Game claims to confirm at publish (each with a primary/near-primary source URL)
| Claim | Value | Source URL |
|---|---|---|
| Provider Pragmatic Play; release 26.05.2022 | 26.05.2022 | https://clashofslots.com/slots/pragmatic-play/cleocatra/ ; https://www.pragmaticplay.com/en/slots/cleocatra/ |
| Grid 5x4; 40 фиксирани линии | 5 барабана, 4 реда, 40 линии | https://fruityslots.com/slots/reviews/cleocatra/ ; https://www.askgamblers.com/casino-games/online-slots/reviews/cleocatra-pragmatic-play |
| Default RTP 96.20% (house 3.80%) | 96.20% | https://www.pragmaticplay.com/en/slots/cleocatra/ ; https://clashofslots.com/slots/pragmatic-play/cleocatra/ |
| Lower configurable builds 95.50% / 94.50% | 95.50% / 94.50% | https://fruityslots.com/slots/reviews/cleocatra/ |
| Volatility HIGH (5/5) | висока | https://clashofslots.com/slots/pragmatic-play/cleocatra/ ; https://fruityslots.com/slots/reviews/cleocatra/ |
| Max win 5000x; bet 0.20–100 | 5000x; 0.20–100 | https://clashofslots.com/slots/pragmatic-play/cleocatra/ |
| Base respin: full cat stack on reel 1 locks + respins to a win | respin | https://www.pragmaticplay.com/en/slots/cleocatra/ ; https://fruityslots.com/slots/reviews/cleocatra/ |
| Wilds carry x2/x3 multiplier | x2 / x3 | https://www.pragmaticplay.com/en/slots/cleocatra/ ; https://fruityslots.com/slots/reviews/cleocatra/ |
| Free spins 3/4/5 scatters → 8/12/16; wilds sticky in bonus | 8/12/16 | https://www.pragmaticplay.com/en/slots/cleocatra/ ; https://www.askgamblers.com/casino-games/online-slots/reviews/cleocatra-pragmatic-play |
| Bonus buy 100x (availability varies by market) | 100x | https://fruityslots.com/slots/reviews/cleocatra/ ; https://www.askgamblers.com/casino-games/online-slots/reviews/cleocatra-pragmatic-play |
| No ante bet | няма | https://fruityslots.com/slots/reviews/cleocatra/ (no ante bet feature stated) |

## Illustrative numbers used (none BG-operator-sourced)
| Where | Figure | Note |
|---|---|---|
| RTP/edge | 96.20% / 3.80% | provider default (confirm live build) |
| Worked example | €1000 оборот → ~€962 / ~€38 | illustrative |
| Max win | 5000x total bet | ceiling, framed as such |
| Wild multipliers | x2 / x3 | provider spec |

## Recalculation shown (per Step-6 requirement)
- House edge (default): 100 − 96.20 = **3.80%**. ✓
- RTP 96.20% on €1000: 0.9620 × €1000 = **€962.00 ≈ €962**; house 0.0380 × €1000 = **€38.00 ≈ €38**; €962 + €38 = €1000. ✓ matches text and infographic.
- SVG house bar: 0.0380 × 600px = **22.8 ≈ 23px**. ✓
- Core honesty claims: default 96.20% sits at the low-mid of the modern range; high volatility → long dry spells; the 5000x is a ceiling, not an expectation; configurable RTP means the operator picks the build; bonus buy (100x) does NOT change the long-run house edge (buys access/variance, not odds); no ante bet. All correct. ✓

## Compliance spot-check (verbatim untouchables present)
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-text closing + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 regime), pending-application wording, NO issued-licence claim, NO invented №. ✓
- Internal links: only the approved set (/slot-igri/, /blog/games-providers/, /kazino-igri/rotativki/, /kak-ocenyavame/, /otgovorna-igra/), 5 distinct, in-context. ✓
- Byline Георги Тодоров; brand „Всички Казина" spelled correctly. ✓
- Zero em-dashes (incl. Title/meta/ALT/captions). En-dash only in the verbatim footer „10:00–17:00". ✓ No promise/hype; high volatility and the 5000x framed as risk/ceiling. ✓ Slot explainer, not an operator review → no affiliate link, no НАП licence №. ✓
- Disambiguation from IGT Cleopatra stated in the intro. ✓

## External check (Step 7 — Gemini cross-model)
external check: skipped (Gemini unavailable). See 07-gemini-check-1.md.

## Images (Step 8)
images: 2 (infographic; hero skipped — Gemini image API down). Hero here is a hand-authored decorative SVG (`cleocatra-hero.svg`), NOT an AI image; the AI hero was skipped per Step 8. Infographic `cleocatra-rtp.svg` — every figure traces to 05b (96.20% / 3.80% / €1000 / ~€962 / ~€38 / 5000x); 18+/RG note. Manual integrity check: 0 fabrications. See 08-image-review-1.md.

## Human-action list (owned by you, Step 6 / Step 8)
1. Fill the „[About Всички Казина boilerplate]" slot.
2. Confirm the live RTP build at the target casino (default 96.20% vs the lower 95.50% / 94.50% versions) and bonus-buy availability in BG — both are prose hedges, not assertions, so no flag blocks publish.
3. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).
