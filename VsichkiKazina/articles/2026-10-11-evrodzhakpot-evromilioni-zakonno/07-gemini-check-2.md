# 07 — Gemini External Check · Pass 2 (gemini-3.1-pro-preview, 2026-10-11)

Normalized human-likeness: **85** (verdict: „Likely human-written (or heavily human-edited), 85% confidence").
>= GEMINI_TARGET_CONFIDENCE (80) -> **PASS** in 1 humaniser pass.
KEEP-BEST: initial HL 25 -> pass 1 HL 85. Highest = pass 1 (current 05b). Remaining Gemini suggestions are optional polish; not applied (keep-best protects the 85).
gemini column: human 85.

## Gemini verbatim verdict + recommendations

Here is my evaluation of the article from the perspective of a senior copywriter and AI-text detection specialist.

### **Verdict: Likely human-written (or heavily human-edited), 85% confidence.**
This text is exceptionally strong. It contains highly idiomatic, natural Bulgarian phrasing that LLMs (even GPT-4) almost never generate organically—such as *"оставате със сканче"* (you're left with a little scan), *"тънка основа да държи парите ви"* (a thin foundation to hold your money), and *"няма откъде да купите законно у нас. Отвътре все пак се играе, разбира се."* 

However, while the *vocabulary* and *voice* are distinctly human, the **macro-structure and pacing** exhibit several classic AI/SEO content-generation patterns. AI detectors often flag texts not just for vocabulary, but for predictable structural rhythms, formulaic transitions, and rigid outlining. 

Here are the specific patterns that trigger AI-detection algorithms, along with actionable recommendations to smooth them out.

---

### **Flagged Passages, Patterns, and Recommendations**

#### **1. Pattern: The "SEO Outline" (Formulaic Subheadings)**
* **Flagged Text:** 
  * *„Какво представляват двете игри“*
  * *„Защо България я няма в списъка“*
  * *„Какво рискувате реално“*
  * *„Чистият ход“*
* **The Issue:** AI models are trained to structure informational articles using a very predictable, linear sequence of generic questions (What is it? -> Why is it like this? -> What are the risks? -> Conclusion). While good for basic SEO, this rigid "question-and-answer" skeleton is a primary trigger for AI detectors. "Чистият ход" acts as a classic AI "In Conclusion" wrapper.
* **Recommendation:** Soften the subheadings so they feel like a continuous narrative rather than a high school essay outline. Instead of asking generic questions, use statement-driven subheadings that hint at the section's specific conclusion. For example, instead of *"Какво рискувате реално"*, you could suggest a heading that directly mentions the lack of a safety net. 

#### **2. Pattern: Staccato Rhythm / Robotic Data Delivery**
* **Flagged Text:** *"Продажбите тръгват на 17.03.2012 г., първият тираж е на 23.03.2012 г. Вторият седмичен тираж във вторник идва чак през март 2022 г., заедно с вдигнатия таван на джакпота, от €90 000 000 на €120 000 000. Самите билети се оценяват в Германия и Дания."*
* **The Issue:** This is the "Wikipedia effect." When AI is fed a list of facts (or asked to summarize history), it tends to spit them out in sentences of identical length and structure, creating a robotic, staccato rhythm. Subject-verb-date, subject-verb-date.
* **Recommendation:** Vary the sentence lengths and combine the historical data points using transitional conjunctions. You can weave the dates into a more fluid narrative sentence so it doesn't read like a bulleted list forced into paragraph form.

#### **3. Pattern: Repetitive Signposting (Forced Internal Linking)**
* **Flagged Text:** 
  * *„...сме писали в раздела за регулации и данъци.“*
  * *„Какво значи „законно“ в тази ситуация, сме разгледали в хъба за легалност.“*
  * *„Как се проверява дали оператор изобщо е вписан, показваме в проверката на лиценз.“*
  * *„Данъчната страна на онлайн печалбите сме я гледали отделно в ръководството за данъци.“*
* **The Issue:** AI instructed to include internal links almost always uses this exact self-referential formula: *"We have discussed [Topic] in our [Link]."* Doing this four times in one short article is a massive red flag for AI-generated SEO content.
* **Recommendation:** Use contextual linking. Suggest integrating the hyperlinks naturally into the flow of the text without explicitly announcing to the reader that "we wrote an article about this." Let the highlighted anchor text do the work.

#### **4. Pattern: The "Moralizing Wrap-Up"**
* **Flagged Text:** *"Така или иначе това си остава лотария, развлечение с предварителен бюджет, не план за доходи."*
* **The Issue:** AI models are heavily aligned to end articles—especially those touching on finance, health, or gambling—with a summarizing, slightly preachy moral takeaway. 
* **Recommendation:** The sentiment here is excellent and aligns perfectly with responsible gambling guidelines (which must stay). However, to make it read less like a ChatGPT sign-off, suggest merging this final thought directly into the preceding paragraph about the state lottery, rather than isolating it under its own concluding subheading (*„Чистият ход“*). 

---

### **A Note on Process Markers (Do Not Touch)**
The inclusion of `[VERIFY: ...]` tags, the Markdown table, the `<!-- HERO HERE -->` placeholders, and the extensive **Отговорна игра** / **Разкриване** sections at the bottom are excellent. These indicate a rigorous editorial and compliance process. As per your hard rules, these have been completely ignored in the critique and should remain exactly as they are.

[exited with code 0]
