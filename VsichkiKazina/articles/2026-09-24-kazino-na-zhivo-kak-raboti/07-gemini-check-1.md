# Gemini Step-7 external check — pass 1 (initial draft)

Command: `python3 scripts/gemini_check.py 05b-final-draft.md`

**Verdict: Shows AI patterns, 85% confidence.** → human-likeness = 100 − 85 = **15**

While the text is highly informative, grammatically flawless, and does an excellent job integrating responsible gambling concepts, its underlying skeleton is heavily reliant on classic Large Language Model (LLM) expository frameworks. It suffers from "hand-holding"—telling the reader what it is about to do, explaining the premise of a paragraph before giving the facts, and summarizing the paragraph immediately after.

### 1. The "Roadmap" Intro (Signposting)
**The Passage:** *"По-долу разглеждаме какво се случва зад стрийма: камерите, устройството на масата, софтуера, който разчита картите, и какво прави рунда проверяем."*
**The Pattern:** AI almost always ends an introduction by giving the reader a literal table of contents for the rest of the article.
**The Recommendation:** Delete this sentence entirely. The paragraph ends perfectly on the previous sentence about the budget.

### 2. Tautological Filler / Robotic Premise-Setting
**The Passage:** *"Един рунд върви по един и същ път всеки път."*
**The Recommendation:** Cut this opening sentence. Start the paragraph directly with the action: *"Свързваш се към стрийма на избраната маса..."*

### 3. The "Neat Bow" (Didactic Paragraph Summaries)
**The Passages:**
*   *"Смисълът на всичко това е да виждаш ясно всяко движение, за да няма съмнение какво се е случило на масата."*
*   *"GCU-то е връзката между физическата маса и софтуера, който води сметката на залозите."*
**The Recommendation:** Delete both of these summarizing sentences.

### 4. Meta-Commentary on Scope
**The Passage:** *"За самите game shows има отделно ръководство при live game shows водачите; тук се спираме само на механиката, обща за всички маси."*
**The Recommendation:** Keep the link to the game shows guide, but delete the meta-commentary (*"тук се спираме само на механиката, обща за всички маси"*).

### 5. The "Philosophical/Balanced" Conclusion
**The Passage:** *"Технологията на живо е впечатляваща и това прави лесно да забравиш, че гледаш добре режисирано забавление с вградена цена."*
**The Recommendation:** Remove this opening sentence. Start the paragraph directly with the practical reality. (Do NOT alter any of the 18+ or responsible gambling language that follows.)

**Summary for the Editor:** The facts, terminology, and responsible gambling integrations are excellent. To humanize the piece, execute a "trimming" pass. Remove the sentences where the author is explaining *how* they are writing the article (signposting) or summarizing what they *just* wrote (the neat bows).

---
Decision: human-likeness 15 < 80 → apply step-7b Humaniser pass 1 (surgical trims per recs; preserve every untouchable: numbers, links, RG lines, 18+, disclosures, dates, byline, brand). Keep-best tracked.
