# 06 — VERIFICATION · vk-0188 · Funky Time (Evolution)

STATUS: for human sign-off before publish.
Surviving flags: [VERIFY] 2 · [DATA NEEDED] 0 · [CONFLICT] 0.
1. [VERIFY] Per-bet RTP figures (95,99% / 95,98% / 95,51% / 95,49% / 95,38%) — source/version-dependent — §„RTP зависи от…".
2. [VERIFY] Bonus max multipliers / Stayin' Alive ladder top (sources disagree; €500 000 cap solid) — §„Големите множители са таван".
Both left IN the body per house rules (a [VERIFY] does not block publish; human resolves at Step 6).

## External checks (finalized by orchestrator)
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402). gemini=skipped. Initial draft stands as final 05b. See 07-gemini-check-1.md.
- Images (Step 8): 1 hand-authored SVG infographic (wheel composition + per-bet RTP extremes + max win cap; numbers verbatim to 05b).
  AI hero SKIPPED (402). Image review SKIPPED (402); manual integrity PASSED. images: 1. See 08-image-review-1.md.

Body word count: ~996 (prose, excluding Title/Meta, ALT/caption, footer). Within the 1000–1800 guide band (house game-guide norm ~930–1080).

## SOURCES REACHED (26.09.2026)
- Evolution — Funky Time: https://games.evolution.com/live-casino/game-shows/funky-time/
- CasinoScores / Casino.org — Funky Time: https://www.casino.org/casinoscores/blog/funky-time-live/
- LiveCasinoComparer — Funky Time: https://www.livecasinocomparer.com/live-casino-software/evolution-live-casino-software/funky-time-live/
- livecasinodata — Funky Time how-to-play: https://livecasinodata.com/games/funky-time/how-to-play

## EVERY SPECIFIC FIGURE → SOURCE
| Figure in body | Value | Source / status |
|---|---|---|
| Wheel segments | 64 | Evolution; livecasinodata |
| Число „1" | 28 полета | livecasinodata |
| Букви | 24 полета | livecasinodata |
| Bar / Disco / Stayin' Alive / VIP Disco | 6 / 3 / 2 / 1 | livecasinodata |
| Bonus segments total | 12 | derived (6+3+2+1) |
| Число „1" payout | 1:1 | livecasinodata |
| Letter payout | 25:1 | livecasinocomparer |
| DigiWheel boost | up to 50x | Evolution; livecasinodata |
| Boosted letter max | 1250x | derived (25 × 50) |
| Worked example | €5 → €125 (25:1); €5 → €6250 (1250x) | derived |
| Bonus frequency | ~once per 5 spins | derived (64/12 ≈ 5,3) |
| Disco / VIP Disco floors | 37 / 63 squares | CasinoScores/livecasinocomparer |
| Stayin' Alive ladder | 20 levels | livecasinocomparer |
| RTP: 1 / Bar / Disco / Letters+Stayin / VIP Disco | 95,99 / 95,98 / 95,51 / 95,49 / 95,38% | CasinoScores/livecasinocomparer — [VERIFY] per version |
| House edge | ≈4,0%–4,6% | derived (100 − RTP) |
| Max win cap | 500 000 € на залог | livecasinocomparer; CasinoScores |
| Release / maker | 2023, Evolution (Riga) | Evolution press |

## NOT USED (avoid fabrication)
- Per-round max multipliers (Stayin' Alive 10 000x vs 1 000x; VIP Disco varies) → only the €500 000 hard cap stated, [VERIFY].
- The "25 000x" figure from an initial brief (unconfirmed by reputable sources) → NOT used.
- A stray "June 2022" release date (contradicted by Evolution's own 2023 press) → 2023 used.

## RECALCULATION (with working)
- Composition: 28 + 24 + 12 = 64; bonus 6 + 3 + 2 + 1 = 12. ✓
- Bonus frequency: 12 / 64 = 0,1875 → 1 per ≈5,3 → „веднъж на около пет завъртания". ✓
- DigiWheel: letter base 25:1 × 50x boost = 1250x; on €5 stake → 25 × 5 = €125, 1250 × 5 = €6250. ✓
- House edge: 100 − 95,99 = 4,01%; 100 − 95,38 = 4,62% → „между около 4,0% и около 4,6%". ✓

## INTERNAL LINKS USED (4, all live in sitemap 26.09.2026)
1. /kazino-igri/kazino-na-zhivo/ — „казино на живо" (§1) and „казиното на живо" (§8)
2. /blog/live-game-shows/ — „другите колела на късмета и шоу формати" (§1) [hub]
3. /otgovorna-igra/ — „инструментите за отговорна игра" (RG)
4. /kak-ocenyavame/ — „публична методика, а не на усещане"

## HUMAN CHECK BEFORE PUBLISH
- CONFIRM the per-bet RTP figures and the per-round max multipliers on the specific Evolution version served in BG —
  resolve the two [VERIFY] flags.
- No operator named, no НАП/tax claim, no affiliate — correct for a provider game explainer (Evolution = maker only).
- Branded spoke of /blog/live-game-shows/; distinct from Crazy Time (vk-0185) and Monopoly Live (vk-0187).
- Fill [About Всички Казина boilerplate] + [author-bio] at publish.
