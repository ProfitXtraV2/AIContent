# 06 — Verification checklist — vk-0275 „Джакпотът в Тото"

Pre-verification text: `05b-final-draft.md`. **NOT publishable until the human resolves every flag below (Step 6).** Flags stay in the text.

## Surviving flags (14 occurrences: 11 [VERIFY] (10 distinct), 2 [CONFLICT], 1 [DATA NEEDED])

| # | Flag | Where | Primary source to check | What reachable sources show |
|---|---|---|---|---|
| 1 | [VERIFY] % награден фонд и дял на I категория (6/49, 6/42) | „Как се натрупва" | БСТ правила на игрите — https://info.toto.bg (CAPTCHA, BG browser) | Old undated mirror toto2-info.w-bg.net: награден фонд ≥ 50% от залозите (garbled) |
| 2 | [DATA NEEDED] таван / принудително разпределение на джакпота | „Как се натрупва" | БСТ правила 6/49 и 6/42 | Nothing found in any reachable source |
| 3 | [CONFLICT] класиране на тираж 21/2026 (5 778 403 €) | records table | БСТ press release / toto.bg архив | dir.bg 19.03.2026 „вторият най-голям"; 5 778 403 × 1,95583 ≈ 11 301 574 лв. < 11 304 948,90 лв. (тираж 23/2025, action.toto.bg) → would be 3rd |
| 4 | [VERIFY] класиране на текущия джакпот (5 060 115,42 € ≈ 9 896 726 лв.) | after records table | toto.bg | action.toto.bg list predates 2026 draws |
| 5 | [VERIFY] прагове за изплащане в евро след 01.01.2026 | „Пътят на парите" | https://info.toto.bg/news/press/kakvo-tryabva-da-znayat-uchastnitsite-za-izplashtaneto-na-pechalbi-ot-igrite-na-balgarski-sporten-totalizator | paragraf.bg 30.03.2026 and totogener (09.10.2025) give лв. thresholds: ≤1 000 лв. в брой; 1 000,01–9 999,99 лв. банков превод (искова форма); ≥10 000 лв. ЦУ София |
| 6 | [VERIFY] онлайн джакпот: автоматично или по общия ред | „Пътят на парите" | toto.bg ЧЗВ — https://info.toto.bg/chesto-zadavani-vaprosi | Source pack: online wins credited automatically (no jackpot-specific rule) |
| 7 | [VERIFY] срок за предявяване 6 месеца | „Колко време имате" | БСТ правила | totogener only („до 6 месеца от датата на тиража"); 45-day payout term confirmed by paragraf.bg 2026 + novinite 2011 |
| 8 | [VERIFY] непотърсен джакпот юни 2010, Ловеч (≈6,6 млн. лв.) | „Колко време имате" | BG news archive 2010 | novinite.com 27.01.2011: record 6.6 M лв., June 2010, Ловеч, 45-day claim period; „never claimed" reported only indirectly |
| 9–10 | [VERIFY] първоначална сума (до 200 000 лв.) и разсрочване (до 14 г.) в евро | „Наведнъж или на вноски" + FAQ | БСТ правила 6/49 | totogener (unsourced), fakti.bg reader comment 2021, old rules mirror example; paragraf.bg 2026 confirms „разсрочени джакпоти" exist |
| 11–12 | [VERIFY] актуална редакция на чл. 13, ал. 1, т. 20 ЗДДФЛ | „Облага ли се" + FAQ | ЗДДФЛ — https://lex.bg/laws/ldoc/2135538631 (403 from cloud) or ДВ | NAP opinions (kik-info.com titles, trudipravo.bg summary): печалби от хазартни игри по ЗХ = необлагаеми, без деклариране |
| 13 | [CONFLICT] totogener „10% окончателен данък" над 10 000 лв. | „Облага ли се" | same as 11 | totogener self-contradicts; no legal basis cited |

## Time-sensitive claims (re-check at publish)
- Jackpots към тираж 79 (08.10.2026): 6/49 5 060 115,42 €; 6/42 1 363 850,28 €; Зодиак 1 500 000,00 €; Рожден ден 7 353,06 €; Джокер „спечелен" — source pack `source-packs/bst-toto-2026-10-10.md` (toto.bg, BG browser 10.10.2026). Will be stale after the next draw → update or keep the date stamp.
- Dateline „Публикувано/Последна актуализация: 10.10.2026" — update if publishing later.
- March 2026 temporary payout suspension (>5 000 €) — paragraf.bg 30.03.2026.
- Draw times (БНТ, Thu/Sun 18:45) — source pack.

## Record figures — sources
- 11 715 401,70 лв. (2022, тираж 31, Сливен, фиш 1,20 лв.): action.toto.bg (БСТ campaign site, 02.2026) — https://www.action.toto.bg/nad-5-miliona-evro-dzhakpotat-v-6-ot-49-chuka-na-vratata-na-istoriyata/ ; profit.bg https://profit.bg/article/2024012513311728911
- 11 304 948,90 / 10 095 908,40 / 9 667 090,20 / 9 501 430,40 лв.; 1 000 000 лв. on 07.04.1991: action.toto.bg (same URL)
- 5 778 403 € (2026, тираж 21, София): https://dnes.dir.bg/obshtestvo/parvi-toto-evromilioner-pusnat-v-sofiya-fish-donese-na-sobstvenika-si-eur5-778-403-evro-video

## Recalculation (worked)
C(49,6) = 49×48×47×46×45×44 / 720 = 10 068 347 520 / 720 = **13 983 816** ✓ (python3 math.comb).
Average wait at 104 draws/year: 13 983 816 / 104 = 134 459,77 → „около 134 460 години" ✓. 6/42: 5 245 786 / 104 = 50 440,25 → „около 50 440" ✓.
10 combinations: 13 983 816 / 10 = 1 398 381,6 → „около 1 към 1 398 382" ✓.
Conversion: 11 715 401,70 / 1,95583 = 5 989 989,77 → „≈ 5 989 990 €" ✓; 5 060 115,42 × 1,95583 = 9 896 725,54 → „около 9 896 726 лв." ✓.

## Pipeline results
- Brand Gate: FAIL 83 → 92 after fixes — blocked ONLY by human-resolvable flags (no factory defect; all mechanical fixes applied). Same convention as sibling lottery articles (flags left for Step 6).
- External check (Gemini Step 7): initial 75 (Likely human-written 75%) → humaniser pass 1 → **85 (Likely human-written 85%) PASS**; passes applied: 1; kept best = pass 1 (85). gemini = `human 85`.
- images: 3 (hero 100, infographic records 100, infographic odds 100 — one combined Gemini review, score 100 PASS, no integrity failure). Files: `images/toto-dzhakpot-natrupvane-hero.webp` (16.7 KB), `images/rekordni-dzhakpoti-toto-6-ot-49-infografika.svg`, `images/shans-dzhakpot-6-ot-49-6-ot-42-godini-infografika.svg`. All infographic figures verbatim from 05b; rendered with headless Chromium and eyeballed.
- Internal links (all live in sitemap.xml 10.10.2026): /blog/progresivni-dzhakpoti/, /blog/danaci-pechalbi-onlajn-kazino/, /otgovorna-igra/, /zakonno-li-e/. No affiliate links (neutral lottery guide).
