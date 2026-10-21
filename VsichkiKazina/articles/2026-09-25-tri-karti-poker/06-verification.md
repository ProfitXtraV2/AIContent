# 06 — VERIFICATION · vk-0176 · Три карти покер (Three Card Poker)

STATUS: for human sign-off before publish.
Surviving flags: [VERIFY] 0 · [DATA NEEDED] 0 · [CONFLICT] 0.
## External checks (finalized by orchestrator)
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402, prepayment credits depleted). gemini=skipped. Only the initial draft exists; it stands as final 05b (keep-best trivial). See 07-gemini-check-1.md.
- Images (Step 8): 1 hand-authored SVG infographic (house edge by bet; numbers verbatim to 05b). AI hero SKIPPED (gemini_image_gen.py HTTP 402). Image review SKIPPED (HTTP 402); manual integrity check PASSED (no fabricated logo/number/screenshot, no faces, no glamorised winning). images: 1 (infographic, review skipped — API down). See 08-image-review-1.md.

Body word count: 1021 (prose, excluding the Pair Plus table, the image ALT and the caption; excludes the footer boilerplate blocks). Within the 1000–1500 guide band.

## EVERY SPECIFIC FIGURE → PRIMARY SOURCE

All figures below appear in the body and/or the infographic. Both sources reached and read on 25.09.2026.

Source A (primary game-math): Wizard of Odds — Three Card Poker — https://wizardofodds.com/games/three-card-poker/
Source B (corroboration, combinatorics + rules): Wikipedia — Three Card Poker — https://en.wikipedia.org/wiki/Three_Card_Poker

| Figure in body | Value | Source |
|---|---|---|
| Тесте карти / раздадени карти | 52 карти, по 3 на играч и дилър | A, B |
| Дилър се квалифицира с | дама-висока (Queen high) или по-добра | A, B |
| Дилър не се квалифицира → Анте / Play | Анте 1:1, Play няма действие (връща се) | B |
| Ante Bonus — плаща се независимо от квалификация/резултат | да | A, B |
| Ante Bonus таблица (Pay Table 1, най-често срещана) | кента 1:1, трипс 4:1, стрейт флъш 5:1 | A, B |
| Pair Plus — оригинална таблица (флъш 4:1) | пара 1:1, флъш 4:1, кента 6:1, трипс 30:1, стрейт флъш 40:1 | A |
| Pair Plus — домашно предимство (флъш 4:1) | 2.32% | A |
| Pair Plus — по-нова / най-разпространена таблица (флъш 3:1) | пара 1:1, флъш 3:1, кента 6:1, трипс 30:1, стрейт флъш 40:1 | A |
| Pair Plus — домашно предимство (флъш 3:1) | 7.28% | A |
| Ante & Play — домашно предимство (спрямо Антето) | 3.37% | A |
| Ante & Play — element of risk (спрямо оборота) | 2.01% | A |
| RTP (Ante & Play) | ≈96.63% (= 100% − 3.37%) | derived from A (see recalc) |
| Оптимална стратегия — праг | дама-6-4 или по-добра → Play; под нея → пас | A, B |
| Подредба (3 карти, високо→ниско) | стрейт флъш > трипс > кента > флъш > пара > висока карта | A, B |
| Общ брой ръце с 3 карти | 22,100 = C(52,3) | B (recalculated below) |
| Комбинации: кента | 720 | B |
| Комбинации: флъш | 1,096 | B |
| Комбинации: трипс | 52 | B |

Note: Pair Plus paytables VARY by casino; the body presents the two most common and states this explicitly. The €10 ante example is labelled примерни (illustrative) in body and infographic.

## RECALCULATION 1 — защо кентата бие флъша (combinatorics), with working

Total 3-card hands from a 52-card deck:
C(52,3) = (52 × 51 × 50) / (3 × 2 × 1) = 132,600 / 6 = 22,100. ✓ matches Source B.

Straight (including straight flush): 12 rank-sequences (A-2-3 up to Q-K-A) × 4³ suit choices = 12 × 64 = 768.
Straight flush: 12 sequences × 4 suits = 48.
Straight (non-flush) = 768 − 48 = 720. ✓ matches Source B.

Flush (including straight flush): C(13,3) ranks × 4 suits = 286 × 4 = 1,144.
Flush (non-straight) = 1,144 − 48 = 1,096. ✓ matches Source B.

720 (кента) < 1,096 (флъш): the straight is the rarer hand, so it ranks ABOVE the flush. This is the reverse of 5-card poker, where a flush is rarer than a straight. Conclusion in the body ("по-рядката ръка получава по-високо място") is therefore correct.

Sanity sum of all categories (Source B): 48 + 52 + 720 + 1,096 + 3,744 + 16,440 = 22,100 = C(52,3). ✓

## RECALCULATION 2 — RTP from house edge

RTP (Ante & Play) = 100% − house edge = 100% − 3.37% = 96.63%. ✓ Body states ≈96.63% over the long run (thousands of hands), not a session promise. Internally consistent.
Element of risk 2.01% < 3.37%: consistent, because the Play raise (made on qualifying hands) increases the total amount wagered, so the edge as a share of total turnover (element of risk) is lower than the edge stated as a share of the Ante alone.

## INTERNAL LINKS USED (4)
1. /blog/kak-se-igrae-poker-kazino/ — anchor „по-общия поглед върху казино покера" (sibling overview; this article is the deep dive)
2. /kazino-igri/ — anchor „игрите на маса в казиното"
3. /otgovorna-igra/ — anchor „инструментите за отговорна игра" (RG touch)
4. /kak-ocenyavame/ — anchor „публична методика, а не през усещане"

## HUMAN CHECK BEFORE PUBLISH
- Confirm the two Pair Plus paytables + edges still match the live Wizard of Odds page (2.32% for flush 4:1; 7.28% for flush 3:1).
- Confirm Ante & Play 3.37% / element of risk 2.01% against Wizard of Odds Ante Bonus Pay Table 1.
- No operator named, no НАП licence claim, no tax claim, no affiliate link — correct for an educational guide.
- Fill [About Всички Казина boilerplate] and [author-bio] slots at publish (Step 8).
