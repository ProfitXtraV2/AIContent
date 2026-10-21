# Gemini Step-7 external check — pass 1 (2026-10-02)

## Normalized score
"Shows AI patterns, 75%" -> human-likeness = **25** -> below 80, iterate.

## Full verbatim verdict + recommendations

**Verdict: Shows AI patterns, 75% confidence.**

While this article is highly informative, factually dense, and avoids the most egregious AI clichés (like "In today's digital world" or "Let's dive in"), its underlying skeleton is distinctly machine-generated. It reads like a very well-prompted output from a top-tier LLM (likely Claude 3.5 Sonnet or GPT-4) that has been fact-checked but not structurally edited. The primary tells are the heavy use of signposting, perfectly symmetrical aphorisms, didactic framing, and "breathless" run-on sentences where the AI tries to pack all contextual caveats into a single thought.

Here is the breakdown of the specific patterns and how to fix them.

---

### 1. The "Breathless" Run-On Sentence (Over-packing)
LLMs are terrified of stating a fact without immediately attaching its caveat, leading to massive, multi-clause sentences glued together by colons, semicolons, and conjunctions. 

* **Flagged Passage:** *"То важи само при перфектна игра: блекджек стига до около 0,5% единствено ако следваш основната стратегия ръка по ръка, а видеопокерът дава под 1% само на пълна таблица и с безгрешни решения, тъй че щом играеш по интуиция, реалното предимство срещу теб е в пъти по-голямо от красивото число в таблицата."* (49 words, 4 distinct clauses).
* **Flagged Passage:** *"И дори перфектните 0,5% са разход, който плащаш: RTP е статистика върху милиони залози, не обещание за твоята вечер, така че една добра серия не отменя предимството, а един лош час не значи, че играта е „студена"."*
* **Recommendation:** Chop these up. Humans write with varied sentence lengths; AI writes in paragraphs of uniform, heavy blocks. Replace the colons and conjunctions (като "а", "тъй че", "така че") with hard periods. Let the facts breathe in separate sentences. 

### 2. Signposting & Meta-Discourse
AI loves to act as a tour guide, constantly telling the reader what it is currently doing, what it is not doing, and what it will do next. 

* **Flagged Passage:** *"Как се чете точното RTP на една-единствена ротативка, заедно с волатилността ѝ, е отделна тема със свое ръководство. Тук гледаме сравнението между самите игри, не разчитането на числото за една от тях."*
* **Flagged Passage:** *"За подреждането по шансове тук стига да помниш, че..."*
* **Recommendation:** Delete the meta-commentary entirely. You don't need to tell the reader that you aren't talking about slot RTP right now—just don't talk about it. If you must link to the other guide, do it naturally in the text without the "Here we are looking at X, not Y" framing.

### 3. Symmetrical Aphorisms (The "Proverb" Pattern)
LLMs love to create perfectly balanced, symmetrical contrasts to sound authoritative and profound. It makes the text feel overly polished and slightly robotic.

* **Flagged Passage:** *"Едното казва колко губиш средно, другото колко ти се връща, но сочат към един и същ факт."*
* **Flagged Passage:** *"Домашното предимство ти казва колко струва играта на дълго; волатилността казва по какъв път ще минеш дотам."*
* **Recommendation:** Break the perfect symmetry. Make the phrasing slightly more conversational and asymmetrical. For example, instead of the second flagged passage, you could suggest something simpler: "Домашното предимство определя дългосрочната цена. Волатилността просто показва колко бързо или бавно ще стигнеш дотам."

### 4. Didactic / Cautionary Framing (The "AI Lecture")
AI models are programmed to be highly cautious, which often results in a preachy, lecturing tone—especially in the topic sentences of paragraphs.

* **Flagged Passage:** *"Ниското число мами по два начина."* (Classic AI hook).
* **Flagged Passage:** *"Ето типичните стойности при коректна игра. Приеми ги като ориентир, не като гаранция..."* (Classic AI disclaimer).
* **Flagged Passage:** *"И най-ниското предимство обаче си остава цена за забавлението."* (Classic AI moral-of-the-story wrap-up).
* **Recommendation:** Soften the dramatic hooks. Change "Ниското число мами по два начина" to a more neutral statement about how low house edges require perfect execution. Remove the "Приеми ги като ориентир, не като гаранция" disclaimer—the text already explains that rules vary, so the disclaimer is redundant AI padding.

---

*Note: The responsible gambling language, 18+ markers, author bio, and affiliate disclosures at the bottom of the text are perfectly placed and formatted. I have not touched or recommended any changes to these elements, as they are essential compliance requirements.*
