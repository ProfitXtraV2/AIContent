# 08 — Gemini image review, pass 1

Command: `python3 scripts/gemini_image_review.py 05b-final-draft.md belot-stoynost-karti-koz-bez-koz.svg belot-anonsi-tochkuvane.svg belot-karti-hero.webp`
Date: 2026-10-20

**Aggregate score: 60 — NEEDS WORK** (dragged down by the hero only).

Per-image read:
- **belot-stoynost-karti-koz-bez-koz.svg → PASS.** Matches article numbers, layout flawless, ALT/filename descriptive, 18+ present.
- **belot-anonsi-tochkuvane.svg → PASS.** Same — accurate, clean, ready as-is.
- **belot-karti-hero.webp → NEEDS WORK.** AI-garbled cards: scattered/invented pip counts (hearts ~15, spades ~11), no corner indices. Decorative, but the reviewer wants real, identifiable cards.

Integrity check (our hard rules): NO operator logos/names, NO fake screenshots, NO invented bonus/RTP/licence numbers, NO people/faces, NO glamorised winning → **no integrity failure**. The flag is an aesthetic/realism nit on a decorative image.

Note on the reviewer's suggested fix (add J/9/A/10 corner indices + exact pip counts): this CONFLICTS with the Step-8 hygiene rule that AI heroes carry NO text/numbers/letters (image models garble them; all numbers live in the SVGs). So we will NOT add indices. Instead, pass-2 regenerates the hero with ONE large single suit pip per card (no scattered pips → no "wrong count" possible), keeping it purely decorative. Keep-best applies; if pass 2 does not clear, keep the best-scoring hero or ship the two PASS infographics alone.

## Gemini verbatim verdict

**Score: 60**
**Verdict: NEEDS WORK**

### Specific Problems

**1. Hero Image (belot-karti-hero.webp) — AI Hallucinations & Inaccurate Cards**
While the visual style is clean, the playing cards depicted are nonsensical AI generations, which is a critical failure for a beginner's guide meant to teach card rules:
- Missing Indices: None of the cards have corner ranks (numbers or letters like 7, 9, J, A). The article explicitly lists the exact cards used in the deck ("7, 8, 9, 10, Вале (J), Дама (Q), Поп (K) и Асо (A)"), but the image shows unidentifiable cards.
- Invented/Impossible Pip Counts: The symbols on the cards do not match any real playing cards. For example, the "Hearts" card has 15 heart symbols scattered randomly, and the "Spades" card has 11. This directly contradicts the educational value of the article.

**2. SVGs (belot-stoynost-karti-koz-bez-koz.svg & belot-anonsi-tochkuvane.svg) — PASS**
- Both infographics are excellent. They match the article text and numbers perfectly.
- The layout integrity is flawless: no text overlaps, margins are generous, and the columns are well-aligned.
- SEO metadata (filenames and ALT text) is highly descriptive, accurate, and correctly formatted.
- The tone is neutral and includes the required 18+ responsible gambling disclaimers.

### Actionable Fixes
- Hero Image (belot-karti-hero.webp): This image must be replaced or regenerated.
  - If using an AI prompt, change it to: "Flat vector illustration of four standard playing cards lying on a blue casino table. The cards MUST be the Jack of Clubs, 9 of Diamonds, Ace of Hearts, and 10 of Spades. Ensure standard corner indices (J, 9, A, 10) are clearly visible in the top-left and bottom-right corners, and the exact correct number of suit symbols are in the center. Minimalist, clean 2D vector art."
  - Alternative: Use a standard stock vector graphic of real playing cards to guarantee accuracy.
- SVGs: No changes required. They are ready to publish as-is.
