# Step 7 — Gemini check, pass 1 — rechnik-kazino-termini

Run: 2026-10-28 · model gemini-3.1-pro-preview · file 05b-final-draft.md
Normalized human-likeness = **85** (verdict: Likely human-written, 85%). **PASS** (≥80) on the first check — no humaniser pass needed; initial 05b kept. gemini column = `human 85`.

---
## Gemini verbatim verdict

**Verdict: Likely human-written, 85% confidence.**

This article reads like the work of an experienced human writer who deeply understands the casino niche. It completely lacks the typical AI "fluff" (e.g., "В днешния дигитален свят," "Важно е да се отбележи," "Нека се потопим"). Furthermore, the tone is distinctly human—it is realistic, slightly cynical, and protective of the reader (e.g., "Голяма печалба от малък бонус рядко излиза цяла," "Думата „ексклузивен“ не е сред тях"). 

However, the **rigid structure** of the glossary triggers several AI-generation patterns. LLMs default to highly repetitive, formulaic structures when generating lists or dictionaries, and this text falls into that syntactic trap. 

Here are the specific patterns that flag as AI-generated and how to break them.

---

### 1. Pattern: Formulaic Definitional Openers (The "X is Y" Loop)
When asked to write a glossary, AI almost always starts every single bullet point with the exact same syntactic structure: *[Term] is [Definition]*. In this article, nearly all 45 terms begin with this exact robotic repetition.

**Flagged Passages:**
*   *"Превъртането е броят пъти..."*
*   *"Множителят е числото..."*
*   *"Приносът е процентът..."*
*   *"Началният бонус е предложение..."*
*   *"Бонусът без депозит е малка сума..."*
*   *"RTP е делът..."*
*   *"Предимството на казиното е частта..."*
*   *"RNG е алгоритъмът..."*
*   *(This continues for almost every term in the text).*

**Recommendation:**
Break the "X is Y" loop. You don't need to change all of them, but alter the sentence structure for at least 30-40% of the terms. 
*   Instead of starting with the noun, start with a scenario: *"Когато видиш изискване x30 или x40, това е превъртането – броят пъти..."*
*   Start with an action verb: *"Това е алгоритъмът, който определя..."* (for RNG).
*   Start with a prepositional phrase: *"При клъстерните печалби се плаща за..."* (You actually did this perfectly for "Cluster pays" and "Безкрайни барабани" — apply this variety to the rest of the text).

### 2. Pattern: Staccato Rhythm & Rigid Paragraph Architecture
AI loves a predictable rhythm. In this text, almost every entry follows the exact same architectural blueprint: Sentence 1 (Definition). Sentence 2 (Context/Warning). Sentence 3 (Link to detailed article). While logical, this creates a metronomic, staccato rhythm that AI detectors flag as non-human.

**Flagged Passages:**
*   *"Демо режимът пуска играта с виртуален баланс, без реални пари и без възможност за печалба. Полезен е, за да видиш механиката и ритъма на една игра, преди да заложиш свои средства. Подробно: безплатни казино игри."*
*   *"Барабанът е всяка вертикална колона от символи, която се върти при завъртане. Класическата ротативка има пет барабана, но броят варира според играта и определя колко символа участват в един изход."*

**Recommendation:**
Vary the paragraph lengths and sentence structures. 
*   Combine the definition and the context into a single, flowing complex sentence using conjunctions (тъй като, въпреки че, затова). 
*   Occasionally drop the formal definition entirely and just explain how the mechanic works in practice. 
*   Allow some entries to be three or four sentences long, while keeping others to just one punchy sentence. 

### 3. Pattern: Over-Polished / Symmetrical Contrasts
AI tends to write perfectly balanced, symmetrical sentences when comparing two things. Human writers usually have a slight asymmetry in their comparisons.

**Flagged Passages:**
*   *"Нелепкавият бонус позволява първо да играеш със собствените си пари и ги връща теглими; лепкавият смесва бонуса с баланса и го задържа до изпълнение на условието."*
*   *"Висока волатилност значи дълги сухи серии и редки големи попадения; ниска значи чести дребни печалби."*

**Recommendation:**
Make the contrasts slightly more conversational and less textbook-perfect. For example, in the volatility section, you could break the symmetry by expanding on the emotional or practical impact of one side more than the other, rather than giving them equal word counts separated by a semicolon.

---

### A Note on the Disclosures and Responsible Gambling Text
The sections at the bottom (**За Всички Казина**, **Отговорна игра**, **Разкриване на партньорства**) are clearly boilerplate legal/compliance text. AI detectors often flag these because they are highly formal and repetitive by nature. 

**Recommendation:** Per your hard rules, **do not touch these**. It is perfectly acceptable (and legally necessary) for compliance text to read in a rigid, formal manner. Do not attempt to "humanize" the 18+ warnings or the affiliate disclosures.
