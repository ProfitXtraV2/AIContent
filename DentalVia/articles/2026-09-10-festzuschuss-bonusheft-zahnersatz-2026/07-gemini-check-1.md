# Step 7 — Gemini cross-model check · Pass 1 (verbatim verdict + recommendations)

Model: gemini-3.1-pro-preview · run 10.09.2026 · input: 05b-final-draft.md

## VERDICT
**Shows AI patterns, 75% confidence.** → Normalised human-likeness = 100 − 75 = **25** (below target 80 → iterate).

Highly informative and compliant, but the structure/rhythm reads AI-templated: repetitive reinforcement
of one core concept, numeric "listicle" signposting, "Angenommen" hypothetical setup, and a slightly
preachy/didactic tone. (Gemini notes the [VERIFY]/[LINK] placeholders + compliance disclosures as
intentional; it did not alter facts/flags.)

## FLAGGED PATTERNS + RECOMMENDATIONS (style only — preserve every number/%/€/date/flag/compliance line)
1. Numeric signposting / listicle framing: „Drei Begriffe entscheiden…"; heading „Zwei Hebel, die Sie
   selbst in der Hand haben" + „Zwei Dinge lohnen sich deshalb handfest." → drop the numeric announcements;
   introduce the concepts directly; do not summarise in a neat bow.
2. Didactic/preachy tone: „Das Heft ist … schlicht Ihr Nachweis; führen Sie es lückenlos, arbeitet es
   für Sie."; „Nehmen Sie sich für diesen Schritt Zeit. Lassen Sie sich den Plan … in Ruhe erklären…" →
   state the objective importance without the unsolicited behavioural advice / aphorism (KEEP the
   patient-protection substance: HKP vom eigenen Zahnarzt prüfen; Kasse ist verbindlich — just less preachy).
3. Repetitive concept reinforcement (befundbezogen, nicht rechnungsbezogen): explained well in intro +
   S1; the reminders in S2 and S5 („Diese Prozentsätze greifen immer an der Regelversorgung…", „In allen
   drei Fällen bleibt der Festzuschuss derselbe befundbezogene Betrag") are redundant → trim the repeats,
   keep the intro/S1 explanation. (Do NOT drop any figure — only the redundant restatement prose.)
4. "Angenommen" hypothetical setup: „Angenommen, für eine einzelne Zahnlücke sieht die Regelversorgung
   eine dreigliedrige Brücke vor…" → „Ein Beispiel: Sieht die Regelversorgung … vor …" (keep 2.200/398/1.802 €).
5. Over-polished/idiomatic wrap-ups → flatten to plain statements.

## NOTE (for the human)
Gemini partly attributes the AI read to the pipeline-required inline [VERIFY] flags and the verbatim
compliance boilerplate, which must stay in the text. A fresh Humaniser pass applies 1–5 without touching
numbers, flags, or compliance lines; re-check follows (MAX_GEMINI_PASSES 2).
