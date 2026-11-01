# Social visual — generated art (prompt template)

`scripts/social/visuals.py` sends the block under **PROMPT** to Gemini (on the social key only):

- `{style}` is the **STYLE** block of `../style/style.md`, the guide Claude also writes to; the
  mascot pictures in `../style/mascot/` go with it as reference images (and, for a point slide,
  the carousel's own cover art, so all slides look alike);
- `{idea}` is the post's `art_idea` (the cover or a single image) or one of its `slide_ideas`
  (a point slide), written in English by the drafting routine (see `post-writing.md`);
- `{composition}` is the line below for that kind of picture;
- the network's aspect ratio is set through `--aspect`.

The hygiene is the same as the article images (`VsichkiKazina/pipeline/prompts/step-8-images.md`,
"Hard hygiene rules"). Good ideas name a scene of one idea, not casino décor: a generic "slot
reels" picture scores 55–65 in review; a clear scene scores 85+.

## Compositions

- **cover**: Keep the top third of the picture calm and simple, with no detail behind where a title will be laid over it; place the main subject in the middle and lower part.
- **point**: The picture is placed in the lower half of a slide, under a line of text: one subject in the centre, whole and uncropped, on a plain flat cream #F7F4EC background with no scenery edges and no frame.

## PROMPT

Draw a picture for a social post in this house style.

STYLE: {style}

THE PICTURE: {idea}.

COMPOSITION: {composition}

If reference pictures are attached, the first ones show the brand's mascot: draw that same
character (same face, colours, proportions and clothing), not a new one, and copy nothing else
from them. A last reference that is not the mascot is the carousel's cover: match its look.
Absolutely NO text, NO numbers, NO letters, NO logos, NO brand names, NO real casino interface
or slot screen, NO humans or human faces, NO photorealism. Neutral and calm: never depict
winning, money raining or euphoria.
