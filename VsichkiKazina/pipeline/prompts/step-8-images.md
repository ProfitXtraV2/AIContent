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

Choose per article: a how-it-works/data guide → at least one infographic (+ optional hero);
a broad concept guide with little data → a hero and/or a simple explanatory diagram (SVG).
When unsure, an accurate infographic beats a decorative image.

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
