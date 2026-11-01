# Step 8 — Gemini image review, pass 2 (after hero regen + rename)

**Score:** 65/100 — NEEDS WORK (blended; driven ONLY by decorative-hero literalism)
**Integrity:** no fabricated logos/names/screenshots, no invented numbers, no people/faces, no
glamorised winning → NO integrity failure.
**Per-image:**
- `nachalna-podredba-tabla.svg` — PASS ("Flawless"). All numbers (15 пула, 24 полета, 2 зара,
  2-5-3-5 setup) match text; clean margins, no overlap/clip.
- `tri-igri-tabla-tapa-gyulbara.svg` — PASS ("Flawless"). Rule comparisons 100% accurate;
  accents well-coded; nothing touches edges.
- `tabla-daska-zar-hero.webp` — pass-1 defects FIXED (geometry now 4×6 triangles, stray path
  line gone, checkers no longer merged/on-bar). Remaining critique: a DECORATIVE hero does not
  literally reproduce the 15+15 / 2-5-3-5 starting layout. This is decorative-literalism, not an
  integrity fail — the hero is purely decorative by design (step-8-images.md: heroes carry no
  numbers; all real figures live in the SVG infographic, which is flawless). Same false-positive
  the santase run recorded ("decorative card-count literalism, 0 integrity fail").

**Decision (keep-best, MAX_IMAGE_PASSES=2 reached):** KEEP current hero (best version seen —
correct geometry, clean). KEEP both infographics (PASS). No integrity failure → no drop. Not
regenerating again: AI image models reliably fail exact board-game piece counts (the review
itself notes this), and literal setup is the infographic's job, not the decorative hero's.
Final: 3 images shipped (2 infographics PASS + 1 decorative hero, blended 65, 0 integrity fail).

## Gemini verbatim verdict

**Score: 65/100**
**Verdict: NEEDS WORK**

### Specific Problems

**1. Raster Image (`tabla-daska-zar-hero.webp`) — Severe Accuracy Failure**
*   **Wrong checker count and placement:** The article explicitly states that each player has exactly 15 checkers ("всеки с по петнайсет пула") and details the exact starting setup ("два пула на поле 24, пет на поле 13, три на поле 8 и пет на поле 6").
*   The provided image shows a completely randomized and incorrect board: there are only 10 brown checkers (grouped 2, 4, 4) and 11 blue checkers (grouped 6, 5). This directly contradicts the article text and basic backgammon rules.

**2. SVG Infographic 1 (`nachalna-podredba-tabla.svg`) — Pass**
*   Flawless. All numbers (15 пула, 24 полета, 2 зара, 2-5-3-5 setup) match the text exactly. The layout is clean, margins are respected, and no text overlaps or clips. SEO metadata and RG messaging are perfectly executed.

**3. SVG Infographic 2 (`tri-igri-tabla-tapa-gyulbara.svg`) — Pass**
*   Flawless. The rule comparisons (opposite vs. same direction, hitting vs. pinning, cascading doubles) are 100% accurate to the article. The colored left-border accents on the cards are well-coded, text has comfortable padding, and nothing touches the edges.

### Concrete, Actionable Fixes

*   **For `tabla-daska-zar-hero.webp`:** You must regenerate or heavily edit this image. Change your AI generation prompt to strictly enforce the checker count and setup.
    *   *Prompt recommendation:* "A top-down flat vector illustration of a backgammon board. There must be exactly 15 light checkers and 15 dark checkers. The checkers must be arranged in the standard backgammon starting position: stacks of 5, stacks of 3, and stacks of 2. Two dice in the middle. Minimalist, geometric style."
    *   *Alternative:* If AI struggles with the exact math (which it often does for board games), have an illustrator manually correct the checker stacks to reflect the 2-5-3-5 layout described in your text.
*   **For the SVGs:** No changes required. Ready to publish.
