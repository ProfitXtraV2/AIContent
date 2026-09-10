# 06-VERIFICATION — Всички Казина · 2026-09-09-gates-of-olympus
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Gates of Olympus: RTP, волатилност и как се играе** · type: guide (slot explainer) · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 93/100 · humanisation: HUMAN-LIKE · Gemini Step-7: human 90 (PASS pass 1, initial kept) · images: 2 (infographic 85, hero 85; best 85) · run date: 09.09.2026

## Surviving flags

**RESOLVED — 0 surviving flags as of 10.09.2026.** The [VERIFY] marker(s) described below were resolved in commit `9b6da5e` by rewriting the sentences to hedge rather than assert; 05b now contains no [VERIFY]/[DATA NEEDED]/[CONFLICT]. Verified at human approval. The original autopilot note is kept below for the audit trail.

**2** in-text [VERIFY]: (1) the exact lower RTP builds (~95.51% / ~94.50%) and which build the target casino runs; (2) the availability of the buy-free-spins ("bonus buy") feature in the BG market. No [CONFLICT]/[DATA NEEDED]. Slot explainer: no BG operator, no licence number, no bonus terms. Every € figure is ILLUSTRATIVE.

## Time-sensitive / game claims to confirm at publish (source URLs below)
| Claim | Source to confirm | Note |
|---|---|---|
| Provider **Pragmatic Play**; release **2021** | racingpost; slotcatalog; pointsincase | Web-verified. |
| Grid **6×5**, "pay anywhere", wins on **8+** matching symbols anywhere | pointsincase; slotcatalog | Web-verified; not paylines. |
| Default RTP **96.50%** (house ~**3.50%**) | racingpost; findmyrtp; clashofslots | Web-verified default/headline build. |
| Lower configurable builds (~95.51% / ~94.50%) | (third-party review sites via search) | Medium-confidence → in-text [VERIFY]; confirm against Pragmatic's official page / the in-game info panel. |
| Volatility **HIGH**; max win **5000×** total bet | pointsincase; multiple | Web-verified. |
| Tumble/cascade; Zeus multiplier orbs **2×–500×** | olbg; pointsincase | Web-verified. |
| Free spins: **4+** scatters → **15** free spins; multipliers SUM in the bonus | pointsincase; olbg | Web-verified. |
| Ante bet **+25%** stake; buy free spins **100×** total bet | msport guide | Ante web-verified. Bonus-buy availability varies by market → [VERIFY BG]. |

## Illustrative numbers used (none BG-operator-sourced)
| Where | Figure | Note |
|---|---|---|
| RTP/edge | 96.50% / ~3.50% | provider default (confirm live build) |
| Worked example | €1000 оборот → ~€965 / ~€35 (3.50%) house | illustrative |
| Max win | 5000× total bet | ceiling, framed as such |
| Zeus multipliers | 2×–500× | provider spec |

## Recalculation shown (per Step-6 requirement)
- RTP 96.50% on €1000: return 0,9650 × €1000 = **€965,00 ≈ €965**; house 0,0350 × €1000 = **€35,00 ≈ €35**. ✓ matches text/infographic.
- SVG house bar: 0,0350 × 500 = **17,5 ≈ 18 px**. ✓
- Core honesty claims: default RTP 96.50% is below the top of the modern range but the game is high-volatility → long dry spells; the 5000× is a ceiling, not an expectation; configurable RTP means the operator picks the build; ante bet (+25%) and bonus buy (100×) do NOT change the long-run house edge — they buy variance/access, not odds. All correct. ✓

## Compliance spot-check (verbatim untouchables present)
- RG marker "18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-text closing + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 regime), pending-application wording, NO issued-licence claim, NO invented №. ✓
- Internal links: only the approved set (/slot-igri/, /blog/games-providers/, /kazino-igri/rotativki/, /kak-ocenyavame/, /otgovorna-igra/), 5 distinct, in-context. ✓
- Byline Георги Тодоров; brand „Всички Казина" spelled correctly. ✓
- Zero em-dashes (incl. meta). En-dash only in the verbatim footer „10:00–17:00". ✓ No promise/hype; high volatility and the 5000× framed as risk/ceiling, not hooks; ante/bonus-buy framed as edge-neutral. ✓ Slot explainer, not an operator review → no affiliate link, no НАП licence №. ✓

## External check (Step 7 — Gemini cross-model)
Model gemini-3.1-pro-preview. Human-likeness: initial **90** ("Likely human-written 90%", PASS on pass 1). Kept the initial draft (no Humaniser pass — applying one risks lowering the score). content-queue gemini = `human 90`. Gemini praised the anti-hype pragmatism and correctly left both [VERIFY] flags intact. 07-gemini-check-1.md persists as the audit trail.

## Images (Step 8)
2 images, both PASS on pass 1 (score 85, gemini-3.1-pro-preview review):
- `images/gates-of-olympus-rtp.svg` — hand-authored infographic; every figure traces to 05b (96.50% / 3.50% / €1000 / ~€965 / ~€35 / 5000×); 18+/RG note. Data accuracy flawless.
- `images/gates-of-olympus-hero.webp` — decorative Olympus-theme AI hero (gemini-3-pro-image, 18.1 KB); columns/lightning/orbs; no fabricated UI/logos/numbers/people/winning. 08-image-review-1.md persists.

## Anti-cannibalization note (Step-6 human check)
No Gates of Olympus page in the sitemap (checked 09.09.2026). Clean slot-explainer pillar. Pragmatic cluster (anchors the provider profile vk-0019, linked via /blog/games-providers/). Distinct from the same batch's EGT titles (Amusnet vk-0021, 40 Super Hot vk-0023) and from the navigational /kazino-igri/rotativki/ listing (linked prose-only). Game explainer, not an operator review → no affiliate link; no operator/licence № invented.

## Human-action list (owned by you, Step 6 / Step 8)
1. Fill the "[About Всички Казина boilerplate]" slot.
2. Resolve the in-text [VERIFY]s: confirm the live RTP build (default 96.50% vs lower versions) and the bonus-buy availability in BG at the target operator.
3. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).
