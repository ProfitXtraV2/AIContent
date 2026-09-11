# Gemini Step-7 check 4 — CORRECTED BASELINE (fixer run, --brand dentalvia) — PASS

Re-measurement with the DentalVia step-7 prompt. The original baseline `ai 75` was measured before the brand-aware prompt binding.

Command: `python3 scripts/gemini_check.py 05b-final-draft.md --brand dentalvia`

**Verdict: Likely human-written or heavily human-edited AI, 80% confidence.**
Normalized human-likeness = **80** >= target (80) -> PASS. No Humaniser loop needed; no over-editing of a passing article. 05b-final-draft.md kept as-is.

Gemini's minor polish suggestions (not applied — article already passes, and applying them risks voice on a borderline-noisy detector read): didactic wrap-up, some thematic repetition, a couple of signposting/idiom phrases. Facts/flags/compliance untouched.

---

**Verdict: Likely human-written or heavily human-edited AI (80% confidence).**

This is a very strong, well-structured text. If an LLM generated this, it was guided by an exceptionally tight prompt or heavily edited by a human afterward. It successfully avoids the most notorious German AI vocabulary tells (there is no "Zusammenfassend lässt sich sagen," "In der heutigen schnelllebigen Welt," "darüber hinaus," or "faszinierend"). The sentences are relatively punchy, and the integration of specific legal codes (§ 55 SGB V) and internal link placeholders feels highly deliberate. 

However, there are a few lingering structural patterns—specifically thematic repetition, formulaic signposting, and a didactic wrap-up—that still give off a faint AI-generated echo. 

Here is the breakdown of the specific passages that triggered my AI radar, along with actionable recommendations to polish them out.

---

### 1. The Didactic "Now it's your turn" Wrap-up
**The Pattern:** LLMs struggle to end informational articles naturally. They almost always default to a patronizing, preachy summary command that tells the reader what to do next, often using phrases like "The next step is yours" or "Ultimately...".
**Flagged Text:** 
> "Der nächste Schritt liegt bei Ihnen: Führen Sie Ihr Bonusheft lückenlos weiter und lassen Sie den Heil- und Kostenplan von Ihrer Kasse genehmigen, bevor Sie sich auf eine Versorgung festlegen."

**Recommendation:** 
*   **Delete this sentence entirely.** You don't need it. The article already flows perfectly into the "Kostenlose Beratung" CTA block. Ending the editorial portion on the strong, factual note about the health insurance fund making the final decision ("Über die Höhe entscheidet auch hier allein Ihre Krankenkasse.") is much more professional and authoritative than giving the reader a generic homework assignment.

### 2. Thematic Repetition (Over-explaining the core premise)
**The Pattern:** LLMs lack object permanence in their narrative flow. When given a core directive (e.g., "Explain that the subsidy stays the same but the patient pays the difference"), the AI will restate this exact premise in almost every single section to ensure it has "answered the prompt." 
**Flagged Text:**
*   *In the Intro:* "Wer sich für eine aufwendigere Versorgung entscheidet, bekommt deswegen keinen Cent mehr und trägt den Aufpreis selbst."
*   *In Section 1:* "Wählen Sie etwas Aufwendigeres als die Regelversorgung, überweist die Kasse trotzdem nur den befundbezogenen Festzuschuss. Alles, was darüber liegt, zahlen Sie als Eigenanteil selbst."
*   *In Section 5:* "Am Zuschuss ändert das nichts, er bleibt bei 398 €... Wird die Behandlung günstiger, sinkt Ihr Eigenanteil im gleichen Maß, während der Zuschuss unangetastet bleibt."

**Recommendation:**
*   **Trim the redundancy.** The reader understands the concept after the first explanation. 
*   I recommend removing the final sentence of the intro ("Wer sich für eine aufwendigere Versorgung entscheidet..."). Let the intro tease the topic, and let Section 1 deliver the detailed explanation. 
*   In Section 5, you can keep the math example, but you don't need to re-explain the philosophy of the subsidy remaining untouched ("während der Zuschuss unangetastet bleibt"), as it feels repetitive by this point.

### 3. Formulaic Signposting & Setup Phrases
**The Pattern:** AI uses highly mechanical, slightly unnatural transition sentences to introduce math, lists, or examples. It reads like a textbook rather than an expert writing a blog post.
**Flagged Text:** 
> "Was Sie selbst tragen, folgt einer einzigen Rechnung: die [LINK: Gesamtkosten der gewählten Versorgung → /kosten/] minus Festzuschuss ergeben Ihren Eigenanteil."

**Recommendation:**
*   **Soften the transition.** The phrase "folgt einer einzigen Rechnung:" feels robotic. Suggest changing it to a more conversational human flow, such as: "Ihr Eigenanteil berechnet sich ganz einfach: Die [LINK...] minus Festzuschuss."

**Flagged Text:**
> "Die folgenden Beispielwerte (Stand 2026) machen die Größenordnung greifbar; verbindlich ist immer der Betrag, den Ihre Kasse für Ihren konkreten Befund festsetzt."

**Recommendation:**
*   **Simplify the table intro.** "Machen die Größenordnung greifbar" is a very common German LLM idiom. Suggest a more direct lead-in, such as: "Die folgenden Beispielwerte (Stand 2026) dienen zur ersten Orientierung. Verbindlich bleibt jedoch immer der Betrag..."

### 4. The "Egal" Absolute
**The Pattern:** AI loves to use absolute framing to emphasize rules, often resulting in slightly clunky phrasing.
**Flagged Text:**
> "Sobald Ihr Befund feststeht, ist auch die Höhe des Zuschusses fixiert, egal für welche Versorgung Sie sich danach entscheiden."

**Recommendation:**
*   **Elevate the vocabulary.** "Egal für welche" is a bit colloquial compared to the rest of the text. Suggest changing it to "unabhängig davon, für welche Versorgung Sie sich danach entscheiden."

---

**A Note on Hard Rules & Process:**
*   The medical disclaimer and the mediation-transparency line are perfectly placed and must remain exactly as they are.
*   The `[VERIFY]` tags are excellent workflow markers. As a process note: ensure a human subject-matter expert clears these tags and confirms the 2026 percentages/amounts before final publication, but structurally, leaving them in the draft at this stage is the correct approach.
