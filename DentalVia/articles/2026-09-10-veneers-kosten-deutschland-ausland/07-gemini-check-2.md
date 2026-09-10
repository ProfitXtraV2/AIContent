# Step 7 — Gemini cross-model check · Pass 2 (after Humaniser pass 1)

Model: gemini-3.1-pro-preview · run 10.09.2026 · input: 05b-final-draft.md (post humaniser pass 1)

## VERDICT
**Shows AI patterns, 85% confidence.** → Normalised human-likeness = 100 − 85 = **15** (unchanged vs pass 1).

Note (Gemini): the remaining [VERIFY]/[DATA NEEDED]/[CONFLICT] flags and the mandatory boilerplate
disclaimers are read as "unfinished/AI" signals; Gemini flags this as a process observation and did
NOT alter numbers/claims/flags. These flags are required by the DentalVia pipeline and MUST stay in
the text for the human's Step-6 verification — they are not removable to satisfy a detector.

## FLAGGED PATTERNS (pass 2)
1. Didactic/"wise advisor" tone: „Ein Veneer ist Kosmetik, keine Notwendigkeit" (H2); „Der niedrige
   Preis allein sagt Ihnen also wenig. Ein Veneer, das Sie gar nicht brauchen, wird auch in Sofia
   nicht zur Ersparnis." → frame around medical indication vs. aesthetic wish, less lecturing.
2. Formulaic micro-transitions: „Der Preisabstand … ist selten Willkür."; „Selten bleibt es bei einem
   Zahn." → delete, start paragraphs on the core info.
3. Repetitive "hängt am/ab" dependency phrasing: „hängt zuerst am Material und an der Herstellung";
   „Wie lange ein Veneer hält, hängt erneut am Material" → vary with active verbs.
4. Stilted "measured against the benchmark" comparative phrasing: „Gemessen wird jede Zeile am
   deutschen Keramik-Richtwert …"; „Gegen den deutschen Referenzwert von ab 4.800 € gerechnet …" →
   simply state DE price, foreign price, and the difference; do not announce the calculation.
5. "Bow-tie"/Fazit conclusion: H2 „Sofia als Option und das Fazit" → drop the „Fazit" framing; let the
   section be practical logistics/legal reality leading into the CTA.

## CONCRETE RECOMMENDATIONS (style only — preserve every number/flag/link/compliance line, and every price stays a dated example)
- Soften the didactic tone: keep the coverage fact (GKV zahlt nicht), drop the lecturing framing.
- Delete filler micro-transitions; open paragraphs on substance.
- Vary the "hängt am/ab" repetition with active constructions.
- Simplify comparative sentences: state DE price, foreign price, difference — without "gemessen/gerechnet gegen den Referenzwert" narration (keep the euro figures + "Stand 09/2026" exactly).
- Rename the closing heading to drop "Fazit"; keep the asymmetric verdict + Sofia logistics.
