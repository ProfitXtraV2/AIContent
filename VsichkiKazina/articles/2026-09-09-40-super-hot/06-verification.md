# 06-VERIFICATION — Всички Казина · 2026-09-09-40-super-hot
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **40 Super Hot: RTP и джакпот функции** · type: guide (game explainer) · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 93/100 · humanisation: HUMAN-LIKE · Gemini Step-7: human 85 (HL 15 → 85, kept pass 1, PASS) · images: 2 (best 82) · run date: 09.09.2026

## Surviving flags

**RESOLVED — 0 surviving flags as of 10.09.2026.** The [VERIFY] marker(s) described below were resolved in commit `e86aafc` by rewriting the sentences to hedge rather than assert; 05b now contains no [VERIFY]/[DATA NEEDED]/[CONFLICT]. Verified at human approval. The original autopilot note is kept below for the audit trail.

**1** in-text [VERIFY]: operators sometimes ship different RTP versions; the real percentage should be confirmed in the info panel of the specific casino. No [CONFLICT]/[DATA NEEDED]. Public game-information explainer; no BG operator, no licence number, no bonus terms. Every € figure is ILLUSTRATIVE.

## Time-sensitive / provider claims to confirm at publish (source URLs below)
| Claim | Source to confirm | Note |
|---|---|---|
| Provider **Amusnet** (formerly EGT); release **2014** | Amusnet game page; askgamblers | Web-verified; year consistent across sources. |
| **5** reels, **40** fixed paylines (5×4) | Amusnet; askgamblers; slotcatalog | Web-verified. The defining difference vs 20 Super Hot (5×3, 20 lines). |
| RTP **95.81%** (house ~4.19%) | Amusnet; askgamblers; slotcatalog; freeslotshub | Web-verified. NB: 95.79% is 20 Super Hot's RTP — this game is 95.81%. Below the modern ~96% average. Operators may run other builds → confirm live build. |
| 7 = wild (subs all but scatter); star = scatter (pays anywhere, top symbol); **single** scatter (no $ scatter) | Amusnet; freeslotshub; askgamblers | Web-verified. |
| Max win **1000×** bet per line; 5 stars top payout | Amusnet; askgamblers; slotcatalog | Web-verified. |
| Jackpot Cards: 4 fixed levels (clubs/diamonds/hearts/spades), random trigger, funded from bets | Amusnet; askgamblers | EGT/Amusnet signature progressive. |
| Gamble (red/black double-up) | freeslotshub; askgamblers | Standard EGT feature. |

## Illustrative numbers used (none BG-operator-sourced)
| Where | Figure | Note |
|---|---|---|
| RTP/edge | 95.81% / ~4.19% | provider-published (confirm per casino) |
| Worked example | €1000 оборот → ~€958 / ~€42 (4.19%) house | illustrative |
| Max win | 1000× bet per line | provider spec, framed as rare |

## Recalculation shown (per Step-6 requirement)
- RTP 95.81% on €1000: return 0,9581 × €1000 = **€958,10 ≈ €958**; house 0,0419 × €1000 = **€41,90 ≈ €42**. ✓ matches text/infographic.
- SVG house bar: 0,0419 × 500 = **20,95 ≈ 21 px**; player bar 0,9581 × 500 = **479,05 ≈ 479 px**; 479 + 21 = 500 ✓ (bars tile the track exactly after the hygiene fix).
- Core honesty claims: RTP 95.81% is below the modern-slot average (~96%+) ✓; 40 lines vs 20 does NOT improve odds — both rest on the same ~95.8% maths model, so more lines only change bet size and hit frequency ✓; Jackpot Cards is funded from bets and triggers at random → does not lower the house edge ✓; the gamble is a coin-flip that adds variance, not value ✓. All correct.

## Compliance spot-check (verbatim untouchables present)
- RG marker "18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-text closing + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 regime), pending-application wording, NO issued-licence claim, NO invented №. ✓
- Internal links: only the approved set (/kak-ocenyavame/, /slot-igri/, /kazino-igri/rotativki/, /otgovorna-igra/), 4 distinct, in-context. ✓
- Byline Георги Тодоров; brand „Всички Казина" spelled correctly. ✓
- Zero em-dashes (incl. meta). En-dash only in the verbatim footer „10:00–17:00". ✓ No promise/hype; the progressive and gamble framed as house-edge-neutral; the 40-lines point framed honestly. ✓ Game explainer, not an operator review → no affiliate link, no НАП licence №. ✓

## External check (Step 7 — Gemini cross-model)
Model gemini-3.1-pro-preview. Human-likeness by version: initial **15** ("Shows AI patterns 85%"); Humaniser pass 1 **85** ("Likely human-written 85%", PASS). Per keep-best, kept **pass 1** (highest HL). content-queue gemini = `human 85`. Detector high-variance on BG EGT explainers (as with the sibling 20 Super Hot). All numbers, links, RG lines, 18+, [VERIFY], dates, byline, brand UNTOUCHED across passes. 07-gemini-check-1/-2.md persist as the audit trail.

## Images (Step 8)
2 images, both PASS on pass 1 (best score 82, gemini-3.1-pro-preview review):
- `images/40-super-hot-rtp.svg` — hand-authored infographic; every figure traces to 05b (95.81% / 4.19% / €1000 / ~€958 / ~€42); 18+/RG note. Applied the reviewer's code-hygiene fix (player bar 479px, house 21px tile the track exactly); numbers unchanged.
- `images/40-super-hot-hero.webp` — decorative fruit-slot flat-vector hero (gemini-3-pro-image, 10.7 KB); no fabricated UI/logos/numbers/people/winning. Minor non-integrity note (omits 2 fruits) — acceptable. 08-image-review-1.md persists.

## Anti-cannibalization note (Step-6 human check)
No 40 Super Hot page in the sitemap (checked 09.09.2026). Clean slot-explainer pillar. Distinct game AND primary keyword from 20 Super Hot (vk-0020) — the article makes the 40-vs-20-lines difference its core, and cross-references the sibling without competing for the same query. Anchors the Amusnet provider profile (vk-0021, same batch). Distinct from the navigational /kazino-igri/rotativki/ listing (linked prose-only). Game explainer, not an operator review → no affiliate link; no operator/licence № invented.

## Human-action list (owned by you, Step 6 / Step 8)
1. Fill the "[About Всички Казина boilerplate]" slot.
2. Resolve the in-text [VERIFY]: confirm the live RTP build (95.81% vs any alternate version) for the target operator.
3. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).
