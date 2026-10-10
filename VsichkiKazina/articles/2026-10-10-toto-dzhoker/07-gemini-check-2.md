# Step 7 — Gemini cross-model check — PASS 2 (after humaniser pass 1)

Command: `python3 scripts/gemini_check.py 05b-final-draft.md`
Date: 2026-10-10 (cloud reconcile of HANDOFF row)

## Verdict (verbatim)

→ Normalized HUMAN-LIKENESS = **90**  (PASS threshold = 80) — PASS

---

**Verdict: Likely human-written (or heavily human-edited), 90% confidence.**

This article reads overwhelmingly like the work of a human subject-matter expert or a highly skilled SEO writer. It lacks the usual LLM fluff ("в днешния забързан свят," "нека се потопим," "от решаващо значение"). Furthermore, the mathematical breakdown—specifically the line *"Този втори път лесно се изпуска при пресмятане"* (This second path is easily missed in calculations)—is a massive human "tell." LLMs rarely correct common human combinatorial oversights unprompted; they usually just hallucinate the math or give a generic summary. The use of colloquialisms like *"не мърда"* and *"горе-долу"* also strongly points to a human author. 

However, because standard SEO formatting often mirrors AI outputs, there are a few structural patterns that might trigger an AI detector or feel slightly formulaic to a discerning reader. 

Here are the specific passages that exhibit minor AI-like patterns, along with actionable recommendations to smooth them out.

### Flagged Passages, Patterns, and Recommendations

**1. Pattern: The Blunt Q&A Opening (Signposting)**
*   **Flagged Text:** 
    > "### Има ли Тото Джокер към 6 от 49?
    > Да. Джокерът си остава добавка към фиша..."
*   **Why it feels AI:** LLMs frequently answer question-based subheadings with a standalone, blunt "Yes." or "No." before launching into the explanation. It creates a slightly robotic, staccato rhythm.
*   **Recommendation:** Remove the standalone "Да." and weave the affirmative directly into the first sentence. (e.g., Start directly with a phrase indicating that the Joker can indeed be added to a 6/49 ticket, while remaining an add-on).

**2. Pattern: ChatGPT-Style Bold Run-in Headers**
*   **Flagged Text:** 
    > "**Платени „системи“ и „печеливши позиции“.** Печеливши позиции не съществуват..."
    > "**„Спечелихте, платете такса.“** Идва съобщение за печалба..."
    > "**Фалшиви сайтове.** Играйте само през официалните канали..."
    > "**Квитанцията.** Пазете я, защото тя е доказателството..."
*   **Why it feels AI:** The `**Concept.** Explanation` format is ChatGPT’s default way of structuring almost any list or breakdown. When stacked back-to-back in a section, it creates a highly recognizable visual and rhythmic AI footprint.
*   **Recommendation:** Break this formula. You can convert these into standard bullet points without the bolded periods, or better yet, turn them into narrative paragraphs with standard H3 subheadings. For the "Квитанцията" point, since it's just one sentence, consider merging it into the introductory or concluding paragraph of that section rather than leaving it as a standalone bolded item.

**3. Pattern: Abrupt List Transition (Formulaic Structure)**
*   **Flagged Text:** 
    > "## Как се играе Тото Джокер?
    > Джокерът се добавя само върху фиш за ТОТО 1 или ТОТО 2. „ТОТО 2 – Рожден ден“ е единственото изключение.
    > 1. Над фабричния номер на фиша има поле..."
*   **Why it feels AI:** AI often jumps straight from a high-level fact into a numbered instructional list without a transitional sentence to guide the reader into the steps. 
*   **Recommendation:** Add a brief, conversational lead-in sentence right before "1. Над фабричния номер..." to bridge the gap between the general rule and the step-by-step instructions (e.g., a sentence introducing the physical steps of filling out the slip).

**4. Pattern: Slightly Stilted/Literal Phrasing**
*   **Flagged Text:** 
    > "**Каквато и да е печалба.** I и II група заедно: 13/5250, около 1 на 404."
*   **Why it feels AI:** "Каквато и да е печалба" reads a bit like a literal, slightly clunky translation of the English phrase "Any win" or "Overall odds of winning." While grammatically correct, it lacks the natural flow of the rest of the Bulgarian text.
*   **Recommendation:** Change the bolded phrase to a more natural Bulgarian gambling/statistical term for overall odds (e.g., phrasing it as "Шанс за каквато и да е печалба" or "Общ шанс за печалба").

---

*Note on Hard Rules: As requested, I have not altered or suggested altering any facts, odds, or dates. The [VERIFY] and [DATA NEEDED] tags, as well as all responsible gambling language, 18+ markers, and legal disclaimers, have been noted and left completely untouched. Their presence is actually a strong indicator of a rigorous human editorial process.*
