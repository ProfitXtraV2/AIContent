# Step 8 — Article images (create)

After the text of an article is final (`05b` locked, Step-7 text check passed/kept-best),
create **at least one image** for it, then send it to review
(`step-8-image-review.md`). Multiple images per article are allowed and encouraged when
they each earn their place. We chase great SEO: images must add real value, not decoration
for its own sake.

## What to make (prefer the highest-SEO option the article supports)

1. **Data infographic — SVG, hand-authored from THIS article's own numbers (PREFERRED).**
   Whenever the article contains figures, comparisons, steps, or a small table (price
   comparison DE↔BG, cost breakdowns, treatment-step sequences, "Ablauf in 2 Reisen"
   timelines, Einheilzeit ranges, insurance-reimbursement figures), render them as a
   compact **inline SVG**. SVG is the SEO winner: it is real text (Google reads the words
   and numbers), tiny (usually < 10 KB → fast LCP), crisp on every screen, and renders
   natively on GitHub. **Every number in the infographic MUST come verbatim from the
   article's `05b`** — never introduce a figure the text does not state. If the numbers are
   illustrative examples, say so on the graphic (e.g. „Stand 09/2026 – Beispielpreise").
   All price data in infographics MUST carry a "Stand MM/JJJJ" label. No clinic logos or
   real operator names. Requires no external API — always possible for data-bearing articles.
   **Match the article's exact number formatting** (e.g. if `05b` writes `2.500 €`, the
   graphic uses `2.500 €`, not `2500€`) so the review's accuracy check passes cleanly.
   **All infographic labels and text in German.**

2. **Concept hero — via the Gemini image API (`scripts/gemini_image_gen.py`).**
   For engagement on top pages, an original decorative illustration. Optional and
   best-effort: if the image API is unavailable, skip it and ship the infographic. Keep it
   purely decorative. **Make it evocative of THIS article's topic, not generic dental
   imagery.** A generic "stylised teeth and dental tools" hero tends to score low in review;
   a concept metaphor (e.g. a travel map with a route from a northern city to Sofia for a
   dental-trip article; a cost-comparison balance scale for a price article; a calendar with
   two journey marks for a "Ablauf in 2 Reisen" article) scores much higher — same effort.

## How many images per article (SEO + UX policy — apply this)
Aim for the count that best serves SEO *and* reading experience, not a fixed number. Each
image must earn its place; never pad, never invent data to justify a graphic. Use this rubric:

- **Always: exactly one concept hero (WebP)** at the top, under the H1 — the visual entry
  point / dwell-time and social-share (OG) image. One only; a second decorative image adds
  page weight without SEO value.
- **Then one data infographic (SVG) per DISTINCT data block the article genuinely contains**
  — a price comparison, a cost breakdown, a treatment-step sequence, a timeline, a
  reimbursement table. Scale to the article, and cap for UX:
  - **Short / one data block** (≈ up to 800 words) → **1 infographic**.
  - **Medium / two data blocks** (≈ 800–1500 words) → **up to 2 infographics**.
  - **Long pillar / three+ data blocks** (≈ 1500+ words) → **up to 3 infographics**.
- **Hard UX cap: ≤ 4 images total per article** (1 hero + up to 3 infographics). More than
  that clutters the read and slows the page — stop before the cap unless every graphic is
  clearly pulling weight.
- **Pure-concept article with no real data** → the hero, plus **at most one** simple
  explanatory diagram (SVG) only if it genuinely aids understanding. Do NOT force an
  infographic where there are no numbers.
- **Spacing (UX):** don't stack images; separate each with enough body text that it sits
  beside the content it illustrates. One infographic per major section at most.
- When unsure, prefer FEWER, higher-value graphics — an accurate infographic beats a
  decorative image, and one strong infographic beats three weak ones.

Rule of thumb: **1 hero + 1–3 infographics**, matched to how many real data blocks the piece
has. Most guides land at 2–3 images total; a rich pillar may reach the 4-image cap.

## DENTAL IMAGE HYGIENE — MANDATORY (apply to EVERY image, no exceptions)

These rules are specific to DentalVia and override any general image guidance:

- **NO realistic before/after teeth imagery.** No clinical photos of teeth, gums, or mouths
  — before or after treatment. These create unrealistic expectations, may breach medical
  advertising rules, and are not appropriate for an information/mediation site.
- **NO clinical photographs of any kind.** No images of operating rooms, dental chairs,
  instruments in use, or close-up clinical shots. Stylised flat illustration only.
- **Flat vector / editorial illustration only** for the concept hero. No photorealism, no
  AI-generated photographic style, no stock-photography look. Clean flat design with a
  limited premium colour palette.
