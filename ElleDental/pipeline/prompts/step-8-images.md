# Step 8 — Images — ELLE Dental

**Default: no new images.** The ELLE Dental site uses the clinic's real photos, managed in
WebPortals (`_publisher/images.json`, `image-alt.json`). A `page-rewrite` never adds, removes
or replaces an image and never generates an AI image. Log `images: none (page-rewrite)`.

A `new-page` (owner-approved only) may add at most ONE explanatory SVG diagram (for example the
steps of a procedure), and only when it genuinely helps:
- every label in Bulgarian, every fact traceable to the page text, no numbers the page does not
  state, no prices, no brand names, no logos;
- no photos, no photorealism, no teeth/gum/mouth close-ups, no before/after, no people or faces,
  no instruments in use;
- descriptive Latin-transliterated lowercase filename (e.g. `etapi-na-korenovo-lechenie.svg`),
  specific Bulgarian ALT text, ≥ 16 px padding, no overlapping or clipped text (render to PNG and
  check every edge before referencing it).
Review it with `python3 scripts/gemini_image_review.py <article>/05b-final-draft.md <svg> --brand elledental`
(`step-8-image-review.md`); ship only at score ≥ 80 with no integrity failure, else drop it.
