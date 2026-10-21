# 06 — VERIFICATION · vk-0186 · Lightning Roulette (Evolution)

STATUS: for human sign-off before publish.
Surviving flags: [VERIFY] 1 (straight-up RTP 97.10% / edge 2.90% — provider-cited, confirm on Evolution paytable) · [DATA NEEDED] 0 · [CONFLICT] 0.
The [VERIFY] flag is intentionally left IN the body per house rules (a [VERIFY] does not block publish; the human resolves it at Step 6).

## External checks (finalized by orchestrator)
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402, prepayment credits depleted). gemini=skipped.
  Initial draft stands as final 05b. See 07-gemini-check-1.md.
- Images (Step 8): 1 hand-authored SVG infographic (round flow + key numbers; numbers verbatim to 05b).
  AI hero SKIPPED (402). Image review SKIPPED (402); manual integrity PASSED. images: 1 (infographic, review skipped — API down).
  See 08-image-review-1.md.

Body word count: 1008 (prose, excluding image ALT/caption and footer blocks). Within the 1000–1500 guide band.

## EVERY SPECIFIC FIGURE → SOURCE
Sources reached 26.09.2026 (Evolution's own paytable cited via live-casino review sites; provider page not read directly).
- livecasinocomparer — Evolution Lightning Roulette review: https://www.livecasinocomparer.com/live-casino-software/evolution-live-casino-software/evolution-roulette/lightning-roulette-review/
- effortlessmath — 500x multipliers don't help the math: https://www.effortlessmath.com/blog/lightning-roulette-500x-multipliers-math/
- roulette-strat — Lightning Roulette strategy/math: https://roulette-strat.com/strategy/lightning-roulette
- Wizard of Odds — Lightning Roulette (per-multiplier weights; NOT read directly): https://wizardofodds.com/games/lightning-roulette/

| Figure in body | Value | Source / status |
|---|---|---|
| Колело | европейска рулетка, едно зеро, 37 числа (0–36) | generic roulette fact; livecasinocomparer, effortlessmath |
| Щастливи числа | от 1 до 5 на рунд | livecasinocomparer, effortlessmath (corroborated) |
| Множители | 50x, 100x, 200x, 300x, 400x, 500x | livecasinocomparer (Evolution set); WoO snippet |
| Множител обхват | важи само върху стрейт-ъп (залог на едно число); външни залози никога | livecasinocomparer, effortlessmath (generic rule) |
| Базова печалба | 29:1 (вместо стандартните 35:1) = 6 единици по-малко | livecasinocomparer, effortlessmath (both) |
| RTP стрейт-ъп | ≈97.10% (таблица на Evolution) | livecasinocomparer — [VERIFY] (not read from Evolution paytable directly) |
| Домашно предимство (числа) | ≈2.90% (= 100% − 97.10%) | derived from straight-up RTP |
| Външни залози | RTP 97.30% / предимство 2.70% (непроменени) | livecasinocomparer; standard European roulette |
| Стандартна европейска стрейт-ъп | 35:1, RTP 97.30%, предимство 2.70% | standard roulette math |
| Разлика | 0.20 процентни пункта (2.90 − 2.70) | derived |
| Пример (примерни) | €1 стрейт-ъп → €35 стандарт vs €29 Lightning; 100x → €100; 500x → €500 | derived, labelled примерни |

## SOURCE DISCREPANCY (resolved, not written as a debate)
effortlessmath asserts the straight-up RTP stays 97.30% / edge 2.70% ("unchanged"). Evolution's own paytable (cited by
livecasinocomparer) states 97.10% / 2.90%. The provider paytable is authoritative and matches the brief's central angle (straight-up
edge ABOVE plain European 2.70%). Body states 97.10% / 2.90% with a single [VERIFY]; the human confirms on the in-game/official
paytable at Step 6. No two-camp "Version A/B" structure in the body.

## NOT USED (avoid fabrication)
- No per-multiplier probability table (Wizard of Odds hosts one but the exact weights were not read directly) → NOT published.
- No claim about whether the multiplier payout includes or excludes the returned stake (sources ambiguous: "30:1 to 500x including
  returned bet" vs "500x") → body states the multiplier pays up to 500x on a single-number hit without asserting the stake-inclusion detail.

## RECALCULATION (with working)
- House edge (straight-up) = 100% − RTP = 100% − 97.10% = 2.90% → body states ≈2.90%. ✓
- Plain European straight-up edge = 100% − 97.30% = 2.70% → body states 2.70%. ✓
- Edge difference = 2.90% − 2.70% = 0.20pp → body states „0.20 процентни пункта". ✓
- Base cut = 35 − 29 = 6 units → body states „шест единици". ✓
  (All RTP/edge marked long-run statistics, not a session promise; multiplier feature funded by the 6-unit base reduction.)

## INTERNAL LINKS USED (4, all live in sitemap 26.09.2026)
1. /kazino-igri/kazino-na-zhivo/ — anchor „казино на живо"
2. /kazino-igri/ruletka/ — anchor „маса за рулетка"
3. /blog/live-game-shows/ — anchor „лайв гейм шоута и рулетки с множители" (link, don't duplicate the overview)
4. /otgovorna-igra/ — anchor „инструментите за отговорна игра" (RG touch)
NOTE: no roulette rules/strategy blog guide exists in the sitemap → linked the /kazino-igri/ruletka/ category; no slug invented.

## HUMAN CHECK BEFORE PUBLISH
- CONFIRM the 97.10% straight-up RTP / 2.90% edge on Evolution's in-game info panel or official paytable — resolve the [VERIFY].
- Confirm the multiplier value set (50x–500x) and the 1–5 lucky-numbers range for the specific version served.
- No operator named, no НАП/tax claim, no affiliate — correct for a provider game explainer (Evolution named only as game maker).
- Fill [About Всички Казина boilerplate] + [author-bio] at publish.
