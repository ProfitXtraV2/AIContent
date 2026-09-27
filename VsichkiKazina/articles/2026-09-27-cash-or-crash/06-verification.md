# 06 — VERIFICATION · vk-0189 · Cash or Crash (Evolution)

STATUS: for human sign-off before publish.
Surviving flags: [VERIFY] 2 · [DATA NEEDED] 0 · [CONFLICT] 0 (RTP fixed-vs-variable resolved at synthesis; see note).
1. [VERIFY] Per-strategy RTP figures (≈99,59% optimal / ≈94,51% chasing top) — source/version-dependent; one
   source (crashgames.guide) describes 99,59% as fixed — §„RTP се движи с твоята дисциплина".
2. [VERIFY] Top-multiplier-to-rung mapping / any euro cap (18 000x без злато, до 50 000x със злато; sources
   disagree on the mapping, 50 000x overall max is solid) — §„Стълбата, 18 000x и 50 000x".
Both left IN the body per house rules (a [VERIFY] does not block publish; human resolves at Step 6).

## RTP CONFLICT — RESOLUTION (not left as a two-camp structure)
crashgames.guide claims RTP is fixed at 99,59% regardless of strategy. Two detailed reviews (crashgamesplay,
americancasinoguide) and Evolution's own „when played optimally" wording give 99,59% as the OPTIMAL ceiling with
realized RTP falling to ≈94,51% at maximum risk. Resolved toward the majority + mathematically-correct reading
(optimal play is the ceiling; poor cash-out decisions lower realized RTP). Written as strategy-dependent with a
[VERIFY] on the exact %; NO „one source says X, another Y" wording in the body.

## External checks (finalized by orchestrator)
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402). gemini=skipped. Initial draft stands as
  final 05b. See 07-gemini-check-1.md.
- Images (Step 8): 1 hand-authored SVG infographic (drum composition + decisions + per-strategy RTP + max
  multipliers; numbers verbatim to 05b). AI hero SKIPPED (402). Image review SKIPPED (402); manual integrity
  PASSED. images: 1. See 08-image-review-1.md.

Body word count: ~986 (prose, excluding Title/Meta, ALT/caption, footer). Within the 1000–1800 guide band
(house game-guide norm ~930–1080).

## SOURCES REACHED (27.09.2026)
- Evolution press — Cash or Crash: https://www.evolution.com/news/evolution-launches-cash-or-crash-unique-high-flying-live-game-show
- LiveCasinoComparer — Cash or Crash: https://www.livecasinocomparer.com/live-casino-software/evolution-live-casino-software/evolution-cash-or-crash-live/
- crashgamesplay — Cash or Crash review: https://crashgamesplay.com/games/cash-or-crash-review/
- crashgames.guide — Cash or Crash Live: https://crashgames.guide/games/cash-or-crash-live/
- americancasinoguide — Cash or Crash: https://www.americancasinoguide.com/crash-games/cash-or-crash

## EVERY SPECIFIC FIGURE → SOURCE
| Figure in body | Value | Source / status |
|---|---|---|
| Balls in drum | 28 | Evolution; livecasinocomparer; crashgamesplay |
| Green / red / gold | 19 / 8 / 1 | livecasinocomparer; crashgamesplay; crashgames.guide |
| First-draw odds | ≈68% / ≈29% / ≈3,6% | derived (19/28, 8/28, 1/28) |
| After 10 greens | 9 green, 8 red, 1 gold = 18; red ≈44% | derived (8/18) |
| Ladder | 20 нива | livecasinocomparer; crashgamesplay; crashgames.guide |
| Decisions | Вземи всичко / Вземи половината / Продължи | Evolution; livecasinocomparer |
| Top без злато / със злато | 18 000x / до 50 000x | livecasinocomparer; crashgamesplay; crashgames.guide — [VERIFY] mapping |
| Worked example | €10 → €180 000 (18 000x); €10 → €500 000 (50 000x) | derived |
| RTP optimal / max risk | ≈99,59% / ≈94,51% | Evolution; crashgamesplay; americancasinoguide — [VERIFY] per version |
| House edge | ≈0,41%–5,49% | derived (100 − RTP) |
| Profit rate | ~71% of rounds | Evolution press |
| Release / maker | 2021, Evolution | Evolution press |

## NOT USED (avoid fabrication)
- Any euro max-win cap for the game → not stated by a reputable source; only the 50 000x multiplier cap used, [VERIFY].
- americancasinoguide's garbled „18 000x with gold" mapping → NOT used; majority reading (18 000x без злато,
  до 50 000x със злато) applied.
- Studio location for Cash or Crash → not confirmed per game; NOT stated.
- Exact bet limits (a review cites $0.20–$2,500) → operator/currency-dependent, NOT used.

## RECALCULATION (with working)
- Composition: 19 + 8 + 1 = 28. ✓
- First-draw: 8/28 = 0,2857 → „близо 29%"; 19/28 = 0,6786 → „около 68%"; 1/28 = 0,0357 → „около 3,6%". ✓
- After 10 greens: 19−10 = 9 green, 8 red, 1 gold = 18; red 8/18 = 0,4444 → „около 44%". ✓
- Worked: €10 × 18 000 = €180 000; €10 × 50 000 = €500 000. ✓
- House edge: 100 − 99,59 = 0,41%; 100 − 94,51 = 5,49% → „между около 0,41% и около 5,49%". ✓

## INTERNAL LINKS USED (5, all in the approved live set)
1. /kazino-igri/kazino-na-zhivo/ — „казино на живо" (§1) and „казиното на живо" (§8)
2. /blog/live-game-shows/ — „шоу форматите с жив водещ" (§1) [hub]
3. /blog/krash-igri-aviator/ — „класическите краш игри като Aviator" (§1) [crash-games cross-link]
4. /otgovorna-igra/ — „инструментите за отговорна игра" (RG)
5. /kak-ocenyavame/ — „публична методика, а не на усещане"

## HUMAN CHECK BEFORE PUBLISH
- CONFIRM the per-strategy RTP figures and the top-multiplier-to-rung mapping on the specific Evolution version
  served in BG — resolve the two [VERIFY] flags.
- No operator named, no НАП/tax claim, no affiliate — correct for a provider game explainer (Evolution = maker only).
- Branded spoke of /blog/live-game-shows/; distinct from Crazy Time (vk-0185), Monopoly Live (vk-0187),
  Funky Time (vk-0188) and the Aviator crash-games guide (cross-linked, not duplicated).
- Fill [About Всички Казина boilerplate] + [author-bio] at publish.
