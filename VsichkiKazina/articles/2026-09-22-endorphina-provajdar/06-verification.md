# 06-VERIFICATION — Всички Казина · 2026-09-22-endorphina-provajdar
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Endorphina: профил на доставчика, механики и топ слотове** · type: guide (provider profile) · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 93/100 · humanisation: kept-best (Gemini HL 75 after 2 Humaniser passes, below 80) · Gemini Step-7: ai 25 (HL 75, kept pass 2) · images: 2 (infographic 100, hero 100; best 100) · run date: 22.09.2026

## Surviving flags
**1** in-text [VERIFY]: the exact per-title RTP and the live build at the target operator (typical ~96%, but varies by title/version). No [CONFLICT]/[DATA NEEDED]. Provider profile: no BG operator, no licence number, no bonus terms. Every € figure is ILLUSTRATIVE and labelled.

## Time-sensitive / provider claims to confirm at publish (source URLs below)
| Claim | Source to confirm | Note |
|---|---|---|
| Founded **2012**, based in **Prague** (Czech Republic), Malta base for licensing | businessofigaming; slotopedia | Web-verified. |
| **Slots only** (no live/table/scratch); **200+** games; ~**2–3** new titles/month | businessofigaming; europebestcasinos | Web-verified. |
| Licensing/certification: **MGA** (Malta), **ONJN** (Romania); RNG tested by **Gaming Laboratories International (GLI)** | businessofigaming; worldwidegamblers | Web-verified. |
| Typical RTP **~96%**; some titles higher, some builds lower | slototimes; europebestcasinos | Web-verified as a range; exact per-title → [VERIFY]. |
| Signature mechanics: Risk (gamble) game to double wins (~×10 ladder); bonus buy; multipliers; wilds; scatters | businessofigaming; europebestcasinos | Web-verified. |
| Notable titles: Lucky Streak 3, Hell Hot 100, Fortune Stars, Sticky Lips | slototimes; businessofigaming | Named as examples only; NO per-title RTP asserted (would be [VERIFY]). |

## Illustrative numbers used (none BG-operator-sourced)
| Where | Figure | Note |
|---|---|---|
| RTP/edge | ~96% / ~4% | typical provider range (confirm per title/live build) |
| Worked example | €1000 оборот → ~€960 / ~€40 | illustrative, at 96% |
| Risk game | ~10 doublings | provider spec |

## Recalculation shown (per Step-6 requirement)
- RTP 96% on €1000: return 0,96 × €1000 = **€960,00 ≈ €960**; house 0,04 × €1000 = **€40,00 ≈ €40**. ✓ matches text/infographic.
- SVG house bar: 0,04 × 500 = **20 px**. ✓ (Gemini image review confirmed 20px = 4%.)
- Core honesty claims: Endorphina is the software maker, not the operator; GLI/RNG certification confirms the rules, not a player advantage, and the house edge stays built in; typical ~96% RTP = ~4% long-run edge, but the real figure depends on the title/build; the Risk game does NOT change the long-run edge, only adds swings. All correct. ✓ No per-title RTP fabricated.

## Compliance spot-check (verbatim untouchables present)
- RG marker "18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-text closing + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 regime), pending-application wording, NO issued-licence claim, NO invented №. ✓
- Internal links: only the approved set (/slot-igri/, /blog/games-providers/, /kazino-igri/rotativki/, /kak-ocenyavame/, /otgovorna-igra/), 5 distinct, in-context. ✓
- Byline Георги Тодоров; brand „Всички Казина" spelled correctly. ✓
- Zero em-dashes (incl. meta). En-dash only in the verbatim footer „10:00–17:00". ✓ No promise/hype; certification framed as no player edge; Risk game framed as edge-neutral swings. ✓ Provider profile, not an operator review → no affiliate link, no НАП licence №. ✓

## External check (Step 7 — Gemini cross-model)
Model gemini-3.1-pro-preview. Human-likeness across versions: initial **15** ("Likely AI-generated 85%"), Humaniser pass 1 **25** ("Shows AI patterns 75%"), Humaniser pass 2 **75** ("Likely human-written with AI assistance 75%"). MAX_GEMINI_PASSES (2) reached; KEPT the highest (pass 2, HL 75). Below the 80 bar → content-queue `gemini = ai 25` (verbatim scale 100 − 75). The provider-profile structure is a known hard case for this noisy detector (cf. the Amusnet EGT profile). All untouchables preserved across passes; the [VERIFY] flag left intact by Gemini. 07-gemini-check-1..3.md persist as the audit trail.

## Images (Step 8)
2 images, both PASS on pass 1 (combined score 100):
- `images/endorphina-rtp.svg` — hand-authored infographic; every figure traces to 05b (~96% / ~4% / €1000 / ~€960 / ~€40); house bar 20px = 4% verified; 18+/RG note. Data accuracy flawless.
- `images/endorphina-hero.webp` — decorative slot-symbol AI hero (gemini-3-pro-image, 30.8 KB); abstract stars/gems/fruit/reel shapes; no fabricated operator/provider logos/UI/numbers/faces/winning. 08-image-review-1.md persists.

## Anti-cannibalization note (Step-6 human check)
No Endorphina page in content-queue (checked 22.09.2026; sitemap geo-blocked, deduped against queue). Distinct provider-hub pillar (own cluster; no overlap with Amusnet/EGT vk-0021 or the Pragmatic / Play'n GO / 3 Oaks / Playson / Stakelogic profiles). Provider profile, not an operator review → no affiliate link; no operator/licence № invented.

## Human-action list (owned by you, Step 6 / Step 8)
1. Fill the "[About Всички Казина boilerplate]" slot.
2. Resolve the in-text [VERIFY]: confirm exact per-title RTP / the live build at the target operator via the in-game info panel before asserting any specific percentage.
3. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).
4. Note the humanisation kept-best at HL 75 (below the 80 bar after 2 passes); optionally re-run gemini_check after light human polish if a higher score is wanted before publish.
