# 06 — VERIFICATION · vk-0187 · Monopoly Live (Evolution)

STATUS: for human sign-off before publish.
Surviving flags: [VERIFY] 3 · [DATA NEEDED] 0 · [CONFLICT] 0.
1. [VERIFY] Number-segment split (1:22 / 2:15 / 5:7 / 10:4) — secondary-sourced; Evolution confirms totals 54/48/2/3/1 — §„54 полета".
2. [VERIFY] Per-bet RTP figures (source/version-dependent) — only headline ~96,2% stated — §„Няма Top Slot, а RTP…".
3. [VERIFY] Max multiplier ~10 000x (version-specific); €500 000 cap is solid — §„Големите множители са таван".
All three left IN the body per house rules (a [VERIFY] does not block publish; human resolves at Step 6).

## External checks (finalized by orchestrator)
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402). gemini=skipped. Initial draft stands as final 05b. See 07-gemini-check-1.md.
- Images (Step 8): 1 hand-authored SVG infographic (wheel composition + RTP/max; numbers verbatim to 05b). AI hero SKIPPED (402).
  Image review SKIPPED (402); manual integrity PASSED. images: 1. See 08-image-review-1.md.

Body word count: ~1000 (prose, excluding Title/Meta, ALT/caption, footer). Within the 1000–1800 guide band.

## SOURCES REACHED (26.09.2026)
- Evolution — Monopoly Live: https://games.evolution.com/live-casino/game-shows/monopoly-live/
- CasinoBeats — How to Play Monopoly Live: https://casinobeats.com/features/how-to-play-monopoly-live/
- LiveCasinoComparer — Monopoly Live: https://www.livecasinocomparer.com/live-casino-software/evolution-live-casino-software/monopoly-live/
- Wizard of Odds — Evolution Gaming overview: https://wizardofodds.com/online-gambling/evolution-gaming/

## EVERY SPECIFIC FIGURE → SOURCE
| Figure in body | Value | Source / status |
|---|---|---|
| Wheel segments | 54 | Evolution (54 total) |
| Numbered segments | 48 | Evolution |
| Число 1 / 2 / 5 / 10 | 22 / 15 / 7 / 4 | CasinoBeats — [VERIFY] internal split (Evolution confirms 48 numbered total) |
| Chance | 2 полета | Evolution |
| „2 Rolls" / „4 Rolls" | 3 / 1 полета | Evolution |
| Number payouts | face value (5→5:1, 10→10:1) | WoO/CasinoBeats |
| Worked example | €10 on 5 → €50; €10 on 10 → €100 | derived from face-value payouts |
| Bonus frequency | ~once per 13–14 spins | derived (54/4 = 13,5) |
| Chance frequency | 2/54 | derived |
| Top Slot | none | CasinoBeats; LiveCasinoComparer |
| Best-bet RTP | ≈96,2% | CasinoBeats/LiveCasinoComparer — [VERIFY] per bet |
| Bonus bets | lower RTP, higher variance | sources above |
| Max win cap | €500 000 на залог | LiveCasinoComparer |
| Max multiplier | ~10 000x | LiveCasinoComparer — [VERIFY] |
| Release / maker | 2019, Evolution | Evolution/CasinoBeats |

## NOT USED (avoid fabrication)
- A per-bet RTP table (sources disagree which segment is highest/lowest) → only the ~96,2% max + "bonus bets return less".
- The stray "2017" release year (Dream Catcher mix-up) → 2019 used.
- Exact bonus max multipliers per round (inconsistent) → only the €500 000 hard cap stated, 10 000x [VERIFY]-flagged.

## RECALCULATION (with working)
- Composition: 22 + 15 + 7 + 4 = 48 numbers; + 2 (Chance) + 3 ("2 Rolls") + 1 ("4 Rolls") = 6 → 48 + 6 = 54. ✓
- Bonus frequency: 4 bonus fields / 54 = 1 per 13,5 → „веднъж на около 13–14 завъртания". ✓
- Face-value payout: €10 × 5 = €50 win; €10 × 10 = €100 win. ✓ (long-run framing preserved)

## INTERNAL LINKS USED (4, all live in sitemap 26.09.2026)
1. /kazino-igri/kazino-na-zhivo/ — „казино на живо" (§1) and „казиното на живо" (§8)
2. /blog/live-game-shows/ — „колела на късмета и подобни шоу формати" (§1) [hub]
3. /otgovorna-igra/ — „инструментите за отговорна игра" (RG)
4. /kak-ocenyavame/ — „публична методика, а не на усещане"

## HUMAN CHECK BEFORE PUBLISH
- CONFIRM the internal number-segment split, the per-bet RTP figures, and the ~10 000x max multiplier on the specific
  Evolution version served in BG — resolve the three [VERIFY] flags.
- No operator named, no НАП/tax claim, no affiliate — correct for a provider game explainer (Evolution = maker only).
- Branded spoke of /blog/live-game-shows/; distinct from Crazy Time (vk-0185); does not duplicate the overview.
- Fill [About Всички Казина boilerplate] + [author-bio] at publish.
