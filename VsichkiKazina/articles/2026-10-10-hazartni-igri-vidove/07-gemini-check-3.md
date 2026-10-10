# Step 7 — Gemini cross-model check — PASS 3 (after humaniser pass 2)

Command: `python3 scripts/gemini_check.py 05b-final-draft.md`
Date: 2026-10-10 (cloud reconcile of HANDOFF row)

## Verdict (verbatim)

→ Normalized HUMAN-LIKENESS = 100 − 80 = **20**  (PASS threshold = 80) — needs changes; MAX_GEMINI_PASSES (2) reached → keep-best.

Keep-best ledger: initial 20 · pass 1 **25** · pass 2 20 → winner = pass 1.

---

**Verdict: Shows AI patterns (Heavily AI-assisted), 80% confidence.**

This article is of very high quality. The grammar is flawless, the legal terminology is precise, and the integration of internal links is contextually accurate. However, the underlying skeleton of the text relies heavily on classic Large Language Model (LLM) structural tropes: didactic analogies, perfectly symmetrical pacing, formulaic signposting, and a highly predictable FAQ rhythm. 

Additionally, there is a **process issue**: several `[VERIFY]` tags have survived into this "finished" article. Per your instructions, I am flagging this as a workflow oversight, but I will not touch or suggest removing them myself.

Here is the breakdown of the specific AI patterns detected and how to humanize them.

---

### 1. The "ChatGPT Explains" Didactic Analogy
**Flagged Passage:** *"Безплатната томбола на училищния празник отпада още на залога, защото никой не плаща за билет. При шахматния турнир с входна такса и награден фонд залог има, само че резултатът зависи от ходовете на играчите, а случайност в основата му липсва."*
**Pattern:** **Synthetic/Textbook Analogies.** LLMs frequently explain definitions by generating two contrasting, slightly sterile hypotheticals (e.g., a school raffle vs. a chess tournament) to isolate variables (stake vs. chance). It reads like a middle-school textbook rather than an engaging expert guide.
**Recommendation:** Break the rigid "Example A lacks X; Example B lacks Y" structure. Instead of hypothetical school raffles, ground the explanation in a more conversational, real-world tone. For example, explain how paying an entry fee for a local sports tournament isn't gambling because skill dictates the outcome, without making it sound like a math word problem.

### 2. Formulaic Signposting & Summarization
**Flagged Passage:** *"Петте вида хазартни игри накратко"* (followed by the markdown table).
**Pattern:** **The "In Short" / "In Summary" Pivot.** LLMs love to use phrases like "накратко" (briefly/in short) to introduce a perfectly symmetrical markdown table. It is a highly mechanical way to transition from paragraphs to structured data.
**Recommendation:** Change the H2 to something more authoritative and less generic, such as "Списък на разрешените хазартни игри по ЗХ". Introduce the table by directly stating what the reader is looking at, rather than announcing that you are about to summarize things "in short."

### 3. Forced Semantic Bridging
**Flagged Passage:** *"За бюджета на играча юридическата дефиниция казва малко; повече зависи от RTP и волатилността на конкретния слот, които са разгледани заедно с механиката на въртенето в Казино игри."*
**Pattern:** **The Awkward Pivot.** The AI was clearly prompted to include a link to a "Casino Games" page and mention RTP/volatility. To get there from a dry legal definition of a slot machine, it uses a forced contrast ("The legal definition says little about the player's budget; that depends more on..."). It feels engineered rather than natural.
**Recommendation:** Disconnect the two thoughts. Let the legal definition stand on its own. Then, start a new sentence or paragraph that simply notes that while the law defines the hardware, the actual payout mechanics (RTP/volatility) are what matter to players, pointing to your internal link without the artificial "A says little about B" contrast.

### 4. Symmetrical, "Echoing" FAQs
**Flagged Passages:** 
* *"Да, две: томболата и моментната лотария (чл. 41, ал. 2 ЗХ). Всичко друго може да се предлага онлайн..."*
* *"Не, от 08.08.2020 г. лицензите ги издава изпълнителният директор..."*
* *"От 18 години [VERIFY...]. Законът допуска само..."*
**Pattern:** **Robotic FAQ Rhythm.** LLMs answer FAQs with a highly predictable cadence: Direct Yes/No/Number -> Core Fact -> Legal Citation in parentheses -> One sentence of elaboration. When stacked together, the symmetry is a dead giveaway of AI generation.
**Recommendation:** Vary the sentence structures and lengths in the FAQ section. Remove the robotic "Yes, two:" or "No, since [date]" openings. Let some answers be a single, flowing sentence, while others take two or three. A human expert answers questions dynamically, not in a rigid template.

### 5. The "Wrap-Up" Moralizing Conclusion
**Flagged Passage:** *"Дали платформата изобщо е регулирана, личи по изискванията на закона (вид, лиценз, евро, 18+), и това се проверява преди първия залог. Дори законният лиценз обаче не прави никоя от тези игри изгодна за играча в дългосрочен план..."*
**Pattern:** **The AI "Bow on Top".** Even when not explicitly asked for a conclusion, LLMs will often generate a final paragraph that summarizes the main points (type, license, euro, 18+) and delivers a slightly preachy, moralizing final thought. 
**Recommendation:** Soften the transition into this final paragraph. Instead of summarizing the checklist again ("вид, лиценз, евро, 18+"), integrate the warning about long-term profitability directly into the responsible gambling advice, making it read like a continuous thought from the author rather than a generated summary of the article's themes.
