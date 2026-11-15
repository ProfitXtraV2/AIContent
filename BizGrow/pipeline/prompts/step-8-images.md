# Step 8 — Images — BizGrow

**Default: no new images.** The BizGrow site's visuals (hero banners per locale, icons) are
designed assets managed in the `biz-grow` repo (`site/public/`, `media/`). A `page-rewrite` never
adds, removes or replaces an image and never generates an AI image. If the page's copy changes
text that is baked into an image (the BG/EN hero banner labels), list it in `06-verification.md`
under REMAINING FOR HUMAN; do not edit the image. Log `images: none`.

A `new-page` may add at most ONE explanatory SVG diagram (for example the four process steps),
and only when the owner's session asks for it:
- every label in the page's language, every fact traceable to the page text and the canon, no
  numbers beyond canon, no prices, no client names or logos, no third-party brand logos;
- no photos, no photorealism, no people or faces, no fake screenshots of dashboards or chats with
  invented data;
- site palette (`docs/ai-consultancy-spec.md` §7 tokens), descriptive lowercase hyphenated
  filename (e.g. `bizgrow-process-4-steps.svg`), specific ALT text in the page's language,
  ≥ 16 px padding, no overlapping or clipped text (render to PNG and check every edge).
Review it with `python3 scripts/gemini_image_review.py <article>/05b-final-draft.md <svg> --brand bizgrow`
(`step-8-image-review.md`); ship only at score ≥ 80 with no integrity failure, else drop it.
