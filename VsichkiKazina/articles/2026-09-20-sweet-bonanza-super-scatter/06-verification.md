# 06-VERIFICATION — Всички Казина · 2026-09-20-sweet-bonanza-super-scatter
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Sweet Bonanza Super Scatter: какво добавя Super Scatter към оригинала** · type: guide (game explainer) · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 94/100 · humanisation: MIXED→HUMAN-LIKE (1 light pass) · Gemini Step-7: human 90 (PASS, initial kept) · images: 2 (infographic + hero, best review 100 PASS) · run date: 20.09.2026

## Surviving flags (STAY IN TEXT)
2 in-text [VERIFY] flags (game explainer on public provider/game-DB data; no BG operator, no licence №, no bonus/tax claims):
1. [VERIFY] точните цени на feature buy (≈100x/500x) + процентът на ante bet (25%) за конкретната версия — Section „Две копчета за купуване вместо едно".
2. [VERIFY] активната RTP версия на конкретното казино (96.51% / 95.56% / 94.48%) — Section „RTP: коя версия ви пуска казиното".

## Time-sensitive / game claims to confirm at publish (source table)
| Claim | Source | Note |
|---|---|---|
| Pragmatic Play; released **31.07.2025**; **6x5**, scatter pays (8+ anywhere), tumble | pragmaticplay.com/en/games/sweet-bonanza-super-scatter/; bigwinboard | Official + DB. Brief assumed „2024" — VERIFIED 2025, corrected. |
| **RTP 96.51% / 95.56% / 94.48%** (multiple versions; operator picks) | pragmaticplay.com (lists 96.51%); bigwinboard (lists all three) | Confirm the operator's active version at publish. [VERIFY] |
| **Висока волатилност** (5/5) | bigwinboard; slotcatalog | Web/DB-verified. |
| **Max win 50 000x** (four Super Scatters) | pragmaticplay.com; bigwinboard | Primary source. |
| **Super Scatter** (златна близалка) на всички барабани; 1/2/3/4 (при 3+ скатера) → **100x/500x/5 000x/50 000x** | pragmaticplay.com; bigwinboard | Primary + DB. |
| **Free spins**: 4/5/6 скатера → 10 завъртания + мигновено **3x/5x/100x**; 3+ скатера вътре = **+5** | bigwinboard; pragmaticplay.com | DB + official. |
| **Множители x2–x100**, само в безплатните завъртания, събират се | pragmaticplay.com; bigwinboard | Primary + DB. |
| **Ante bet +25%** (удвоява шанса за бонус); **feature buy 100x / 500x** (super, мин. x20) | bigwinboard | DB. Confirm at operator info-panel. [VERIFY] |
| Original Sweet Bonanza: 2019, RTP **96.48%**, max win **21 100x**, 4=10 / 5=15 завъртания, скатерът само задейства бонуса | racingpost; pragmaticplay.com/en/games/sweet-bonanza-slot/ | Contrast facts. |

## Illustrative numbers used
| Where | Figure | Note |
|---|---|---|
| RTP/edge worked example | ~96% / ~4% | example rounded; labelled „илюстративно" |
| Worked example | 1000 € → ~960 € / ~40 € | illustrative, labelled „илюстративно" |
| SVG player/house split | 4% = 20px of 500px (480+20 flush) | math checked |

## Recalculation shown
- RTP ~96% on 1000 €: 0,96 × 1000 = **960 €** back; house 0,04 × 1000 = **40 €** (4%). ✓ illustrative.
- RTP version spread: 96.51% − 94.48% = **2,03 pp** → „над два процентни пункта". ✓
- Super Scatter tiers (1/2/3/4 → 100x/500x/5 000x/50 000x) and max win 50 000x quoted from provider/DB, not computed. ✓
- Max-win contrast: original 21 100x vs 50 000x — both quoted from source. ✓

## Compliance spot-check (verbatim untouchables present)
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — body + footer. ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026), pending-application, NO issued claim, NO invented №. ✓
- Internal links (approved/sitemap set, 4 + RG): /blog/sweet-bonanza/, /kak-ocenyavame/, /slot-igri/visok-rtp/, /blog/pragmatic-play-provajdar/, /otgovorna-igra/. ✓
- Byline Георги Тодоров; brand „Всички Казина". ✓ Zero em-dashes. En-dash only in footer „10:00–17:00". ✓ Game explainer → no affiliate link, no operator, no licence №. ✓

## Anti-cannibalization note
Original Sweet Bonanza has its own pillar (/blog/sweet-bonanza/). THIS page is a distinct 2025 title
and is written entirely as the diff (Super Scatter symbol → instant base-game pay; 21 100x → 50 000x
max; one bonus buy → two-tier feature buy; 96.48% → 96.51%/95.56%/94.48% version split). Base game
cross-linked, not re-explained. Distinct branded kw „sweet bonanza super scatter" (vol 20).

## External check (Step 7 — Gemini)
HL **90** ("Likely human-written 90%") → **PASS** on the initial draft (no Humaniser pass; keep-best = initial). content-queue gemini = `human 90`. 07-gemini-check-1.md persists. [VERIFY] tags flagged as a process point by Gemini but correctly NOT removed (stay for the human).

## Images (Step 8)
images: 2 (infographic 95 pass 1 → 100 pass 2 after fix; hero PASS in both). Both PASS, 0 integrity failures. Best 100.
- `images/sweet-bonanza-super-scatter-vs-original.svg` — hand-authored comparison infographic (оригинал vs Super Scatter); every number traces to 05b (21 100x/50 000x, 100x/500x/5 000x/50 000x, 96.48% vs 96.51%/95.56%/94.48%, 1 vs 2 нива); 18+/RG note. Pass-1 flagged a tight-margin RISK on the payout line → font-size reduced for guaranteed margin (numbers unchanged); pass 2 confirms.
- `images/sweet-bonanza-super-scatter-hero.webp` — decorative abstract candy/fruit AI hero (gemini-3-pro-image, 24.4 KB); no UI/logos/numbers/people/winning.
08-image-review-1.md and 08-image-review-2.md persist.

## Human-action list (Step 6 / Step 8)
1. Fill the „[About Всички Казина boilerplate]" slot.
2. Resolve the two [VERIFY] flags (feature-buy/ante-bet figures; active RTP version) at the operator info-panel at publish.
3. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).
