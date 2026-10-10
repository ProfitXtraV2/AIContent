# Step 7 — Gemini cross-model check — PASS 2 (after humaniser pass 1)

Command: `python3 scripts/gemini_check.py 05b-final-draft.md`
Date: 2026-10-10 (cloud reconcile of HANDOFF row)

## Verdict (verbatim)

→ Normalized HUMAN-LIKENESS = 100 − 75 = **25**  (PASS threshold = 80) — needs changes

---

Here is my evaluation of the article from the perspective of a senior copywriter specializing in AI text detection.

### **Verdict**
**Shows AI patterns, 75% confidence.** 

While this is a highly disciplined, well-prompted draft (evidenced by the precise legal citations and the survival of `[VERIFY]` tags), the stylistic execution relies heavily on classic LLM writing patterns. It suffers from forced conversational asides, robotic signposting, formulaic internal linking, and a perfectly symmetrical, repetitive FAQ section. It reads like a very good AI draft that needs a human editor to smooth out the synthetic transitions.

*(Note: The `[VERIFY]` tags are clearly artifacts of a structured AI prompt or content brief. As per your instructions, I am ignoring them for the purpose of stylistic editing, but they indicate this is an unfinished draft in your production pipeline).*

---

### **Flagged Passages and AI Patterns**

**1. The "Forced Conversational / Didactic" Pattern**
LLMs often try to inject a "helpful" or "relatable" human voice into dry topics, which usually ends up sounding jarring, preachy, or overly dramatic.
*   *Flagged Text:* „Конкретни продукти законът не посочва (и ние няма да измисляме такива).“
*   *Flagged Text:* „Валутата също издава много.“
*   *Flagged Text:* „Печеливша игра в този списък няма.“
*   *Flagged Text:* „Онлайн сайт, който приема залози в долари или криптовалута, е червен флаг още преди да сте отворили общите условия.“

**2. Robotic Signposting & Formulaic Internal Linking**
AI struggles with natural transitions. Instead of weaving information or links organically into a paragraph, it announces *what* it is about to do or uses a rigid "If you want X, we explain it in Y" formula.
*   *Flagged Text (Signposting):* „Какво точно е „залог", пише в § 1, т. 1 от допълнителните разпоредби на ЗХ...“
*   *Flagged Text (Formulaic Linking):* „Как работи един слот, какво е RTP и защо волатилността има значение за бюджета, обясняваме в раздела Казино игри.“
*   *Flagged Text (Formulaic Linking):* „Правилата на масата разглеждаме отделно в как се играе покер в казино.“

**3. The "Symmetrical Summary" FAQ Pattern**
LLMs generate FAQs by simply summarizing the exact H2s and H3s they just wrote, often repeating the exact same phrasing and citations used earlier in the text. It feels like a machine summarizing its own output rather than answering actual user queries.
*   *Flagged Text:* „Всяка игра на случайността, в която плащате залог и можете да спечелите или да загубите залога (чл. 2, ал. 1 ЗХ).“ *(Direct repetition of the definition in the first H2).*
*   *Flagged Text:* „Лотарийни игри, залагания на спорт и надбягвания с коне и кучета, залагания на случайни събития и на познаване на факти, игри с игрални автомати и игри в игрално казино (чл. 41, ал. 1 ЗХ).“ *(Direct repetition of the H2/Table).*

**4. The "Wrap-Up / Housekeeping" Conclusion**
AI models love to end articles with a neat, sweeping summary that points to other topics, tying a perfect (but unnatural) bow on the text.
*   *Flagged Text:* „Данъчното третиране на печалбите е отделна тема, разгледана в [данъци върху печалбите от онлайн казино], а останалите правни въпроси са в категорията [Регулации и данъци].“

---

### **Concrete Recommendations**

*   **Neutralize the forced conversational tone:** Remove the parenthetical aside „(и ние няма да измисляме такива)“ entirely; it adds nothing but synthetic personality. Change „Валутата също издава много“ to a direct, objective statement about currency regulations. Soften the dramatic „червен флаг“ metaphor to a standard warning about regulatory compliance.
*   **Fix the robotic transitions:** Instead of announcing „Какво точно е „залог", пише в...“, suggest starting the sentence directly with the legal definition (e.g., "According to the supplementary provisions..."). 
*   **Integrate internal links organically:** Break the "we explain X in section Y" formula. Suggest rewriting these sentences so the anchor text is a natural part of the explanation, rather than a signpost pointing to another room.
*   **Vary the FAQ phrasing:** Suggest rewriting the FAQ answers so they sound like plain-language explanations rather than copy-pasting the exact legal citations (чл. 2, ал. 1 ЗХ; чл. 41, ал. 1 ЗХ) that were already heavily established in the main body. The FAQ should translate the article for a layman, not summarize the legal code again.
*   **Cut the housekeeping conclusion:** Suggest removing the final paragraph entirely. The article already ends strongly with the Responsible Gambling section and the FAQ. The final sentence reads like an AI fulfilling a "include these internal links at the end" prompt instruction.
