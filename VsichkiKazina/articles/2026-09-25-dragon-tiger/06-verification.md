# 06-VERIFICATION — Всички Казина · 2026-09-25-dragon-tiger (vk-0175)
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Дракон Тигър (Dragon Tiger): правила, залози и шансове** · type: guide · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES → PASS 94/100 · humanisation: HUMAN-LIKE 51/60 · run date: 25.09.2026

## Surviving flags
**0.** No [VERIFY], [CONFLICT], or [DATA NEEDED] flags in the body. Evergreen Dragon Tiger rules/math guide; no claim about any real operator, table, provider, or licence number. House-edge/payout figures are standard, publicly-computable constants verified against Wizard of Odds; every € figure is ILLUSTRATIVE and marked примерни.

## External checks (finalized by orchestrator)
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402, prepayment credits depleted). gemini=skipped. Only the initial draft exists; it stands as final 05b (keep-best trivial). See 07-gemini-check-1.md.
- Images (Step 8): 1 hand-authored SVG infographic (house edge by bet; numbers verbatim to 05b). AI hero SKIPPED (gemini_image_gen.py HTTP 402). Image review SKIPPED (HTTP 402); manual integrity check PASSED (no fabricated logo/number/screenshot, no faces, no glamorised winning; source conflict on Tie 8:1 resolved to WoO 32,77% by EV check). images: 1 (infographic, review skipped — API down). See 08-image-review-1.md.
Gemini text cross-check (Step 7), decorative hero image generation, and image review are handled by the orchestrator. This writer produced only the researched text and the hand-authored SVG infographic.

## Time-sensitive claims needing a primary-source check
**None.** No operator terms, no live offers, no НАП licence numbers, no tax thresholds. Dated strings are only the run date 25.09.2026 and the verbatim affiliate footer's legal citation (ДВ бр. 69 от 31.07.2026).

## Every specific figure → primary source URL (all reachable; all verified)
| Figure in body | Value | Primary source (reachable) |
|---|---|---|
| Card ranking, ace low | асо най-ниско; асо…поп | https://wizardofodds.com/games/dragon-tiger/ ; https://www.coololdgames.com/card-games/gambling/dragon-tiger/ |
| Decks assumed | осем тестета | https://wizardofodds.com/games/dragon-tiger/ |
| Dragon/Tiger payout | 1:1 | https://wizardofodds.com/games/dragon-tiger/ |
| Tie payout (standard) | 8:1 | https://wizardofodds.com/games/dragon-tiger/ |
| Tie payout (variant) | 11:1 | https://wizardofodds.com/games/top-card/ |
| Suited Tie payout | 50:1 | https://wizardofodds.com/games/dragon-tiger/ |
| Tie rule on main bet | равенството губи половин залог | https://wizardofodds.com/games/dragon-tiger/ ; https://www.coololdgames.com/card-games/gambling/dragon-tiger/ |
| House edge Dragon/Tiger | 3,73% (~3,8%) | https://wizardofodds.com/games/dragon-tiger/ |
| House edge Tie at 8:1 | 32,77% | https://wizardofodds.com/games/dragon-tiger/ |
| House edge Tie at 11:1 | 10,36% | https://wizardofodds.com/games/top-card/ |
| House edge Suited Tie | 13,98% | https://wizardofodds.com/games/dragon-tiger/ |
| Tie probability (8 decks) | ~7,47% | computed (see recalc); consistent with WoO edge |
| Tie frequency | ~1 на тринайсет ръце | computed 415/31=13,39 |
| Baccarat Banco edge (contrast) | ~1,06% | https://wizardofodds.com/games/baccarat/basics/ (sibling guide vk-0012) |
| Blackjack edge (contrast) | под 1% | standard basic-strategy constant (sibling context) |
| € examples (€20×50=€1000; ~€37/~€328/~€140) | illustrative | computed from the edges above; marked примерни |

### Conflict caught and resolved BEFORE the body (not written as a Version A/B debate)
CoolOldGames states the Tie (8:1) house edge as **13,6%**, which is mathematically wrong and fails the EV check below. Wizard of Odds gives **32,77%**, which the recalculation confirms. The body uses 32,77% only; the erroneous value is excluded, not flagged in text. (Documented in 01-synthesis.md and 05-gate-report.md.)

## Recalculation shown (per Step-6 requirement) — 8 тестета = 416 карти
- **Tie probability:** given Dragon's card, 31 cards of the same rank remain out of 415 → 31/415 = **0,074699 ≈ 7,47%**. ✓
- **Dragon/Tiger house edge (tie loses half):** by symmetry P(win)=P(lose); those cancel in EV, leaving only the half-loss on ties → edge = ½ × P(tie) = 0,074699/2 = **0,037349 ≈ 3,73%**. ✓ matches WoO.
- **Tie bet at 8:1:** EV = 0,074699×8 − (1−0,074699)×1 = 0,597590 − 0,925301 = **−0,327711 → 32,77%** house edge. ✓ (rejects the 13,6% claim.)
- **Tie bet at 11:1:** EV = 0,074699×11 − 0,925301 = 0,821686 − 0,925301 = **−0,103615 → 10,36%**. ✓ matches WoO Top Card.
- **Suited Tie at 50:1:** P = 7/415 = 0,016867; EV = 0,016867×50 − 0,983133 = 0,843373 − 0,983133 = **−0,139759 → 13,98%**. ✓
- **Tie frequency:** 415/31 = **13,39 ≈ тринайсет ръце**. ✓ (corrected from „четиринайсет" at the Brand Gate.)
- **€ illustration (€20×50 = €1000 оборот):** 3,73%×€1000 = **€37,30 ≈ €37**; 32,77%×€1000 = **€327,70 ≈ €328**; 13,98%×€1000 = **€139,80 ≈ €140**. ✓ long-run, illustrative.

## Compliance spot-check (verbatim untouchables present)
- RG marker line "18+ Хазартът може да пристрасти. Играйте отговорно." — present (inline RG touch in body + footer block). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + Солидарност 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 regime), pending-application wording, NO issued-licence claim, NO invented №. ✓
- Byline Георги Тодоров; brand "Всички Казина" spelled correctly (≤3 mentions). ✓
- Zero em-dashes (incl. title tag + meta). En-dash only in verbatim footer "10:00–17:00". ✓
- No operator names, no НАП licence №, no bonus terms, no sports, no promise/hype/FOMO words, no tax figures. ✓

## Body word count
**1025 words** (H1 + body prose, excluding title tag/meta, image ALT/caption, and footer boilerplate). Within the 1000–1500 guide range.

## Internal links (4, all from the approved/sibling set)
- /kak-ocenyavame/ (методологията ни)
- /blog/bakara-pravila/ (гайда за бакара — sibling contrast)
- /kazino-igri/ (казино игрите)
- /otgovorna-igra/ (инструментите за отговорна игра; repeated in footer RG block)

## Infographic
images/dragon-tiger-house-edge-infografika.svg — every number copied verbatim from 05b (3,73% / 32,77% / 10,36% / 13,98% / 1:1 / 8:1 / 50:1 / 11:1 / €1000 / €37 / €328 / €140), example values marked „примерни", dark card, aria-label in Bulgarian, 18+ mark, no operator names/logos/faces. Rendered to PNG and visually verified: no overlap, no clipping.

## Human-action list (owned by you, Step 6 / Step 8)
1. Fill the "[About Всички Казина boilerplate]" slot.
2. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).
3. Optional: add a contextual cross-link if/when a Dragon Tiger listing page later exists (do not invent /kazino-igri/dragon-tiger/).
