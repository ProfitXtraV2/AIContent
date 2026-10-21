# 07 — Gemini check, pass 2 (gemini-3.1-pro-preview)

Normalized human-likeness: **85** ("Highly likely human-written or heavily human-edited AI, 85% confidence" → 85). **PASS** (≥ 80).
Keep-best: initial 75 → pass 1 humaniser 85. Highest = current version (pass 1). Kept as final 05b. gemini column: human 85.
Remaining flags below are minor polish only; not applied since target is met and over-editing strips voice (per Step-7 policy).

## Verbatim Gemini verdict + recommendations

**Verdict: Highly likely human-written or heavily human-edited AI (85% confidence).**

This is an exceptionally well-crafted article. If an LLM generated this, it was guided by a masterful, highly specific prompt (likely using Claude 3.5 Sonnet or a custom GPT). It successfully avoids almost all classic AI tells: there is no "В динамичния свят на онлайн казината" (In the dynamic world of...), no robotic "В заключение" (In conclusion), and it uses highly contextual, localized human logic (e.g., explicitly addressing the common Bulgarian player confusion between Novomatic and EGT). The tone is authoritative yet conversational. 

However, there are a few minor structural habits and phrasing choices in the final third of the text that trigger AI detection patterns. Here is what stands out and how to polish it to 100% human parity.

---

### Flagged Passages & AI Patterns

**1. Pattern: The "One Thing is Clear" Trope (Formulaic Emphasis)**
*   **The text:** *"Няколко заглавия държат името на Novomatic живо, а числата им показват едно нещо ясно: това са класики отпреди ерата на рекордните тавани."*
*   **Why it flagged:** LLMs frequently rely on phrases like "one thing is clear," "one thing is certain," or "it is safe to say" to create artificial narrative tension before delivering a straightforward fact. It’s a filler mechanism that pads the sentence without adding meaning.

**2. Pattern: The Generic Localization Signpost (Formulaic Heading)**
*   **The text:** *"Какво значи това за играча в България"*
*   **Why it flagged:** When AI is instructed to localize an international topic (like an Austrian game studio) for a specific market, it almost always generates this exact H2 ("What this means for players in [Country]"). It acts as a blunt, generic signpost rather than a natural, content-driven sub-heading.

**3. Pattern: The Redundant "Wrap-Up" Reflex (Over-summarization)**
*   **The text:** 
    *(End of paragraph 1 in the final section):* *"За вас като играч в България значение има лицензът на самия оператор пред НАП, защото той регулира къде и при какви условия залагате."*
    *(Start of paragraph 2 in the final section):* *"За българския играч решаващото остава едно: лицензът на казиното пред НАП, не лицензът на австрийското студио зад играта."*
*   **Why it flagged:** LLMs have a deeply ingrained habit of summarizing their own points immediately after making them, especially at the end of an article. The second paragraph repeats the exact same thesis as the first paragraph (NAP license vs. Studio license) using slightly different words. Humans rarely repeat their core argument back-to-back like this.

---

### Concrete Recommendations

*   **For Flag 1:** Remove the artificial emphasis. Suggest tightening the sentence to connect the titles directly to their era. You can simply delete "а числата им показват едно нещо ясно:" and bridge the two halves of the sentence directly (e.g., stating that the titles keep the name alive and their numbers reflect an era before record ceilings).
*   **For Flag 2:** Change the H2 to reflect the actual technical information in the paragraph. Instead of the generic "What this means for you," use a heading that mentions B2B vs. B2C licenses, or how NAP regulates the operator rather than the studio. 
*   **For Flag 3:** Eliminate the redundancy by deleting the first sentence of the final paragraph (*"За българския играч решаващото остава едно..."*). The point was already made perfectly in the preceding paragraph. 
    *   *Crucial Note:* When you delete this redundant sentence, ensure you **keep all the responsible gambling language, 18+ markers, and limit-setting advice** that follows it exactly as they are. Just merge the RG advice smoothly into the end of the text.
