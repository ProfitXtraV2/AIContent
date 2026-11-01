# 06 — Verification · vk-0285 · Покер чипове

**Type:** guide (reference / how-it-works) · **Scope:** guides-only (0 operator T&C, 0 НАП, 0 affiliate)
**Byline:** Георги Тодоров · **Brand:** Всички Казина

## Brand Gate
PASS WITH FIXES — 93/100 (see `05-gate-report.md`). 0 criticals. Byline, brand name, RG footer,
18+ markers, affiliate-disclosure footer all present and verbatim. The 3 MODERATE fixes (fill trust
slots, 0 em-dashes, specific hero alt) applied into 05b.

## Step-7 external Gemini text check (human-likeness)
| version | verdict (verbatim) | human-likeness |
|---|---|---|
| initial draft | Shows AI patterns, 65% | **35 — KEPT (highest)** |
| humaniser pass 1 | Shows AI patterns, 85% | 15 |
| humaniser pass 2 | Shows AI patterns, 75% | 25 |

Result: loop ended at MAX_GEMINI_PASSES=2 with no version ≥ 80. Detector adversarial/noisy on dry BG
reference content (different flags each pass; applying its own recs lowered the score). **Keep-best =
initial draft, HL 35.** `gemini` column → `ai 65`. Trail: `07-gemini-check-1..3.md`. The style notes
from pass 3 (plastic-motif repetition, forced SEO bridge, two signpost openers) are recorded there for
the human editor's Step-6 polish, NOT applied (would exceed the pass cap and the initial scores highest).
Gemini confirmed the RG block, 18+ markers and disclosures are correct and must remain.

(API note: the Gemini text endpoint repeatedly hit read timeouts at the script's 120s limit today; each
verdict was obtained on a faithful re-run with a longer read timeout — same model, same Step-7 prompt.)

## Step-8 images
images: 2 (infographic 95, hero PASS) — Gemini image review score **95 PASS**, no integrity failure.
- `images/poker-chipove-cvetove-stoinosti.svg` — colour/value scheme (примерни) + кеш vs турнир split.
  Every figure traces to 05b: примерни values 1/5/10/25/100/500/1000, blue variation 1/2/50, cash green
  25→25, tournament stack напр. 10 000, smallest denom 25 or 100. Graphic labelled „числата са примерни".
  Rendered-verified (Chromium) no clipping/overlap; one cosmetic line-spacing fix applied per review.
- `images/poker-chipove-hero.webp` — abstract chips+cards on green felt (23 KB WebP < 100 KB), textless,
  no operator logos, no faces, no glamorised winning. ALT specific BG.
Trail: `08-image-review-1.md`.

## Surviving flags
None in-text. No [VERIFY], no [DATA NEEDED], no [CONFLICT].

## Fact sourcing (public reference — no operator T&C / НАП / affiliate)
- No worldwide standard for chip values; casinos set their own colour scheme, usually with the
  denomination printed on the chip. (cardplayer.com/online-poker/poker-chip-values; poker.fandom.com
  Chip_colors — web 2026-10-19.) The typical scheme presented (бял 1 / червен 5 / син 10 / зелен 25 /
  черен 100 / лилав 500 / жълт 1000; blue varies 1/2/50) is labelled ПРИМЕРНА, never asserted as fixed.
- Tournament chips have no cash value (points only); denominations set by the organiser, smallest often
  25 or 100+; payout by finishing position, not chip count. (cardplayer.com — web 2026-10-19.)
- Chips stacked in 20s so they can be counted at a glance; standard rack = 5 tubes × 20 = 100 chips.
  (pokernews.com/strategy/chip-stacking-tips; denexa.com — web 2026-10-19.)
- „Color up" = swapping many small chips for fewer larger ones, at table-leave and as tournament blinds
  rise. (pokernews.com/casino/casino-terms/color-up; pokerlistings.com — web 2026-10-19.)

## Figure / fact recheck (working shown)
- Cash worked example: 100 чипа × 5 = 500 ✓; 2 купчини × 20 × 25 = 1000 ✓ (both labelled illustrative).
- Counting conventions: 4 × 20 = 80 ✓; 5 × 20 = 100 ✓; стелаж 5 tubes × 20 = 100 ✓.
- Every number in the infographic is one of the above; no figure appears that the text does not state.

## No operator/НАП/€-wagering maths of the review kind in this reference piece → nothing operator-specific to recalc.
