# 06 — Verification · vk (теглене на тото днес)

Article: **Теглене на Тото: кога са тиражите на 6 от 49, 6 от 42 и 5 от 35 и къде да ги гледате**
(guide, slug `2026-10-27-teglene-na-toto-dnes`)
Byline: Георги Тодоров (editorial „ние" voice) · Published/updated: 27.10.2026

## Surviving flags (STAY IN THE TEXT for human Step 6 — not resolved by autopilot)
- **1 [VERIFY]**, pointed at a primary source, not fabricated:
  1. [VERIFY] the specific БНТ channel the draw airs on now. The source page says БНТ 1; a web
     claim (read on the 2026-10-27 6th fire) said БНТ 2. Not asserted — text writes „БНТ".
- **0** [DATA NEEDED]/[CONFLICT]. No draw numbers or prize amounts printed (brand doctrine).
- No tax claim raised (so no tax [VERIFY] needed). No operator recommended → no affiliate link, no НАП licence №.

## Time-sensitive / sourceable claims (traced to the human source packs; cloud env geo-blocked, no live fetch)
| Claim in text | Source | Note |
|---|---|---|
| Теглене в четвъртък и неделя от 18:45 ч. | toto-draw-schedule.md + bst-toto-2026-10-10.md | both packs agree (info.toto.bg) |
| В слота: 6 от 49, 6 от 42, 5 от 35, Тото Джокер, Зодиак, Рожден ден, Втори тото шанс | toto-draw-schedule.md | human pack, newest/authoritative |
| На живо по БНТ; само по БНТ от 3 май 2020 г.; тричленна комисия | toto-draw-schedule.md | specific channel → [VERIFY] |
| ТВ теглене от септември 1975 г.; студио на БНТ до юни 2013 г.; оттогава собствено HD студио | toto-draw-schedule.md | official site history |
| Онлайн сайтът недостъпен за играчи ~18:40–19:10 ч. в дните на теглене | bst-toto-2026-10-10.md l.23 | verbatim pack fact |
| Тиражът се пуска за изплащане до ~1 ч. след края на ТВ предаването | bst-toto-2026-10-10.md l.27 | verbatim pack fact |
| Официални резултати на info.toto.bg; последен тираж по подразбиране + „ИЗБЕРИ ТИРАЖ"; показва №+дата, числа, джакпот, таблица с печалби; суми в евро | toto-draw-schedule.md | official site |
| Джокер върви с номера на фиша; Втори тото шанс = жребий между касовите бележки | toto-draw-schedule.md + carried vk-0268/vk-0287 | not a number check |

## "Recalculate one figure" (working shown)
No computational figures in this piece — no odds, RTP, превъртане or € math. The only literal
numbers are times/dates (18:45; 18:40–19:10; 1975; 2013; 2020; 27.10.2026) and game names
(6 от 49, 6 от 42, 5 от 35), reproduced verbatim from the source packs. Infographic ↔ 05b
cross-check: every infographic label traces to a 05b sentence (четвъртък и неделя; 18:45 ч.;
на живо по БНТ; комисия; 6 от 49 / 6 от 42 / 5 от 35 / Тото Джокер / Зодиак / Рожден ден /
Втори тото шанс; online недостъпен 18:40–19:10; резултат ~1 ч. след ефира; info.toto.bg;
последният тираж по подразбиране; „ИЗБЕРИ ТИРАЖ"). No number introduced that the text does
not state. Number set byte-identical 02→03→04→05b (diff-checked); the humaniser pass touched
style only and was then reverted by keep-best.

## Gemini Step-7 (text, cross-model)
- Baseline draft (check 1): **HL 90** („Likely human-written, 90%") — PASS.
- Humaniser pass 1 (deleted a didactic signpost, varied one „Ако", simplified a heading):
  check 2 **HL 85** („Likely human-written 85%") — PASS but LOWER.
- MAX_GEMINI_PASSES=2. **Kept pass 1 / baseline** (highest HL = 90). gemini column: **human 90**.
- Files: 07-gemini-check-1.md (90 PASS), 07-gemini-check-2.md (85 + keep-best ledger).

## Step-8 images
- **images: 2** — infographic `teglene-na-toto-grafik.svg` (schedule/games/online-window/results;
  every label traces to 05b) + decorative hero `teglene-na-toto-grafik-hero.webp` (7.4 KB,
  1200×509: TV draw drum + calendar + clock; no faces/logos/numbers/money/euphoria).
- Gemini image review: **100/100 PASS** pass 1, **0 integrity failures**. Infographic 100% data
  match; layout clean (0 overlaps, no clipping). **Best score 100.**
- Files: 08-image-review-1.md.

## Human-owned (Step 6)
Resolve the 1 [VERIFY] (specific БНТ channel) against a БСТ/БНТ primary source before publish.
No posting, no merge, no flag-resolution by autopilot. PR for human review.
