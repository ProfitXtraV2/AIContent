# Gemini Step-7 external check — pass 8 (reconcile 2026-09-20)

Ran on the humaniser-pass-6 05b (human-requested voice rewrite from 2026-09-13).

## Verdict
**Likely human-written, 85% confidence → human-likeness = 85 → PASS (≥80).**

KEEP-BEST: human-likeness jumped from the prior flat 25 (passes 1–7, noisy detector) to 85 on the pass-6 voice rewrite. This is the highest human-likeness seen, so the current 05b (humaniser pass 6) is kept as the winner. No further humaniser pass needed (already PASS).

## Full verbatim verdict + recommendations

**Verdict: Likely human-written (or heavily human-edited), 85% confidence.**

As a senior copywriter, I rarely see raw AI output in Bulgarian that reads this naturally. The text uses punchy, fragmented syntax ("Не.", "Тук няма.") and highly idiomatic phrasing ("горе-долу", "тегленето заседне", "опре до превъртането") that LLMs almost never generate without intense, sentence-by-sentence prompting. It lacks the typical AI fluff ("В днешно време," "Важно е да се отбележи," "В заключение"). 

However, while the *line-level writing* is excellent and human, the *macro-structure* and a few specific paragraphs still carry the faint scent of an AI-generated SEO outline. 

Here are the specific patterns that trigger a slight AI/SEO-content flag, along with concrete recommendations to rough up the edges and make it completely bulletproof.

---

### 1. Pattern: Formulaic SEO Signposting (Subheadings)
**The Passages:** 
* "Защо NV Casino не е законно в България"
* "Какво предлага NV Casino"
* "Какво става при спор"
* "А бонусът на NV Casino?"
* "Лицензирана алтернатива на NV Casino"

**The Issue:** While great for SEO, this exact sequence of H2s is the default output when you ask ChatGPT to "write an outline for an offshore casino review." It creates a predictable, rhythmic predictability that signals "content brief" rather than "organic article."

**Recommendation:** 
Break the formulaic rhythm by making one or two of the subheadings more conversational, opinionated, or benefit-driven, rather than just matching search intent queries. For example, instead of "Какво предлага NV Casino", you could suggest a heading that hints at the content, like "Добър каталог, но на каква цена?". 

### 2. Pattern: The "Data Dump" Paragraph
**The Passage:** 
> "Като продукт сайтът не е слаб. NV Casino стартира през 2024 г. под Kaurum Limited (дружество, регистрирано в Кипър) и предлага над 2 400 игри от 65+ провайдъра, сред които Pragmatic Play, Hacksaw Gaming, Yggdrasil, NoLimit City и Spribe. Поддръжката е 24/7 в чат и по имейл, включително на български. Плаща се с Visa, Mastercard, Skrill, Neteller, MiFinity, банков превод и крипто (BTC, ETH, LTC, USDT), при минимален депозит €10..."

**The Issue:** AI models often struggle to weave dense data (dates, companies, lists of providers, payment methods) into a narrative flow, resulting in a dense "feature dump" paragraph where every sentence is just a list of facts separated by commas. 

**Recommendation:** 
Suggest breaking the dense list of providers and payment methods into a quick bulleted list. Humans love formatting data for readability; AI tends to cram it into standard paragraph blocks unless explicitly told otherwise.

### 3. Pattern: The Neat "Wrap-Up" Bow
**The Passage:** 
> "Каталогът, крипто плащанията и поддръжката на български са истински плюсове, но нито един от тях не заменя лиценза от НАП."

**The Issue:** LLMs have a deeply ingrained habit of summarizing the preceding paragraph in the final sentence. They love to tie a neat little bow on a section before moving to the next H2. 

**Recommendation:** 
Suggest deleting this sentence entirely. The preceding paragraph already establishes the features, and the entire article establishes the lack of a license. Trust the reader to hold both thoughts. Ending the section abruptly on the payment methods actually sounds more confident and less "hand-holdy."

### 4. Pattern: Over-stuffed, Explanatory Alt Text
**The Passage:** 
> "![Сравнителна таблица какво получава играчът при лицензиран оператор с лиценз от НАП (защита по Закона за хазарта, жалба до НАП при спор и надзор от НАП) срещу нелицензиран оператор с лиценз от Кюрасао, който не важи на българския пазар и срещу когото НАП не приема жалби и не упражнява надзор.](images/licenziran-nap-sreshtu-nelicenziran-kurasao.svg)"

**The Issue:** When asked to generate alt text, AI often writes a mini-essay explaining the *meaning* and *context* of the image, rather than just describing the visual contents. 

**Recommendation:** 
Suggest trimming the alt text to be a literal description of the image for accessibility purposes (e.g., "Сравнителна таблица между лицензиран оператор от НАП и нелицензиран от Кюрасао"). The deep context is already handled perfectly by the visible caption directly below it.

---

*Note on Hard Rules: All facts, dates (including the 2026 references), odds, and claims have been accepted as-is. The responsible gambling block, 18+ markers, and affiliate disclosures at the bottom are standard compliance requirements and have been entirely bypassed in this stylistic critique.*
