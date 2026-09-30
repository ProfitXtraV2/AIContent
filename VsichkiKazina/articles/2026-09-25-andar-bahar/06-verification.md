# 06 — VERIFICATION · vk-0179 · Andar Bahar

STATUS: for human sign-off before publish.
Surviving flags: [VERIFY] 0 · [DATA NEEDED] 0 · [CONFLICT] 0.

## External checks (finalized by orchestrator)
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402, prepayment credits depleted). gemini=skipped. Initial draft stands as final 05b. See 07-gemini-check-1.md.
- Images (Step 8): 1 hand-authored SVG infographic (win share 51.5%/48.5% + payouts/edges; numbers verbatim to 05b). AI hero SKIPPED (402). Image review SKIPPED (402); manual integrity PASSED. images: 1 (infographic, review skipped — API down). See 08-image-review-1.md.

Body word count: 1066 (prose, excluding the payout table, the image ALT and caption; excludes footer blocks). Within the 1000–1500 guide band.

## EVERY SPECIFIC FIGURE → PRIMARY SOURCE
Both sources reached and read on 25.09.2026.
Source A (probabilities/edges/side bets): Wizard of Odds — Andar Bahar — https://wizardofodds.com/games/andar-bahar/
Source B (rules/positions/first-card convention): Pagat — Andar Bahar — https://www.pagat.com/banking/andar_bahar.html
NOT a source: Wikipedia /wiki/Andar_Bahar = a 2013 film; deliberately excluded.

| Figure in body | Value | Source |
|---|---|---|
| Тесте | едно, 52 карти | A, B |
| Средна карта | една, задава съвпадението (не е жокер/коз) | A, B |
| Позиции | Andar (отвътре) / Bahar (отвън) | A, B |
| Раздаване | последователно към двете страни до съвпадение по ранг (без значение боята) | A, B |
| Средно карти до решаване | ≈13 след средната | A |
| Дял на страната с първата карта | ≈51.5% (51.5006%) | A |
| Дял на другата страна | ≈48.5% (48.4994%) | A |
| Andar/Bahar по позиция | Andar печели на нечетна, Bahar на четна (Andar тегли първа) | A |
| Коя страна тегли първа | различава се по казина (цвят на средната карта / винаги Andar); едж следва първата карта | A, B |
| Изплащане — страна с първата карта | 0.90:1 | A |
| Домашно предимство — 0.90:1 | 2.15% | A |
| Изплащане — другата страна | 1:1 (равни пари) | A |
| Домашно предимство — равни пари | 3.00% | A |
| По-стиснати варианти | 0.85:1 → 4.72% / 0.95:1 → 5.43% | A |
| Страничен залог „1–5 карти" | ≈2.50:1, предимство ≈5% (5.13%) | A |
| Страничен залог — цвят на средната карта | ≈0.90:1, предимство ≈5% | A |
| Страничен залог — точна стойност | плаща едро, предимство над 7% | A |
| RTP — 0.90:1 | ≈97.85% (= 100% − 2.15%) | derived from A |
| RTP — равни пари | ≈97.00% (= 100% − 3.00%) | derived from A |

Note: payout specifics VARY by casino/provider; the body presents the most common (Wizard-documented) values and states this explicitly. The €20 example is labelled примерни.

## RECALCULATION — edges from the win probabilities (with working)
Andar (first-card side), pays 0.90:1: EV per unit = 0.515006 × 0.90 − 0.484994 × 1 = 0.463505 − 0.484994 = −0.021489 → house edge 2.15%. ✓ matches Source A.
Bahar (other side), pays 1:1 (evens): EV = 0.484994 × 1 − 0.515006 × 1 = −0.030012 → house edge 3.00%. ✓ matches Source A.
Win probabilities sum to 51.5006% + 48.4994% = 100% (a match always eventually appears; no push). ✓
RTP = 100% − edge → 97.85% (0.90:1) and 97.00% (evens). Internally consistent.

## INTERNAL LINKS USED (4, all live in sitemap 25.09.2026)
1. /kazino-igri/kazino-na-zhivo/ — anchor „казиното на живо"
2. /blog/bakara-pravila/ — anchor „бакара" (sibling simple card game contrast)
3. /otgovorna-igra/ — anchor „инструментите за отговорна игра" (RG touch)
4. /kak-ocenyavame/ — anchor „публична методика, а не през усещане"

## HUMAN CHECK BEFORE PUBLISH
- Payout specifics vary by casino — confirm the target operator's Andar/Bahar payouts and which side is dealt first (that side carries the ~51.5% edge and the lower payout).
- Confirm 51.5006% / 48.4994% and the 2.15% / 3.00% edges vs the live Wizard of Odds page.
- Wikipedia was NOT used (the plain title is a film); sources are Wizard of Odds + Pagat.
- No operator named, no НАП/tax claim, no affiliate — correct for an educational guide.
- Fill [About Всички Казина boilerplate] + [author-bio] at publish.
