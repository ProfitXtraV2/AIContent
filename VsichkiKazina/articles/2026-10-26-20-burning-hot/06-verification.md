# 06-VERIFICATION — Всички Казина · 2026-10-26-20-burning-hot
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **20 Burning Hot (Amusnet/EGT): RTP, характеристики и Jackpot Cards** · type: guide (slot explainer, public game data) · byline: editorial (signed Георги Тодоров) · gate: PASS 97/100 (0 critical) · humanisation: HUMAN-LIKE · Gemini Step-7: **human 90** (HL 25 → pass1 35 → pass2 90/80 PASS; kept pass 2) · images: 2 (infographic + hero; best review 95 PASS, 0 integrity fail) · run date: 26.10.2026

## Surviving flags
**0 surviving flags.** 05b contains no `[VERIFY]` / `[DATA NEEDED]` / `[CONFLICT]` / `[LINK NEEDED]`. Public game-information explainer: no BG operator named, no licence number, no bonus terms, no tax claim → nothing requiring a flag. Every specific figure is sourced below; none was fabricated.

## Provider/game claims to confirm at publish (source URLs)
| Claim | Source | Note |
|---|---|---|
| Provider **Amusnet Interactive** (formerly **EGT Interactive**); rebrand completed **June 2022** | Amusnet official; CasinoBeats (07.06.2022) | Same company, new name. Text hedges correctly; game predates rebrand. |
| Release **24 August 2017** (game ID 530) | Amusnet official game page | Text says „от 2017 г." / „24 август 2017 г." |
| **5×3, 20 fixed paylines** | Amusnet official (20 Fixed); SlotCatalog; AskGamblers | Fixed, not selectable. |
| **RTP 95.88%** (declared default); operator-configurable builds exist | Amusnet official; SlotCatalog; AskGamblers | Do NOT import sibling RTPs (96.45% = original Burning Hot; 95.89/95.93 = 40/100). Text states 95.88% + „операторът може да пусне друга конфигурация, провери инфо-панела". |
| **House edge 4.12%** = 100 − 95.88 | arithmetic | See recalculation below. |
| **Comparison:** original 5-line Burning Hot declared **RTP 96.45%**, above the 20-line version's 95.88% | Amusnet official (Burning Hot page) | Honest „more lines ≠ better odds" angle; both are declared RTPs. |
| **Volatility 2/5** (low to low-medium) | Amusnet official; SlotCatalog; AskGamblers | |
| **Max win 3,000× the LINE bet** (five red 7s on a line), excl. progressive | Amusnet official (3000× bet per line); SlotCatalog | Per line bet, NOT total stake — text states „залога на линия". |
| **Expanding clover wild** on middle three reels (2/3/4), subs all but scatters | SlotCatalog (clover wilds, three middle reels); ClashOfSlots (feature list „Expanding Wilds"); family mechanic (Burning Hot) | |
| **$ scatter** anywhere, up to **100× total bet**; **star scatter** reels 1/3/5, **20× total bet**; **no free spins** | SlotCatalog; AskGamblers FAQ ("no free spins in the 20 Burning Hot slot") | Scatters pay directly. |
| **Gamble** (red/black card colour double); **Jackpot Cards** random mystery progressive, 4 suit levels (Spades highest), 12 cards / reveal 3 same suit, trigger scales with bet size | SlotCatalog (Jackpot Cards 4 levels); AskGamblers; family mechanic | |

## Sources
- https://amusnet.com/games/online-casino/20-burning-hot (official — RTP 95.88%, 5 reels / 20 fixed, release 2017-08-24, game ID 530, volatility 2/5, max 3000× bet per line, clover wild, gamble, autoplay)
- https://slotcatalog.com/en/slots/20-Burning-Hot (RTP 95.88%, 5×3, 20 lines, low-med; clover wilds three middle reels; $ scatter up to 100× total; star scatter reels 1/3/5 20×; no free spins; gamble; Jackpot Cards 4 levels)
- https://clashofslots.com/slots/egt/20-burning-hot/ (feature list incl. „Expanding Wilds", „Jackpot Cards"; Betways 20)
- https://amusnet.com/games/online-casino/burning-hot (original Burning Hot RTP 96.45% — for the honest comparison)
- https://casinobeats.com/2022/06/07/egt-interactive-completes-rebrand-to-become-amusnet-interactive/ (rebrand June 2022)

## Recalculation shown (per Step-6 requirement)
- House edge: 100 − 95.88 = **4.12%**. ✓ matches text.
- RTP 95.88% on €1000 turnover: player return 0.9588 × €1000 = **€958.80**; house 0.0412 × €1000 = **€41.20**; €958.80 + €41.20 = €1000. ✓ matches text and infographic.
- SVG bar geometry: house 4.12% × 500 px track = 20.6 ≈ **21 px** overlaid at right (x=529–550); player fills track. ✓
- Honesty claims: declared RTP 95.88% is below the original's 96.45% (more lines do not raise the return); gamble is ~coin-flip and adds no value over RTP; Jackpot Cards trigger scales with bet size (burns budget faster, no skill); max 3,000× is per line bet and rare. All correct. ✓

## Compliance spot-check (verbatim untouchables present)
- RG marker "18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-body volatility section + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (делнични дни 10:00–17:00). ✓
- Affiliate-licensing footer (1 Aug 2026 regime, „подало заявление … очаква издаването му") — verbatim, no „issued" claim, no invented licence №. ✓
- Byline Георги Тодоров; brand „Всички Казина"; no team/editorial byline. ✓
- No operator named → no affiliate link needed; no tax claim. ✓

## Images
- `images/20-burning-hot-rtp.svg` — RTP/house-edge infographic (€1000 split; every number verbatim from 05b). Gemini review 95 PASS.
- `images/20-burning-hot-hero.webp` — decorative hero (5×3 fire-fruit grid, centre reel = expanded clover wild; no text/logos/people). 32 KB. Gemini review 95 PASS.
- images: 2 (infographic + hero, best review score 95, 0 integrity failures). Two cosmetic SVG micro-nits noted by the reviewer (corner radius, 4.12% label a few px past the bar edge) — human polish only, non-blocking.
