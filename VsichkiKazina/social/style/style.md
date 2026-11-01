# Всички Казина — the look of the social images

One guide for everyone who makes the pictures, so that Claude and Gemini work to the same style:

- **The drafting routine (Claude)** reads it before it writes a post's `art_idea` (the cover)
  and `slide_ideas` (one per point slide): it describes scenes in this guide's words.
- **Gemini** gets the block under **STYLE** word for word in every picture it draws
  (`prompts/visual-art.md`), with the mascot pictures in `mascot/` attached as references, and
  the review (`prompts/visual-review.md`) checks every slide against the same block.
- **People** change the look here: edit this file (or swap the pictures in `mascot/`) in a PR,
  and the next pack follows it. Whether the point slides get a picture too is the `art` setting in
  `settings.md` (`every slide` or `cover`).

The mascot pictures are the brand's own (Всички Казина holds the rights).

## STYLE

Flat vector editorial illustration, like a modern explainer: clean shapes, bold even dark-ink
outlines (#14161A), soft flat shading, no textures, no gradients, no photorealism.
Palette: cream background #F7F4EC or deep green #0F7B5A, warm gold #C9962C for accents and
props, ink #14161A for outlines; the mascot keeps its own colours.
The mascot is the brand's fox, exactly as in the reference pictures: a slim adult red-orange fox
(#EE6A24) with a white muzzle and chest, dark ears and nose, a friendly calm smile, standing
upright like a person. It wears a navy suit with a white shirt and a dark tie, or a white lab coat;
round dark glasses when it explains or studies something. It is a grown-up expert who explains:
it points at a chart, holds a magnifying glass, writes on a board, weighs things on a scale, reads
a rule book, checks a stopwatch. One fox at most per picture, the same character every time.
The fox never plays, bets, deals, spins, holds chips, cards, cash or a phone with a game,
celebrates a win, drinks or looks sad over a loss; it never looks like a toy or a baby animal.
Objects of the idea (a balance scale, a padlock, a dice, a stopwatch, simple charts and icons in
round badges) are big, simple and few: one clear idea, generous empty space.
No humans, no text, letters or numbers anywhere, no logos or brand names, no real casino screen
or slot machine interface, no money raining, no glamour.

## The slides

| Slide | Picture | Words (set by our own tool, never by Gemini) |
|---|---|---|
| Cover | The post's idea as one scene, the fox in it when it helps (`art_idea`). The top third stays calm: the title goes there | The title (the hook) |
| Point | A small scene or object for that one point, on a plain cream background (`slide_ideas`, one per point), in the lower half | The point, above the picture, and the counter 2/5 |
| Closing | No picture: deep green, the call to read or save, the domain and „18+“ | |

Every slide carries the brand band: the name, the domain and „18+“.

## Good scene ideas

Write them in English, concrete and textless; say what the fox does and with which object.

- House edge → "the fox in a lab coat weighs two piles of identical gold tokens on a balance
  scale that tips slightly to one side".
- Wagering requirements → "the fox in a suit studies a padlock on a box through a magnifying
  glass; looping arrows circle the box".
- Volatility → "the fox points at two lines on a board: one jagged, one smooth".
- Set a limit → "the fox checks a big stopwatch next to a small locked piggy bank".
- A point slide without the fox is fine: "a gold padlock with a looping arrow in a round badge".

Weak: "slot reels", "casino chips and cards", "a happy fox with money" (décor or glamour: the
review scores it low or fails it).

## Rules this guide keeps

- The mascot is an adult professional who informs; it must never make gambling look fun or
  attractive to young people (no toy-like look, no playing, no winning). Our compliance line
  and „18+“ are on every post.
- The fox stays one recognisable character: the same face, colours and clothes as the pictures in
  `mascot/`. To change it, replace those pictures.
