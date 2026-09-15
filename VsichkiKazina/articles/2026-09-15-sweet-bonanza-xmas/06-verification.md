# 06-VERIFICATION — Всички Казина · 2026-09-15-sweet-bonanza-xmas
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Sweet Bonanza Xmas: какво променя коледната версия** · type: guide (game explainer, seasonal variant) · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 94/100 · humanisation: HUMAN-LIKE · Gemini Step-7: **skipped (429 credits depleted)** · images: 2 (both hand-authored SVG, review skipped 429, 0 integrity) · run date: 15.09.2026

## Surviving flags
**1** in-text `[VERIFY]`: exact RTP build AND exact max-win figure at the target operator. Sources conflict — RTP cited as 96.48% / 96.49–96.60% / 96.51%; max win as 21 100× (base engine) vs 21 175× (some Xmas listings). Text hedges to „около 96.5%" + „от порядъка на 21 100 пъти" and defers the exact number to the info panel. No [CONFLICT]/[DATA NEEDED]. Public game-information explainer; no BG operator, no licence number, no bonus terms. Every € figure is ILLUSTRATIVE.

## Time-sensitive / provider claims to confirm at publish (source URLs below)
| Claim | Source to confirm | Note |
|---|---|---|
| RTP **~96.5%** default (base build 96.48%); Pragmatic ships lower configs | Pragmatic Play info panel; progambler.org; clashofslots (cited in 00-brief) | Provider-configurable; text says „обявеният RTP" + „провери инфо-панела". Confirm which build the target operator runs. |
| **6×5** grid, pay-anywhere; **tumble** caskade | progambler.org / Pragmatic (cited) | Same engine as base Sweet Bonanza. |
| Free spins: **4+** scatters (близалка) = **10** spins; multiplier bombs **2x–100x** (free spins only, sum on tumble end) | progambler.org (cited) | Standard feature set; confirm wording matches live build. |
| Ante bet **+25%**; bonus buy **~100×** total bet | progambler.org (cited) | Availability varies by jurisdiction/operator. |
| Max win **~21 100×** | progambler.org (21 100×) vs gameshub/clashofslots (21 175×) — CONFLICT | Hedged in text + [VERIFY]. |

## Illustrative numbers used (none BG-operator-sourced)
| Where | Figure | Note |
|---|---|---|
| RTP/edge | 96.48% / ~3.52% (base build) | provider-published (confirm per above) |
| Worked example | €1000 оборот → ~€965 връщане / ~€35 (3.52%) house | illustrative, base build |
| Multiplier | 2x–100x bombs, free spins only | standard feature |
| Max win | ~21 100× | theoretical, extremely rare — framed as such |
| Bonus buy | ~100× total bet | illustrative |

## Recalculation shown (per Step-6 requirement)
- RTP 96.48% on €1000: return 0,9648 × €1000 = **€964,80 ≈ €965**; house 0,0352 × €1000 = **€35,20 ≈ €35**. ✓ matches text/infographic.
- SVG bar widths (RTP infographic): player 0,9648 × 500 = **482 px** (visible), house 0,0352 × 500 = **17,6 ≈ 18 px**. ✓
- Core honesty claims: the Xmas version reskins the base game (same math); RTP is operator-configurable; tumble redistributes staked RTP (adds nothing outside it); bonus buy pays upfront for variance and does not lower the house edge; high volatility = long dry runs + rare big hit; the cap is a rarity not a target. All correct. ✓

## Compliance spot-check (verbatim untouchables present)
- RG marker "18+ Хазартът може да пристрасти. Играйте отговорно." — present (inline in ante/buy section + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 regime), pending-application wording, NO issued-licence claim, NO invented №. ✓
- Internal links: only the approved set (/blog/sweet-bonanza/, /kak-ocenyavame/, /slot-igri/, /otgovorna-igra/), 4 distinct. ✓
- Byline Георги Тодоров; brand „Всички Казина" spelled correctly. ✓
- Zero em-dashes (incl. meta). En-dash only in „2x–100x" and verbatim footer „10:00–17:00". ✓ No promise/hype; the „бонусът" pull is framed as risk, not hook. Game named educationally, no affiliate link (guide, not operator review). ✓

## External check (Step 7 — Gemini cross-model)
**SKIPPED — Gemini API HTTP 429 RESOURCE_EXHAUSTED ("prepayment credits are depleted").** Per
daily-run.md Step 7, the run did not halt; logged `external check: skipped (Gemini unavailable)`.
Draft authored human-first (varied rhythm, no rule-of-three, no per-paragraph bows, no manufactured
hook). content-queue `gemini` = `skipped`. 07-gemini-check-1.md persists as the audit record.
Re-runnable on the next fire once credits reset.

## Images (Step 8)
2 images, both hand-authored SVG (Gemini image gen + review both 429 — skipped, not halted):
- `images/sweet-bonanza-xmas-vs-baza.svg` — „what changes vs base" comparison (visual new / math same); every claim traces to 05b; 18+/RG note. No fabrication.
- `images/sweet-bonanza-xmas-rtp.svg` — RTP infographic; every figure traces to 05b (96.48% / 3.52% / €1000 / ~€965 / ~€35); 18+/RG + "operator may lower RTP" note. No fabrication.
No decorative AI hero (image gen 429). 08-image-review-1.md persists. Manual integrity check: 0 issues (no logos/people/fake UI/invented numbers/glamorised winning).

## Anti-cannibalization note (Step-6 human check)
No Sweet Bonanza Xmas page in the sitemap (checked 15.09.2026; only base `/blog/sweet-bonanza/` exists). Distinct primary keyword („sweet bonanza xmas" / „свит бонанза коледа") from the base Sweet Bonanza (vk-0018) and from Sweet Bonanza 1000 (vk-0080) — this is the seasonal-variant pillar, hub-and-spoke to the base. Game explainer, not an operator review → no affiliate link; no operator/licence № invented.

## Human-action list (owned by you, Step 6 / Step 8)
1. Fill the "[About Всички Казина boilerplate]" slot.
2. Resolve the in-text [VERIFY]: confirm the live RTP build (96.48% vs a lower config) and the exact max-win figure (21 100× vs 21 175×) for the target operator at publish.
3. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).
4. Optional: re-run `gemini_check.py` + `gemini_image_review.py` once Gemini credits reset, then apply keep-best.
