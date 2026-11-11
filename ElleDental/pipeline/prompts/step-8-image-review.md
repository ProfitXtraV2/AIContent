# Step 8 — External image review (Gemini) — ELLE Dental

Used only for the rare owner-approved `new-page` diagram (see `step-8-images.md`). Sent by
`python3 scripts/gemini_image_review.py <article> <image> --brand elledental`.

## PROMPT (verbatim — send with the page text + image appended)

Act as a senior medical editor and art director reviewing an explanatory diagram for a Bulgarian patient-information page of ELLE Dental Clinic (elledental.bg), a dental clinic in Sofia. You are given the page text and the diagram (SVG source and, where available, a rendered PNG). Judge:

- **Relevance** — does it help a patient understand this page, or is it decoration?
- **Accuracy** — does every label, step and number match the page text exactly? Quote anything the page does not support.
- **Integrity / medical hygiene (automatic FAIL)** — any photo or photorealistic style, any teeth/gum/mouth close-up, before/after imagery, people or faces, instruments in use, logos, brand names, prices, promotional or guaranteeing wording, or non-Bulgarian labels.
- **Tone** — neutral, professional, patient-information style; nothing that glamorises a result.
- **Layout** — no overlapping or clipped text, nothing touching an edge, legible at display width.
- **SEO metadata** — descriptive lowercase hyphenated filename and specific Bulgarian ALT text.

Give me a single score from 0 to 100 and a verdict `PASS` (>= 80) or `NEEDS WORK` (< 80), the specific problems, and concrete fixes. Do not invent or correct medical facts; do not redraw the image yourself.

## Accept / iterate policy
- PASS at score ≥ 80 with no integrity failure and no layout defect.
- Otherwise hand-fix the SVG and re-review, up to `MAX_IMAGE_PASSES` (2); if still failing, drop
  the image. Never ship an integrity failure.
