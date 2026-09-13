# Step 7 — Gemini check, pass 3 (after Humaniser pass 2)

Model: gemini-3.1-pro-preview
Normalized: **"Shows AI patterns, 85% confidence"** → human-likeness = **100 − 85 = 15** → still 15.

## Decision — KEEP BEST
MAX_GEMINI_PASSES (2) reached. Human-likeness by version:
- initial 05b draft: **15** ("Shows AI patterns, 85%")
- after Humaniser pass 1: **15** ("Shows strong AI patterns, 85%")
- after Humaniser pass 2: **15** ("Shows AI patterns, 85%")

The detector returns a flat 85%-AI verdict on every read while each pass moves the goalposts to entirely new flagged passages (pass 1 → pass 2 → pass 3 name different sentences each time), and it explicitly praises the article's substance, RG/18+ boilerplate, affiliate disclosure and the surviving [VERIFY]/[DATA NEEDED] tags. This is the documented high-variance / whack-a-mole behavior of the Gemini heuristic seen across this queue (e.g. vk-0008, vk-0015, vk-0018); further edits chase a noisy score and risk stripping voice.

**Kept: Humaniser pass-2 version** (current 05b-final-draft.md). All three versions score 15 — pass 2 is not lower-scoring than any prior version, and its prose is the most flattened (metaphors, em-dash contrasts, semicolon-balanced clauses and grandiose absolutes all reduced), so it is retained per KEEP-BEST. Final human-likeness logged for the human: **15** (below the 80 target; noisy detector, do not loop further).

All numbers, links, [VERIFY]/[DATA NEEDED] flags, RG/18+ lines, the affiliate disclosure, byline (Георги Тодоров) and brand (Всички Казина) preserved verbatim across both humaniser passes. Flags remain the human's to resolve.

---

**Verdict: Shows AI patterns, 85% confidence.**

While this article is highly informative, grammatically flawless, and clearly part of a rigorous editorial process (evidenced by the excellent use of `[VERIFY]` and `[DATA NEEDED]` tags), the prose itself relies heavily on classic Large Language Model (LLM) structural tropes. It suffers from "hand-holding" transitions, forced neutrality, and formulaic summarization. It reads like a very well-prompted GPT-4 or Claude 3 draft that hasn't yet had its robotic scaffolding dismantled.

Here is the breakdown of the specific AI patterns detected and how to fix them.

---

### Flagged Passages & AI Patterns

**1. The "Mind-Reading / User Journey" Intro**
> *Quote:* "Ако сте търсили „NV Casino законно ли е", вероятно вече сте попаднали на десетки страници, представени като „официален партньор 2026", които подминават правния статус напълно; тук той е самата тема."
*   **Pattern:** *Narrated Empathy / Search Intent Echoing.* AI frequently tries to build rapport by explicitly narrating the user's presumed search journey or frustrations. It feels overly conversational in a way that human journalists rarely write.

**2. The "To Be Fair" Pivot & Micro-Summary**
> *Quote:* "Продуктът сам по себе си не е слаб. [...] Въпреки добрите характеристики, липсата на лиценз от НАП остава основният проблем; нищо от изброеното не я заменя."
*   **Pattern:** *Forced Nuance & Paragraph Bow-Tying.* AI struggles to be purely critical. It almost always inserts a "balanced" perspective ("Продуктът сам по себе си не е слаб"), lists the features, and then uses a formulaic concluding sentence to remind the reader of the main thesis. It treats every paragraph like a mini-essay that needs its own conclusion.

**3. Didactic / Philosophical Truisms**
> *Quote:* "Този разход не пише никъде в офертата и изглежда нулев, докато няма проблем. Появява се тогава, когато трябва да поискате парите си обратно."
*   **Pattern:** *Preachy Hypotheticals.* When explaining risks, AI tends to slip into a slightly dramatic, philosophical tone, explaining obvious concepts as if revealing a profound truth. 

**4. "If X, Then Y" Signposting**
> *Quote:* "Ако желанието е същото (голям каталог игри и удобни плащания), разумният избор е оператор, вписан в регистъра на НАП."
*   **Pattern:** *Conditional Logic Transitions.* AI relies heavily on "If you want [Benefit A], then [Option B] is the logical choice" to transition between sections, especially when introducing an alternative.

**5. The Regurgitation Conclusion**
> *Quote:* "NV Casino не е законно за българския пазар и това остава решаващото. Липсата на лиценз от НАП и на защита по Закона за хазарта тежи повече от реалния каталог и удобните плащания, а кюрасаоският лиценз не замества нито едно от двете."
*   **Pattern:** *The "In Conclusion" Summary.* AI almost always uses the final paragraph to regurgitate the exact points made in the body paragraphs (no license, good catalog but doesn't matter, Curacao doesn't count). Human writers usually end on a forward-looking thought or a final punchy statement without summarizing the whole article.

---

### Concrete Recommendations

To make this read like it was written by a human expert, apply the following edits:

*   **Trim the Intro:** Delete the sentence about what the user "probably searched for" and the "official partner 2026" meta-commentary. Let the strong opening ("Не. NV Casino няма лиценз...") stand on its own. It’s much punchier without the AI throat-clearing.
*   **Kill the Micro-Summaries:** In the "NV Casino, какво всъщност представлява" section, delete the final sentence entirely (*"Въпреки добрите характеристики..."*). The reader already knows the lack of a license is the main problem; you don't need to hold their hand and remind them at the end of a paragraph about game providers.
*   **Ground the Preachy Language:** In the "Какво губиш конкретно" section, remove the philosophical sentences about the cost "looking like zero until there's a problem." Stick strictly to the mechanics of what happens to the player's money when a domain is blocked.
*   **Vary the Transitions:** In the "Честната алтернатива" section, remove the "Ако желанието е същото..." setup. Start the paragraph directly by introducing Betano as the licensed equivalent for players looking for large catalogs and crypto/convenient payments.
*   **Gut the Conclusion:** Delete the first two sentences of the "Заключение" section. You do not need to summarize the article again. Start the conclusion directly with the actionable advice: "Ако решите да играете, направете го при оператор..."

### Process Note
*Excellent workflow visibility.* The inclusion of `[VERIFY: ...]`, `[DATA NEEDED: ...]`, the 18+ markers, and the responsible gambling boilerplate are perfect. Do not touch or remove any of these during your stylistic edits; they are vital compliance and editorial safety nets that should only be resolved by the final publisher.
