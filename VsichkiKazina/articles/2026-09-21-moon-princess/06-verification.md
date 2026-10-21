# 06-VERIFICATION — Всички Казина · 2026-09-21-moon-princess
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Moon Princess (Play'n GO): RTP, клъстер механика и как се играе** · type: guide (slot explainer) · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 93/100 · humanisation: human 85 (Gemini PASS pass 1, initial kept) · images: 2 (infographic 100, hero 100; best 100) · run date: 21.09.2026

## Surviving flags
**1** in-text [VERIFY]: which RTP version (96.50% default vs 94.51% secondary) the target casino actually runs — the reader reads it in the in-game info panel. No [CONFLICT]/[DATA NEEDED]. Slot explainer: no BG operator, no licence number, no bonus terms. Every € figure is ILLUSTRATIVE.

## Time-sensitive / game claims to confirm at publish (source URLs below)
| Claim | Source to confirm | Note |
|---|---|---|
| Provider **Play'n GO**; release **27.07.2017** | slotcatalog; gmblrs | Web-verified. |
| Grid **5×5**, cluster pays — wins on **3+** matching symbols in a horizontal/vertical row; cascades; grid-clear | askgamblers; playngo | Web-verified; not paylines. |
| Three princesses: **Love** (turns one symbol type into another), **Star** (adds 1–2 wilds), **Storm** (removes two symbol types) | askgamblers; playngo | Web-verified. |
| **Girl Power** random feature on non-winning base-game spins | askgamblers | Web-verified. |
| Free spins on grid clear; princess pick **Love 4 / Star 5 / Storm 8** spins | askgamblers | Web-verified. |
| Multiplier **+1×** per winning cascade, max **x20**, carried into free spins | gmblrs; askgamblers | Web-verified. |
| Default RTP **96.50%** (house ~**3.50%**); secondary build **94.51%** offered by some operators | gmblrs; slotcatalog | Web-verified; the live per-casino build → in-text [VERIFY]. |
| Volatility **HIGH**; max win **5000×** bet | askgamblers; slotcatalog; gmblrs | Web-verified. |

Sources (fetched 21.09.2026):
- https://www.askgamblers.com/casino-games/online-slots/reviews/moon-princess-play-n-go
- https://www.gmblrs.com/game-provider/play-n-go/moon-princess
- https://slotcatalog.com/en/slots/Moon-Princess
- https://www.playngo.com/games/moon-princess

## Illustrative numbers used (none BG-operator-sourced)
| Where | Figure | Note |
|---|---|---|
| RTP/edge | 96.50% / ~3.50% | provider default (confirm live build) |
| Secondary RTP | 94.51% | some operators (confirm in info panel) |
| Worked example | €1000 оборот → ~€965 / ~€35 (3.50% house) | illustrative |
| Max win | 5000× bet | ceiling, framed as such |
| Free-spins multiplier | +1× per cascade, max x20 | provider spec |

## Recalculation shown (per Step-6 requirement)
- RTP 96.50% on €1000: return 0,9650 × €1000 = **€965,00 ≈ €965**; house 0,0350 × €1000 = **€35,00 ≈ €35**. ✓ matches text/caption/infographic.
- SVG house bar: 0,0350 × 500 px = **17,5 ≈ 18 px**. ✓
- Secondary build gap: 96.50% − 94.51% = **1,99 п.п.** ≈ „близо два процентни пункта" as stated in-text. ✓
- Core honesty claims: default RTP 96.50% with a lower 94.51% build the operator can pick → check the info panel; high volatility → long dry spells; 5000× is a ceiling; the Girl Power modifiers and the growing x20 multiplier are spectacle, not a change in the house edge. All correct. ✓

## Compliance spot-check (verbatim untouchables present)
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-text closing + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 regime), pending-application wording, NO issued-licence claim, NO invented №. ✓
- Internal links: approved set + one sitemap-confirmed cross-link (/slot-igri/, /blog/games-providers/, /kak-ocenyavame/, /blog/gates-of-olympus/, /otgovorna-igra/), 5 distinct, in-context. ✓
- Byline Георги Тодоров; brand „Всички Казина" spelled correctly. ✓
- Zero em-dashes in body/meta. En-dash only in the verbatim footer „10:00–17:00". ✓ No promise/hype; high volatility and the 5000× framed as risk/ceiling. Slot explainer, not an operator review → no affiliate link, no НАП licence №. ✓
- No Sailor Moon / franchise licensing claim (anime-styled „Girl Power" theme only). ✓

## External check (Step 7 — Gemini cross-model)
Model gemini-3.1-pro-preview. Human-likeness: initial **85** („Likely human-written 85%", PASS on pass 1). Kept the initial draft (no Humaniser pass — applying one risks lowering the score; keep-best keeps the highest). content-queue gemini = `human 85`. Gemini praised the idiomatic BG and offered four optional style nits (intro contrast, one forward-reference, the princesses' triple cadence, „сърцето на рунда" metaphor); the verdict clears the bar, so the initial is kept. 07-gemini-check-1.md persists as the audit trail.

## Images (Step 8)
images: 2 (infographic 100, hero 100; best 100). Both PASS on pass 1 (gemini-3.1-pro-preview review):
- `images/moon-princess-rtp.svg` — hand-authored infographic; every figure traces to 05b (96.50% / 3.50% / €1000 / ~€965 / ~€35 / 94.51% / 5000×); 18+/RG note. Data accuracy flawless; no layout defects.
- `images/moon-princess-hero.webp` — decorative lunar-grid concept hero (gemini-3-pro-image, 17.8 KB); 5×5 tiles cascading into star-dust with a rising multiplier arrow; no fabricated UI/logos/numbers/faces/glamorised winning. 08-image-review-1.md persists.

## Anti-cannibalization note (Step-6 human check)
No Moon Princess page in the sitemap (checked 21.09.2026). Clean slot-explainer pillar. Play'n GO cluster (routed via /blog/games-providers/). Cross-linked to the sitemap-present Gates of Olympus explainer (Pragmatic, 6×5 pay-anywhere) as a related high-volatility grid slot — distinct intent, not duplicated. Game explainer, not an operator review → no affiliate link; no operator/licence № invented.

## Human-action list (owned by you, Step 6 / Step 8)
1. Fill the „[About Всички Казина boilerplate]" slot.
2. Resolve the in-text [VERIFY]: confirm which RTP build (96.50% vs 94.51%) runs at the target operator (in-game info panel).
3. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).
