# 06 — Verification — 2026-10-27-sudoku-kak-se-igrae (vk-0302)

## Surviving flags
- **None.** 0 [VERIFY], 0 [DATA NEEDED], 0 [CONFLICT]. All content is universal, well-established
  sudoku rules; no operator-, НАП-, licence-, or tax claim appears, so nothing is flagged.

## Time-sensitive claims
- None. The rules of sudoku are evergreen. The sourced specifics are historical facts (publication
  years) and a proven mathematical result, none of which change:
  - „Number Place", Dell, май 1979 — authorship приписва се на Howard Garns (hedged, per sources
    that call it „most likely").
  - Nikoli, Япония, 1984 — name shortened to „судоку".
  - Световен бум ~2004–2005 via The Times (London).
- „Судоку онлайн безплатно" platforms are named generically (no brand, no figures) — no timestamp needed.

## Primary sources
- https://bg.wikipedia.org/wiki/Судоку — rules, terminology, history (BG), fetched 27.10.2026.
- WebSearch corroboration 27.10.2026 (multiple independent sources): 9×9 structure with nine 3×3 boxes;
  each of 1–9 exactly once per row/column/box; a proper puzzle has one unique solution; minimum 17 givens
  (G. McGuire, B. Tugemann, G. Civario, „There Is No 16-Clue Sudoku", arXiv 2012, published 2014);
  origin Garns 1979 (Number Place / Dell) → Nikoli 1984.

## Recalculated figures (working shown)
- Board size: 9 rows × 9 columns = 81 cells. Text states „решетка от 9 на 9 клетки, общо 81" → 9×9 = 81. ✓
- Nine 3×3 boxes: a 9×9 board partitions into (9/3) × (9/3) = 3 × 3 = 9 boxes of 3×3 = 9 cells each;
  9 boxes × 9 cells = 81, consistent with the cell count. ✓
- Minimum-givens claim: text says „не съществува коректно судоку с по-малко от 17 дадени цифри" — matches
  the cited 2012 computational proof (no 16-clue sudoku); 17 is the established floor. Stated with
  attribution („екип математици, 2012 г."), not as the autopilot's own assertion. ✓
- Infographic numbers (2, 7, 9 givens; candidate/eliminated/survivor „4") are explicitly labelled
  примерни (illustrative) on the graphic and in the caption — they illustrate the technique, not a
  specific puzzle, so no fabrication. ✓

## Gemini Step-7 (text)
- Baseline 05b: „Likely human-written, 90% confidence" → human-likeness 90 → **PASS** (≥80).
- Passes applied: 0 (baseline clears the gate; keep-best = baseline). `gemini` = **human 90**.
- Three style/structure recommendations (signposting „две неща започват да изпъкват", the history
  section placement, the online-section pivot) left as optional taste notes for the human Step-6 editor;
  facts/links/RG/disclosures clean. (07-gemini-check-1.md)

## Step-8 images
- **images: 2 (infographic 100, hero 100)** — best review score 100, 0 integrity failures.
- Infographic `sudoku-skrit-edinak.svg` (hidden-single technique, illustrative numbers labelled примерни).
- Hero `sudoku-reshetka-hero.svg` (hand-authored exact 9×9 grid in 3×3 blocks, colored tiles, no digits/
  text/people). The AI hero (gemini-3-pro-image) failed twice on grid accuracy (5×5 / 8-col); replaced
  with the hand-authored SVG per Gemini's own recommendation — never added fabricated digits.
  (08-image-review-1.md = score 45; 08-image-review-2.md = score 100 PASS.)

## Brand Gate
- PASS 95/100, 0 criticals (see 05-gate-report.md). Byline Георги Тодоров, brand „Всички Казина",
  dates 27.10.2026, About + bio + verbatim 18+ RG line + RG signposting (/otgovorna-igra/ + регистър на
  уязвимите лица) + affiliate footer; no operator referenced → „Тази статия не съдържа партньорски връзки."
  (correct). 0 em-dashes in body. 2 live internal links (/otgovorna-igra/, /blog/tabla-pravila/).

## Status
Publish-ready for human Step-6 review. FLAGS STAY IN THE TEXT (there are none). Do NOT resolve flags,
post, or merge — human owns Step 6 and publishing.
