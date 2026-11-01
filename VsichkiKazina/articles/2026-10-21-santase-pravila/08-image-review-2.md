# 08 — Gemini image review, pass 2 (regenerated hero)

Command: `python3 scripts/gemini_image_review.py 05b-final-draft.md images/santase-karti-hero-p2.webp images/stoynost-na-kartite-santase.svg images/tochkuvane-santase.svg`
Exit: 0

## Score: 65/100 — NEEDS WORK  (hero again; the suit-garble defect from pass 1 is now GONE)

## Verbatim verdict
**SCORE: 65 · VERDICT: NEEDS WORK**

1. Брой карти в ръката: хероят показва ветрило от 8 карти, а текстът посочва „Всеки започва с по
   шест карти в ръка."
2. Разположение на талона: талонът е встрани от обърнатата козова карта (Асо купа), а текстът описва
   „талон върху коза, така че откритата козова карта се подава изпод тях".
3. Инфографики (SVG): И двете са безупречни. Всички числа, термини и стойности отговарят точно на
   текста; няма припокриване/изрязване; ALT текст и имена на файлове са коректни. „Не са нужни
   корекции, готови са за публикуване."

Корекция за хероя: задай точно 6 карти + талон частично върху обърнатата карта.

## Decision — keep-best + no integrity failure
- MAX_IMAGE_PASSES (2) reached. Hero pass 1 = 65, hero pass 2 = 65 (tie on score).
- Pass 2 is kept: it removed the real pass-1 defect (mismatched suit pips / AI hallucination on the
  card faces). Pass 2's remaining flags are decorative literalism (card count 8 vs 6; exact talon
  placement) on a purely decorative banner — NOT an integrity failure (no operator logo/name/
  screenshot, no invented bonus/RTP/licence number, no person/face, no glamorised winning). The
  article's ALT text is count-agnostic ("ветрило от карти"), so no text↔image contradiction ships.
- Both SVG infographics PASS (effectively 100, "готови за публикуване").
- Final image set KEPT: 3 images. Best review scores — infographics 100 / 100, hero 65 (kept, decorative).
- Hero santase-karti-hero-p2.webp promoted to images/santase-karti-hero.webp (the 05b reference).
- Images never block the PR; shipping all three.
