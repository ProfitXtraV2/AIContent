# 06-VERIFICATION — Всички Казина · 2026-09-09-big-bass-bonanza
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Big Bass Bonanza: RTP, волатилност и как се играе** · type: guide (slot explainer) · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 93/100 · humanisation: HUMAN-LIKE · Gemini Step-7: **human 90** (PASS on the initial check, kept) · images: 3 (hero 100, RTP infographic 100, bonus infographic 100) · run date: 09.09.2026

## Surviving flags
**1** in-text [VERIFY]: the exact lower RTP builds (≈95.67% and 94.02%) come from a secondary listing; only the default 96.71% is universally confirmed. Text states 96.71% (default) + "operator may run a lower configuration, check the info panel" and flags the lower figures. No [CONFLICT]/[DATA NEEDED]. Public game-information explainer; no BG operator, no licence number, no bonus terms. (The "x4" multiplier step some sources mention is NOT included — verified sources give only x2/x3/x10.)

## Provider/game claims to confirm at publish (source URLs)
| Claim | Source | Note |
|---|---|---|
| Developer **Reel Kingdom** (owned/operated by **Pragmatic Play**); release **December 2020** | Pragmatic Play official; OLBG; PokerNews | Published under Pragmatic Play. |
| **5×3, 10 fixed paylines**; bet **€0.10–€250** | PokerNews; GamblingZone; SlotArk | |
| **RTP 96.71%** (default); configurable builds ≈**95.67%** / **94.02%** → in-text [VERIFY] | Pragmatic Play official; GamblingZone; SlotArk/RotoWire (trio) | 88% variant from one source rejected as unreliable. Confirm per casino paytable. |
| **Volatility 4/5** (high / medium-high) | OLBG; reviews | |
| **Max win 2,100×** | PokerNews; GamblingZone; SlotArk; OLBG | |
| **Bass scatter**: 3→**10**, 4→**15**, 5→**20** free spins | Pragmatic Play official; GamblingZone | |
| **Fisherman wild** (free spins only) collects money-fish values; single money symbol up to **2,000×** | Pragmatic Play official | Collector mechanic. |
| **Retrigger + multiplier**: every 4 collected wilds → **+10** spins & multiplier steps **x2 (4)** / **x3 (8)** / **x10 (12)** | Pragmatic Play official; mrq | No x4 step in verified sources → omitted. |

## Sources
- https://www.pragmaticplay.com/en/games/big-bass-bonanza/ (official)
- https://www.pokernews.com/casino/slots/big-bass-bonanza-slot-review/
- https://www.gamblingzone.com/uk/slots/big-bass-bonanza/
- https://www.slotark.com/slots/big-bass-bonanza/
- https://www.olbg.com/slots/articles/big-bass-slot-series-guide
- https://mrq.com/slots-and-games/big-bass-bonanza (multiplier ladder)

## Recalculation shown (per Step-6 requirement)
- RTP 96.71% on €1000: return 0.9671 × €1000 = **€967.10**; house 0.0329 × €1000 = **€32.90**. ✓ matches text/infographic.
- SVG bar widths (RTP): player 0.9671 × 500 = **483.55 px** (track); house 0.0329 × 500 = **16.45 ≈ 16 px** overlaid at right. ✓
- Bonus infographic cross-check: scatters 3/4/5 → 10/15/20 ✓; fishermen 4/8/12 → 2x/3x/10x, each +10 spins ✓; money symbol up to 2000× ✓ — all trace to 05b.
- Core honesty claims: the base game is thin, value concentrates in the bonus; high volatility (4/5) means long dry runs + a rare big bonus; RTP is operator-configurable (96.71% default may be lower); 2,100× max is a rarity. All correct. ✓

## Compliance spot-check (verbatim untouchables present)
- RG marker "18+ Хазартът може да пристрасти. Играйте отговорно." — present (inline in volatility section + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 regime), pending-application wording, NO issued-licence claim, NO invented №. ✓
- Internal links: only the approved set (/kak-ocenyavame/, /slot-igri/, /otgovorna-igra/), 3 distinct. ✓
- Byline Георги Тодоров; brand „Всички Казина" spelled correctly. ✓
- Zero em-dashes (incl. meta). En-dash only in footer „10:00–17:00". ✓ No promise/hype (the „големият спин е на косъм" pull is named as a risk to resist). Game explainer, no specific operator → no affiliate link. ✓

## External check (Step 7 — Gemini cross-model)
Model gemini-3.1-pro-preview. Human-likeness: initial draft **90** ("Likely human-written, 90%") → **PASS on the first check**, initial kept (no Humaniser pass; over-editing a passing draft risks lowering the noisy detector). content-queue gemini = `human 90`. All numbers, links, RG lines, 18+, [VERIFY], dates, byline, brand intact. 07-gemini-check-1.md persists.

## Images (Step 8)
3 images, ALL PASS (best/every score 100, gemini-3.1-pro-preview):
- `images/big-bass-bonanza-hero.webp` — decorative fishing-theme hero (gemini-3-pro-image, 9.8 KB); no fabricated UI/logos/numbers/people/winning. **PASS 100** pass 1.
- `images/big-bass-bonanza-rtp.svg` — RTP infographic; figures trace to 05b (96.71% / 3.29% / €1000 / €967.10 / €32.90). **PASS 100** pass 1.
- `images/big-bass-bonanza-bonus.svg` — bonus-mechanics infographic; scatters/free-spins + fishermen/multiplier ladder + 2000× money symbol, all trace to 05b. **PASS 100** pass 1.
08-image-review-1.md persists.

## Anti-cannibalization note (Step-6 human check)
No Big Bass page in the sitemap (checked 09.09.2026). Clean slot-explainer pillar. Distinct game + primary keyword from the other Pragmatic titles already queued (Sweet Bonanza vk-0018, Gates of Olympus vk-0022) and from the Pragmatic Play provider profile (vk-0019), which this piece naturally anchors to. Distinct from the /slot-igri/ and /slot-igri/visok-rtp/ listings. Game explainer, not an operator review → no affiliate link; no operator/licence № invented.

## Human-action list (owned by you, Step 6 / Step 8)
1. Fill the "[About Всички Казина boilerplate]" slot.
2. Resolve the in-text [VERIFY]: confirm the live RTP build at the target operator (96.71% default vs ≈95.67% / 94.02% lower builds).
3. Confirm feature wording (fisherman collector, money symbols up to 2000×, free-spins counts, multiplier ladder) matches the live build at publish.
4. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).
