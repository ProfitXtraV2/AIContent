# 06-VERIFICATION — Всички Казина · 2026-09-15-100-burning-hot
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **100 Burning Hot: RTP, характеристики и Jackpot Cards** · type: guide (game explainer) · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 94/100 · humanisation: HUMAN-LIKE · Gemini Step-7: **skipped (429 credits depleted)** · images: 2 (both hand-authored SVG, review skipped 429, 0 integrity) · run date: 15.09.2026

## Surviving flags
**1** in-text `[VERIFY]`: exact RTP build at the target operator. Official Amusnet lists **95.89%**; some review sites cite **96.45%** (possibly confusing the base Burning Hot) — text cites the official 95.89% and defers the exact build to the info panel. No [CONFLICT]/[DATA NEEDED]. Public game-information explainer; no BG operator, no licence number, no bonus terms. Every € figure is ILLUSTRATIVE.

## Time-sensitive / provider claims to confirm at publish (source URLs below)
| Claim | Source to confirm | Note |
|---|---|---|
| RTP **95.89%** (official); EGT ships configurable builds | amusnetgaming.com official page; askgamblers; wizardofodds (cited in 00-brief) | Provider-configurable; text says „по данни на Amusnet" + „провери инфо-панела". 96.45% appears in some reviews — CONFLICT, hedged + [VERIFY]. |
| **5×4** grid, **100** fixed paylines; base Burning Hot = **5** lines, low vol | amusnetgaming.com; vegasslotsonline/bestcasinos (base) | Line count contrast is the article's spine. |
| Wild = **four-leaf clover**; two scatters (**dollar**, **star**); star pays up to **2000×** | amusnetgaming.com; wizardofodds (star 2000×) | Provider spec. |
| Top symbol **seven** pays up to **3000×** per line (5 of a kind) | wizardofodds; amusnet ("3000× bet per line") | Per-line, framed as theoretical cap. |
| **Jackpot Cards**: 4-level mystery progressive (4 suits), random trigger, 12 cards, match 3 of a suit | amusnetgaming.com; askgamblers (Burning Hot Jackpot Cards mechanic) | Standard EGT shared progressive; funded by player stakes. |
| Volatility **level 3** (medium/medium-high) | amusnetgaming.com | Provider scale. |

## Illustrative numbers used (none BG-operator-sourced)
| Where | Figure | Note |
|---|---|---|
| RTP/edge | 95.89% / ~4.11% | provider-published (confirm per above) |
| Worked example | €1000 оборот → ~€959 връщане / ~€41 (4.11%) house | illustrative |
| Star scatter | up to 2000× | theoretical cap |
| Seven | up to 3000× per line | theoretical cap |

## Recalculation shown (per Step-6 requirement)
- RTP 95.89% on €1000: return 0,9589 × €1000 = **€958,90 ≈ €959**; house 0,0411 × €1000 = **€41,10 ≈ €41**. ✓ matches text/infographic.
- SVG bar widths (RTP infographic): player 0,9589 × 500 = **479,45 px** (visible), house 0,0411 × 500 = **20,55 ≈ 21 px**. ✓
- Core honesty claims: 100 lines = more frequent but smaller hits AND a higher total bet per spin (each line is paid); RTP (95.89%) is below the „high-RTP" norm and does not improve with more lines; Jackpot Cards is a rare mystery draw funded by player stakes, not a casino add-on; the gamble is a ~50/50 double-up that raises session variance without changing the long-run edge. All correct. ✓

## Compliance spot-check (verbatim untouchables present)
- RG marker "18+ Хазартът може да пристрасти. Играйте отговорно." — present (inline in gamble section + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 regime), pending-application wording, NO issued-licence claim, NO invented №. ✓
- Internal links: only the approved set (/kak-ocenyavame/, /slot-igri/visok-rtp/, /slot-igri/, /otgovorna-igra/), 4 distinct. ✓
- Byline Георги Тодоров; brand „Всички Казина" spelled correctly. ✓
- Zero em-dashes (incl. meta). En-dash only in verbatim footer „10:00–17:00". ✓ No promise/hype; the gamble is framed as risk, not hook. Game named educationally, no affiliate link (guide, not operator review). ✓

## External check (Step 7 — Gemini cross-model)
**SKIPPED — Gemini API HTTP 429 RESOURCE_EXHAUSTED ("prepayment credits are depleted").** Per
daily-run.md Step 7 the run did not halt; logged `external check: skipped (Gemini unavailable)`.
Draft authored human-first. content-queue `gemini` = `skipped`. 07-gemini-check-1.md persists.

## Images (Step 8)
2 images, both hand-authored SVG (Gemini image gen + review both 429 — skipped, not halted):
- `images/100-burning-hot-vs-baza.svg` — base (5 lines) vs 100-line comparison; every claim traces to 05b; 18+/RG note. No fabrication.
- `images/100-burning-hot-rtp.svg` — RTP infographic; every figure traces to 05b (95.89% / 4.11% / €1000 / ~€959 / ~€41); 18+/RG + "below high-RTP norm, check info panel" note. No fabrication.
No decorative AI hero (image gen 429). 08-image-review-1.md persists. Manual integrity check: 0 issues.

## Anti-cannibalization note (Step-6 human check)
No 100 Burning Hot page in the sitemap (checked 15.09.2026). Distinct primary keyword („100 burning hot" / „100 бърнинг хот") from the base Burning Hot (vk-0027, 5-line — folded in as the contrast) and from the Amusnet provider profile (vk-0021, folded in as the studio anchor). Game explainer, not an operator review → no affiliate link; no operator/licence № invented.

## Human-action list (owned by you, Step 6 / Step 8)
1. Fill the "[About Всички Казина boilerplate]" slot.
2. Resolve the in-text [VERIFY]: confirm the live RTP build (95.89% official vs 96.45% cited elsewhere) for the target operator at publish.
3. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).
4. Optional: re-run `gemini_check.py` + `gemini_image_review.py` once Gemini credits reset, then apply keep-best.
