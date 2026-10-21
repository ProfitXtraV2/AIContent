# Step 8 — Gemini image review, pass 2 (hero regeneration)

Model: gemini-3.1-pro-preview (multimodal). Only the hero was iterated (infographic already PASS 100 in pass 1).

## Hero regeneration attempt (v2)
Prompt hardened to force standard casino pips (dots 1–6), no geometric/fantasy symbols.
**Score: 35/100 · NEEDS WORK.** Gemini flagged the right die as showing an impossible pip count (~8 dots on one face) — an AI-generation hallucination. No integrity failure (still abstract, neutral, no people/logos/fake UI/fabricated casino numbers/glamorised winning). Score is LOWER than v1 (60).

## Decision — keep-best (MAX_IMAGE_PASSES=2 reached)
Both hero attempts have a minor AI dice-face artifact (v1: geometric pip patterns, score 60; v2: extra-pip die, score 35). Neither is an integrity failure. Per keep-best, **restored v1 (score 60)** — the highest-scoring version seen. The die-face quirk is cosmetic on a purely decorative banner; the article's data is carried entirely by the infographic (PASS 100), which is the primary illustration for this math-focused guide.

## Final image set
- `images/kraps-domashno-predimstvo.svg` — infographic, **100/100 PASS** (all figures trace to 05b).
- `images/kraps-zarove-hero.webp` — decorative hero, **60/100** (kept-best; no integrity issue).
images: 2 · best review score 100.
