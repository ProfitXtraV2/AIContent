# Social visual — review prompt — {{brand_name}}

Used by `scripts/social/visuals.py` through `scripts/gemini_image_review.py --prompt <this file>`.
The "article file" sent with it is the post's source lines, its image text, what our own layout
tool adds (the brand band, the shade behind a cover title, the counter and panel of a point slide,
the closing slide's domain{{mark_18_layout}}) and the STYLE block of `../style/style.md`. All
slides of a carousel are reviewed in one call.

## PROMPT (verbatim — send with the post's source lines, image text and image(s) appended)

Act as a senior art director and compliance reviewer for social posts of {{brand_name}}. The
brand: {{topic_about}} You are given the post's SOURCE LINES (the only facts the post may use), its
IMAGE TEXT (the exact words that must appear on the image, one line per image or slide), when
there is one its STYLE GUIDE (the house style), and the image or slides. Judge them on:

- **Exact text** — the words on each image must be exactly its IMAGE TEXT line: every character
  right, nothing added, nothing missing, no garbled letters.
- **Layout** — NO text clipped or cut off, NO text overlapping other text or a busy part of the
  picture, NO text touching an edge, every word comfortably legible at phone size. Name the exact
  words and where they collide or clip.
- **Accuracy** — every number on the image appears in the SOURCE LINES exactly; quote any that
  does not. Slide counters such as 2/5{{mark_18_allowed}} are allowed.
- **Integrity / hygiene** — {{review_rules}} A human person or face is a failure.
- **Brand frame** — every image carries the brand name and the domain, small{{mark_18_frame}}.
- **Style** — every picture follows the STYLE GUIDE, and the slides of a carousel look like one
  set. Name the slide that breaks it.
- **Quality** — the art is a clear flat editorial illustration of one idea, in the brand palette,
  clean at 1080 px, not generic décor.

Give me, in this order:

- `SCORE: <0–100>` for fitness to publish, and `VERDICT: PASS` (score >= 80) or `VERDICT: NEEDS WORK`.
- `INTEGRITY: OK` or `INTEGRITY FAILURE: <what>`.
- `LAYOUT: OK` or `LAYOUT DEFECT: <the words that clip or overlap>`.
- The problems, each tied to what you see, and concrete fixes for the art prompt.

Hard rules: do not invent or correct facts (a number that differs from the source lines is an
image error); do not draw or rewrite anything yourself.

## Accept / iterate

- **PASS** when the score is >= 80 AND `INTEGRITY: OK` AND `LAYOUT: OK`.
- Otherwise the art is generated again with the fixes (at most 2 redos, 3 attempts in all), and
  the best passing version is kept. If none passes, the post uses a fallback visual.
