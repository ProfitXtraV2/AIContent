# 06-VERIFICATION — Всички Казина · 2026-09-15-bonus-kolelo
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Бонус колело: как колелото определя наградата** · type: guide (concept explainer) · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 94/100 · humanisation: HUMAN-LIKE · Gemini Step-7: **skipped (429 credits depleted)** · images: 2 (both hand-authored SVG, review skipped 429, 0 integrity) · run date: 15.09.2026

## Surviving flags
**0** in-text [VERIFY]/[CONFLICT]/[DATA NEEDED]. The concept is general; the one concrete example (Dream Catcher) uses a publicly documented segment distribution, sourced below. Illustrative wheel proportions are labelled „схематично / примерно". No BG operator, no licence number, no bonus terms.

## Time-sensitive / factual claims to confirm at publish (source URLs below)
| Claim | Source to confirm | Note |
|---|---|---|
| Dream Catcher: **54** segments; distribution 1→**23**, 2→**15**, 5→**7**, 10→**4**, 20→**2**, 40→**1**, + **2** multiplier segments (2x, 7x) | Evolution Dream Catcher game page; casinos.com / slottyhouse statistics (cited in 00-brief) | Published game data. Sum = 54 ✓. |
| Hit frequencies: 1 ~**42.6%**, 2 ~27.8%, 5 ~13.0%, 10 ~7.4%, 20 ~3.7%, 40 ~**1.9%** | derived from the 54-segment distribution (1/54, 23/54 …) | Recalculated below. |
| RTP by bet: „1" ~**95.69%**, „40" ~**92.72%**, cumulative **96.58%** | casinos.com / slottyhouse (cited) | Confirm against the live paytable/help. |

## Recalculation shown (per Step-6 requirement)
- „40" occupies 1 of 54 segments: 1/54 = **1.85% ≈ 1.9%**. ✓ matches text/infographic.
- „1" occupies 23 of 54: 23/54 = **42.6%**. ✓
- Segment sum: 23+15+7+4+2+1+2 = **54**. ✓
- Core honesty claims: equal-looking segments are not equal probability (visible narrow big-prize sector + hidden RNG weighting); the big value sits on the rarest sector AND returns the lowest RTP per bet; the wheel's payouts are baked into game RTP, not added on top. All correct. ✓

## Compliance spot-check (verbatim untouchables present)
- RG marker "18+ Хазартът може да пристрасти. Играйте отговорно." — present (inline in conclusion + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 regime), pending-application wording, NO issued-licence claim, NO invented №. ✓
- Internal links: only the approved set (/blog/progresivni-dzhakpoti/, /kak-ocenyavame/, /slot-igri/, /otgovorna-igra/), 4 distinct. ✓
- Byline Георги Тодоров; brand „Всички Казина" spelled correctly. ✓
- Zero em-dashes (incl. meta). En-dash only in verbatim footer „10:00–17:00". ✓ No promise/hype; the „на косъм" pull is framed as risk, not hook. Concept explainer, no affiliate link. ✓

## External check (Step 7 — Gemini cross-model)
**SKIPPED — Gemini API HTTP 429 RESOURCE_EXHAUSTED ("prepayment credits are depleted").** Per
daily-run.md Step 7 the run did not halt; logged `external check: skipped (Gemini unavailable)`.
Draft authored human-first. content-queue `gemini` = `skipped`. 07-gemini-check-1.md persists.

## Images (Step 8)
2 images, both hand-authored SVG (Gemini image gen + review both 429 — skipped, not halted):
- `images/bonus-kolelo-koncept.svg` — schematic (big prize = thin/rare sector); labelled „схематично / примерно", no invented figures. No fabrication.
- `images/dream-catcher-sektori.svg` — data infographic; every figure traces to 05b + the sourced Dream Catcher distribution (54 segments, hit %, RTP by bet). No fabrication.
No decorative AI hero (image gen 429). 08-image-review-1.md persists. Manual integrity check: 0 issues.

## Anti-cannibalization note (Step-6 human check)
No wheel-bonus page in the sitemap (checked 15.09.2026). Distinct concept hub: separate from
/blog/progresivni-dzhakpoti/ (that is the pool/jackpot concept; this is the wheel mechanic that
sometimes *decides* a jackpot) and from branded wheel games (Mega Fortune vk-0066, Fire Joker
vk-0070 — folded in as examples/links, not duplicated). Concept explainer, not an operator review
→ no affiliate link.

## Human-action list (owned by you, Step 6 / Step 8)
1. Fill the "[About Всички Казина boilerplate]" slot.
2. Optional: confirm the Dream Catcher figures against the live game help at publish (published game data, unlikely to change).
3. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).
4. Optional: re-run `gemini_check.py` + `gemini_image_review.py` once Gemini credits reset, then apply keep-best.
