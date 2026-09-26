# 06 — VERIFICATION · vk-0185 · Crazy Time (Evolution)

STATUS: for human sign-off before publish.
Surviving flags: [VERIFY] 3 · [DATA NEEDED] 0 · [CONFLICT] 0.
1. [VERIFY] Per-bet RTP figures (source/version-dependent) — §„RTP зависи от това на какво залагаш".
2. [VERIFY] Max-win cap ~20 000x / advertised ~25 000x (version-specific) — §„Гигантските множители са опашка".
3. [VERIFY] Top Slot max multiplier ~50x (not read from provider in-game panel) — §„Top Slot решава нещо…".
All three are intentionally left IN the body per house rules (a [VERIFY] does not block publish; human resolves at Step 6).

## External checks (finalized by orchestrator)
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402, prepayment credits depleted). gemini=skipped.
  Initial draft stands as final 05b. See 07-gemini-check-1.md.
- Images (Step 8): 1 hand-authored SVG infographic (wheel composition + per-bet RTP range + max win; numbers verbatim to 05b).
  AI hero SKIPPED (402). Image review SKIPPED (402); manual integrity PASSED. images: 1. See 08-image-review-1.md.

Body word count: 1038 (prose, excluding Title/Meta, image ALT/caption, footer blocks). Within the 1000–1500 guide band.

## SOURCES REACHED (26.09.2026)
- Wizard of Odds — Crazy Time: https://wizardofodds.com/games/crazy-time/
- CasinoBeats — How to Play Crazy Time: https://casinobeats.com/features/how-to-play-crazy-time/
- Deucescracked — Crazy Time 2026 strategy/RTP: https://www.deucescracked.com/blog/crazy-time-2026-strategy-rtp-multipliers-smart-play

## EVERY SPECIFIC FIGURE → SOURCE
| Figure in body | Value | Source / status |
|---|---|---|
| Колело | 54 полета | Wizard of Odds; CasinoBeats (54, 9 bonus) |
| Число 1 | 21 полета | Wizard of Odds (composition table) |
| Число 2 | 13 полета | Wizard of Odds |
| Число 5 | 7 полета | Wizard of Odds |
| Число 10 | 4 полета | Wizard of Odds |
| Coin Flip | 4 полета | Wizard of Odds |
| Cash Hunt | 2 полета | Wizard of Odds |
| Pachinko | 2 полета | Wizard of Odds |
| Crazy Time | 1 поле | Wizard of Odds |
| Числа общо / бонуси | 45 (~83%) / 9 (~17%) | derived (21+13+7+4=45; 9/54=16,7%); CasinoBeats corroborates 9 bonus |
| Бонус честота | ~веднъж на 6 завъртания | derived (54/9=6); search corroboration |
| Числа плащат | X:1 (5 → 5:1) | Wizard of Odds / search |
| Top Slot | 1 залог + 1 множител на рунд; до ~50x | CasinoBeats (one multiplier for one bet spot); ~50x → [VERIFY] |
| Cash Hunt | 108 скрити множителя | CasinoBeats |
| RTP число 1 | ≈96,08% (най-висок) | Deucescracked / search — [VERIFY] (source/version dependent) |
| RTP число 2 / 5 / 10 | ≈95,95% / 95,78% / 95,73% | Deucescracked / search — [VERIFY] |
| RTP Cash Hunt / Coin Flip | ≈96,05% / 95,70% | Deucescracked / search — [VERIFY] |
| RTP Pachinko / Crazy Time | ≈94,33% / 94,41% (най-нисък) | Deucescracked / search — [VERIFY] |
| RTP средно | ≈95,41% | published average — [VERIFY] |
| Домашно предимство | ≈5,6% (бонус) / <4% (число 1) | derived from RTP |
| Таван на печалбата | ≈20 000x (версия) | Wizard of Odds (20 000:1) — [VERIFY] |
| Рекламиран максимум | до ≈25 000x | CasinoBeats (Cash Hunt); real 25 000x hit 11.12.2022 (search) — [VERIFY] |
| Пуснат | 2020, Evolution | search corroboration |

## NOT USED (avoid fabrication)
- Per-bonus max-cap table (Coin Flip ~5 000x / Pachinko ~10 000x / Cash Hunt ~25 000x / Crazy Time ">20 000x") — sources
  inconsistent → only the headline ~20 000x cap and ~25 000x advertised max stated, version-flagged.
- The "40 000x promotional" figure (single source) — NOT stated.
- Wizard of Odds' own EV computation (all bets ~96,06–96,08%) — NOT presented as the per-bet table; the widely-published
  per-bet spread is used instead, with the [VERIFY] caveat that figures depend on source/version.

## RECALCULATION (with working)
- Wheel composition: 21 + 13 + 7 + 4 (numbers) = 45; + 4 + 2 + 2 + 1 (bonus) = 9; 45 + 9 = 54. ✓ Matches body.
- Number share: 45 / 54 = 0,8333 → „около 83%"; bonus 9 / 54 = 0,1667 → „около 17%"; frequency 54 / 9 = 6 → „веднъж на шест". ✓
- House edge: 100% − 96,08% = 3,92% → „под 4%"; 100% − 94,33% = 5,67% and 100% − 94,41% = 5,59% → „около 5,6%". ✓
  (all marked long-run over thousands of rounds, not a session promise)

## INTERNAL LINKS USED (4, all live in sitemap 26.09.2026 — verified via curl)
1. /kazino-igri/kazino-na-zhivo/ — anchor „казино на живо"
2. /blog/live-game-shows/ — anchor „казиното на живо и подобните му game show заглавия" (the HUB / game-show overview)
3. /otgovorna-igra/ — anchor „инструментите за отговорна игра" (RG touch)
4. /kak-ocenyavame/ — anchor „публична методика, а не на усещане"

## HUMAN CHECK BEFORE PUBLISH
- CONFIRM the per-bet RTP figures, the max-win cap (~20 000x) / advertised max (~25 000x), and the Top Slot cap (~50x) on
  the specific Evolution version served in BG — resolve the three [VERIFY] flags.
- No operator named, no НАП/tax claim, no affiliate — correct for a provider game explainer (Evolution named only as maker).
- This is the branded spoke of the /blog/live-game-shows/ hub; it links to the hub and does not duplicate the overview.
- Fill [About Всички Казина boilerplate] + [author-bio] at publish.
