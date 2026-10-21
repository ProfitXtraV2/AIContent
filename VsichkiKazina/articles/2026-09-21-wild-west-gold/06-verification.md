# 06-VERIFICATION — Всички Казина · 2026-09-21-wild-west-gold
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Wild West Gold (Pragmatic): RTP, sticky wilds и как се играе** · type: guide (slot explainer) · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 93/100 · humanisation: HUMAN-LIKE · Gemini Step-7: human 80 (PASS pass 2, after 1 Humaniser pass; initial 25) · images: 2 (infographic + hero; best 85) · run date: 21.09.2026

## Surviving flags
**2** in-text [VERIFY]: (1) кой RTP билд върви при конкретния оператор (96.51% по подразбиране vs по-ниските 95.56% / 94.53%) — проверява се в инфо-панела на играта; (2) наличност на bonus buy в BG (варира по юрисдикция; забранен в някои пазари). No [CONFLICT]/[DATA NEEDED]. Slot explainer: no BG operator, no licence number, no bonus terms. Every € figure is ILLUSTRATIVE.

## Time-sensitive / game claims to confirm at publish (source URLs below)
| Claim | Source to confirm | Note |
|---|---|---|
| Provider **Pragmatic Play**; release **март 2020** | pragmaticplay.com; slotcatalog (26.03.2020); fruityslots | Web-verified. |
| Grid **5×4**, **40 фиксирани линии** | slotcatalog; fruityslots | Web-verified. |
| Default RTP **96.51%** (house ~**3.49%**) | pragmaticplay.com (официален); slotcatalog; fruityslots | Web-verified default/top build. |
| Lower configurable builds **95.56%** / **94.53%** | slotcatalog; fruityslots | Web-verified; operator picks → in-text [VERIFY] which runs live (info panel). |
| Volatility **HIGH (5/5)**; max win **10 000×** залога | slotcatalog; fruityslots | Web-verified. Base-game cap ~6 750× (fruityslots) — not stated in body; 10 000× headline is the free-spins ceiling. |
| Wilds on reels 2/3/4, multipliers **2×/3×/5×**; in free spins **sticky**, multipliers **SUM** on a line (3×+5×=8×) | pragmaticplay.com; slotcatalog; fruityslots | Web-verified across all three. |
| Free spins: **3 scatter** on reels 1/3/5 → **8** spins; retrigger 2/3/4/5 stars → **4/8/12/20** spins | slotcatalog; fruityslots | Web-verified. |
| Bonus buy **100×** stake; availability varies (не UK) | slotcatalog; fruityslots | Cost web-verified. BG availability → [VERIFY]. |
| Bet range **€0.20–€100** | slotcatalog; fruityslots | Web-verified (source quotes £/€ equivalents). |

## Illustrative numbers used (none BG-operator-sourced)
| Where | Figure | Note |
|---|---|---|
| RTP/edge | 96.51% / ~3.49% | provider default (confirm live build) |
| Worked example | €1000 оборот → ~€965 / ~€35 (3.49%) house | illustrative |
| Max win | 10 000× залога | ceiling, framed as such |
| Wild multipliers | 2×/3×/5×, събиране | provider spec |

## Recalculation shown (per Step-6 requirement)
- RTP 96.51% на €1000: връщане 0,9651 × €1000 = **€965,10 ≈ €965**; house 0,0349 × €1000 = **€34,90 ≈ €35**. ✓ matches text/infographic.
- Домашно предимство: 100% − 96.51% = **3.49%**. ✓
- Sticky пример: 3× + 5× = **8×** (събиране, не 3×5=15×). ✓
- SVG house bar: 0,0349 × 500 = **17,45 ≈ 17 px**. ✓
- Core honesty claims: default RTP 96.51% е топ-билдът, но операторът може да пусне 95.56% / 94.53%; играта е високоволатилна → дълги сухи серии; 10 000× е таван, не очакване; bonus buy (100×) НЕ мени дългосрочното предимство — купува достъп до вариацията. All correct. ✓

## Compliance spot-check (verbatim untouchables present)
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-text closing + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 regime), pending-application wording, NO issued-licence claim, NO invented №. ✓
- Internal links: approved set + sitemap-потвърден Pragmatic cross-link (/slot-igri/, /blog/pragmatic-play-provajdar/, /blog/games-providers/, /kazino-igri/rotativki/, /kak-ocenyavame/, /otgovorna-igra/), 6 distinct, in-context. ✓
- Byline Георги Тодоров; brand „Всички Казина" spelled correctly. ✓
- Zero em-dashes (incl. meta). En-dash only in the verbatim footer „10:00–17:00". ✓ No promise/hype; high volatility and the 10 000× framed as risk/ceiling; bonus buy framed as edge-neutral. ✓ Slot explainer, not an operator review → no affiliate link, no НАП licence №. ✓

## External check (Step 7 — Gemini cross-model)
Model gemini-3.1-pro-preview. Human-likeness: initial **25** ("AI patterns 75%") → Humaniser pass 1 (applied Gemini's transition/signposting/over-dramatization/metaphor recs) → **80** ("Likely human-written 80%", PASS on pass 2). Keep-best = 80 (current 05b, pass 1 version). content-queue gemini = `human 80`. 07-gemini-check-1.md and 07-gemini-check-2.md persist as the audit trail. Gemini left both [VERIFY] flags intact (correctly, as items for the human publisher).

## Images (Step 8)
2 images, combined review score **85 · PASS** (gemini-3.1-pro-preview), no integrity failures:
- `images/wild-west-gold-rtp.svg` — hand-authored infographic; every figure traces to 05b (96.51% / 3.49% / €1000 / ~€965 / ~€35 / 10 000×); 18+/RG note; math and layout flawless.
- `images/wild-west-gold-hero.webp` — decorative wild-west AI hero (gemini-3-pro-image, 15.9 KB); canyon/sheriff-star/gold-bars; no fabricated UI/logos/numbers/people/winning. Hero ALT corrected to match the rendered art (review pass 1). 08-image-review-1.md persists.

## Anti-cannibalization note (Step-6 human check)
No Wild West Gold page in the sitemap (checked 21.09.2026). Clean slot-explainer pillar. Pragmatic cluster (anchors the provider profile via /blog/pragmatic-play-provajdar/, present in sitemap). Distinct from the on-main Gates of Olympus explainer (different game, different math; used only as a STYLE model). Game explainer, not an operator review → no affiliate link; no operator/licence № invented.

## Human-action list (owned by you, Step 6)
1. Fill the „[About Всички Казина boilerplate]" slot.
2. Resolve the in-text [VERIFY]s: confirm the live RTP build at the target operator (info panel: 96.51% vs 95.56% / 94.53%) and the bonus-buy availability in BG.
3. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).
