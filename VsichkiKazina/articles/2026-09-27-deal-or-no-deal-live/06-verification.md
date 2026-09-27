# 06 — VERIFICATION · vk-0194 · Deal or No Deal Live (Evolution)

STATUS: for human sign-off before publish.
Surviving flags: [VERIFY] 2 · [DATA NEEDED] 0 · [CONFLICT] 0.
1. [VERIFY] Множителят, с който класиращият слот 3×3 задава стойността на топ куфарчето — източниците се разминават (олбг „до 10x"; други по-високо). Механиката е описана без фиксирано число. §„Класиране".
2. [VERIFY] Точният по-нисък RTP при платените режими за класиране (Instant/Easy) — посочва се в диапазон по източници (напр. базов ≈95,42% срещу по-широк диапазон/оптимален по олбг). §„RTP: 95,42%…".
Both left IN the body per house rules (a [VERIFY] does not block publish; human resolves at Step 6). No Version A/B debate structure written into the body.

## External checks (finalized by orchestrator)
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402). gemini=skipped. Initial draft stands as final 05b. See 07-gemini-check-1.md.
- Images (Step 8): 1 hand-authored SVG infographic (three stages + RTP/edge/max-win; numbers verbatim to 05b).
  AI hero SKIPPED (402). Image review SKIPPED (402); manual integrity PASSED. images: 1. See 08-image-review-1.md.

Body word count: 958 (prose, excluding Title/Meta, ALT/caption, footer). Within the ~950–1300 guide band.

## SOURCES REACHED (27.09.2026)
- CasinoBeats — How to Play Deal or No Deal Live: https://casinobeats.com/features/how-to-play-deal-or-no-deal/
- olbg — Evolution Deal or No Deal (review & guide): https://www.olbg.com/casino-sites/articles/evolution-deal-or-no-deal
- casinos.com — Deal or No Deal Live: https://www.casinos.com/games/deal-or-no-deal-live
- (Evolution own game page games.evolution.com/... → HTTP 404 at fetch; onlinecasinogameshows.com → HTTP 503; neither reachable, not used.)

## EVERY SPECIFIC FIGURE → SOURCE
| Figure in body | Value | Source / status |
|---|---|---|
| Maker / format | Evolution, живо гейм шоу с водещ | all sources |
| Briefcases in play | 16 | CasinoBeats; casinos.com; olbg |
| ТВ формат кутии | 26 | casinos.com |
| Number of stages | три (класиране → топ-ъп → куфарчета) | all sources |
| Qualifying round | слот 3×3, скатери | CasinoBeats; olbg |
| Instant qualification skip | 18x залога | casinos.com |
| Top-up wheel | 15 полета, множители 5x–50x | CasinoBeats; olbg |
| Banker offers | до 4 | CasinoBeats; olbg; casinos.com |
| Max win | 500x залога | CasinoBeats; casinos.com |
| RTP (base) | 95,42% | CasinoBeats; casinos.com — [VERIFY] per version/mode |
| House edge | ≈4,58% | derived (100 − 95,42) |
| €100 return | ≈€95,42 | derived (100 × 0,9542) |
| Пример: две куфарчета €10 и €1000 | средно €505 | derived, labelled примерни |
| Qualifying multiplier for top case | not stated | sources disagree — [VERIFY] |
| Reduced RTP on paid modes | not stated | range across sources — [VERIFY] |

## NOT USED (avoid fabrication)
- Конкретен паричен таван в €/$ (напр. $450 000 при макс. залог) → валутно- и залог-зависим; тялото държи само 500x залога.
- Точен множител на класиращия слот и точен по-нисък RTP при бързите режими → [VERIFY], без число в тялото.
- Година на пускане (источниците дават 2019 срещу 2021) → не се посочва в тялото; не е сред задължителните числа.

## RECALCULATION (with working)
- Домашно предимство: 100 − 95,42 = 4,58%. ✓
- Възвръщаемост на €100: 100 × 0,9542 = €95,42. ✓
- Примерна средна стойност: (10 + 1000) / 2 = €505 (labelled примерни). ✓
- Няма превъртане/bonus math (provider explainer). ✓

## INTERNAL LINKS USED (4, all from the confirmed-live set)
1. /kazino-igri/kazino-na-zhivo/ — „казино на живо" (§1) и „казино на живо" (close)
2. /blog/live-game-shows/ — „живите гейм шоу формати" (§1) [hub]
3. /otgovorna-igra/ — „инструментите за отговорна игра" (close + RG footer)
4. /kak-ocenyavame/ — „публична методика, а не на усещане" (close)

## HUMAN CHECK BEFORE PUBLISH
- CONFIRM the base/standard RTP and the reduced RTP for the paid qualification modes on the specific Evolution version served in BG, and the qualifying-slot top-case multiplier — resolve the two [VERIFY] flags.
- No operator named, no НАП/tax claim, no bonus terms, no affiliate links — correct for a provider game explainer (Evolution = maker only).
- Branded spoke of /blog/live-game-shows/; distinct from the wheel-format шоу заглавия (Dream Catcher etc.).
- Fill [About Всички Казина boilerplate] + [author-bio] at publish.
