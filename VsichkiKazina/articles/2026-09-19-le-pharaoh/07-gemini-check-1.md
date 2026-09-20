# Gemini Step-7 external check — pass 1 (initial draft)

Model: gemini-3.1-pro-preview · Date: 2026-09-19

**Verdict: Shows AI patterns, 75% confidence** → human-likeness = 100 − 75 = **25**

Verbatim verdict + recommendations:

---

**Verdict: Shows AI patterns, 75% confidence**

While this article is highly informative, well-structured, and does an excellent job integrating specific data and compliance language, the connective tissue between the facts relies heavily on recognizable LLM writing tropes. It reads like a heavily prompted AI draft that has been fact-checked and polished by a human, or a human writer who has adopted a highly formulaic SEO style.

### 1. The Robotic Transition (Signposting)
* **The Quote:** *"Ето как работи всичко това на практика."*
* **The Pattern:** LLMs struggle to transition naturally between an introduction and the body text. They almost always use a variation of "Here is a look at...", "Let's dive into...", or "Here is how it works in practice" to announce that the article is beginning.
* **Recommendation:** Delete this sentence entirely.

### 2. Metaphorical Fluff
* **The Quote:** *"Сърцето на основната игра е механиката Sticky Re-drops..."*
* **The Pattern:** AI loves to assign biological or grandiose metaphors to mechanical features ("the heart of," "a testament to," "a symphony of").
* **Recommendation:** Replace the metaphor with direct, confident phrasing (e.g., "Основната механика в базовата игра е...").

### 3. Narrated Emotion / Persona Injection
* **The Quote:** *"За нетърпеливите има и опция Feature Buy..."*
* **The Pattern:** LLMs frequently assign emotional states to players based on the mechanics they use. Calling bonus-buy players "impatient" is a classic trope.
* **Recommendation:** State the fact objectively — that the game includes a Feature Buy option, its cost, its effect on the math — without judging the player.

### 4. Didactic Filler (explaining basic concepts)
* **The Quote:** *"Волатилността показва колко често и колко едро плаща една игра: ниска волатилност значи чести дребни печалби, висока значи дълги сухи периоди с редки големи удари."*
* **The Pattern:** AI pauses to explain basic terminology like a dictionary.
* **Recommendation:** Cut the generic definition; start the paragraph with the specific analysis of THIS game's volatility.

### 5. Formulaic Audience Targeting ("If X, then Y")
* **The Quote:** *"Ако предпочитате плавен баланс и чести дребни връщания, високо-вариативното поведение тук ще ви се стори изнервящо."*
* **The Pattern:** "If you like X, you will love Y" close, plus telling the reader exactly how they will feel.
* **Recommendation:** Describe the game's profile objectively (larger bankroll tolerance due to dry spells) rather than predicting the reader's emotional reaction.

*(Note: The responsible gambling language, disclosures, and RTP math explanations in the latter half are excellent and should remain exactly as they are.)*

---

**Decision:** human-likeness 25 < 80 → apply recommendations via a fresh Humaniser pass (Step 7b), preserving every number/link/RG line/disclosure/date/byline/brand, then re-check. Record baseline HL = 25 for keep-best.
