# Step 7 — Gemini cross-model check · Pass 2 (after Humaniser pass 1)

Model: gemini-3.1-pro-preview · run 10.09.2026 · input: 05b-final-draft.md (post humaniser pass 1)

## VERDICT
**Shows AI patterns, 75% confidence.** → Normalised human-likeness = 100 − 75 = **25** (improved from 15 after pass 1).

## FLAGGED PATTERNS + DECISION
1. Repetitive elaboration (cosmetic-exclusion stated ~3× in five sentences): condense — merge Bleaching/
   kosmetische Veneers into the first exclusion sentence, delete the redundant final restatement. APPLY.
2. Formulaic W-question headings ("Wann das Finanzamt…", "Wie hoch Ihre zumutbare Belastung…", "Warum das
   Timing…"): change to punchier noun-based headings ("Die Grenze der zumutbaren Belastung", "Zahlungen
   bündeln: das Kalenderjahr entscheidet", etc.). APPLY.
3. Stilted persona → Gemini again recommends FIRST-PERSON ("Aus meiner Erfahrung als Patientenkoordinator
   rate ich…"). **NOT APPLIED — violates DentalVia brand voice** (no default „ich"; no first-person
   experiential claim). Keep neutral/organisational framing.
4. Generic "wrap-up" opener „…lohnt der Versuch fast immer, denn…": drop the generic opener; start the
   final paragraph directly with the actionable insight (the gestaffelte Berechnung lets more through).
   KEEP the disclaimers that follow. APPLY.
5. Over-polished transition on the deductions sentence: Gemini suggests turning it into a BULLET LIST.
   **NOT APPLIED as a list — the pipeline REDUCES lists and never adds them (humaniser rule).** May break
   the rhythm / shorten in PROSE only. APPLY (prose only, no new bullet list).

## NOTE
Pass 2 applies 1, 2, 4 and the prose-only part of 5; rejects the first-person (#3) and the new-bullet-list
(#5) suggestions as brand/pipeline violations. No figure/flag/link/compliance line touched. Re-check follows
(MAX_GEMINI_PASSES 2 → this is the final pass; keep-best after).
