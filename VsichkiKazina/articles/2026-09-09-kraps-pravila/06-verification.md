# 06-VERIFICATION — Всички Казина · 2026-09-09-kraps-pravila
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Крапс: как се играе и кои залози си струват** · type: guide (table-game rules explainer) · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 96/100 · humanisation: HUMAN-LIKE · Gemini Step-7: **human 85** (HL 20 → 25 → 85 PASS, pass 2 kept) · images: 2 (infographic 100, hero 60 kept-best) · run date: 09.09.2026

## Surviving flags
**0** in-text [VERIFY] / [CONFLICT] / [DATA NEEDED]. Every figure is public, evergreen game mathematics (Wizard of Odds house-edge table), not operator-specific. No BG operator, no licence number, no bonus terms involved.

## Facts to confirm at publish (source URLs)
| Claim | Source | Note |
|---|---|---|
| Pass line house edge **1.41%** (1.414%) | Wizard of Odds craps appendix | Standard, universal rules. |
| Don't pass **1.36%** (1.364% of all wagered) | Wizard of Odds | Also quoted **1.40%** per resolved bet (excluding 12-pushes) — both conventions correct; text uses 1.36%/1.364%. „bar 12" push confirmed. |
| Come 1.41% / Don't Come 1.36% | Wizard of Odds | Same as pass/don't pass, made after point. |
| Odds bet **0.00%** edge; true odds **4/10 = 2:1, 5/9 = 3:2, 6/8 = 6:5**; combined pass+2x ≈ **0.57%**, don't pass+2x ≈ **0.46%** | Wizard of Odds; PokerNews (odds bet) | The one zero-edge bet; combined figures are WoO's 2x-odds examples. |
| Place **6/8 = 1.52%** (1.515%), **5/9 = 4%**, **4/10 = 6.67%** (6.667%) | Wizard of Odds | Cited exactly. |
| Field **2.78%** (12 pays 3:1) / **5.56%** (12 pays 2:1) | Wizard of Odds | Paytable-dependent; text states both and says „провери таблицата". |
| Any 7 **16.67%**; Any Craps **11.11%**; hardways **9.09%–11.11%** | Wizard of Odds | Worst common bets; Any 7 is the single worst. |

## Sources
- https://wizardofodds.com/games/craps/appendix/1/ (house-edge table — authoritative, internally consistent)
- https://wizardofodds.com/games/craps/
- https://www.pokernews.com/casino/casino-terms/odds-bet.htm
- https://www.winstar.com/blog/how-do-you-play-craps-at-a-casino/
- https://www.venetianlasvegas.com/resort/casino/table-games/craps-basic-rules.html

## Recalculation shown (per Step-6 requirement)
- Pass line 1.41% on €10 per resolved bet: 0.0141 × €10 = **€0.141 ≈ 14 стотинки**. ✓ matches text.
- Odds dilution: pass line alone 1.41%; with 2× free odds (0% edge) the extra stake is edge-free, pulling the combined edge to ≈ **0.57%** (WoO). ✓
- SVG bar scaling: max 16.67% → 400px (24 px per %). Any 7 = 400px; Place 4/10 = 6.67% × 24 = 160px; Field = 2.78% × 24 = 66.7 ≈ 67px; Pass = 1.41% × 24 = 33.8 ≈ 34px; Don't pass = 1.36% × 24 = 32.6 ≈ 33px; Place 6/8 = 1.52% × 24 = 36.5 ≈ 36px; odds 0% = 4px min-visible sliver. ✓
- Core honesty claims: strategy does not beat the house edge (dice have no memory, each roll independent); bet choice moves the edge from <1% to >15%; odds bet is the only 0% bet; center/prop bets are the trap. All correct. ✓

## Compliance spot-check (verbatim untouchables present)
- RG marker "18+ Хазартът може да пристрасти. Играйте отговорно." — present (inline in strategy section + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 regime), pending-application wording, NO issued-licence claim, NO invented №. ✓
- Internal links: only the approved set (/kak-ocenyavame/, /kazino-igri/, /otgovorna-igra/), 3 distinct. ✓
- Byline Георги Тодоров; brand „Всички Казина" spelled correctly. ✓
- Zero em-dashes (incl. meta). En-dash only in footer „10:00–17:00". ✓ No promise/hype words. Game explainer, no specific operator → no affiliate link (guide, not review). ✓

## External check (Step 7 — Gemini cross-model)
Model gemini-3.1-pro-preview. Human-likeness by version: initial **20** ("Shows AI patterns 80%"); Humaniser pass 1 **25** ("Shows AI patterns 75%"); Humaniser pass 2 **85** ("Likely human-written 85%", PASS). Kept **pass 2 (HL 85)** — highest and passing. content-queue gemini = `human 85`. All numbers, links, RG lines, 18+, dates, byline, brand UNTOUCHED across every pass. 07-gemini-check-1/-2/-3.md persist as the audit trail.

## Images (Step 8)
2 images (best review score 100, gemini-3.1-pro-preview):
- `images/kraps-domashno-predimstvo.svg` — hand-authored house-edge bar chart; every figure traces to 05b (0.00%/1.36%/1.41%/1.52%/2.78%/6.67%/16.67%); source line (Wizard of Odds) + 18+/RG. **PASS 100** (flawless, no integrity issue).
- `images/kraps-zarove-hero.webp` — decorative abstract dice + looping-arrow hero (gemini-3-pro-image, 14.9 KB); no fabricated UI/logos/numbers/people/winning. Review pass 1 = 60 (AI dice-face pip artifact, no integrity fail); regen v2 = 35 (worse) → kept-best v1 (60) at MAX_IMAGE_PASSES. 08-image-review-1/-2.md persist.

## Anti-cannibalization note (Step-6 human check)
No craps page in the sitemap (checked 09.09.2026). Clean table-game pillar completing the games set (blackjack vk-0009, baccarat vk-0012, roulette vk-0024, poker vk-0008, keno vk-0016) — distinct game, distinct primary keyword (крапс / как се играе крапс / казино зарове), no overlap with the /kazino-igri/ listing (linked, not duplicated). Game explainer, not an operator review → no affiliate link; no operator/licence № invented.

## Human-action list (owned by you, Step 6 / Step 8)
1. Fill the "[About Всички Казина boilerplate]" slot.
2. Confirm the Field paytable convention (12 pays 3:1 = 2.78% vs 2:1 = 5.56%) matches the target live/online craps table at publish; text already states both.
3. Optional: replace the decorative hero (score 60, minor AI dice-face artifact) with a cleaner asset if desired — the infographic carries all the data and passes at 100.
4. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).
