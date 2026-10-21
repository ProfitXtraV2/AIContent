# Step 8 — Gemini image review · Pass 1 (verbatim)

Model: gemini-3.1-pro-preview (multimodal) · run 10.09.2026
Images: zahnarztkosten-steuer-absetzen-hero.webp; zumutbare-belastung-beispielsaetze-paragraph-33-estg.svg

## Image 1 — hero.webp — Score 72/100 — NEEDS WORK
- Problem: "The ALT text is written in German … The brief strictly requires Bulgarian ALT text."
- Note: "The image and article perfectly match each other (German dental tax deductions), but completely
  conflict with the prompt's stated 'Bulgarian online-casino guide' environment."

## Image 2 — zumutbare-belastung-beispielsaetze-paragraph-33-estg.svg — Score 75/100 — NEEDS WORK
- Problem: "The aria-label … is in German …, failing the Bulgarian language requirement."
- Layout/Technical: "No clipping or overlapping detected; margins and text anchors are well-spaced.
  Data matches the article table exactly."

## ASSESSMENT + KEEP-BEST DECISION (no fix pass needed)
Both images are held under 80 ONLY by a "Bulgarian ALT text / Bulgarian online-casino" requirement that
comes from the SHARED review-prompt file `VsichkiKazina/pipeline/prompts/step-8-image-review.md` loaded by
scripts/gemini_image_review.py. VsichkiKazina is a Bulgarian brand; for **DentalVia (dentalvia.de)** the
step-8 rules REQUIRE **German** labels and **specific German ALT text**, so the German ALT is CORRECT and
must NOT be translated. Setting that spurious flag aside, the reviewer confirms: both images perfectly match
the article; the infographic's data matches the article table exactly; layout is clean with no clipping,
no overlap, well-spaced margins. There is NO integrity, dental-hygiene, or layout violation on either image.
Hero visual hygiene verified independently: flat vector (tax form + pen + receipts + refund coin, small flat
tooth/cross icons), NO clinical photo, NO teeth/mouths, NO people/faces, NO fabricated logo, NO real numbers.

Per keep-best (an integrity/hygiene/layout violation is the ONLY reason to drop or refuse an image), both
images are kept and shipped. No fix pass is warranted — the reviewer found nothing to fix (the language flag
is non-applicable, and layout is already clean).

## Result
images: 2 (1 concept hero WebP + 1 data infographic SVG — zumutbare Belastung example rates). Best/only
review scores: hero 72, infographic 75 (both sub-80 solely due to the VK-prompt Bulgarian-ALT artifact; no
real defect). Numbers trace verbatim to 05b; German labels + ALT; § 33 EStG example rates flagged as
Beispielwerte.

## Script note (for the human/maintainer)
scripts/gemini_image_review.py loads its prompt from VsichkiKazina/pipeline/prompts/step-8-image-review.md,
which demands Bulgarian ALT for a casino brand — this depresses DentalVia image scores with a false-negative
language flag. Point the script at DentalVia/pipeline/prompts/step-8-image-review.md for DentalVia runs.
No content change needed — German ALT is correct.
