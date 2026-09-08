# Step 7 — Gemini check, pass 3 (after Humaniser pass 2)

Model: gemini-3.1-pro-preview
Normalized: **"Likely AI-generated (via a highly constrained, high-quality prompt), 75% confidence"** → human-likeness = **100 − 75 = 25** → ties pass 1 (also 25); detector high-variance.

## Decision — KEEP pass 2 (tied-highest HL, cleaner Bulgarian)
MAX_GEMINI_PASSES (2) reached. Human-likeness by version:
- initial draft: **15**
- Humaniser pass 1: **25**
- Humaniser pass 2: **25** ← tied-highest, and the only version that removes the „люлките" anglicism (a genuine machine-translation red flag) plus the „подписната"/„емблематичната" filler.

Keep-best requires the final 05b to be a version with the highest human-likeness seen (25). Pass 2 is such a version and is objectively better Bulgarian, so it is kept (not a lower version). content-queue `gemini` = `ai 75` (winning version's verdict: "Likely AI-generated 75%"). All numbers, links, RG lines, 18+, [VERIFY], dates, byline, brand identical across every version.

---

**Verdict (verbatim opening): Likely AI-generated (via a highly constrained, high-quality prompt), 75% confidence.**

Exceptionally clean, no flowery adjectives or hype; reads as objective/math-focused/responsible. Residual tell is the rigid structural rhythm and the slightly didactic tone in the probability explanations. (The [VERIFY] release-year flag and RG/18+ language are intact; the human resolves the flag at Step 6.)
