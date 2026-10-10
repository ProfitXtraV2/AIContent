# Step 7 — Gemini cross-model check — PASS 1 (initial 05b)

Command: `python3 scripts/gemini_check.py 05b-final-draft.md`
Date: 2026-10-10 (cloud reconcile of HANDOFF row)

## Verdict (verbatim)

→ Normalized HUMAN-LIKENESS = 100 − 85 = **15**  (PASS threshold = 80) — needs changes

---

**Verdict: Shows AI patterns, 85% confidence.**

While this article is highly factual, well-researched, and contains excellent localized Bulgarian context, the structural skeleton and transitional phrasing heavily betray an LLM’s involvement. It reads like a high-quality AI output generated from a very strict, data-rich prompt. The AI reveals itself through classic signposting, forced conversational asides, didactic moralizing, and over-explaining its own limitations. 

*(Note: The inclusion of [VERIFY] and [DATA NEEDED] tags is an excellent editorial process practice. As per your rules, I am ignoring these and the responsible gambling disclosures at the bottom, which should remain exactly as they are).*

Here is the breakdown of the specific AI patterns and how to fix them.

### 1. Pattern: Signposting / Formulaic Roadmap
**The Passage:** *"Тук ще намерите правилата, графика на тиражите, сметката на шансовете и най-честите измами. Няма да намерите „печеливши" позиции, защото такива не съществуват, нито обещания за печалба."*
**Why it flagged:** LLMs almost always use the intro to write a "table of contents" for the article (e.g., "In this article, we will explore X, Y, and Z. We will not..."). Human writers usually just hook the reader and transition straight into the first point.
**Recommendation:** Delete this entire paragraph. The preceding paragraph already perfectly sets up the premise, odds, and price. You don't need to tell the reader what they are about to read; just let them read it.

### 2. Pattern: AI Transparency / Over-explaining Limitations
**The Passage:** *"Как се дели половината между I и II група, публикуваните правила не казват, така че тук цифра няма да има."*
**Why it flagged:** When an LLM cannot find data, it often feels compelled to explicitly narrate its inability to provide it. Human writers typically just state the known facts and move on, rather than drawing attention to what they *aren't* writing.
**Recommendation:** Remove the phrase *"така че тук цифра няма да има."* Simply state: *"Публикуваните правила не уточняват как се дели половината между I и II група."* 

### 3. Pattern: Narrated Emotion & Moralizing
**The Passage:** *"...което звучи успокояващо, докато не си припомните, че 1 на 84 000 пак е шанс, на който никой разумен човек не би разчитал."*
**Why it flagged:** LLMs love to tell the reader how to feel ("звучи успокояващо" / sounds comforting) and frequently insert moral judgments about what a "reasonable person" would do. It shifts the tone from an objective breakdown to a preachy lecture.
**Recommendation:** Keep the mathematical comparison, but strip the emotional narration. Change it to something objective, like: *"Главната печалба на ТОТО 2 – 6/49 е 1 на 13 983 816 (приблизително 166 пъти по-трудна от I група на Джокера), но 1 на 84 000 остава изключително ниска вероятност."*

### 4. Pattern: Quirky / Forced Conversational Aside
**The Passage:** *"Таблиците с „най-често изтеглени" описват миналото (понякога доста красиво) и с това се изчерпват."*
**Why it flagged:** The parenthetical aside *(понякога доста красиво)* is a classic LLM attempt to inject "human voice" or wit into a dry topic. It feels unnatural and disrupts the otherwise analytical tone of the section.
**Recommendation:** Delete the parenthetical *(понякога доста красиво)*. Let the sharp, factual statement stand on its own.

### 5. Pattern: The "In Conclusion" Summary Wrapper
**The Passage:** *"Тото Джокер е проста и евтина добавка към фиша, но по конструкция губеща: на всеки €0,20 връща средно €0,10. Ако я играете, нека е заради тръпката и с пари, които спокойно можете да загубите."*
**Why it flagged:** Even when not using the words "In conclusion," LLMs are programmed to wrap up articles by summarizing the main points (simple, cheap, but losing) and offering a final piece of generalized advice. 
**Recommendation:** You already have excellent, mandatory responsible gambling language in this section and at the bottom of the page. You don't need this AI-generated summary bow. I recommend moving the factual part of this sentence (*"на всеки €0,20 връща средно €0,10"*) up into the "Колко пари се връщат средно?" section, and deleting this final paragraph entirely so the article ends naturally on the hard facts of the law and the official NAP guidelines.
