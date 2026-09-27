# 06 — VERIFICATION · vk-0189 · Dream Catcher (Evolution)

STATUS: for human sign-off before publish.
Surviving flags: [VERIFY] 2 · [DATA NEEDED] 0 · [CONFLICT] 0.
1. [VERIFY] Per-bet RTP figures (96,58% / 95,51% / 95,34% / 92,74% / 91,24% / 90,81%) — sources disagree;
   Wizard of Odds (rigorous house-edge math) used — §„RTP зависи от…".
2. [VERIFY] Max win multiplier / cap (7 000x / 10 000x / 20 000x cited; €500 000 cap solid) — §„Максималната печалба е таван".
Both left IN the body per house rules (a [VERIFY] does not block publish; human resolves at Step 6).

## External checks (finalized by orchestrator)
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402). gemini=skipped. Initial draft stands as final 05b. See 07-gemini-check-1.md.
- Images (Step 8): 1 hand-authored SVG infographic (wheel composition + per-bet RTP extremes + max win cap; numbers verbatim to 05b).
  AI hero SKIPPED (402). Image review SKIPPED (402); manual integrity PASSED. images: 1. See 08-image-review-1.md.

Body word count: ~975 (prose, excluding Title/Meta, ALT/caption, footer). Within the 1000–1800 guide band (house game-guide norm ~930–1080).

## SOURCES REACHED (27.09.2026)
- Evolution — Dream Catcher: https://games.evolution.com/live-casino/game-shows/dream-catcher/
- Evolution news — Dream Catcher awards/history: https://www.evolution.com/news/evolutions-dream-catcher-wins-digital-product-year-g2e-las-vegas
- Wizard of Odds — Dream Catcher (house edge / segments): https://wizardofodds.com/games/dream-catcher/
- casinos.com — Dream Catcher: https://www.casinos.com/games/dream-catcher
- LiveCasinoComparer — Dream Catcher: https://www.livecasinocomparer.com/live-casino-software/evolution-live-casino-software/evolution-dreamcatcher/

## EVERY SPECIFIC FIGURE → SOURCE
| Figure in body | Value | Source / status |
|---|---|---|
| Wheel segments | 54 | Evolution; Wizard of Odds; all agree |
| Число „1" | 23 полета | Wizard of Odds; livecasinocomparer |
| Число „2" | 15 полета | Wizard of Odds; livecasinocomparer |
| Число „5" | 7 полета | Wizard of Odds; livecasinocomparer |
| Число „10" | 4 полета | Wizard of Odds; livecasinocomparer |
| Число „20" | 2 полета | Wizard of Odds; livecasinocomparer |
| Число „40" | 1 поле | Wizard of Odds; livecasinocomparer |
| Number segments / multiplier segments | 52 / 2 | derived (23+15+7+4+2+1=52; +2x+7x) |
| Payouts | 1:1 … 40:1 | all sources |
| Hit frequency 1 / 2 / 5 / 40 | 42,59 / 27,78 / 12,96 / 1,85% | derived from 54ths (WoO probs) |
| Multiplier frequency | ~3,70% | derived (2/54) |
| Multiplier stack 2x+7x | 14x | Wizard of Odds; casinos.com |
| Worked example | €5 → €200 (40:1); €5 → €1400 (7x×40) | derived |
| RTP: 10 / 2 / 1 / 20 / 5 / 40 | 96,58 / 95,51 / 95,34 / 92,74 / 91,24 / 90,81% | Wizard of Odds — [VERIFY] per version |
| House edge | ≈3,42% (10) – 9,19% (40) | derived (100 − RTP) |
| €100 return on 40 / on 10 | <€91 / ≈€96,58 | derived (100×RTP) |
| Max win cap | 500 000 € на залог | casinos.com; livecasinocomparer |
| Max multiplier | 7 000x / 10 000x / 20 000x | sources disagree — [VERIFY] |
| Release / maker | 2017, Evolution (Riga); original money wheel | Evolution news |

## NOT USED (avoid fabrication)
- Conflicting per-bet RTP sets from LiveCasinoComparer / casinos.com → not blended; Wizard of Odds used as
  the single stated set, [VERIFY] caution added (no Version-A/B debate written into body).
- A stray "June 2021" release date (LiveCasinoComparer) → contradicted by Evolution's own 2017 launch/awards → 2017 used.
- Exact per-round max multiplier → only the €500 000 hard cap stated; multiplier list flagged [VERIFY].

## RECALCULATION (with working)
- Composition: 23 + 15 + 7 + 4 + 2 + 1 = 52 number segments; + 2x + 7x = 54. ✓
- Frequencies: 23/54 = 0,4259; 15/54 = 0,2778; 7/54 = 0,1296; 1/54 = 0,0185; 2/54 = 0,0370. ✓
- Multiplier: 2 × 7 = 14x; on €5 stake at 40:1 → 40 × 5 = €200; 40 × 7 × 5 = €1400. ✓
- House edge: 100 − 96,58 = 3,42%; 100 − 90,81 = 9,19%. ✓
- Return on €100: 90,81% → €90,81 (< €91); 96,58% → €96,58. ✓

## INTERNAL LINKS USED (4, all live in sitemap 27.09.2026)
1. /kazino-igri/kazino-na-zhivo/ — „казино на живо" (§1) and „казино на живо" (§7)
2. /blog/live-game-shows/ — „останалите колела на късмета и шоу формати" (§1) [hub]
3. /otgovorna-igra/ — „инструментите за отговорна игра" (RG)
4. /kak-ocenyavame/ — „публична методика, а не на усещане"

## HUMAN CHECK BEFORE PUBLISH
- CONFIRM the per-bet RTP figures and the max win multiplier/cap on the specific Evolution version served in
  BG — resolve the two [VERIFY] flags.
- No operator named, no НАП/tax claim, no bonus terms, no affiliate — correct for a provider game explainer
  (Evolution = maker only).
- Branded spoke of /blog/live-game-shows/; distinct from Crazy Time (vk-0185), Monopoly Live (vk-0187) and
  Funky Time (vk-0188).
- Fill [About Всички Казина boilerplate] + [author-bio] at publish.
