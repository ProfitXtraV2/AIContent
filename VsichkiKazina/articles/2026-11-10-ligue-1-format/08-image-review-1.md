# 08 — Step-8 image review · pass 1

## Images shipped
1. `images/liga-1-format.svg` — hand-authored data infographic (format + records of Ligue 1).
   Every displayed number copied VERBATIM from 05b (1932/33, 18, 34, 306, 3, 2016/17,
   16-и/3-ти, ПСЖ 14, Сент Етиен 10, Марсилия 9, Лион 7 / 2002–2008, Ландро 618, Онис 299,
   „към есента на 2026 г.", име „Лига 1" 2002). No fabricated numbers. No operator logos/names,
   no screenshots, no people/faces, no glamorised winning. Specific Bulgarian ALT + caption.

## AI hero: SKIPPED
`python3 scripts/gemini_image_gen.py ... liga-1-stadion-hero.webp 100` → **HTTP 402
(GEMINI_UNAVAILABLE, prepayment credits depleted)**. Per Step 8: do NOT halt — logged
`image gen: skipped (Gemini unavailable)`; ship the infographic alone. No hero reference
left in 05b.

## Gemini visual review: SKIPPED
`python3 scripts/gemini_image_review.py 05b-final-draft.md images/liga-1-format.svg` →
**HTTP 402 (GEMINI_UNAVAILABLE)**. Per Step 8: unavailable → log
`image review: skipped (Gemini unavailable)` and keep the image. SVG integrity verified by
hand: all displayed figures trace 1:1 to 05b (0 fabrication); no integrity failure.

## Result
images: 1 (infographic — hand-verified, numbers 1:1 vs 05b; Gemini review skipped/unavailable).
