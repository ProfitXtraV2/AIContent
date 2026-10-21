# Gemini Step-7 check 4 — CORRECTED BASELINE (fixer run, --brand dentalvia)

Re-measurement with the DentalVia step-7 prompt (the original baseline `ai 85` was
measured before the brand-aware prompt binding; this confirms it with the correct prompt).

Command: `python3 scripts/gemini_check.py 05b-final-draft.md --brand dentalvia`

**Verdict: Likely AI-written or heavily AI-edited, 85% confidence.**
Normalized human-likeness = 100 − 85 = **15**. Below target (80) → run Humaniser loop.

Patterns flagged by Gemini:
1. "Neat bow" concluding sentences (formulaic topic-body-conclusion). Examples: "Wer im Ausland behandelt wird, bezahlt damit vor allem eine andere Kostenstruktur. Die Arbeit selbst muss deswegen nicht schlechter sein." / "Kein Veneer hält ewig; irgendwann steht ein Austausch an, und das macht den günstigen Auslandspreis zu einer wiederkehrenden, nicht einmaligen Rechnung." / "Der niedrige Preis allein entscheidet nichts."
2. AI antithesis / syntactic symmetry ("nicht X, sondern Y"). Examples: "Der niedrigere Auslandspreis ist kein Qualitätssignal, sondern eine Kostenfrage..." / "Diese Nähe und der rechtliche Rahmen sind prüfbare Vorteile, kein Versprechen auf ein bestimmtes Ergebnis." / "Der Eingriff verbessert das Aussehen, ein medizinisches Problem behebt er nicht."
3. Rigid sequential signposting: "Der Ablauf selbst folgt drei Schritten. Am Anfang stehen... folgt... Zuletzt..."
4. Over-engineered meta-descriptive ALT text (hero ALT "...Symbol für den Kostenvergleich...").
5. Clunky LLM-speak / hedging: "das oben Gesagte ist der deutsche Grundsatz"; heavy hedged intro hook.
6. Formulaic bridging transition: "Worauf Sie bei [LINK...] sonst noch achten sollten, klären Sie am besten vor der Buchung."

Recommendations are style-only; facts/figures/links/compliance lines/flags preserved. Applied via a fresh Humaniser pass (step-7b) — see next iteration.
