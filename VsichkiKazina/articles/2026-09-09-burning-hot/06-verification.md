# 06-VERIFICATION — Всички Казина · 2026-09-09-burning-hot
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Burning Hot: RTP и характеристики (EGT/Amusnet класика)** · type: guide (slot explainer) · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 93/100 · humanisation: HUMAN-LIKE · Gemini Step-7: **human 85** (HL 75 → 85 PASS, pass 1 kept) · images: 2 (infographic 100, hero 75 kept-best) · run date: 09.09.2026

## Surviving flags
**1** in-text [VERIFY]: the exact alternate RTP configurations for the *original* Burning Hot are not publicly listed. The announced/default RTP is 96.45%; EGT/Amusnet is known to ship operator-selectable RTP builds, but no reachable page enumerates the specific tiers for this title (one source, clashofslots, lists the original at 95.97%). The text asserts only 96.45% (default) + „operator may run a different configuration, check the info panel" — nothing fabricated. No [CONFLICT]/[DATA NEEDED]. Public game-information explainer; no BG operator, no licence number, no bonus terms.

## Provider/game claims to confirm at publish (source URLs)
| Claim | Source | Note |
|---|---|---|
| Provider **Amusnet Interactive** (formerly **EGT Interactive**); rebrand completed **June 2022** | Amusnet official; CasinoBeats (07.06.2022) | Same company, new name. Text hedges correctly. |
| Release **2014** (03.12.2014 official) | Amusnet game page | Some third-party pages say 2015; clashofslots lists a 2019 re-cert. Text says „от 2014 г." |
| **5×3, 5 fixed paylines** | Amusnet official; SlotCatalog; AskGamblers | Fixed, not selectable. |
| **RTP 96.45%** (default); configurable builds exist; exact alt tiers for the original **not publicly listed** → in-text [VERIFY] | Amusnet official; SlotCatalog; Wizard of Odds; clashofslots (95.97%) | Do NOT import sibling-title RTPs (95.79/95.88/95.89/95.93 = 20/40/100 Burning Hot). |
| **Volatility 2/5** (low–low/med) | Amusnet official; SlotCatalog; AskGamblers | |
| **Max win 3,000× the LINE bet** (five red 7s on a line) | Amusnet official; AskGamblers | Per line bet, NOT total stake — text states „залога на линия". |
| **Expanding clover wild** on reels 2/3/4 (subs all but scatters) | AskGamblers; Amusnet | |
| **$ scatter** anywhere, up to **100× total bet** (×5); **star scatter** reels 1/3/5, **20× total bet**; no free spins | AskGamblers; SlotCatalog | |
| **Gamble** (red/black card double); **Jackpot Cards** random mystery progressive, 4 suit levels (Spades highest), 12 cards / reveal 3 same suit, trigger tied to bet size | AskGamblers; SlotCatalog | |

## Sources
- https://amusnet.com/games/online-casino/burning-hot (official — RTP 96.45%, 5×3/5 fixed, 03.12.2014, expanding wild, 11 symbols)
- https://slotcatalog.com/en/slots/Burning-Hot
- https://www.askgamblers.com/casino-games/online-slots/reviews/burning-hot-euro-games-technology
- https://wizardofodds.com/games/best-payout-slots/amusnet-interactive/
- https://clashofslots.com/slots/egt/burning-hot/ (95.97% original — divergence)
- https://casinobeats.com/2022/06/07/egt-interactive-completes-rebrand-to-become-amusnet-interactive/

## Recalculation shown (per Step-6 requirement)
- RTP 96.45% on €1000: return 0.9645 × €1000 = **€964.50**; house 0.0355 × €1000 = **€35.50**. ✓ matches text/infographic.
- SVG bar widths: player 0.9645 × 500 = **482.25 px** (track); house 0.0355 × 500 = **17.75 ≈ 18 px** overlaid at right. ✓
- Core honesty claims: RTP is operator-configurable (announced 96.45% may not be what a given casino runs); the gamble feature is ~coin-flip and adds no value over RTP; Jackpot Cards trigger scales with bet size, not skill, and does not improve base-spin odds; max 3,000× per line bet is a rarity. All correct. ✓

## Compliance spot-check (verbatim untouchables present)
- RG marker "18+ Хазартът може да пристрасти. Играйте отговорно." — present (inline in volatility section + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 regime), pending-application wording, NO issued-licence claim, NO invented №. ✓
- Internal links: only the approved set (/kak-ocenyavame/, /slot-igri/, /otgovorna-igra/), 3 distinct. ✓
- Byline Георги Тодоров; brand „Всички Казина" spelled correctly. ✓
- Zero em-dashes (incl. meta). En-dash only in footer „10:00–17:00". ✓ No promise/hype. Game explainer, no specific operator → no affiliate link. ✓

## External check (Step 7 — Gemini cross-model)
Model gemini-3.1-pro-preview. Human-likeness by version: initial **75** ("Mostly human-written with lingering AI patterns 75%"); Humaniser pass 1 **85** ("Likely human-written 85%", PASS). Kept **pass 1 (HL 85)** — highest + passing. content-queue gemini = `human 85`. All numbers, links, RG lines, 18+, [VERIFY], dates, byline, brand UNTOUCHED. 07-gemini-check-1/-2.md persist. (One transient API timeout on the first attempt; retried successfully.)

## Images (Step 8)
2 images (best review score 100, gemini-3.1-pro-preview):
- `images/burning-hot-rtp.svg` — hand-authored RTP infographic; every figure traces to 05b (96.45% / 3.55% / €1000 / €964.50 / €35.50); 18+/RG + „operator may run a different RTP" note. **PASS 100** (flawless, no integrity issue).
- `images/burning-hot-hero.webp` — decorative flaming-reels hero (gemini-3-pro-image, 16 KB); no fabricated UI/logos/bonus numbers/people/winning (fruit + red-7 are generic game symbols). Review pass 1 = 60 (showed 3 reels), regen v2 = 75 (reads as 6 reels) → kept-best v2 (75) at MAX_IMAGE_PASSES. 08-image-review-1/-2.md persist.

## Anti-cannibalization note (Step-6 human check)
No Burning Hot page in the sitemap (checked 09.09.2026). Clean slot-explainer pillar. Distinct title + primary keyword from the other EGT/Amusnet classics already queued (Shining Crown vk-0026, 20 Super Hot vk-0020, 40 Super Hot vk-0023) and from the Amusnet provider profile (vk-0021), which this piece naturally anchors to. Distinct from the /slot-igri/ and /slot-igri/visok-rtp/ listings. Game explainer, not an operator review → no affiliate link; no operator/licence № invented.

## Human-action list (owned by you, Step 6 / Step 8)
1. Fill the "[About Всички Казина boilerplate]" slot.
2. Resolve the in-text [VERIFY]: confirm the live RTP build for the original Burning Hot at the target operator (96.45% default vs a lower configuration); the exact alt tiers are not publicly enumerated.
3. Confirm feature wording (expanding clover wild, $/star scatters, Jackpot Cards) matches the live build at publish.
4. Optional: the decorative hero (score 75, minor AI reel-count artifact) can be swapped for a cleaner asset; the infographic carries the data and passes at 100.
5. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).
