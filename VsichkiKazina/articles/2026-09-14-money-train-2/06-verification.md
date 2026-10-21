# 06-VERIFICATION — Всички Казина · 2026-09-14-money-train-2 (vk-0069)
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Money Train 2: RTP, много висока волатилност и какво купуваш с feature buy** · type: guide (branded slot explainer) · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 94/100 · humanisation: Gemini Step-7 HL 80 (PASS pass 1, original kept) · images: 2 (infographic 85, hero 85; best 85) · run date: 14.09.2026

## Surviving flags (2 [VERIFY], both LEFT IN 05b — the human resolves them)
1. **[VERIFY] точната по-ниска RTP версия (94.0% vs 94.40%) и коя пуска конкретното казино.** Sources disagree on the exact lower build; the operator picks which build to run. Confirm against Relax Gaming's official spec / the in-game info panel at the target casino.
2. **[VERIFY] наличност на feature buy при конкретния оператор/пазар.** Feature buy is jurisdiction-dependent (banned in the UK, see below); confirm it is present in the game at the target operator before relying on it.

No [DATA NEEDED]. No unresolved Version A/B structure in the text.

## [CONFLICT] logged (resolved to the corroborated value; NOT written as a two-camp structure)
- **Max win.** relax-gaming.com's own page + Bigwinboard + AskGamblers + Stakers + PlayUSA + SlotsMate all state **50,000x**. VegasSlotsOnline lists **2,500x** (outlier/error, contradicted by the provider itself). Draft uses **~50 000x** per the provider's own page. Human confirms at publish.
- **Lower RTP build.** 94.0% (AskGamblers, Bigwinboard) vs 94.40% (VegasSlotsOnline) → carried as in-text [VERIFY #1], stated only as „в порядъка на 94%".

## Time-sensitive / game claims to confirm at publish (primary-source URLs + what they show)
| Claim | Source to confirm | What the source shows |
|---|---|---|
| Provider **Relax Gaming**; released **2 Sept 2020**; sequel to Money Train (2019) | relax-gaming.com/products/casino/moneytrain2; relax-gaming.com launch news 08/2020 | Provider's own page: launched September 2nd; 50,000x; Money Cart with Collector/Payer/Sniper; Game of the Year 2020. |
| Grid **5×4**, **40 fixed paylines** | askgamblers; bigwinboard; vegasslotsonline | 5 reels, 4 rows, 40 paylines. |
| Default RTP **96.40%** (house ~**3.60%**) | bigwinboard; askgamblers; stakers; playusa | 96.4% headline/default build. |
| Lower configurable build ~**94%** | askgamblers/bigwinboard (94.0%); vegasslotsonline (94.40%) | Conflict on exact value → in-text [VERIFY #1]. |
| **Feature buy** = **100× залога**, effective RTP **~98%** | bigwinboard; askgamblers; vegasslotsonline; slotsmate | Buy Money Cart for 100x stake; ~98% RTP in bought mode. |
| Volatility **много висока (5/5)**; max win **~50 000×** | bigwinboard (High 5/5); relax-gaming.com (50,000x) | Web-verified; VSO 2,500x is an outlier (see conflict). |
| Money Cart: **3+** scatter/bonus symbols; **3** respins; reset to 3 on each new symbol; up to 2 extra reels | bigwinboard; askgamblers; relax-gaming.com | Persistent respins, expanding reels. |
| Special symbols: Collector, Payer, Sniper, Necromancer, Reset Plus, Persistent, Collector-Payer | bigwinboard; askgamblers; relax-gaming.com | All confirmed. |
| Base respin: **2** scatters, multiplier **+1** per losing spin | bigwinboard; askgamblers | Confirmed. |
| **Feature buy banned in the UK (UKGC)** | gamblingzone.com; onlinegamblingwebsites.com; bigwinboard.com | UKGC prohibits feature/bonus buys on the UK-regulated market. Stated as a UK jurisdiction fact, never a BG legal claim. |

## Illustrative numbers used (none BG-operator-sourced)
| Where | Figure | Note |
|---|---|---|
| RTP/edge | 96.40% / ~3.60% | provider default (confirm live build) |
| Worked example | €1000 оборот → ~€964 / ~€36 (3.60%) house | illustrative |
| Max win | ~50 000× залога | ceiling, framed as such |
| Feature buy | 100× залога → ~98% RTP | cost of access, not better odds |

## Recalculation shown (per Step-6 requirement)
- RTP 96.40% on €1000: return 0.9640 × €1000 = **€964.00 ≈ €964**; house 0.0360 × €1000 = **€36.00 ≈ €36**. ✓ matches text + infographic.
- SVG house bar: 0.0360 × 500 = **18 px**. ✓
- Feature buy 100× at €1 stake = **€100**. ✓
- Core honesty claims: default RTP 96.40% is configurable downward (operator's choice); the game is very high volatility → long dry runs; ~50 000× is a ceiling, not an expectation; feature buy at 100× buys variance/guaranteed access, not a lower house edge (long-run edge unchanged). All correct. ✓

## Compliance spot-check (verbatim untouchables present)
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-text closing + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 regime), pending-application wording, NO issued-licence claim, NO invented №. ✓
- Internal links: only the approved set (/blog/games-providers/, /kazino-igri/rotativki/, /kak-ocenyavame/, /otgovorna-igra/), 4 distinct, in-context. ✓
- Byline Георги Тодоров; brand „Всички Казина" spelled correctly. ✓
- Zero em-dashes (incl. title/meta). En-dash only in the verbatim footer „10:00–17:00". ✓ No promise/hype; volatility and the ~50 000× framed as risk/ceiling; feature buy framed as edge-neutral. ✓ Slot explainer, not an operator review → no affiliate link, no НАП licence №. ✓

## External check (Step 7 — Gemini cross-model)
Model gemini-3.1-pro-preview. Human-likeness: **HL 80** („Likely human-written, 80% confidence" → PASS on pass 1). Original kept (keep-best; the draft passed at the threshold and a rewrite risks dropping below 80). Gemini praised the pragmatic BG metaphors („чакалня към бонуса", „да кроиш бюджет около джакпот") and confirmed all [VERIFY]/18+/disclosure elements are correctly placed and must not be touched. 07-gemini-check-1.md persists as the audit trail.

## Images (Step 8)
2 images, both PASS on pass 1 (score 85, gemini-3.1-pro-preview review):
- `images/money-train-2-rtp.svg` — hand-authored infographic; every figure traces to 05b (96.40% / 3.60% / €1000 / ~€964 / ~€36 / 50 000x / 100x); 18+/RG + „числата са примерни" note. Accuracy flawless, no layout defect.
- `images/money-train-2-hero.webp` — decorative steampunk-cart + volatility-graph metaphor (gemini-3-pro-image, 26.8 KB); no fabricated UI/logos/numbers/people/winning.

## Anti-cannibalization note
Distinct branded slot explainer (a specific game), not the bonus-buy CONCEPT guide (the mechanic) — the concept guide is referenced in plain text only, no invented /blog/ slug. Anchored to the Relax Gaming provider profile via a plain-text mention „нашия профил на Relax Gaming" + the live /blog/games-providers/ hub. Game explainer, not an operator review → no affiliate link, no НАП licence № invented.

## Human-action list (owned by you, Step 6 / Step 8)
1. Fill the „[About Всички Казина boilerplate]" slot.
2. Resolve the two in-text [VERIFY]s (exact lower RTP build + which the casino runs; feature-buy availability at the target operator/market).
3. Confirm the max-win value (50 000x per provider; ignore the VSO 2,500x outlier) and the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).
