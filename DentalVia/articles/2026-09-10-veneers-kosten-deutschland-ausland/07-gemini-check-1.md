# Step 7 — Gemini cross-model check · Pass 1 (verbatim verdict + recommendations)

Model: gemini-3.1-pro-preview · run 10.09.2026 · input: 05b-final-draft.md

## VERDICT
**Shows strong AI patterns (Likely an AI-generated draft or heavily AI-edited), 85% confidence.**
→ Normalised human-likeness = 100 − 85 = **15** (below GEMINI_TARGET_CONFIDENCE 80 → iterate).

While the article is highly informative and well-structured, it relies heavily on classic LLM
syntactical habits: rigid signposting, repetitive "Not X, but Y" contrast structures, tautological
filler sentences, and a highly didactic, summarizing conclusion.

(Process note from Gemini: the text contains [VERIFY]/[DATA NEEDED]/[CONFLICT]/[LINK] tags — flagged
as a workflow/unfinished-draft signal; Gemini did NOT suggest removing or altering them. These are
intentional pipeline flags and stay in the text for the human's Step-6 verification.)

## FLAGGED PATTERNS
1. "Thesis/Roadmap" setup (signposting): „Der Preis hängt an drei Größen: Material, Umfang und
   Eignung. Sie bestimmen, wann sich der Blick ins Ausland lohnt und wann er ins Leere geht." —
   three-pillars announcement of structure.
2. "Not X, but Y" contrast (robotic cadence), 3 instances:
   „Das ist Ästhetik, keine medizinische Notwendigkeit…"; „Der niedrigere Auslandspreis ist kein
   Qualitätssignal, sondern eine Kostenfrage…"; „Ein niedriger Preis für ein Veneer, das Sie gar
   nicht brauchen, ist keine Ersparnis, sondern eine überflüssige Ausgabe."
3. Tautological/over-explained transition: „Zwei Angebote sind erst vergleichbar, wenn Sie wissen,
   was jeweils darinsteht."
4. Didactic, summarizing conclusion: „Das Ausland senkt bei gleicher Leistung den Preis spürbar …
   Der Vergleich trägt aber nur bei gleichem Material, gleicher Zahnzahl und gleicher Eignung …"
5. Symmetrical/over-polished phrasing: „Ob diese Differenz eine echte Ersparnis ist, entscheidet
   sich weniger am Endpreis als daran, was in einem Angebot tatsächlich steckt …"

## CONCRETE RECOMMENDATIONS (style only — apply via fresh Humaniser, preserve every number/flag/link/compliance line)
- Break the "roadmap": do not announce the three variables (Material, Umfang, Eignung); weave them in.
- Dismantle "Not X, but Y": keep one instance, flatten the other two to direct statements.
- Cut transitional filler that states the obvious (delete the "Zwei Angebote sind erst vergleichbar…" opener; start with the actionable advice).
- Kill the recap in the conclusion; let the close focus on practical next steps (Befund prüfen) + the Sofia option.
- Flatten the bloated symmetrical compound sentence into plainer web copy.
