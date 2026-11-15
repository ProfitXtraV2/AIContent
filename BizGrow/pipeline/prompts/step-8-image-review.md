# Step 8 — External image review (Gemini) — BizGrow

Used only for the rare `new-page` diagram (see `step-8-images.md`). Sent by
`python3 scripts/gemini_image_review.py <article> <image> --brand bizgrow`. Like Step 7 it needs
`GEMINI_API_KEY`, which exists only in the cloud routine environment.

## PROMPT (verbatim — send with the page text + image appended)

Act as a senior copy editor and art director reviewing an explanatory diagram for a page of BizGrow, a practical AI and automation consultancy for small businesses in Bulgaria. The page is in Bulgarian or English. You are given the page text and the diagram (SVG source and, where available, a rendered PNG). Judge:

- **Relevance** — does it help a small-business owner understand this page, or is it decoration?
- **Accuracy** — does every label, step and number match the page text exactly? Quote anything the page does not support.
- **Integrity (automatic FAIL)** — any photo or photorealistic style, people or faces, fake screenshots with invented data, client names or logos, third-party brand logos, prices, guarantee or hype wording, or labels not in the page's language.
- **Tone** — clear and professional; nothing that overstates a result.
- **Layout** — no overlapping or clipped text, nothing touching an edge, legible at display width.
- **SEO metadata** — descriptive lowercase hyphenated filename and specific ALT text in the page's language.

Give me a single score from 0 to 100 and a verdict `PASS` (>= 80) or `NEEDS WORK` (< 80), the specific problems, and concrete fixes. Do not invent or correct facts; do not redraw the image yourself.

## Accept / iterate policy
- PASS at score ≥ 80 with no integrity failure and no layout defect.
- Otherwise hand-fix the SVG and re-review, up to `MAX_IMAGE_PASSES` (2); if still failing, drop
  the image. Never ship an integrity failure.
