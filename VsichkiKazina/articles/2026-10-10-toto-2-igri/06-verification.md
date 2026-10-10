# 06 — VERIFICATION (Step 6, human-owned) · vk-0267

**Article:** Тото 6 от 49, 6 от 42 и 5 от 35: правила, шансове и разлики
**05b status:** pre-verification text. NOT publishable until every [VERIFY] below is resolved by the human and the brackets removed.
**Brand Gate:** PASS WITH FIXES 88/100 · **Humanisation (Stage 3):** MIXED 45/60 → light rewrite
**External check (Step 7):** skipped (Gemini unavailable — cloud backfill pending)
**Images:** 1 (SVG infographic, odds comparison) · image review: skipped (Gemini unavailable — cloud backfill pending); self-check: rendered in headless Chrome at 760×480, no overlap/clipping, every figure traced to 05b.

> Note: toto.bg / info.toto.bg are behind a Radware bot-CAPTCHA (confirmed 2026-10-10: info.toto.bg → validate.perfdrive.com). All BST checks below must be done by the human in a normal browser.

## Surviving [VERIFY] flags (10 inline, 8 distinct)

| # | Claim in text | Where | Primary source to check | What we found |
|---|---|---|---|---|
| 1 | Тираж 04.10.2026, 6/49: 3 познати 3,30 €, 4 → 21,10 €, 5 → 1 051,60 €; шестиците в 6/49 и 6/42 не са спечелени | „Трите игри…" | toto.bg → резултати (архив тиражи) | lotteryextreme.com/toto2/results(04.10.2026) shows exactly these amounts (unofficial aggregator). Gate also asks to confirm the „шестиците неспечелени" sentence (same source, not separately flagged). |
| 2 | Една комбинация в 5 от 35 участва и в двете тегления | „5 от 35" | toto.bg/toto1-i-toto2/toto-2-5-ot-35 (rules) | toto49.com („може да спечелите в едно от двете тегления") + totogener.com („всеки фиш участва автоматично в две отделни тегления"). Secondary only. |
| 3 | 5 от 35 няма натрупващ се джакпот; непоетите суми се разпределят към другите групи | таблица + „Коя игра…" | правила 5 от 35 на toto.bg | toto49.com („Няма джакпот"), totogener.com (redistribution). Secondary only. |
| 4 | Актуална цена на една комбинация в € (6/49, 6/42, 5/35) | „Колко струва…" | toto.bg (цени / правила на игрите) | Not found. Only trud.bg 11.06.2019: 5/35 = 0,70 лв. (outdated, leva) — NOT used in text. |
| 5 | Дял от постъпленията за награден фонд | „Колко струва…" | Правила за игрите на БСТ (PDF на toto.bg) | Only totogener.com (commercial) says 50% — NOT used in text. |
| 6 | Как работи „Втори Тото Шанс – 6 от 42" | таблица + „Втори ТОТО Шанс" | toto.bg/toto1-i-toto2/vtc-6-ot-42 | Source pack: the name appears in the prize list; page did not render. |
| 7 | ≈0,098 € (≈0,10 €) очаквана стойност от категории 3–5 в 6/49; ≈0,36 € от джакпота | „Колко струва…" | depends on #1 | Recomputed below — arithmetic correct given #1. |
| 8 | ЗХ: минимална възраст 18 (формулировка) | „Закон, възраст…" | lex.bg — Закон за хазарта | НАП pack: „ЗХ забранява участието на малолетни и непълнолетни" (no exact article quoted). |

## Time-sensitive claims (re-check at publish)
- Джакпот 6/49 към тираж 79 от 08.10.2026: 5 060 115,42 € — source pack (toto.bg, read 2026-10-10). Will be stale after the next draw; label already dated.
- Джакпот 6/42 към тираж 79 от 08.10.2026: 1 363 850,28 € — same.
- График на залозите (в сила от 08.12.2022), БНТ 18:45, сайт недостъпен 18:40–19:10 — source pack (toto.bg „Информация").
- ПМС № 50 от 15.02.2021 (в сила от 21.02.2021) — source pack.
- НАП: 5% от нетния доход; регистър чл. 10г, мин. 12 месеца; 0700 18 700 — source pack nap-gambling-law-and-rg-2026-10-10 (nra.bg/wps/portal/nra/gambling/responsible.gambling).
- Солидарност 0888 99 18 66, делнични дни 10:00–17:00 — brand canon (brand-gate-vsichkikazina.md); confirm still current.
- History: БСТ 12.05.1957; 6/49 29.12.1957; 5/35 15.07.1989; 6/42 1993; Втори ТОТО шанс 2002 — https://bg.wikipedia.org/wiki/Български_спортен_тотализатор (fetched 2026-10-10).

## Figure recalculation (working shown)
6 от 49, jackpot: C(49,6) = 49·48·47·46·45·44 / 720 = 10 068 347 520 / 720 = **13 983 816** ✓.
Five correct: C(6,5)·C(43,1) = 6·43 = 258 → 13 983 816 / 258 ≈ 54 200,8 → „1 към ≈54 201" ✓.
5 от 35, two draws (if #2 holds): p = 1/324 632; P(≥1 jackpot) = 1 − (1 − p)² → 1 / 162 316,25 → „около 1 към 162 316" ✓.
Expected value #7: (1 051,60·258 + 21,10·13 545 + 3,30·246 820) / 13 983 816 = (271 312,8 + 285 799,5 + 814 506) / 13 983 816 = 1 371 618,3 / 13 983 816 ≈ **0,0981 €** ✓; 5 060 115,42 / 13 983 816 ≈ **0,3619 €** ✓.
All tier counts/odds verified in python3 (math.comb) at Stage 0 and again by the Brand Gate.

## Links
Internal (all in live sitemap 2026-10-10): /blog/progresivni-dzhakpoti/, /blog/danaci-pechalbi-onlajn-kazino/, /blog/keno-pravila/, /otgovorna-igra/. External: https://www.toto.bg/ (results pointer). No affiliate links.

## Notes for the human
- H1 was changed at Stage 4 (SEO) from the queued title „Тото 2: 6 от 49, 6 от 42 и 5 от 35 — правила, шансове и разлики" to „Тото 6 от 49, 6 от 42 и 5 от 35: правила, шансове и разлики" (exact head query first, no dash). Revert if you prefer the queued title.
- If #2 turns out false (one combination ≠ both draws), the two-draw odds sentence and the infographic's „при две тегления" line must be removed.
- If #4/#5 are found, the EV section can state a concrete return % — re-run the gate after that edit.
- Do NOT publish with live [VERIFY] tags.
