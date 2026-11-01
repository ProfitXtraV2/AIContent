# 08 — Gemini image review — pass 1 — vk-0302

Model: gemini-3-pro-image review · run 2026-10-27 · inputs: sudoku-skrit-edinak.svg + sudoku-reshetka-hero.webp

## Result
- **Combined score: 45/100 — NEEDS WORK** (dragged down by the hero; infographic passed).
- Infographic `sudoku-skrit-edinak.svg`: **PASS** — accurate „скрит единак" logic, flawless layout,
  no overlaps/clipping, descriptive ALT. No changes required.
- Hero `sudoku-reshetka-hero.webp`: fails on (1) grid reads as 5×5, not the article's 9×9/3×3;
  (2) ALT text mismatch — says „с няколко вписани цифри" but the image has no digits (intentionally).

## Verbatim verdict
**Score: 45/100 — Verdict: NEEDS WORK**

1. Image 1 (sudoku-reshetka-hero.webp) — Accuracy & Relevance (Critical Failure)
   - Wrong Grid Dimensions: the image displays a 5x5 grid (25 cells). The article states Sudoku is
     „решетка от 9 на 9 клетки, общо 81" divided into 3x3 squares. A 5x5 grid cannot function as a board.
   - Missing Digits / Metadata Mismatch: ALT/prompt specify „с няколко вписани цифри" but the image
     contains zero digits — only blank colored rounded squares and a glowing white circle.
2. Image 2 (sudoku-skrit-edinak.svg) — PASS. Excellent infographic; accurately reflects „Скрит единак";
   layout integrity flawless (legend „2 7 9" spacing perfect, nothing clipped by 720x430); ALT accurate.

Fixes: regenerate the hero (Gemini suggested adding typographic digits 1–9 + a 9x9 grid); SVG no changes.

## Disposition (pass 1 → pass 2 planned)
- Infographic kept as-is (PASS).
- Hero: Gemini's „add digits 1–9" is REJECTED — the Step-8 hard hygiene rule bans text/numbers/letters
  in AI heroes (models garble them; numbers ride the SVG). Legitimate parts taken: (a) fix the hero ALT
  to describe the colored-tile grid honestly (no „цифри" claim); (b) regenerate as a proper 9×9 grid
  clearly divided into 3×3 sub-grids, still textless (colored tiles = the article's own „замени 1–9 с
  девет цвята" metaphor). Re-review in pass 2. If the hero still can't clear 80, drop it and ship the
  infographic alone (which already PASSES) — never add fabricated digits to force a score.