- **All price graphics carry „Stand MM/JJJJ"** — every price or cost figure shown in any
  infographic must have a date label. No undated price claims in any visual.
- **All labels and text in German.** No mixed-language infographics.
- **No clinic branding or partner-clinic logos.** No real dental brand names in imagery.

## Hard hygiene rules (apply to EVERY image — infographic and hero alike)
- **No fabrication.** No real clinic logos, brand names, or UI. No invented prices, insurance
  figures, or success rates. Infographic numbers must trace to `05b`; if a figure cannot be
  supported, remove it (never fake it). No fake screenshots.
- **No people or faces.** No photoreal imagery. No depictions of clinical procedures.
- **Medically neutral.** Non-hype, non-promotional tone. Never depict treatment results as
  guaranteed. Never depict "happy patient" imagery that glamorises outcomes as a promise.
- **SEO metadata (mandatory for every image):**
  - **Filename** = descriptive, lowercase, hyphenated, German-topical
    (e.g. `zahnimplantat-kosten-vergleich-deutschland-bulgarien.svg`,
    `ablauf-2-reisen-zahnbehandlung-sofia.webp`).
  - **ALT text** = specific German description of what the image shows (not "Bild").
  - **Raster format** = **WebP < 100 KB** (the gen script enforces this); vector stays SVG.
- **Placement + reference.** Save under `DentalVia/articles/<slug>/images/`. Reference the
  image from `05b-final-draft.md` at the natural spot (hero near the top under the H1; an
  infographic beside the data it visualises) with the German ALT and, for infographics, a
  one-line German caption. Images travel in the SAME content PR as the article.

## SVG layout safety — nothing overlaps, nothing clips, everything is readable

Every infographic SVG MUST be visually clean at its display size. These are hard
requirements, not preferences — a single overlapping or clipped character is a defect:

- **Fits the canvas with margin.** Keep a ≥ 16 px inner padding on all four sides of the
  `viewBox`; NO stroke, box, or text may cross or touch the `viewBox` edge (or, if there is a
  rounded card/background rect, that card's edge).
- **Estimate every text width before you place it.** Rendered width ≈ `chars × font-size × 0.62`
  for mixed/Latin text (`× 0.55` for pure digits). Account for `text-anchor`:
  `start` grows right from `x`, `end` grows left from `x`, `middle` grows both ways by half.
  The resulting box must sit fully inside its container/column with ≥ 8 px slack.
- **No two elements overlap.** A right-anchored header label must NOT collide with an adjacent
  badge/value. If they share a row and the estimated boxes would touch, put them on separate
  rows (different `y`) or move the small value inside the graphic element — never stack a
  number on top of a label.
- **Tables / columns.** Compute each column's center so the WIDEST cell text in that column
  fits within the column width with padding. The rightmost column's text must END ≥ 16 px
  before the card's right edge. If the widest label does not fit: WIDEN the `viewBox`, narrow
  other columns, or reduce that column's font — do NOT let it clip.
- **Prefer width + smaller type over cramming.** A wider `viewBox` (e.g. 700–760) with breathing
  room beats a 600-wide canvas with text jammed to the edges.
- **Verify before locking.** After authoring, (a) re-check every `<text>`'s estimated extent
  against its container per the formula above, then (b) RENDER the SVG to PNG at the display
  width and eyeball all four corners and every column — confirm no character is cut off, no
  two texts overlap, and nothing touches an edge. Only then reference it from `05b`.

## AI-image prompt guidance (when generating a concept hero)
Write the gen prompt in English for the model. **Depict a VISUAL METAPHOR of the article's
core idea — not generic dental imagery.** Concept metaphors score far higher than generic
tooth/drill illustrations:

1. Name the article's ONE central concept, then a concrete textless metaphor for it, e.g.
   cost comparison → a balance scale with a euro sign and a map of Bulgaria;
   two-trip treatment journey → a calendar with two circled dates connected by a flight arc;
   implant osseointegration → a root growing into solid ground;
   insurance reimbursement → a document with an approval stamp and a coin.
2. Always append the hygiene as explicit constraints, verbatim-style:
   "Flat vector editorial illustration. Clean modern flat design, limited premium palette,
   soft shadows, balanced composition, generous negative space, lightweight hero banner.
   Absolutely NO text, NO numbers, NO letters, NO logos, NO brand names, NO clinical photos,
   NO teeth close-ups, NO before/after imagery, NO people or faces, NO photorealism,
   NO dental instruments or clinical settings."
3. Because text/numbers are banned in the hero (and image models garble them anyway), NEVER
   ask for a price, percentage, or label in the hero image — carry all numbers in the SVG
   infographic instead. If a hero scores < 80 in review, the usual fix is a stronger
   metaphor, not more dental imagery.
