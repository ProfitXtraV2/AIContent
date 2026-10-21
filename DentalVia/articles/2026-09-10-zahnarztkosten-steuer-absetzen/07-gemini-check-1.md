# Step 7 — Gemini cross-model check · Pass 1 (verbatim verdict + recommendations)

Model: gemini-3.1-pro-preview · run 10.09.2026 · input: 05b-final-draft.md

## VERDICT
**Shows AI patterns, 85% confidence.** → Normalised human-likeness = 100 − 85 = **15** (below target 80 → iterate).

Tells named: the inline [VERIFY]/[LINK] placeholders (flagged by Gemini as an unfinished-draft signal —
pipeline-required, NOT removable), a rigid "Schritt 1–5" listicle structure, forced metaphors, symmetrical
"if A then B" phrasing, and a sterile expert persona.

## FLAGGED PATTERNS + RECOMMENDATIONS
1. Formulaic "Schritt 1–5" framework → convert the "Schritt N:" subheadings to natural descriptive
   headings (keep the procedural order and clarity). APPLIED (headings de-numbered, sequence kept).
2. Forced/awkward metaphors: „Der Haken sitzt in einer Schwelle…"; „…die Schwelle nur einmal überspringen
   statt über zwei Jahre verteilt zweimal an ihr zu scheitern." → flatten to plain explanation. APPLIED.
3. Symmetrical „Wird ein Zahn … spricht das für die Absetzbarkeit; geht es allein um die Optik …, nicht."
   → break into asymmetrical sentences. APPLIED.
4. Generic expert persona: Gemini recommends injecting FIRST-PERSON author voice
   („Aus meiner Erfahrung … weiß ich …"). **NOT APPLIED — this violates the DentalVia brand voice rules**
   (markets/de/author.md PRONOUN AUDIT: avoid „ich" as a default narrative voice; no first-person
   clinical/experiential claim; prefer the neutral patient-guide / „wir organisieren…" framing). The brand
   compliance spine overrides a style detector. The section keeps the neutral/organisational framing.
5. Inline [VERIFY]/[LINK] tags: intentionally retained for the human's Step-6 verification.

## NOTE
A fresh Humaniser pass applies 1–3 (and de-numbers headings) without touching any figure, flag, link, or
compliance line, and WITHOUT adding first-person „ich"; re-check follows (MAX_GEMINI_PASSES 2).
