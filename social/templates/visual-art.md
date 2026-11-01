# Social visual — generated art (prompt template) — {{brand_name}}

`scripts/social/visuals.py` sends the block under **PROMPT** to Gemini (on the social key only):

- `{style}` is the **STYLE** block of `../style/style.md`; pictures in `../style/mascot/`, if the
  brand has a mascot, go with it as reference images;
- `{idea}` is the post's `art_idea` (the cover or a single image) or one of its `slide_ideas`;
- `{composition}` is the line below for that kind of picture;
- the network's aspect ratio is set through `--aspect`.

## Compositions

- **cover**: Keep the top third of the picture calm and simple, with no detail behind where a title will be laid over it; place the main subject in the middle and lower part.
- **point**: The picture is placed in the lower half of a slide, under a line of text: one subject in the centre, whole and uncropped, on a plain flat {{paper}} background with no scenery edges and no frame.

## PROMPT

Draw a picture for a social post in this house style.

STYLE: {style}

THE PICTURE: {idea}.

COMPOSITION: {composition}

If reference pictures are attached, the first ones show the brand's mascot: draw that same
character, not a new one, and copy nothing else from them. A last reference that is not the
mascot is the carousel's cover: match its look.
Absolutely NO text, NO numbers, NO letters, NO logos, NO brand names, NO humans or human faces,
NO photorealism. {{art_rules}}
