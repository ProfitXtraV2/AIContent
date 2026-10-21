# Gemini external check — pass 3 / after humaniser pass 2 (2026-09-12)

**Verdict: Shows AI patterns, 75% confidence** → human-likeness = 25

## Keep-best decision
Human-likeness: initial 15 → humaniser pass 1 = 25 → humaniser pass 2 = 25. Cap (MAX_GEMINI_PASSES=2) reached. Highest = 25; kept pass 2 (tied-highest, plus the punctuation sweep, de-'X-not-Y' headers, integrated links, RG line split into its own paragraph). Recorded `ai 75`. gemini-3.1-pro-preview rates these BG guides harshly even after humanising (cf. wild-simvoli and posted rotativki-s-plodove HL 30); human owns final approval.

## Verbatim verdict + recommendations

**Verdict: Shows AI patterns, 75% confidence.**

While the article is highly accurate, well-structured, and free of fluff, the sentence-level mechanics heavily rely on standard Large Language Model (LLM) tropes. The text frequently uses manufactured misconceptions, staccato transitions, robotic hedging ("this is not universal"), and exhaustive logical permutations. It reads like a very well-prompted AI that has been instructed to be concise, but it still lacks the natural, conversational flow of a human expert. 

Here is the breakdown of the specific patterns and how to fix them.

### Flagged Passages & AI Patterns

**1. Pattern: Manufactured Misconception / Narrated Confusion**
*   **Quote:** *"Двата символа често се бъркат, защото изглеждат еднакво "специални" на екрана..."* AND *"а объркването между тях остава една от най-честите грешки на нови играчи."*
*   **Why it flagged:** AI loves to invent a scenario where people are constantly confusing two concepts to justify explaining the difference. Human experts rarely frame basic mechanics as a "common mistake" unless it actually costs players money. 

**2. Pattern: Staccato Rhythm & Repetitive Signposting**
*   **Quote:** *"Обикновените символи работят различно. Те трябва да са подредени по конкретна активна линия, за да платят. Wild е нещо съвсем различно."*
*   **Why it flagged:** AI frequently uses short, abrupt, parallel sentences to pivot between ideas. Starting consecutive thoughts with "[Subject] works differently" and "[Other Subject] is completely different" creates a robotic, stop-and-go rhythm.

**3. Pattern: The "Not Universal" Disclaimer (AI Hedging)**
*   **Quote:** *"Това не е универсално правило."* AND *"Тази опция обаче не е повсеместна."*
*   **Why it flagged:** LLMs are programmed to be overly cautious and avoid absolute statements. Instead of just stating the exception, the AI inserts a dedicated disclaimer sentence to announce that exceptions exist.

**4. Pattern: Exhaustive Permutation Listing**
*   **Quote:** *"Един слот може да носи само wild, друг само scatter, трети и двата, а някой нито един."*
*   **Why it flagged:** This is a classic machine-logic pattern. The AI feels the need to list every single mathematical permutation of a scenario to ensure its answer is "complete," even though a human reader already implicitly understands this.

**5. Pattern: Stating the Obvious (Over-explaining)**
*   **Quote:** *"Не е задължителна и не е достъпна във всяка игра."* (Referring to the Feature Buy option).
*   **Why it flagged:** AI often pads explanations by stating what a feature *isn't*, resulting in overly didactic sentences that treat the reader like a child.

---

### Concrete Recommendations

*   **Fix the "Confusion" Trope:** Remove the meta-commentary about players being confused or making mistakes. In the intro and the first H2, simply state how the Scatter behaves independently of paylines, and how the Wild relies on them. You don't need to justify the explanation by claiming players mix them up.
*   **Smooth the Staccato Intro:** Combine the choppy transition sentences in the opening paragraph. Instead of announcing that normal symbols work differently and then announcing that Wilds work differently, weave them into a single comparative thought (e.g., contrasting the Scatter's freedom with the strict payline rules of normal and Wild symbols).
*   **Cut the Hedging Disclaimers:** Delete the sentences *"Това не е универсално правило"* and *"Тази опция обаче не е повсеместна."* Let the sentences that immediately follow them do the work. Just state what usually happens, and then state the exception (e.g., "Usually it takes 3 scatters, though games like Sweet Bonanza require 4 to 6").
*   **Delete the Permutation List:** Completely remove the sentence *"Един слот може да носи само wild, друг само scatter, трети и двата, а някой нито един."* It adds zero value to the reader and is a dead giveaway of AI generation. The Starburst example preceding it makes the point perfectly on its own.
*   **Trim the Didactic Feature Buy Intro:** Remove *"Не е задължителна и не е достъпна във всяка игра."* The reader already knows they don't *have* to buy the bonus. Start directly with what the button does and how the math behind it works.

*(Note: As per your hard rules, the responsible gambling language, 18+ markers, and affiliate disclosures at the bottom of the text have been completely ignored in this critique and should remain exactly as they are.)*
