# 07 — Gemini external check · pass 2 (after Humaniser pass 1)

Model: gemini-3.1-pro-preview · run 2026-09-08 · article: 2026-09-08-keno-pravila
Verdict normalization: "Shows AI patterns, 80% confidence" → **human-likeness = 100 − 80 = 20** (up from initial 15).
Compliant recs to apply in the FINAL Humaniser pass 2: break the "Улучиш три/пет/осемте" rule-of-three and the "и двата…и двата" repetition into flowing prose; fix the calques ("Кено на прости думи" meta → natural; delete "За перспектива"); cut the fluff transition "Голямото попадение е съвсем друг мащаб"; lightly soften the most melodramatic phrasings ("балансът бавно се топи", "това, което боли"). REJECTED: removing "Хазартът не е финансова стратегия" — that is site RG DOCTRINE and an untouchable (brand bible), and the natural-voice RG touch is required; it stays.

## Gemini verbatim verdict + recommendations

Here is my evaluation of the article based on LLM writing patterns and AI text detection.

### **Verdict: Shows AI patterns, 80% confidence**

While the article is highly informative, grammatically flawless, and well-structured, it exhibits several classic hallmarks of AI generation. The text relies heavily on rhetorical parallelism, slightly melodramatic phrasing to force "engagement," direct translations of English AI idioms (Anglicisms), and a highly formulaic, didactic conclusion. It reads like a well-prompted LLM output that hasn't been fully scrubbed of its synthetic stylistic quirks.

*(Note: The [VERIFY] tags, 18+ markers, and responsible gambling disclosures are present and correctly formatted. As per your instructions, I am ignoring these from a stylistic standpoint—they are necessary process/compliance elements and should remain exactly as they are).*

---

### **Flagged Passages and AI Patterns**

**1. Narrated Emotion & Melodrama**
AI models are trained to make dry topics "engaging," which often results in injecting unnecessary emotional weight or dramatic flair into objective subjects.
*   *Quote:* "Онова, което почти никой не ти казва на входа, е цената..." (What almost no one tells you at the entrance is the price...)
*   *Quote:* "...докато балансът бавно се топи." (...while the balance slowly melts away.)
*   *Quote:* "Сравнението с останалите игри в игралната зала е това, което боли." (The comparison with other games on the floor is what hurts.)

**2. Staccato Rhythm & Forced Parallelism**
AI frequently uses repetitive, rhythmic sentence structures to build rhetorical emphasis. While effective in a speech, in an article, it reads like a robotic chant.
*   *Quote:* "Улучиш три, връщаш нула. Улучиш пет, таблицата ти дава някаква сума. Улучиш и осемте, идва големият множител."
*   *Quote:* "Два автомата за кено стоят един до друг, и двата искат €1 за pick-6, и двата уж плащат за същите шест улучени числа."

**3. Anglicisms & Formulaic AI Transitions**
LLMs often think in English and translate into Bulgarian, leaving behind structural idioms that sound slightly unnatural or overly formal in Bulgarian.
*   *Quote (Meta Description):* "Кено на прости думи..." (A direct translation of the classic AI phrase "In simple words/terms").
*   *Quote:* "За перспектива, всяко отделно число има 1 на 80 шанс..." (A direct, clunky translation of the AI transition "For perspective...").
*   *Quote:* "Голямото попадение е съвсем друг мащаб." (Classic AI fluff used to transition between paragraphs without adding actual information).

**4. The Didactic / Preachy Conclusion**
Because of Reinforcement Learning from Human Feedback (RLHF) safety training, AI models almost always end gambling articles with a moralizing, neatly wrapped summary that sounds like a lecture.
*   *Quote:* "Хазартът не е финансова стратегия, а платено забавление, и при кено сметката за това забавление излиза по-солена от почти всичко друго наоколо."

---

### **Concrete Recommendations**

To make this read more like it was written by a human expert, apply the following stylistic adjustments:

*   **Tone down the drama:** Remove the emotional framing. Instead of saying "what hurts is the comparison," simply state that Keno has a significantly higher house edge compared to other casino games. Instead of "the balance slowly melts," describe it objectively as "depleting the bankroll."
*   **Break up the repetitive rhythm:** In the "Как се играе кено" section, combine the "Улучиш X..." sentences into a single, flowing explanation. For example, explain that payouts scale based on hits, from zero return for three numbers up to the jackpot multiplier for all eight. Do the same for the "и двата" repetition in the payouts section.
*   **Fix the Anglicisms:**
    *   Change the meta description from "Кено на прости думи" to something more natural in Bulgarian, like "Кратко ръководство за кено" or "Основи на кено".
    *   Remove "За перспектива". You can just delete this phrase entirely and start the sentence directly with the fact: "Всяко отделно число има..."
    *   Cut the fluff transition "Голямото попадение е съвсем друг мащаб" and just merge the paragraph with the actual statistics.
*   **Soften the conclusion:** The final paragraph is too preachy. Keep the practical advice (checking the paytable, setting limits, playing fewer numbers), but remove the moralizing tone about gambling not being a financial strategy and the bill being "salty." Let the math you presented earlier speak for itself.

## Decision
hl 20 (> initial 15). Apply the compliant subset in FINAL Humaniser pass 2 (cap). KEEP "Хазартът не е финансова стратегия" (RG doctrine/untouchable) — only smooth the "по-солена" flourish delivery. Then re-check; keep the highest-hl version across initial(15)/pass1(20)/pass2.
