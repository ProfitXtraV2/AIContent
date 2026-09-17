# 06-VERIFICATION — Всички Казина · 2026-09-17-pirots-2
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Pirots 2: как работи, RTP и волатилност** · type: guide (game explainer) · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 92/100, zero criticals · humanisation: HUMAN-LIKE · Gemini Step-7: skipped (HTTP 429) · images: 2 (infographic + hero-position SVG; AI hero skipped — Gemini image API down) · run date: 17.09.2026 · introduces NEW provider ELK Studios

## Surviving flags (2 in-text [VERIFY], allowed to remain)
1. **[VERIFY] точна по-ниска/конфигурируема RTP версия за Pirots 2 и коя работи при конкретния оператор.** Sourced default is 94.0% (bigwinboard, hideousslots, aboutslots). ELK titles are commonly shipped in operator-configurable RTP versions; no specific *lower* Pirots 2 build figure was reachable and confirmable, so none is stated. The text hedges ("ELK често доставя заглавията си в няколко RTP версии… провери в инфо-панела") rather than asserting a number. Confirm the live build in the game's info panel at the target casino before publish.
2. **[VERIFY] наличност на X-iter купуванията на БГ лицензирания пазар.** X-iter buy modes (3×/10×/25×/100×/500×) are a provider feature; bonus-buy availability varies by jurisdiction/operator. Confirm whether the buys are enabled for BG-licensed operators.

No [CONFLICT]/[DATA NEEDED]. Game explainer: no BG operator, no НАП licence №, no bonus terms. Every € figure is ILLUSTRATIVE.

## Numeric facts stated, each with a primary/reachable source (confirm at publish)
| Claim | Figure | Source(s) |
|---|---|---|
| Provider / release | ELK Studios · 2023 (07.11.2023) · sequel to Pirots | elk-studios.com; bigwinboard; fruityslots |
| Grid, no paylines, CollectR | starts **6×6**, expands to max **8×8** (Red Button/meteor) | elk-studios.com; bigwinboard; hideousslots |
| Collector birds | **4** — red, blue, green, purple; collect orthogonally-adjacent same-colour amber | bigwinboard; hideousslots; elk-studios.com |
| Symbol upgrade | amber symbols have **7** payout levels; upgrade via grey/multicolour arrows | elk-studios.com; respinix |
| Feature symbols | **8** types (upgrade, upgrade-all, egg/dino, mushroom, popcorn, Red Button, coins, wild) | bigwinboard; respinix |
| Coin symbol | up to **1000×** bet | respinix |
| Default RTP | **94.0%** (house edge **6.00%**) | bigwinboard; hideousslots; aboutslots |
| Volatility / hit freq | HIGH, **8/10** · hit frequency **25.4%** | hideousslots; aboutslots; revpanda |
| Max win | **10 000×** bet | elk-studios.com; bigwinboard; hideousslots |
| Bonus | **3** bonus symbols → bonus with **5** free drops + Super Bonus | bigwinboard; hideousslots |
| X-iter buys | Bonus Hunt **3×** · Popcorn Fiesta **10×** · Max Grid **25×** · Bonus **100×** · Super Bonus **500×** | elk-studios.com; bigwinboard; hideousslots |
| Stakes | max bet **€100** / min **€0.20** (brief; not forced into body) | bigwinboard |

Source URLs:
- https://www.elk-studios.com/games/pirots-2/
- https://www.bigwinboard.com/pirots-2-elk-studios-slot-review/
- https://hideousslots.com/slot-review/pirots-2/
- https://www.aboutslots.com/casino-slots/pirots-2
- https://respinix.com/demo/pirots-2/

## Illustrative numbers used (none BG-operator-sourced)
| Where | Figure | Note |
|---|---|---|
| RTP/edge | 94.0% / 6.00% | provider default (confirm live build) |
| Worked example | €1000 оборот → ~€940 / ~€60 (6.00%) house | illustrative |
| Max win | 10 000× bet | ceiling, framed as such |
| Coin symbol | up to 1000× | provider spec |

## Recalculation shown (per Step-6 requirement)
- RTP 94.0% on €1000: return 0,9400 × €1000 = **€940,00 ≈ €940**; house 0,0600 × €1000 = **€60,00 ≈ €60**. ✓ matches text + infographic.
- House edge = 100% − 94.0% = **6.00%**. ✓
- SVG house bar: 0,0600 × 600 = **36 px**. ✓ (rect x=614, width=36, card inner edge 650 → 0 px overflow, ≥16 px card padding kept).
- Hit frequency 25.4% → 1 / 0,254 = **3.94**, i.e. ~1 winning spin in 4 → text says "около… едно на четири". ✓ honest rounding.
- Core honesty claims: 94.0% is below the modern ~96% norm; high volatility (8/10) → long dry spells; 10 000× is a ceiling; configurable RTP means the operator picks the build; X-iter buys buy variance/access, not better odds (edge stays 6.00%). All correct. ✓

## Compliance spot-check (verbatim untouchables present)
- RG marker "18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-text closing + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 regime), pending-application wording, NO issued-licence claim, NO invented №. ✓
- Internal links: only the approved LIVE set (/slot-igri/, /blog/games-providers/, /kak-ocenyavame/, /otgovorna-igra/), 4 distinct, in-context, within the 2–4 guide count. ✓
- Byline Георги Тодоров; brand „Всички Казина" spelled correctly. ✓
- Zero em-dashes (body + meta + ALT + captions + both SVGs). En-dash only in the verbatim footer „10:00–17:00". ✓ No promise/hype; high volatility and the 10 000× framed as risk/ceiling; X-iter/RTP framed as edge-neutral/configurable. ✓ Game explainer, not an operator review → no affiliate link, no НАП licence №. ✓

## External check (Step 7 — Gemini cross-model)
Skipped: Gemini unavailable (HTTP 429, prepayment credits depleted). No external human-likeness score. In-pipeline Humaniser (HUMAN-LIKE) and Brand Gate (92/100, 0 criticals) stand. 07-gemini-check-1.md persists as the audit trail.

## Images (Step 8)
2 images; Gemini visual review skipped (HTTP 429), manual integrity check: 0 fabrications.
- `images/pirots-2-rtp-volatilnost.svg` — hand-authored infographic; every figure traces to 05b (94.0% / 6.00% / €1000 / ~€940 / ~€60 / 8/10 / 25.4% / 10 000×); 18+/RG note; rendered + eyeballed clean.
- `images/pirots-2-hero.svg` — abstract concept hero (grid + 4 collector colours + expanding-frame motif); no fabricated UI/logos/numbers/people/winning; rendered + eyeballed clean. 08-image-review-1.md persists.

## Anti-cannibalization note (Step-6 human check)
No Pirots 2 page in the sitemap. Clean game-explainer pillar; first ELK Studios title on the site (links to the providers context via /blog/games-providers/). Distinct from the /kazino-igri/rotativki/ listing (referenced as a term, prose-only). Game explainer, not an operator review → no affiliate link; no operator/licence № invented.

## Human-action list (owned by you, Step 6 / Step 8)
1. Fill the "[About Всички Казина boilerplate]" slot.
2. Resolve the 2 in-text [VERIFY]s: confirm the live RTP build (default 94.0% vs any lower configurable version) and the X-iter bonus-buy availability in the BG-licensed market.
3. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).
4. Optional: swap the hero-position SVG for an AI concept hero once the Gemini image API is back (HTTP 429 now).
