# Step 8 — Article images (create)

After the text of an article is final (`05b` locked, Step-7 text check passed/kept-best),
create **at least one image** for it, then send it to Gemini for visual review
(`step-8-image-review.md`). Multiple images per article are allowed and encouraged when they
each earn their place. We chase great SEO: images must add real value, not decoration for
its own sake.

## What to make (prefer the highest-SEO option the article supports)

1. **Data infographic — SVG, hand-authored from THIS article's own numbers (PREFERRED).**
   Whenever the article contains figures, comparisons, steps, or a small table (wagering
   math, RTP/volatility, a "base × multiplier = turnover" calc, a checklist), render them as
   a compact **inline SVG**. SVG is the SEO winner: it is real text (Google reads the words
   and numbers), tiny (usually < 10 KB → fast LCP), crisp on every screen, and renders
   natively on GitHub. **Every number in the infographic MUST come verbatim from the
   article's `05b`** — never introduce a figure the text does not state. If the numbers are
   illustrative, say so on the graphic (e.g. „числата са примерни"). No operator logos/names.
   Requires no external API — always possible for data-bearing articles.
   **Match the article's exact number formatting** (e.g. if `05b` writes `€3,000`, the graphic
   uses `€3,000`, not `€3 000`) so the review's accuracy check passes cleanly.

2. **Decorative AI hero — via the Gemini image API (`scripts/gemini_image_gen.py`).**
   For engagement on top pages, an original decorative illustration (stylised slot reels,
   abstract casino motifs, a themed flat illustration). Optional and best-effort: if the
   image API is unavailable, skip it and ship the infographic. Keep it purely decorative.
   **Make it evocative of THIS article's topic, not generic filler** — a generic decorative
   image tends to score low in review (~55). For a data/mechanics-heavy article, an
   infographic is strongly preferred over a decorative hero; add a hero only when it genuinely
   helps. (The gen script auto-installs Pillow if the environment lacks it, so it can always
   deliver a WebP < 100 KB; if conversion still fails it warns and you ship the infographic.)

## How many images per article (SEO + UX policy — apply this)
Aim for the count that best serves SEO *and* reading experience, not a fixed number. Each
image must earn its place; never pad, never invent data to justify a graphic. Use this rubric:

- **Always: exactly one concept hero (WebP)** at the top, under the H1 — the visual entry
  point / dwell-time and social-share (OG) image. One only; a second decorative image adds
  page weight without SEO value.
- **Then one data infographic (SVG) per DISTINCT data block the article genuinely contains**
  — a comparison, a formula/calc, a step sequence, a paytable/stat set, a "how it works"
  flow. Scale to the article, and cap for UX:
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

## Hard hygiene rules (apply to EVERY image — infographic and AI alike)
- **No fabrication.** No real operator logos, brand names, or UI. No invented bonus numbers,
  licences, RTP %, or offers. Infographic numbers must trace to `05b`; if a figure cannot be
  supported, remove it (never fake it). No fake screenshots of operator sites.
- **No people or faces.** No photoreal gambling imagery that glamorises play.
- **Responsible-gambling appropriate.** Neutral, non-hype; where natural, an infographic may
  carry a small „18+ Играйте отговорно". Never depict winning/euphoria as a promise.
- **SEO metadata (mandatory for every image):**
  - **Filename** = descriptive, lowercase, hyphenated, Bulgarian-transliterated or topical
    (e.g. `razigravane-mnozhitel-baza-oborot.svg`, `bezplatni-kazino-igri-demo-hero.webp`).
  - **ALT text** = specific Bulgarian description of what the image shows (not "изображение").
  - **Raster format** = **WebP < 100 KB** (the gen script enforces this); vector stays SVG.
- **Placement + reference.** Save under `VsichkiKazina/articles/<slug>/images/`. Reference the
  image from `05b-final-draft.md` at the natural spot (hero near the top under the H1; an
  infographic beside the data it visualises) with the Bulgarian ALT and, for infographics, a
  one-line caption. Images travel in the SAME content PR as the article.

## SVG layout safety — nothing overlaps, nothing clips, everything is readable

Every infographic SVG MUST be visually clean at its display size. These are hard
requirements, not preferences — a single overlapping or clipped character is a defect:

- **Fits the canvas with margin.** Keep a ≥ 16 px inner padding on all four sides of the
  `viewBox`; NO stroke, box, or text may cross or touch the `viewBox` edge (or, if there is a
  rounded card/background rect, that card's edge).
- **Estimate every text width before you place it.** Rendered width ≈ `chars × font-size × 0.62`
  for Cyrillic/mixed text (`× 0.55` for pure Latin/digits). Account for `text-anchor`:
  `start` grows right from `x`, `end` grows left from `x`, `middle` grows both ways by half.
  The resulting box must sit fully inside its container/column with ≥ 8 px slack.
- **No two elements overlap.** A right-anchored header label (e.g. „Домашно предимство") must
  NOT collide with an adjacent badge/percentage/value. If they share a row and the estimated
  boxes would touch, put them on separate rows (different `y`) or move the small value onto the
  graphic it annotates (e.g. inside the bar segment) — never stack a number on top of a label.
- **Tables / columns.** Compute each column's center so the WIDEST cell text in that column
  fits within the column width with padding. The rightmost column's text must END ≥ 16 px
  before the card's right edge. If the widest label (header or any cell, incl. „✓ Най-добър",
  „✗ Избягвай") does not fit: WIDEN the `viewBox`, narrow other columns, or reduce that
  column's font — do NOT let it clip. Left/right-anchor edge columns inward instead of
  centering them tight against the border when space is short.
- **Prefer width + smaller type over cramming.** A wider `viewBox` (e.g. 700–760) with breathing
  room beats a 600-wide canvas with text jammed to the edges.
- **Verify before locking.** After authoring, (a) re-check every `<text>`'s estimated extent
  against its container per the formula above, then (b) RENDER the SVG to PNG at the display
  width and eyeball all four corners and every column — confirm no character is cut off, no two
  texts overlap, and nothing touches an edge. Only then reference it from `05b`.

## AI-image prompt guidance (when generating a hero)
Write the gen prompt in English for the model. **Depict a VISUAL METAPHOR of the article's
core idea — not generic casino imagery.** Live testing on the wagering guide proved this: a
generic "stylised slot reels" hero scored **55–65/100 (NEEDS WORK)**, while a concept metaphor
("a padlock on a stack of chips with circular arrows = the bonus is locked until money cycles
through / turnover") scored **85/100 (PASS)** — a +30 jump for the same effort. So:

1. Name the article's ONE central concept, then a concrete textless metaphor for it, e.g.
   wagering/turnover → padlock on chips with looping arrows, or a coin travelling a looped
   track to an open padlock; volatility → a jagged vs smooth line/wave; RTP → a split
   proportion / pie; bankroll management → a wallet with a measured/portioned meter.
2. Always append the hygiene as explicit constraints, verbatim-style:
   "Flat vector editorial illustration. Clean modern flat design, limited premium palette,
   soft shadows, balanced composition, generous negative space, lightweight hero banner.
   Absolutely NO text, NO numbers, NO letters, NO logos, NO brand names, NO real casino
   interface, NO people or faces, NO photorealism."
3. Because text/numbers are banned (and image models garble them anyway), NEVER ask for a
   „x30", a percentage, or any label in the image — carry all numbers in the SVG infographic
   instead. If a hero scores < 80 in review, the usual fix is a stronger metaphor, not more
   decoration. Keep the SVG infographic as the primary illustration for data articles; the AI
   hero is the optional visual entry-point at the top.
