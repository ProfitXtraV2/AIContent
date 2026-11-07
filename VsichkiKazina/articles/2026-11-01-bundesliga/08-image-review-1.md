# 08 — Gemini image review, pass 1 (Бундеслига)

Reviewed: `images/bundesliga-format.svg` (SVG source) + `images/bundesliga-stadion-hero.webp` (pixels).
Ran 2026-11-01.

## Result
**Score: 75/100 · Verdict: NEEDS WORK.** No integrity failure (no fake logos, faces, or
gambling-promotion; SEO filenames + ALT correct; neutral tone).

- **Infographic (SVG): excellent, 100% accurate to the article, no cut elements, clean code.**
  Only a non-defect recommendation: right-column 3-digit numbers (602, 365 at x=440) sit ~15px from
  their labels (x=500); widen the gap for breathing room.
- **Hero (raster): two AI artifacts drag the score down.** (1) Impossible pitch lines: a vertical
  centre line + circle (implies goals left/right) but penalty-box corners drawn on the bottom
  touchline — confusing/unrealistic geometry. (2) Crowd/seating rendered as a QR-code / maze-like
  block pattern, a typical AI artifact.

## Verbatim verdict
Оценка: 75/100 · Присъда: NEEDS WORK.
Инфографиката (SVG) е отлична, напълно точна спрямо текста и с безупречен код. Проблемът е в
растерното изображение: (1) невъзможни очертания на терена (вертикална централна линия с кръг, но
ъгли на наказателно поле на долната линия); (2) трибуните са блоков патерн, приличащ на QR код/
лабиринт — типичен AI артефакт. Инфографика: само лека препоръка да се отместят етикетите в дясната
колона от x=500 на x=510/520. SEO + Отговорна игра: и двете покриват изискванията; няма фалшиви
лога, лица или насърчаване на хазарт; неутрален тон.

## Decision → pass 2
Score < 80 (IMAGE_TARGET_SCORE), no integrity fail → iterate (MAX_IMAGE_PASSES 2). Plan:
(a) nudge SVG right-column labels for polish; (b) regenerate the hero with an improved prompt
(accurate pitch lines, goals at the ends, halfway line in the middle, simple dotted crowd, avoid
maze/QR artifacts). Re-review. If the set still < 80, keep-best: ship the flawless infographic alone
(drop the decorative hero) per Step-8 keep-best — never block the PR on a decorative image.
