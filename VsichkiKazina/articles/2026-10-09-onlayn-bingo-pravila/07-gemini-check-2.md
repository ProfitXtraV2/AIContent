# 07 — Gemini Step-7 check · pass 2 (after humaniser pass 1) · vk-0262

**Date:** 2026-10-10

**Verdict (verbatim):** Shows AI patterns, 65% confidence.
**Human-likeness (normalized):** 100 − 65 = **35** → below target (80) → NEEDS CHANGES
(improved from pass-1 baseline human-likeness 20)

---

Gemini recommendations (verbatim):

### 1. Clunky Signposting (Telegraphing)
*   Flagged: "...и за нея става дума по-долу." (end of intro)
*   Flagged: "...а за това след малко." (end of first section)
*   Recommendation: Delete both phrases entirely.

### 2. Forced Conversational Idioms (Semantic Calques)
*   Flagged: "Бингото е лотария с компания."
*   Flagged: "Правилата се хващат за пет минути..."
*   Recommendation: adjust opening hook; change "се хващат" to "се научават"/"се усвояват".
    (NOTE: Brand Gate VOICE NOTES explicitly say KEEP the „лотария с компания" intro — brand voice authority overrides this style rec; the "се хващат" softening is applied.)

### 3. Symmetrical/Formulaic Contrast
*   Flagged: "В пълна зала с много играчи една карта печели рядко. В полупразна зала печалбата идва по-често, но е по-малка..."
*   Recommendation: merge into a fluid asymmetrical sentence (e.g. with "докато").

### 4. The "Wrap-up + Moral" Conclusion Pattern
*   Flagged: heading "Струва ли си да играеш бинго" + pivot "Затова сложи си лимит..."
*   Recommendation: more specific heading; remove the "Затова" connector.

### Process Note
*   `[VERIFY]` flag, RG boilerplate, 18+ markers left untouched (per instructions).
