# 07 — Gemini Step-7 cross-model check · pass 3 (after humaniser pass 2) + KEEP-BEST decision

Model: gemini-3.1-pro-preview · file: 05b-final-draft.md
**Verdict: Shows strong AI patterns, 85% confidence → human-likeness = 100 − 85 = 15**

## KEEP-BEST (mandatory) — MAX_GEMINI_PASSES (2) reached
Human-likeness seen across the loop:
- baseline (initial 05b): **HL 35** ("Shows AI patterns, 65%")  ← HIGHEST
- humaniser pass 1: HL 25 ("Shows AI patterns, 75%")
- humaniser pass 2: HL 15 ("Shows strong AI patterns, 85%")

Each Humaniser pass applied Gemini's own recommendations yet scored LOWER — the adversarial/noisy detector relocated its flags onto the revised text every read (documented repeatedly in content-queue.md for this brand). Per keep-best, the shipped 05b = the BASELINE (HL 35, highest seen), NOT a later lower version.
gemini column → **ai 65** (baseline verdict, verbatim scale: Shows AI patterns 65%).

NOTE (brand-gate native-register fix, not a Gemini style rec): the baseline contained one Bulgarian calque, 'карта игра', which the Brand Gate's native-register rule independently flags. That single two-word grammar correction ('карта игра' → 'игра на карти') is applied to the kept baseline; it changes no fact, number, link, date or RG line and does not materially affect the style verdict. All other pass-1/pass-2 style changes are discarded (reverted to baseline) per keep-best.

Style nits remain for the human editor at Step 6 (facts/numbers/links/RG are clean; 0 flags).

---

## Gemini verdict + recommendations (verbatim)

**Verdict: Shows strong AI patterns, 85% confidence.**

While the article is grammatically flawless, highly informative, and well-structured, it exhibits several classic hallmarks of Large Language Model (LLM) generation. The text relies heavily on symmetrical paragraph structures, didactic "guide" personas, broad definitional introductions, and clunky transitional signposting. It reads like a very well-prompted AI output (likely GPT-4 or Claude) that has been instructed to be concise and direct, but it lacks the natural asymmetry and conversational rhythm of a human writer.

Here is the breakdown of the specific patterns that triggered this assessment, along with actionable recommendations to humanize the text.

---

### 1. The "Broad Definition" Intro
**The Flagged Text:** *„Игри с карти" звучи като едно нещо, а покрива доста различни занимания.*
**The Pattern:** The "Illusion of Complexity" / Definitional Opening. AI models almost universally struggle to start an article *in media res*. They default to starting with a broad, philosophical statement that defines the topic or contrasts a simple concept with a complex reality (e.g., "X might seem simple, but it's actually Y"). 
**The Recommendation:** Cut the philosophical opening entirely. Start directly with the cultural reality or the core action. For example, begin immediately with the contrast between playing with friends at a table versus playing against a casino algorithm, skipping the "sounds like one thing" filler.

### 2. Formulaic "Listicle" Symmetry
**The Flagged Text:** 
* *Paragraph 1:* "Белот е най-широко разпространената игра..."
* *Paragraph 2:* "Сантасе, която мнозина знаят като..."
* *Paragraph 3:* "Свара се раздава..."
*(This exact same pattern repeats in the Casino section: Blackjack paragraph, Baccarat paragraph, Casino Poker paragraph).*
**The Pattern:** Symmetrical Structure. The AI was likely prompted to cover specific games, so it allocated exactly one perfectly balanced paragraph of similar length to each game. Human writers naturally favor certain topics, resulting in asymmetrical paragraphs (e.g., a massive paragraph on Belot because of its cultural weight, and just a passing sentence on Svara).
**The Recommendation:** Break the symmetry. Combine Santase and Svara into a single, faster-paced paragraph, or expand the Belot section to be noticeably longer and more detailed than the others. Do the same in the casino section—disrupt the "one game, one paragraph" rhythm.

### 3. Robotic Transitions and Signposting
**The Flagged Text:** 
* *"Същата маса събира и други познати имена."*
* *"Казино игрите с карти са друго."*
**The Pattern:** Clunky Signposting. AI uses these empty, declarative sentences as glue to transition between its internal bullet points. They add no value and sound like a textbook transitioning to a new chapter.
**The Recommendation:** Delete these transitional sentences entirely. You don't need to announce that you are moving to other games. Just jump straight into the next thought (e.g., instead of "Същата маса събира...", just start with "Блато, канаста и бридж също...").

### 4. The Didactic "Helpful Guide" Persona
**The Flagged Text:** *"Игрите с хора и решения възнаграждават опита, затова ги избирай, ако искаш да ставаш по-добър с времето. Друг подход е да тръгнеш от компанията: колко души имаш подръка... и вечерта почти се подрежда сама."*
**The Pattern:** Prescriptive Advice / Narrated Logic. AI often adopts a slightly patronizing, overly helpful tone, telling the reader exactly *how* to make a decision based on a logical matrix. Humans rarely tell other adults "choose this if you want to get better" in an informational article about card games.
**The Recommendation:** Remove the prescriptive instructions ("затова ги избирай", "тръгнеш от компанията"). Reframe this section as an observation about *why* people play these games, rather than a step-by-step instruction manual on how the reader should plan their Friday night.

### 5. Forced Parallelism / Staccato Rhythm
**The Flagged Text:** *"Пасиансът не иска противник и не иска залог."*
**The Pattern:** Staccato Rhythm / Forced Parallelism. AI frequently uses repetitive sentence structures to sound punchy or authoritative, but it often comes off as robotic and unnatural.
**The Recommendation:** Rephrase to sound more conversational and fluid. Combine the thoughts to remove the repetitive "не иска... не иска" structure.

---

*Note on Hard Rules: The responsible gambling language, 18+ markers, author bio, affiliate disclosures, and legal/tax references in the final sections ("Когато влязат реални пари", "Колко струва играта", and the footer) have been completely ignored in this critique per your instructions. They are structurally necessary and should remain exactly as they are.*
