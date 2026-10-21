# 06-VERIFICATION — Всички Казина · 2026-09-21-rise-of-olympus
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Rise of Olympus (Play'n GO): RTP, каскади и как се играе** · type: guide (slot explainer) · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 93/100 (0 criticals) · humanisation: HUMAN-LIKE · Gemini Step-7: human 85 (PASS pass 1, initial kept) · images: 2 (infographic 100, hero 100; best 100) · run date: 21.09.2026

## Surviving flags
**1** in-text [VERIFY]: the live per-casino RTP build — which of the configurable versions the target operator actually runs (default 96.50% vs the lower 94.51% / 91.49% / 87.50% / 84.50% builds), verifiable in the in-game info panel. No [CONFLICT]/[DATA NEEDED]. Slot explainer: no BG operator, no licence number, no bonus terms. Every € figure is ILLUSTRATIVE.

## FACT-CORRECTION vs the query brief
The topic line suggested a default RTP "~96.05%". The verified default is **96.50%** (SlotCatalog, AboutSlots, AskGamblers all agree; Play'n GO's own listing). Used 96.50% throughout; 96.05% was NOT used.

## Time-sensitive / game claims to confirm at publish (source URLs below)
| Claim | Source to confirm | Note |
|---|---|---|
| Provider **Play'n GO**; release **2018** | playngo.com; slotcatalog; askgamblers | Web-verified (Aug 2018; exact day 22 vs 23 differs across sources → year only in text). |
| Grid **5×5**; wins on **3+** matching symbols in a horizontal/vertical line | aboutslots; askgamblers; slotcatalog | Web-verified; not paylines, not clusters (clusters are the Origins/100 sequels). |
| Cascade: winning symbols clear, new fall; each cascade **+1** to the multiplier | aboutslots | Web-verified. |
| Default RTP **96.50%** (house ~**3.50%**) | slotcatalog; aboutslots; adventuregamers | Web-verified default/headline build. |
| Lower configurable builds **94.51% / 91.49% / 87.50% / 84.50%** | slotcatalog; aboutslots | Web-verified list; which one is live is per-operator → in-text [VERIFY]. |
| Volatility **HIGH** (10/10 Play'n GO scale); max win **5000×** | slotcatalog; askgamblers | Web-verified (one outlier said "medium"; majority + provider scale = high). |
| Hand of God: Zeus removes 2 sets · Poseidon adds **1–2** wilds · Hades transforms 1 set | slotcatalog; aboutslots; askgamblers | Web-verified. |
| Wrath of Olympus meter: 5/4/3-symbol win = **3/2/1** segments; full → respin + all 3 powers | slotcatalog; aboutslots | Web-verified. |
| Free spins: clear the grid → pick a god — Zeus **8** / Poseidon **5** / Hades **4**; multiplier persists up to **×20** | askgamblers; aboutslots | Web-verified. |
| Sequels distinct (100/Extreme/1000/Origins — different numbers) | askgamblers; playngo.com | Web-verified; named only to disambiguate. |

Sources: https://www.playngo.com/games/rise-of-olympus · https://slotcatalog.com/en/slots/Rise-Of-Olympus · https://www.aboutslots.com/casino-slots/rise-of-olympus · https://www.askgamblers.com/casino-games/online-slots/reviews/rise-of-olympus-play-n-go

## Illustrative numbers used (none BG-operator-sourced)
| Where | Figure | Note |
|---|---|---|
| RTP/edge | 96.50% / ~3.50% | provider default (confirm live build) |
| Worked example | €1000 оборот → ~€965 / ~€35 | illustrative |
| Max win | 5000× stake | ceiling, framed as such |
| Free-spins multiplier | up to ×20 | provider spec |

## Recalculation shown (per Step-6 requirement)
- RTP 96.50% on €1000: return 0.9650 × €1000 = **€965.00 ≈ €965**; house 0.0350 × €1000 = **€35.00 ≈ €35**. ✓ matches text/infographic.
- House edge = 100% − 96.50% = **3.50%**. ✓
- SVG house bar: 0.0350 × 500px = **17.5 ≈ 18px**. ✓
- Core honesty claims: the god powers and the cascade multiplier redistribute variance but do NOT change the house edge; configurable RTP means the operator picks the build (check the info panel); high volatility → long dry spells; the 5000× is a ceiling, not an expectation. All correct. ✓

## Compliance spot-check (verbatim untouchables present)
- RG marker "18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-text close + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 regime), pending-application wording, NO issued-licence claim, NO invented №. ✓
- Internal links: approved set + one on-site cross-link (/slot-igri/, /blog/games-providers/, /kazino-igri/rotativki/, /kak-ocenyavame/, /otgovorna-igra/, /blog/gates-of-olympus/), 6 distinct, in-context. ✓
- Byline Георги Тодоров; brand „Всички Казина" spelled correctly. ✓
- Zero em-dashes (incl. title/meta). En-dash only in the verbatim footer „10:00–17:00". ✓ No promise/hype; high volatility and the 5000× framed as risk/ceiling, not hooks. ✓ Slot explainer, not an operator review → no affiliate link, no НАП licence №. ✓

## External check (Step 7 — Gemini cross-model)
Human-likeness: initial **85** ("Likely human-written, 85% confidence", PASS on pass 1). Kept the initial draft (a Humaniser pass risks lowering the score; keep-best keeps the highest). content-queue gemini = `human 85`. Gemini praised „таван, а не очакване" and the natural 2nd-person voice; offered three optional style nits (surface-vs-reality hook, two paragraph-closing summaries, one signposting sentence) that were not required for the PASS and were not applied to avoid regressing the score. 07-gemini-check-1.md persists as the audit trail.

## Images (Step 8)
2 images, both PASS (best 100):
- `images/rise-of-olympus-rtp.svg` — hand-authored infographic; every figure traces to 05b (96.50% / 3.50% / €1000 / ~€965 / ~€35 / 5000×); 18+/RG note. Pass 1: 92 (minor bottom-margin note) → 6px lift applied → Pass 2: 100.
- `images/rise-of-olympus-hero.webp` — decorative Greek-myth AI hero (21.0 KB); 5x5 cascading grid, three god emblems (lightning/trident/flame), marble columns; no fabricated UI/logos/numbers/people/winning. 92 → 100. 08-image-review-1.md and 08-image-review-2.md persist.

## Anti-cannibalization note (Step-6 human check)
No Rise of Olympus page in the sitemap (checked 21.09.2026). Clean slot-explainer pillar. Distinct from the on-site Greek-theme gates-of-olympus (Pragmatic, 6×5 pay-anywhere) — different game, cross-linked at /blog/gates-of-olympus/, not duplicated. Play'n GO cluster (links via /blog/games-providers/). Game explainer, not an operator review → no affiliate link; no operator/licence № invented.

## Human-action list (owned by you, Step 6 / Step 8)
1. Fill the "[About Всички Казина boilerplate]" slot.
2. Resolve the in-text [VERIFY]: confirm the live RTP build at the target operator (default 96.50% vs the lower versions) via the in-game info panel.
3. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).
