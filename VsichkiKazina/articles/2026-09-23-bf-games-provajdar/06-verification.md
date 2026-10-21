# 06-VERIFICATION — Всички Казина · 2026-09-23-bf-games-provajdar
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **BF Games: профил на доставчика, механики и топ слотове** · type: guide (provider profile) · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 92/100 · humanisation: Gemini Step-7 human 85 (HL 25 → 15 → 85, kept pass 2, PASS) · images: 2 (infographic 100, hero 100; best 100) · body ~963 words (~1,150 incl. footer) · run date: 23.09.2026

## Surviving flags
**1** in-text [VERIFY]: BF Games' precise corporate relationship to the LV Group and the „over 15 years experience" claim are described differently across third-party databases; the official site (bfgames.com) confirms only the founding year (2013) and the legal entities (Bee-Fee Limited, London; Malta subsidiary). The text hedges („част от източниците я описват като част от групата LV Group … не се потвърждават еднозначно от официалния сайт") and asserts no fixed corporate structure. No [CONFLICT]/[DATA NEEDED]. Provider profile: no BG operator, no licence number, no bonus terms.

## Time-sensitive / provider claims to confirm at publish (source URLs below)
| Claim | Source to confirm | Note |
|---|---|---|
| Founded **2013**; Bee-Fee Limited (London) + Malta subsidiary | bfgames.com („Since 2013…"); aboutslots | Web-verified. |
| LV-Group relationship + „15 years" experience | — | Sources conflict → in-text [VERIFY]; hedged wording used. |
| Portfolio **185+** titles across **25+** markets (incl. Bulgaria) | bfgames.com | Provider's own figure; third-party DBs quote lower (65–110+) → attributed as „по данни на самата компания". |
| B2B **supplier** licences: UK Gambling Commission (2017) + Malta MGA (2019); eCOGRA testing | bfgames.com; casinohawks; softswiss | Supplier, NOT an operator/casino licence. Body states regulator+year only; identifiers (UKGC #48761; MGA/B2B/614/2018) held in reserve, not invented into the copy. |
| BF Daily Jackpots: daily-drop progressive across most titles | casinohawks; bfgames.com | Funding-from-bets framed as the standard industry description. |
| Top-title RTPs: Lucky Tropics **97.00%**, Aztec Adventure **96.22%**, Buffalo Trail **96.16%**, Book of Gods **96.12%**, Cave of Fortune **96.04%**, Book of Gates **96.03%** | casinohawks provider page; AskGamblers/slotsmate per-game | Web-verified. Cluster at/just above the ~96% modern average. Adjustable builds exist (Magic Hunter 94.19–98.14) → operator chooses → confirm per casino. |
| Book of Gods: 96.12% RTP, high volatility, 5x3 / 10 lines, released **July 2019**, 3+ books = 10 FS + expanding symbol, gamble double/quadruple, max ~**x5015** | AskGamblers; slotsmate; slotslaunch | Web-verified. |

## GUARDRAIL EXCLUSIONS (seed candidates that FAILED verification — deliberately NOT written as BF Games games)
| Seed candidate | Finding | Action |
|---|---|---|
| **Rise of Egypt** | This is a **Playson** slot (certified RTP ~95.82%), not a BF Games title. | EXCLUDED — no other company's game attributed to BF Games. |
| **Lucky Book** | No BF Games title by this name found across the game DBs. | EXCLUDED. (BF Games does have „Lucky Tropics" — a different, verified title, which IS used.) |
| **Book of Gods** | Confirmed BF Games title (AskGamblers/slotsmate/slotslaunch). | KEPT — used as the flagship deep-dive. |

## Illustrative / interpretive figures (none BG-operator-sourced)
| Where | Figure | Note |
|---|---|---|
| Adjustable-RTP band | Magic Hunter 94.19%–98.14% | third-party DB quotes this certified range for one title; stated as an example of multi-build variance, not per-casino. |
| Infographic scale | 95.50%–97.50% | visual scale only; the six RTP labels are the article's real figures. |

## Recalculation shown (per Step-6 requirement)
- Infographic bar math (Lucky Tropics 97.00% on a 95.50–97.50 scale over a 410px track):
  width = (97.00 − 95.50) / (97.50 − 95.50) × 410 = 1.50 / 2.00 × 410 = **307.5 ≈ 308 px** ✓ (SVG uses 308).
- 96% reference line: x = 150 + (96.00 − 95.50) / 2.00 × 410 = 150 + 102.5 = **252.5 ≈ 253** ✓ (SVG uses 253).
- Honesty claims: the top-title RTPs sit at/just above the ~96% modern average ✓; titles ship in multiple adjustable builds so the operator picks the number (Magic Hunter 94.19–98.14) ✓; BF Daily Jackpots is funded from bets and triggers at random → does not lower the house edge ✓; the B2B licence + eCOGRA test confirm fairness to the stated rules, not a player advantage ✓; the gamble is a coin-flip that adds variance, not value ✓. All correct.

## Compliance spot-check (verbatim untouchables present)
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-text closing + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 regime), pending-application wording, NO issued-licence claim, NO invented №. ✓
- Internal links: only the approved set (/kak-ocenyavame/, /slot-igri/, /kazino-igri/rotativki/, /blog/games-providers/, /otgovorna-igra/), 5 distinct, in-context. ✓
- Byline Георги Тодоров; brand „Всички Казина" spelled correctly. ✓
- Zero em-dashes (incl. meta). En-dash only in the verbatim footer „10:00–17:00" and in the illustrative RTP ranges. ✓ No promise/hype; certificates and the progressive framed as house-edge mechanics, not hooks. ✓ Provider profile, not an operator review → no affiliate link, no НАП licence №. ✓

## External check (Step 7 — Gemini cross-model)
Model gemini-3.1-pro-preview. Human-likeness by version: initial 05b **25** („Shows AI patterns 75%"); Humaniser pass 1 **15** („Likely AI-written 85%"); Humaniser pass 2 **85** („Likely human-written 85%", PASS). Per keep-best, kept **pass 2** (highest HL). content-queue gemini = `human 85`. All numbers, links, RG lines, 18+, [VERIFY], dates, byline, brand UNTOUCHED across every pass. 07-gemini-check-1/-2/-3.md persist as the audit trail.

## Images (Step 8)
2 images:
- `images/bf-games-rtp.svg` — hand-authored infographic; every figure traces to 05b (97.00 / 96.22 / 96.16 / 96.12 / 96.04 / 96.03 / ~96% / Magic Hunter 94.19–98.14); source cited; 18+/RG note. Gemini review 75 → fix (footer line split, canvas extended) → 75 → fix (ref line + title spacing) → **100 PASS**.
- `images/bf-games-book-hero.webp` — decorative flat-vector „book + gears/tech" concept hero (gemini-3-pro-image, 23 KB); no fabricated UI/logos/numbers/people/winning. Reviewed **100 PASS**. 08-image-review-1/-2.md persist.

## Anti-cannibalization note (Step-6 human check)
No BF Games provider page in the sitemap. Clean provider-profile pillar. Provider-hub sibling to Amusnet/EGT (vk-0021) and Pragmatic (vk-0019). Distinct from the /blog/games-providers/ listing hub (BF-Games-specific profile, distinct primary kw), linked prose-only. Not an operator review → no affiliate link; no operator/licence № invented.

## Human-action list (owned by you, Step 6 / Step 8)
1. Fill the „[About Всички Казина boilerplate]" slot.
2. Resolve the in-text [VERIFY]: confirm the LV-Group relationship + „15 years" claim, or keep the hedged wording.
3. Confirm per-casino RTP builds for the target operator at publish (multiple certified versions exist; some drop well below 96%).
4. If provider licence identifiers are wanted (UKGC Account #48761; MGA/B2B/614/2018), pull them from the official registers — none invented into the body.
5. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).
6. Guardrail confirmed: Rise of Egypt (Playson) and Lucky Book (unverified) are NOT presented as BF Games games.
