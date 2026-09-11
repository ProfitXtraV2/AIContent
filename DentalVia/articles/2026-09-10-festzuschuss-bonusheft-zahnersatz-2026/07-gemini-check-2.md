# Step 7 — Gemini cross-model check · Pass 2 (after Humaniser pass 1)

Model: gemini-3.1-pro-preview · run 10.09.2026 · input: 05b-final-draft.md (post humaniser pass 1)

## VERDICT
**Shows AI patterns, 75% confidence.** → Normalised human-likeness = 100 − 75 = **25** (unchanged vs pass 1).

Remaining tells: a "regurgitated summary" closing section, redundant micro-summaries, forced symmetry
(chiasmus), and a parallel "glossary" definition rhythm. (Gemini explicitly praises the [VERIFY]/[LINK]
placeholders and the medical disclaimer as good practice and did NOT suggest removing them — they stay.)

## FLAGGED PATTERNS + RECOMMENDATIONS (style only — preserve every number/%/€/date/flag/compliance line)
1. Redundant micro-summary: after the 60→70→75 % paragraph, delete the standalone sentence
   „Ein volles Bonusheft hebt damit den Zuschuss." (the preceding paragraph already says it).
2. Over-engineered symmetry (chiasmus): „Der Betrag steht fest, sobald der Befund feststeht, und er
   bleibt gleich, gleichgültig für welche Versorgung…" → break the symmetry, e.g. „Sobald Ihr Befund
   klar ist, ist auch die Höhe des Zuschusses fixiert, egal für welche Behandlungsmethode Sie sich
   danach entscheiden." (keep the meaning; do not restate it again elsewhere).
3. Glossary rhythm (three parallel "[Noun] [Verb]…" definitions for Regelversorgung/gleichartig/
   andersartig): vary the sentence openings and combine, e.g. introduce Regelversorgung as the baseline,
   then „Wer auf diesem Weg bleibt, aber Extras wie eine Vollverblendung wünscht, wählt eine gleichartige
   Versorgung. Entscheiden Sie sich für eine andere Methode, etwa ein Implantat statt einer Brücke,
   spricht man von einer andersartigen Versorgung." (KEEP all figures + the Eigenanteil formula + LINK).
4. "Neat bow" regurgitated conclusion under „Was Sie selbst in der Hand haben" (repeats the four main
   points in order): scrap the summary paragraph; transition directly into the „Kostenlose Beratung" CTA,
   or replace it with ONE forward-looking sentence about the next step (Bonusheft lückenlos führen; HKP
   genehmigen lassen). Do NOT drop the 75 %/60 % figures if a single closing sentence keeps them; if the
   section is removed, those percentages already appear earlier and stay flagged there.

## NOTE (for the human)
Detector score held at 25 across the initial draft and pass 1; the residual read is driven largely by
the pipeline-required inline [VERIFY] flags and verbatim compliance boilerplate, which cannot be removed
to satisfy a detector. Pass 2 applies 1–4 and re-checks; keep-best then finalises (MAX_GEMINI_PASSES 2).
