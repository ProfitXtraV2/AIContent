# 07-GEMINI-CHECK — pass 3 (after humaniser pass 2) — chargeback-kazino
# Model: gemini-3.1-pro-preview · run 2026-10-01 (3rd fire)
# Normalized human-likeness = 100 − 85 = 15 (Shows AI patterns, 85%). DOWN from 25.
# Remaining recs now target brand-REQUIRED elements (first-person Георги-Тодоров persona voice; the mandatory in-body RG touch) — applying them would FAIL the Brand Gate, and Gemini is style-only/recommendations-only (never overrides persona/RG). Detector is the documented noisy whack-a-mole: goalposts relocate each pass.
# MAX_GEMINI_PASSES (2) reached. KEEP-BEST = humaniser pass 1 (HL 25). Reverting 05b to that version; gemini column = 'ai 75'.

## Gemini verbatim verdict + recommendations

**Verdict: Shows AI patterns, 85% confidence**

While the article is highly informative, grammatically flawless, and well-structured, it exhibits several classic hallmarks of an LLM instructed to write a "helpful, expert blog post." The primary giveaways are the bolted-on first-person statements used to simulate a human persona, the slightly preachy/didactic tone in the explanatory paragraphs, and the highly formulaic transitions. 

Here is the breakdown of the specific patterns and how to fix them.

### 1. Artificial Persona / Bolted-on First Person
AI models prompted to write from a first-person perspective often struggle to weave the "I" naturally into the narrative. Instead, they write a standard, objective encyclopedia-style paragraph and tack a first-person statement onto the very end or beginning to check the "personal experience" box.

* **Flagged Passage 1:** *"От тази разлика зависи дали изобщо имаш случай, затова започвам с нея."* (Intro)
* **Flagged Passage 2:** *"Дали едно казино изобщо е законно у нас проверявам в страницата за законността."* (Section: Защо лицензът от НАП е истинската разлика)
* **Flagged Passage 3:** *"...как изглежда този път съм описал в раздела за жалби."* (Section: Какво да направиш вместо това)
* **Flagged Passage 4:** *"...съм разписал в прегледа на методите за плащане и в раздела за депозити и теглене."* (Section: Какво да направиш вместо това)
* **Recommendation:** Remove the forced "I" statements. Instead of saying "I start with this" or "I have described this in," transition naturally by focusing on the reader's needs. For example, recommend that the *reader* checks the legality page, or simply state that the step-by-step complaint process can be found in the linked guide. 

### 2. Didactic / Moralizing Wrap-ups
LLMs are programmed to be helpful and safe, which often results in them ending factual paragraphs with a moral lesson, a warning, or a behavioral lecture. 

* **Flagged Passage:** *"Затова бюджетът за игра са пари за развлечение, които можеш да загубиш изцяло, а лимитите за депозит и загуба се задават преди първия депозит, не се спасяват със спор после."* (Section: Кога chargeback няма да ти помогне)
* **Recommendation:** This sentence shifts the tone from a financial/legal explanation of banking rules to a lecture on personal responsibility. To sound more human and less like an AI safety filter, remove the lecture about setting limits. Keep the focus strictly on the fact that banks do not view buyer's remorse or gambling losses as valid grounds for a chargeback. *(Note: Do not touch the actual Responsible Gambling disclosures at the bottom of the article; this recommendation applies only to the body copy).*

### 3. Formulaic Signposting & List Introductions
AI relies heavily on predictable structural markers to introduce lists or transition between thoughts. It creates a rhythm that feels slightly robotic.

* **Flagged Passage:** *"Няколко ясни случая:"* (Section: Кога оспорването е основателно)
* **Recommendation:** Soften the transition into the bullet points. Instead of a staccato announcement, blend the introduction into the preceding sentence (e.g., explaining that a chargeback is justified specifically when...).

### 4. Over-Summarized / Prompt-like Alt Text
When AI generates image alt text, it often writes a dense summary of the entire section or outputs something that reads exactly like an image-generation prompt, rather than describing the visual contents of the image.

* **Flagged Passage:** *"![Инфографика: кога картовият chargeback при онлайн казино е основателен (неоторизирана транзакция, неполучен депозит, двойно таксуване) и кога не е (доброволна загуба, разкаяние, неразбрани условия), със срока от 60 до 120 дни и бележката, че при лицензиран оператор защитата минава през НАП, а не през картовия спор]"*
* **Recommendation:** Edit the alt text to be a concise description of the image's visual layout for accessibility purposes, rather than a stuffed, keyword-heavy summary of the article's entire thesis. 

***

**A Note on Compliance & Disclosures:**
The responsible gambling warnings, 18+ markers, author bio, and affiliate/licensing disclosures at the bottom of the text are excellent. They are legally necessary and properly formatted. **Do not alter, remove, or edit any of the text from "18+ Хазартът може да пристрасти..." down to the end of the document.**
