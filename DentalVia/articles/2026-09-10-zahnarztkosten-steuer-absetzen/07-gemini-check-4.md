# Gemini Step-7 check 4 — CORRECTED BASELINE (fixer run, --brand dentalvia)

Re-measurement with the DentalVia step-7 prompt. Original baseline `ai 75` predates the brand-aware prompt binding.

Command: `python3 scripts/gemini_check.py 05b-final-draft.md --brand dentalvia`

**Verdict: Shows AI patterns (Human-edited AI draft), 65% confidence.**
Normalized human-likeness = 100-65 = **35** (up from wrong-prompt hl 25). Below target (80) -> run Humaniser loop.

Style flags: rule-of-three list-sentence (Erstattungen), echoed 'je nach' openers, an over-dramatic idiom ('wiegt besonders schwer'), a forced /finanzierung/ link pivot. Facts/flags/compliance untouched.

---

**Verdict: Shows AI patterns (Human-edited AI draft), 65% confidence.**

This is a surprisingly good text. It successfully avoids the most egregious German AI clichés (you won't find "Darüber hinaus", "Zusammenfassend lässt sich sagen", or "In der heutigen komplexen Welt" here). It even features some punchy, very human-sounding sentences like *"Ausschlaggebend ist der Grund, nicht die Bezeichnung"* and *"Maßgeblich ist das Datum der Zahlung, nicht das der Behandlung."* 

However, the underlying structural rhythm, a few forced transitions, and the glaring presence of unresolved editorial tags reveal its likely origin as a well-prompted AI draft that hasn't fully cleared the editorial desk.

Here is the detailed breakdown of the patterns and how to fix them.

### 1. Leftover AI/Editorial Flags (Process Issue)
* **The Pattern:** Unresolved placeholder tags. AI models (or editors using them) frequently generate these when instructed to flag unverified claims or when using a specific drafting framework.
* **Flagged Passages:** 
  * `[VERIFY: gestaffelte Berechnung seit 2017]`
  * `[VERIFY: 664,70 €, Finanztip Stand 2024]`
  * `[VERIFY: Auslandsbehandlung deutsche Rechtslage/BFH]`
  * `[VERIFY]`
* **Recommendation:** As per your hard rules, I am not touching or removing these. However, from a workflow perspective, their survival into a "finished" article is a critical process issue. A human fact-checker needs to verify the specific dates, amounts, and legal precedents, and then clear these tags before the piece goes live.

### 2. The "A, ebenso B, und schließlich C" List-Sentence (Formulaic Rhythm)
* **The Pattern:** LLMs love this exact tripartite structure to group related items in a single sentence. It feels overly symmetrical, rhythmic, and slightly robotic.
* **Flagged Passage:** *"Dazu gehört der Festzuschuss der gesetzlichen Krankenkasse, ebenso alles, was eine private Krankenversicherung oder Zahnzusatzversicherung erstattet, und schließlich jede sonstige Kostenübernahme."*
* **Recommendation:** Break the artificial symmetry to make it sound more conversational. 
  * *Example fix:* "Ziehen Sie vom Rechnungsbetrag alles ab, was Sie erstattet bekommen: den Festzuschuss der Krankenkasse, Leistungen der Zahnzusatzversicherung oder andere Zuschüsse."

### 3. Repetitive Phrasing / Echoing
* **The Pattern:** AI often echoes its own phrasing in adjacent sentences when explaining variables, lacking the human instinct to vary the vocabulary.
* **Flagged Passage:** *"Diese Schwelle liegt **je nach** Fall zwischen 1 und 7 %... **Je nach** Familienstand und Einkommen bewegt sich der Satz zwischen diesen Beispielwerten:"*
* **Recommendation:** Vary the start of the second sentence so it doesn't mirror the first.
  * *Example fix:* Change the second sentence to: "Die genauen Prozentsätze bewegen sich dabei zwischen diesen Beispielwerten:"

### 4. Overly Dramatic/Formal Phrasing (Narrated Weight)
* **The Pattern:** Because AI lacks actual human emphasis, it often uses slightly melodramatic or overly formal idioms to signal that something is important.
* **Flagged Passage:** *"Im Auslandsfall wiegt der Nachweis der Notwendigkeit besonders schwer."*
* **Recommendation:** Tone this down to standard, pragmatic advisory language. 
  * *Example fix:* "Bei Behandlungen im Ausland schaut das Finanzamt beim Nachweis der Notwendigkeit oft genauer hin."

### 5. The "Helpful Pivot" (Forced Link Integration)
* **The Pattern:** When LLMs are instructed to include internal links, they often tack them onto the end of a paragraph with a smooth but highly predictable "If X, then you can also Y" transition. It feels like a sudden sales pitch at the end of an informational paragraph.
* **Flagged Passage:** *"Bleibt danach ein größerer Eigenanteil, lässt er sich bei Bedarf auch [LINK: in Raten finanzieren → /finanzierung/]."*
* **Recommendation:** Integrate the financing mention more organically into the reality of the patient's financial planning, rather than as a tacked-on afterthought.
  * *Example fix:* "Ein verbleibender hoher Eigenanteil muss nicht sofort komplett bezahlt werden – oft bietet sich hierfür eine [LINK: Ratenfinanzierung → /finanzierung/] an."

*(Note: The medical disclaimer and mediation-transparency boilerplate at the end are perfectly fine and standard for YMYL/medical content. They have been left entirely untouched.)*
