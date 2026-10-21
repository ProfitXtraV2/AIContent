# 06 — VERIFICATION · vk-0184 · Teen Patti (тийн пати)

STATUS: for human sign-off before publish.
Surviving flags: [VERIFY] 1 (total-bet RTP ≈97.99% — search-snippet, confirm on the live table) · [DATA NEEDED] 0 · [CONFLICT] 0.
The [VERIFY] flag is intentionally left IN the body per house rules (a [VERIFY] does not block publish; the human resolves it at Step 6).

## External checks (finalized by orchestrator)
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402, prepayment credits depleted). gemini=skipped.
  Initial draft stands as final 05b. See 07-gemini-check-1.md.
- Images (Step 8): 1 hand-authored SVG infographic (ranking order + round flow + key numbers; numbers verbatim to 05b).
  AI hero SKIPPED (402). Image review SKIPPED (402); manual integrity PASSED (rendered to PNG, no overlap/clip). images: 1.
  See 08-image-review-1.md.

Body word count: 1034 (prose, excluding image ALT/caption and footer blocks). Within the 1000–1500 guide band.

## EVERY SPECIFIC FIGURE → SOURCE
Sources reached and read 26.09.2026.
A = Wikipedia — Teen patti — https://en.wikipedia.org/wiki/Teen_patti
B = Wizard of Odds — Teen Patti — https://wizardofodds.com/games/teen-patti/  (ranking confirmation; Super Spade version paytables NOT used)
C = Evolution official — Teen Patti — https://games.evolution.com/live-casino/live-poker/teen-patti/
D = livecasinocomparer — Evolution Teen Patti — https://www.livecasinocomparer.com/live-casino-software/evolution-live-casino-software/evolution-teen-patti/
E = casinos.com (search snippet) — total-bet RTP 97.99% → [VERIFY], not read directly

| Figure in body | Value | Source / status |
|---|---|---|
| Тесте | 52 карти без жокери | A |
| Раздадени карти | 3 на всеки, срещу дилъра (live) | A, C |
| Подредба | тройка (trail) > пюр секванс > секванс > цвят > чифт > висока карта | A, B |
| Комбинации от 22 100 | тройка 52 · пюр секванс 48 · секванс 720 · цвят 1096 · чифт 3744 · висока карта 16 440 | A |
| Обръщане | секванс 720 < цвят 1096 → кентата бие цвета | A (derived from counts) |
| Домашна игра | 3 до 6 играчи, бут (boot), на сляпо/на виждане, chaal | A |
| Ход (live) | Ante → 3 карти → Play (=Ante) или Fold | C, D |
| Класиране на дилъра | дама висока (Queen high) | C, D |
| Изплащания | не се класира → Ante 1:1, Play push; класира се + печелиш → Ante 1:1, Play 1:1 | C |
| Ante бонус | при секванс или по-добра ръка, независимо от дилъра | C |
| Pair Plus paytable | чифт 1:1 · цвят 4:1 · кент 5:1 · тройка 30:1 · пюр секванс 40:1 · мини роял 100:1 | D |
| 6 Card Bonus | плаща от тройка нагоре, до 1000:1 (роял флош) | C |
| RTP на Ante | ≈96.63% (edge ≈3.37%) | D (RTP); edge derived |
| Pair Plus RTP | ≈95.51% (edge ≈4.49%) | D (RTP); edge derived |
| 6 Card Bonus RTP | ≈91.44% (edge ≈8.56%) | D (RTP); edge derived |
| Total-bet RTP | ≈97.99% | E — [VERIFY] (not read from the studio spec directly) |
| Пример €10 → €400 | 40:1 на пюр секванс | illustrative (примерни); recalculated below |

## NOT USED / OMITTED (avoid fabrication or version-mixing)
- Wizard of Odds Super Spade Games paytables/edges (Pair Plus 50/40/30/6/3/1; Ante edge 3.79%, Pair Plus 6.91%, 6 Card 15.28%)
  are a DIFFERENT version → NOT stated; the body uses only the Evolution-cited figures to avoid a mixed/version-A-vs-B tell.
- Evolution's exact Ante-bonus pay odds were not read → body states only „секванс или по-добра ръка", no invented numbers.

## RECALCULATION (with working)
- House edge = 100% − RTP: 100 − 96.63 = 3.37% (Ante) ✓ · 100 − 95.51 = 4.49% (Pair Plus) ✓ · 100 − 91.44 = 8.56% (6 Card Bonus) ✓.
  All marked long-run (върху хиляди ръце, не върху сесията).
- Side-bet check: 4.49% and 8.56% both exceed the 3.37% main-game edge → body's „страничните струват повече" holds. ✓
- Combination sum: 52 + 48 + 720 + 1096 + 3744 + 16 440 = 22 100 ✓ (matches the stated total).
- Illustrative payout: €10 × 40 (from 40:1) = €400 profit → body states „носи печалба €400". ✓ (labelled примерни)

## INTERNAL LINKS USED (4, all live in sitemap 26.09.2026)
1. /kazino-igri/kazino-na-zhivo/ — anchor „казиното на живо"
2. /blog/kak-se-igrae-poker-kazino/ — anchor „Западният покер" (contrast: inverted rankings vs Western poker)
3. /otgovorna-igra/ — anchor „инструментите за отговорна игра" (RG touch)
4. /kak-ocenyavame/ — anchor „публична методика, а не на усещане"

## HUMAN CHECK BEFORE PUBLISH
- CONFIRM total-bet RTP ≈97.99% (currently a search-snippet, NOT read from the studio spec) — resolve the [VERIFY].
- Confirm the Pair Plus / 6 Card Bonus paytables and RTPs and the Ante-bonus odds for the specific studio version served
  (figures here are the Evolution live version; other providers' Teen Patti differ).
- No operator named, no НАП/tax claim, no affiliate — correct for a provider game explainer (Evolution named only as the game maker).
- Fill [About Всички Казина boilerplate] + [author-bio] at publish.
