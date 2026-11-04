# 06-VERIFICATION — Всички Казина · 2026-09-20-money-train-4
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Money Train 4 (Relax Gaming): какво променя четвъртата част** · type: guide (game explainer) · byline: editorial (signed Георги Тодоров) · gate: PASS 94/100 · humanisation: HUMAN-LIKE · Gemini Step-7: human 85 (PASS, initial kept) · images: 2 (infographic 100 + hero 100, review pass 2 PASS) · run date: 20.09.2026

## Surviving flags
1 in-text [VERIFY] flag:
- [VERIFY] exact number of Money Cart symbols „21, от които 8 напълно нови" — cited in game DBs/aggregators, NOT on the official Relax Gaming product page. The named NEW mechanics themselves (Arms Dealer, Upgrader, Unlocker, Reset Plus, Persistent Shapeshifter; Absorber removed; „20+ функции") are provider/DB-verified; only the precise count/„8 new" is unconfirmed.

Game explainer on public provider/game-DB data: no BG operator named, no НАП licence №, no bonus T&C, no affiliate link (nothing recommended).

## Time-sensitive / game claims to confirm at publish (source URLs below)
| Claim | Source | Note |
|---|---|---|
| Relax Gaming; released **20.09.2023** network-wide; sequel to MT1 (2019), MT2 (2020), MT3 (2022) | relax-gaming.com news 2023; slotbeats; gamingintelligence | Fact-correction: brief anchor guessed „2024"; verified 2023. |
| **RTP 96.10%** default; **96.50%** on Bonus Buy versions | relax-gaming.com; bigwinboard; casinorange | Provider + DBs. Confirm the operator's live config at publish (Relax ships several). |
| **Max win 150 000× залога** (MT3 = 100 000×, MT2 = 50 000×) | relax-gaming.com (official spec); bigwinboard | Primary source. Extreme figure — confirm at publish. |
| Base grid **6×6**, scatter pays (≥8 високи / ≥10 ниски); Money Cart starts **6×4** | bigwinboard | DB-verified. MT3 contrast: 5×4, 40 линии (askgamblers/aboutslots). |
| **Bonus buy 100× stake** (entry) / **500× stake** (with 1 persistent symbol) | bigwinboard; relax-gaming-provider | Extreme-cost figure — confirm at publish. |
| **Волатилност екстремно висока (5/5)** | relax-gaming.com; bigwinboard | Provider rating. |
| NEW vs MT3: Arms Dealer, Upgrader, Unlocker, Reset Plus, Persistent Shapeshifter; Absorber removed; „20+ функции" | bigwinboard; relax-gaming.com | DB + provider. Exact symbol count flagged [VERIFY]. |
| Bet range **€0.10–€6** | relax-gaming.com; relax-gaming-provider | Provider spec. |

## Illustrative numbers used
| Where | Figure | Note |
|---|---|---|
| RTP worked example | €1 000 → ~€961 / ~€39 | illustrative, labelled примерно/илюстративно |
| Bonus-buy cost | at €1 stake: €100 / €500; at €6 max stake: €600 / €3 000 | derived from 100×/500× × stated stake, labelled примерен/при максималния залог |
| SVG RTP bar | 96.10% = 519px of 540px (519 + 21 = 540, flush) | math checked |

## Recalculation shown
- RTP 96.10% on €1 000 oborot: 0.9610 × €1 000 = **€961.00**; house = 0.0390 × €1 000 = **€39.00 (3.90%)**. ✓ (illustrative; text shows „~€961 / ~€39").
- Bonus buy at €1 stake: 100 × €1 = **€100**; 500 × €1 = **€500**. At €6 max stake: 100 × €6 = **€600**; 500 × €6 = **€3 000**. ✓
- SVG player bar: 0.9610 × 540 = **518.9 ≈ 519 px**; house 540 − 519 = **21 px** (flush at 540). ✓
- Honesty claims: high volatility redistributes the same house edge into rarer/bigger swings (not better odds); bonus buy buys access not a result; 150 000× is the tail of the distribution, not a target. All correct. ✓

## Compliance spot-check (verbatim untouchables present)
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — body + footer. ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026), pending-application, NO issued claim, NO invented №. ✓
- Internal links: sitemap/approved set (/blog/games-providers/, /slot-igri/visok-rtp/, /slot-igri/, /otgovorna-igra/), 4 distinct. ✓ Money Train 2/3 named but NOT linked (not yet in live sitemap). ✓
- Byline Георги Тодоров; brand „Всички Казина". ✓ Zero em-dashes. En-dash only in numeric/time ranges (€0.10–€6, 10:00–17:00). ✓ Game explainer → no operator, no licence №, no affiliate link. ✓
- Extra RG caution present (bonus-buy is real money at risk; max win is a tail, not a target) beyond the footer block. ✓

## External check (Step 7 — Gemini cross-model)
gemini_check.py. HL: initial **85** („Highly likely human-written 85%") → **PASS** on the initial draft (anti-AI applied proactively; no Humaniser pass). content-queue gemini = `human 85`. 07-gemini-check-1.md persists. Gemini flagged optional style nits (a „despite X, Y" transition, one „not just X" flourish, caption redundancy) — NOT applied (PASS at 85; keep-best forbids risking a lower score; the caption's verbatim numbers are the Step-8 convention). The [VERIFY] flag correctly left for the human.

## Images (Step 8)
2 images, both PASS at review pass 2 (score 100, 0 integrity failures):
- `images/money-train-4-rtp-cena.svg` — illustrative RTP + bonus-buy-cost + max-win infographic; every figure traces to 05b; 18+/RG note. Pass 1 flagged long subtexts (85); pass 2 flagged descender margins (75) → boxes enlarged/re-centred → final 100.
- `images/money-train-4-hero.webp` — dystopian sci-fi industrial train (34.3 KB); no UI/logos/numbers/people/winning. Pass 1 theme-mismatch (65, 19th-c steam) → regenerated toward sci-fi/neon → final 100. 08-image-review-1.md / -2.md persist.

## Anti-cannibalization note
No Money Train 4 page in the sitemap (checked 20.09.2026). Distinct branded kw „money train 4 / мъни трейн 4". Distinct from any Money Train 2/3 page (different game: 6×6 scatter-pays vs 5×4/40-lines, 150 000× vs 100 000× cap, new Money Cart symbols). Money Train 2/3 named, not linked (not in live sitemap). Game explainer → no affiliate link; no operator/licence № invented.

## Human-action list (Step 6 / Step 8)
1. Fill the „[About Всички Казина boilerplate]" slot.
2. Resolve the [VERIFY] flag: confirm the exact Money Cart symbol count („21, 8 new") against Relax Gaming's paytable, update the preceding sentence if needed, then remove the bracketed tag.
3. Confirm at publish the operator's live RTP configuration (96.10% vs 96.50%) and the max-win (150 000×) + bonus-buy (100×/500×) figures against the game's live paytable.
4. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).
