# Step 8 — External image review (Gemini, multimodal)

Canonical prompt sent to a multimodal Gemini model to review each article image. Raster images
are sent as pixels. **SVG infographics are sent BOTH ways: rendered to a PNG at the display
width (so overlap, clipping and legibility are actually visible) AND as their source (so the
numbers can be checked).** Rendering the SVG to pixels is mandatory — a source-only review
cannot see that text overlaps or is cut off at the edge. **Recommendations + a score only** —
the image is regenerated (AI hero) or the SVG is hand-fixed (infographic) by our own pipeline,
never by Gemini.

## PROMPT (verbatim — send with the article text + image(s) appended)

Act as a senior SEO editor and art director reviewing an image that will accompany a Bulgarian online-casino guide. You are given the article text and one or more images (raster images as pixels; infographics as SVG source). Judge each image on:

- **Relevance & value** — does it genuinely support this specific article and its topic, or is it filler?
- **Accuracy** — for an infographic, does EVERY number, label, and relationship match the article text exactly? Quote any figure in the image that the article does not support. For any image, flag anything misleading.
- **Integrity / hygiene** — any real operator logo, brand name, fake UI/screenshot, invented bonus number, or promotional claim? Any depiction of people/faces or glamorised winning? These are failures.
- **Responsible gambling** — is the tone neutral and non-hype, appropriate for an 18+ responsible-gambling context?
- **SEO metadata** — is the filename descriptive/lowercase/hyphenated and is the Bulgarian ALT text specific and accurate to what the image shows?
- **Technical quality** — legibility, clarity, composition, aspect ratio, and (for raster) that it looks clean at web sizes.
- **Layout integrity (infographics — inspect the RENDERED pixels, and zoom every corner and column)** — NO text may overlap another text or element, NO text may be clipped or cut off by the canvas/card edge, and NO text may touch an edge. Every label, number and word must be fully visible and comfortably legible at the display width, with clear margins. A single overlapping or cut-off character is a defect. Call out the exact label and where it collides/clips.

Give me:

- A single **score from 0 to 100** for the image's overall fitness to publish (higher = better), and a one-line **verdict**: `PASS` (>= 80) or `NEEDS WORK` (< 80).
- The specific problems, each tied to what you see (or to the exact SVG number/label), named plainly.
- Concrete, actionable fixes — for an AI image, how to change the generation prompt; for an infographic, exactly which label/number/element to correct.

Hard rules:
- Do NOT invent or "correct" article facts — your accuracy check is only "does the image match the article text". If a number differs, the image is wrong, not the article.
- Do NOT output a rewritten/redrawn image or new SVG yourself — recommendations and the score only.
- Treat any fabricated operator logo/name, fake screenshot, invented bonus figure, human/face, or glamorised-winning imagery as an automatic fail regardless of visual polish.

## Accept / iterate policy (used by daily-run.md Step 8)
- **PASS** when the score is **>= IMAGE_TARGET_SCORE (80)** AND there is no integrity failure
  (a fabricated logo/number/screenshot, a person/face, or glamorised winning is an automatic
  fail even at a high score — fix it before shipping) AND no layout defect (any overlapping or
  clipped/edge-touching text is an automatic NEEDS WORK even at a high score — fix the SVG
  layout before shipping).
- **Otherwise:** apply Gemini's fixes — regenerate the AI hero with an improved prompt, or
  hand-correct the SVG (numbers must still trace to `05b`) — then re-run this review. Repeat
  up to `MAX_IMAGE_PASSES` (default 2).
- **Keep-best:** if still < 80 after the cap, keep the highest-scoring version seen (never a
  later, lower one) and log the verdict for the human. An integrity failure is the exception:
  never ship a fabrication — drop that image entirely and keep the article's other image(s),
  or ship the infographic alone.
