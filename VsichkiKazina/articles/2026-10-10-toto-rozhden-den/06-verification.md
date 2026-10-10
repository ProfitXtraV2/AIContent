# 06 — Verification checklist (Step 6, HUMAN-OWNED) — vk-0274 „Тото Рожден ден"

Status: **PUBLISH HOLD** until a human clears the items below. Flags stay in the text of
`05b-final-draft.md`; Claude resolved none of them.

## Surviving flags in 05b (9 × [VERIFY], 0 × [DATA NEEDED])
| # | Flag (verbatim topic) | Where to check | What the source currently shows (2026-10-10) |
|---|---|---|---|
| 1 | текуща цена 0.50 € | https://info.toto.bg/toto1-i-toto2/toto-2-rozhden-den/palno-kombinirane-v-toto-2-rozhden-den | One WebFetch on 2026-10-10 returned the system table: 0.50 EUR / комбинация; 4 комб. = 2.00 EUR; 9 комб. = 4.50 EUR. Confirm in a browser (CAPTCHA blocks scripts). |
| 2 | механизъм на тегленето (отделни барабани?) | toto.bg правила / Facebook излъчване на БСТ | Not found. Inference only: тираж 79 = 81/06/17/5, but 17.06.1981 was a Wednesday (3) → the weekday is drawn independently of the date. |
| 3 | валидност на изтеглената дата | правила на БСТ | Validity rule confirmed for the SLIP only (31 април / 29 февр. in non-leap year rejected). Not confirmed for the draw. |
| 4 | печели ли една позната цифра от годината | правила на БСТ | Groups are named „Година" (whole year) in launch news / aggregator; digit-level wins not confirmed. |
| 5 | текущ джакпот 7 353.06 € | https://www.toto.bg/ (results, тираж 79, 08.10.2026) | Source pack: 7 353.06 euro at тираж 79. Update to the publication-date draw. |
| 6 | % фонд печалби; фиксирани vs делими групи | правила на БСТ (rules PDF did not render in BG browser either) | Not found in any reachable source. |
| 7 | правила за прехвърляне на джакпота | правила на БСТ | Not found. |
| 8 | кои групи са делими | правила на БСТ | Not found. |
| 9 | актуален график (залози от 08.12.2022 г.) | https://www.toto.bg/ „Информация" | Source pack (read 2026-10-10): нечетен — нд 19:20 → чт 18:00; четен ТОТО 2 — чт 19:20 → нд 18:00. |

## Open [CONFLICT] (kept here per brief, NOT in the article text)
- **Launch year.** БНТ Новини 08.05.2016 (https://bntnews.bg/bg/a/toto-s-nova-igra) and utroruse
  28.04.2016 (https://utroruse.com/article/712706/): bets from 9 May 2016, first draw 12 май 2016 г.
  bg.wikipedia „Български спортен тотализатор" chronology: „2017 г.: Започва новата игра на Тото 2
  „Рожден Ден"". Article says „от май 2016 г. (според новините при старта)". Human: confirm.

## Other time-sensitive / sourced claims
- 15 печеливши групи; „едно към четири" (Веселин Кюркчиев) — БНТ 08.05.2016; utroruse 28.04.2016.
- Тото Джокер не се добавя към фиш за Рожден ден — info.toto.bg/toto1-i-toto2/toto-2-toto-dzhoker (fetched 2026-10-10 for vk-0266).
- Тегленето — на живо след 19:00 ч. във Facebook на БСТ; 6/49, 5/35, 6/42, Джокер, ВТШ — БНТ чт/нд 18:45 ч.; онлайн сайт недостъпен чт/нд 18:40–19:10 ч.; изплащане до 1 ч. след предаването; ePay.bg / БОРИКА — source pack bst-toto-2026-10-10.md (toto.bg).
- ЗХ чл. 3, 18+, 5 % бюджет, чл. 10г регистър, НАП 0700 18 700 — source pack nap-gambling-law-and-rg-2026-10-10.md.
- Editorial note for the human: Step-7 pass 1 added the phrase „ако барабаните не са честни, нищо от нея не важи" as a statement of the maths assumption. It is style, not a claim, but tone it down if it reads as insinuating anything about БСТ.

## Recalculated figure (working shown)
Assumptions: year 1 of 100; month 1 of 12; weekday 1 of 7, independent of the date; 365.25/12 = 30.4375 valid dates per month on average; all valid combinations equally likely.
- Combinations: 100 × 365 + 25 (29 Feb in years 00, 04, …, 96) = 36 525 valid dates × 7 = **255 675** → jackpot 1 на 255 675.
- No match at all: 99/100 × 11/12 × (1 − 1/30.4375) × 6/7 = 0.99 × 0.916667 × 0.967146 × 0.857143 ≈ **0.7523**
  → at least one win ≈ 1 − 0.7523 = **0.2477 ≈ 24.8 % ≈ 1 на 4.04** (matches BST's „1 към 4").
- 6/49 comparison: C(49,6) = 13 983 816; 13 983 816 / 255 675 ≈ **54.69** → „около 54.7 пъти".
- Group odds (python3, exact under the assumptions above) match the 05b table (e.g. Г+М+Д: 1/(1/100 × 1/12 × 1/30.4375 × 6/7) = 42 612.5 → 42 613).

## External checks
- Step 7 Gemini text: check 1 „Shows AI patterns, 75%" (human-likeness 25) → humaniser pass 1 (7b) + mechanical Brand-Gate re-check (byline, brand, 0 em-dashes, 18+, footer, 4 approved links, 9 [VERIFY], numdiff clean) → check 2 „Highly likely human-written, 90%" → **PASS**. Keep-best = pass 1 (90). gemini: `human 90`.
- Step 8 images: **images: 2 (hero 100, infographic 100)** — Gemini image review 1 score 100 PASS (both images in one review). Infographic figures verbatim from 05b; rendered to PNG via headless Chromium and inspected (no overlap/clip).
