# 06-VERIFICATION — Всички Казина · 2026-09-14-fruit-party
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Fruit Party: RTP, cluster pays и множители** · type: guide (branded game explainer) · byline: editorial (signed Георги Тодоров) · gate: PASS 93/100 · humanisation: HUMAN-LIKE · Gemini Step-7: human 85 (HL: initial/kept **85**, PASS on pass 1) · images: 3 (rtp 85, mnozhiteli 85, hero 65 kept-best) · word count ~798 (core prose) · em-dashes: 0 · run date: 14.09.2026

## Surviving flags
**1 in-text [VERIFY]** — волатилност band (section „Волатилност и таванът от 5000x"): game databases classify it differently, from medium (SlotCatalog, 3.5/5) to high / very high (AskGamblers). Handled in-text as ONE practical caution grounded in real uncertainty (author rule 12), not a Version A/B structure. Not resolved by the autopilot.
Every other specific figure is provider-published / game-database-verified. Every € figure is ILLUSTRATIVE (no BG operator, no licence №, no bonus terms). No affiliate link (game explainer, not an operator review).

## Time-sensitive / provider claims to confirm at publish (source URLs below)
| Claim | Source to confirm | Note |
|---|---|---|
| RTP **96.50%** default (house edge 3.50%); lower configurable builds ~**95.50%** and ~**94.50%** | pragmaticplay.com game page; SlotCatalog; SlotsMate | Pragmatic's official page states 96.50%. Game databases list the precise three-tier as **96.47% / 95.48% / 94.45%** (top build 96.47%). RTP is operator-selectable — confirm which build the target operator runs via the info panel. |
| Grid **7×7** (49 клетки), Cluster Pays (5+ connected H/V), tumble/cascades | AskGamblers; SlotCatalog; Pragmatic | Provider spec. |
| Random multipliers: base **x2**; free spins **x2 or x4**; combine multiplicatively to **256x** cap | Pragmatic official page; AskGamblers | Provider spec. NOT persistent marked-cell spots (differs from Sugar Rush). |
| Free spins: **3+** scatters → **10** spins, retriggerable to **14**; Buy Feature **100x** stake | AskGamblers; Pragmatic | AskGamblers lists 3-7 scatters → 10-14 FS; Pragmatic: „3+ award 10, retrigger 10-14". |
| Max win **5000x** the stake | AskGamblers; SlotCatalog; slotsoo | Theoretical, framed as rarity. |
| Release **May 2020** | SlotCatalog (21.05 / 28.05.2020) | Provider release. |
| Bet range **€0.20–€100** | AskGamblers; SlotCatalog | Currency shown as € in-article (illustrative). |

## Illustrative numbers used (none BG-operator-sourced)
| Where | Figure | Note |
|---|---|---|
| RTP/edge | 96.50% / 3.50% (default build) | provider-published (confirm build per above) |
| Worked example | €1000 оборот → ~€965 връщане / ~€35 house | illustrative, default build |
| Multiplier | x2 (base), x2/x4 (FS) → cap 256x | provider spec |
| Max win | 5000x (e.g. €1 → €5000) | theoretical, extremely rare — framed as such |

## Recalculation shown (per Step-6 requirement)
- RTP 96.50% on €1000: return 0.9650 × €1000 = **€965.00**; house 0.0350 × €1000 = **€35.00**. ✓ matches text + rtp infographic.
- House edge: 100% − 96.50% = **3.50%**. ✓
- SVG bar widths (rtp): player track fills 500 px; house 0.0350 × 500 = **17.5 ≈ 18 px**, flush right. ✓
- Multiplier: base x2 combine multiplicatively, cap **256x**; free spins x2/x4, same 256x cap. ✓ matches mnozhiteli infographic.
- Max win 5000x at €1 stake = **€5000**. ✓
- Core honesty claims: cluster pays (groups) does NOT move the house edge/RTP vs paylines; random multipliers scale variance, not the long-run edge (already inside RTP); RTP operator-configurable (same game, different %); buy feature does not change RTP; 5000x is a rarity not a target. All correct. ✓

## Compliance spot-check (verbatim untouchables present)
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (inline in „Как да подходиш разумно" + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 regime), pending-application wording, NO issued-licence claim, NO invented №. ✓
- Internal links: only the approved whitelist — /blog/pragmatic-play-provajdar/ (Pragmatic profile anchor), /blog/sugar-rush/ (cluster-pays sibling fold-in), /kak-ocenyavame/ (real vs advertised RTP), /otgovorna-igra/ (RG). 4 distinct URLs. Reactoonz = plain-text mention only (no link). ✓
- Byline Георги Тодоров; brand „Всички Казина" spelled correctly. ✓
- Zero em-dashes. En-dash only in verbatim footer „10:00–17:00". ✓ No promise/hype; the „усещане за близка голяма печалба" pull is named as an illusion to resist, not a hook. ✓ Game named educationally, no affiliate link (guide, not operator review). ✓

## External check (Step 7 — Gemini cross-model)
Human-likeness: initial 05b **85** („Likely human-written, 85% confidence") → **PASS on pass 1** (≥ 80), kept. No Humaniser pass needed. One genuine grammar slip flagged (heading „подходиш го" → „подходиш") corrected as a grammar fix; other style crutches left (piece already PASSED; over-editing strips voice per keep-best). All numbers, links, RG lines, 18+, dates, byline, brand, [VERIFY] flag UNTOUCHED. content-queue gemini = `human 85`. 07-gemini-check-1.md persists as the audit trail.

## Images (Step 8)
3 images shipped (best score 85):
- `images/fruit-party-rtp.svg` — hand-authored infographic; every figure traces to 05b (96.50% / 3.50% / €1000 / ~€965 / ~€35 / 95.50% / 94.50%); 18+/RG + „operator may load a lower RTP" note. Score **85** PASS (pass 2, after a layout fix).
- `images/fruit-party-mnozhiteli.svg` — multiplier-mechanic infographic; figures trace to 05b (x2 base, x2/x4 free spins, 256x cap); 18+ note + „множителите разтягат вариацията, не RTP-то". Score **85** PASS.
- `images/fruit-party-hero.webp` — decorative concept hero (gemini-3-pro-image, 13.4 KB); abstract fruit-coloured dots with same-colour clusters, no lines/UI/logos/numbers/people/winning. Score **65** kept-best (55 → 35 → 65; the abstract grid reads ~8×8 vs the body's 7×7, an image-model limitation, not an integrity failure). MAX_IMAGE_PASSES reached.
- images: 3 (rtp 85, mnozhiteli 85, hero 65)

## Anti-cannibalization note (Step-6 human check)
Distinct branded slot-explainer pillar for Fruit Party (target „fruit party" / „фрут парти" / „fruit party rtp"). Anchored to the LIVE Pragmatic Play profile (/blog/pragmatic-play-provajdar/) hub-and-spoke. Sugar Rush (/blog/sugar-rush/) folded in as a cluster-pays sibling; Reactoonz a plain-text mention only. Kept Fruit Party-specific (its distinctive random per-spin multiplier combining to 256x), NOT a general cluster-pays lecture (that concept hub exists separately). Game explainer → no affiliate link; no operator/licence № invented. Confirm no existing /blog/fruit-party/ in the live sitemap at publish.

## Human-action list (owned by you, Step 6)
1. Fill the „[About Всички Казина boilerplate]" slot.
2. Resolve the [VERIFY] волатилност band (medium vs high) for the target build / operator at publish.
3. Confirm Fruit Party's live RTP build (96.50% default vs lower 95.50% / 94.50%; databases: 96.47% / 95.48% / 94.45%) + feature wording for the target operator at publish.
4. Confirm no /blog/fruit-party/ already in the live sitemap (anti-cannibalization).
5. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).
