# Step 7 — Gemini check, pass 3 (after Humaniser pass 2)

Model: gemini-3.1-pro-preview
Normalized: **"Likely AI-generated (or heavily AI-structured), 80% confidence"** → human-likeness = **100 − 80 = 20** → LOWER than pass 2 (HL 75). This is the high-variance behavior of the detector seen on prior articles (a further Humaniser pass measurably lowered the score).

## Decision — KEEP BEST
MAX_GEMINI_PASSES (2) reached. Human-likeness by version:
- initial draft: **15**
- Humaniser pass 1: **75** ← highest
- Humaniser pass 2: **20**

Per keep-best (mandatory), 05b is reverted to the **Humaniser pass-1** version (HL 75). content-queue `gemini` = `ai 25` (winning version's own verdict: "Likely human-written 75%" → recorded on the verbatim scale as ai 25 since HL < 80). Pass 2's edits are discarded; all numbers, links, RG lines, 18+, [VERIFY], dates, byline, brand identical across every version.

---

**Verdict (verbatim opening): Likely AI-generated (or heavily AI-structured), 80% confidence.**

While this article is highly accurate, free of typical AI "fluff," and adheres to responsible gambling guidelines, its underlying skeleton gives it away: rigid paragraph structures (premise → explanation → instructional takeaway), a didactic tone, and a formulaic conclusion under a clever heading. (Full recommendations not applied — pass-1 version kept per keep-best.)
