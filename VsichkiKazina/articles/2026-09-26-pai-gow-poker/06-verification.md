# 06 — VERIFICATION · vk-0181 · Pai Gow Poker (Пай Гоу покер)

STATUS: for human sign-off before publish.
Surviving flags: [VERIFY] 0 · [DATA NEEDED] 0 · [CONFLICT] 0.
(Uncertain figures — element of risk ≈2.73% and exact per-holding house-way splits — were OMITTED from the body, not flagged into prose or fabricated. See „OMITTED" below.)

## External checks (finalized by orchestrator)
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402, prepayment credits depleted). gemini=skipped.
  Initial draft stands as final 05b. See 07-gemini-check-1.md.
- Images (Step 8): 1 hand-authored SVG infographic (7→5+2 split + edge/commission/push; numbers verbatim to 05b).
  AI hero SKIPPED (402). Image review SKIPPED (402); manual integrity PASSED. images: 1 (infographic, review skipped — API down).
  See 08-image-review-1.md.

Body word count: 1002 (prose, excluding image ALT/caption and footer blocks). Within the 1000–1500 guide band.

## EVERY SPECIFIC FIGURE → PRIMARY SOURCE
Sources reached and read 26.09.2026.
A = Wizard of Odds — Pai Gow Poker — https://wizardofodds.com/games/pai-gow-poker/ (+ /play/ headline, FAQ, side-bet appendix)
B = Pagat — Pai Gow Poker — https://www.pagat.com/partition/paigowp.html
C = Wikipedia — Pai gow poker — https://en.wikipedia.org/wiki/Pai_gow_poker

| Figure in body | Value | Source |
|---|---|---|
| Тесте | 53 карти = 52 + 1 жокер | A,B,C |
| Жокер — петкартова ръка | асо, или допълва кент/флош/флош роял | A,B,C |
| Жокер — двукартова ръка | винаги асо | A,C |
| Раздадени карти | 7 на играч и на дилър | A,B,C |
| Подредба | 5-картова задна (силна) + 2-картова предна (малка) | A,B,C |
| Foul | задната по-слаба от предната → автоматична загуба | B,C |
| Печалба | и двете ръце трябва да бият дилъра; една:една = push; copy → дилър | A,B,C |
| Комисиона | 5% върху печелившите залози | A,C |
| Пушове (домашен метод) | ≈40.5% (40.4958%) | A |
| Домашно предимство — headline | ≈2.84% | A (/play/) |
| Домашно предимство — по домашния метод | ≈2.72% (2.7212%, non-banking) | A |
| RTP | ≈97.16% (= 100% − 2.84%) | derived from A |
| Странични залози | предимство няколко пъти по-високо, често >4%, двуцифрено при прогресивните | A (appendix: Emperor's 4.171%, Progressive 11.5428%) |
| Банкуване от играча | предимството срещу него почти изчезва (context, not advised) | A |

## OMITTED (uncertain — not stated, not fabricated)
- Element of risk ≈2.73%: could not be reproduced from a reachable Wizard page this run → NOT stated.
- Exact per-holding house-way splits: Wizard house-way sub-page 404'd → body gives only the general split principle, no per-hand table.

## RECALCULATION (with working)
- RTP = 100% − 2.84% = 97.16% → body states ≈97.16% (long-run, per initial wager, commission already inside the 2.84% edge). ✓
- Commission illustration: €100 winning bet × 5% = €5 → €95 net. Body states €100 → €95. ✓ (labelled примерни)
- 2.84% = rounded headline edge; 2.72% = precise house-way (non-banking). Both Wizard; presented as headline vs house-way, not mixed. ✓

## INTERNAL LINKS USED (4, all live in sitemap 26.09.2026)
1. /kazino-igri/ — anchor „казиното"
2. /blog/kak-se-igrae-poker-kazino/ — anchor „покера срещу други играчи" (contrast: player-vs-player poker)
3. /otgovorna-igra/ — anchor „инструментите за отговорна игра" (RG touch)
4. /kak-ocenyavame/ — anchor „публична методика, а не на усещане"

## HUMAN CHECK BEFORE PUBLISH
- Confirm house edge ≈2.84% (headline) / ≈2.72% (house way, non-banking) and ≈40.5% push rate vs the live Wizard page.
- Confirm the 5% commission and the copy→dealer rule vs the target operator's rules (commission can be a flat fee at some tables).
- Confirm the general house-way split principle; exact per-holding splits vary by casino appendix and were intentionally not tabled.
- No operator named, no НАП/tax claim, no affiliate — correct for an educational guide.
- Fill [About Всички Казина boilerplate] + [author-bio] at publish.
