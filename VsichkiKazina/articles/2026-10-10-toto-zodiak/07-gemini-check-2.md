# Step 7 — Gemini cross-model check — PASS 2 (after humaniser pass 1)

Command: `python3 scripts/gemini_check.py 05b-final-draft.md`
Date: 2026-10-10 (cloud reconcile of HANDOFF row)

## Verdict (verbatim)

→ Normalized HUMAN-LIKENESS = **85**  (PASS threshold = 80) — PASS

---

**Verdict: Likely human-written (or heavily human-edited AI), 85% confidence.**

This is a very strong, high-quality piece of copy. It successfully avoids the most egregious AI traps: there is no overly enthusiastic fluff ("Dive into the exciting world of..."), the tone is grounded and appropriately cynical ("Плащате за тръпката от тегленето, и толкова"), and it uses punchy, human-like syntax (like the single-word paragraph "Не."). The framing of the odds ("ще чакате средно около 244 000 години") is excellent human copywriting. 

However, there are a few lingering structural "tells" that mimic LLM writing patterns—specifically, robotic disclaimers and classic AI signposting. 

Here are the specific patterns that triggered my radar, along with actionable recommendations to polish them out.

*(Note: As requested, I am ignoring the [VERIFY], [DATA NEEDED], and [CONFLICT] tags, as well as the 18+ and licensing boilerplate. Leaving editorial bracket tags in a "finished" piece is a workflow/process issue, but I have not factored them into the stylistic evaluation or suggested their removal).*

### 1. The "Roadmap" Signpost
**The Pattern:** AI models are heavily trained to introduce a topic, state a problem, and then explicitly announce what the rest of the text will do. 
**The Passage:** *"Затова тук ще намерите правилата, тиражите и сметката, но не и числа за залагане или съвети кога и колко да играете."* (Intro)
**Recommendation:** Delete this sentence entirely. Your introduction is already incredibly strong because it hits the reader with the harsh reality of the odds right away. You don't need to announce the table of contents to the reader. Let the transition from the odds directly into the "Как се играе" section happen naturally.

### 2. The "Knowledge Cutoff" Disclaimer
**The Pattern:** LLMs frequently use defensive, overly formal phrasing when they cannot find a specific piece of data, mimicking their system prompts regarding knowledge cutoffs or search limitations.
**The Passage:** *"В достъпните ни източници към момента на писане цена на една комбинация няма, така че сума не посочваме..."* (Section: Как се играе)
**Recommendation:** Rephrase this to sound like a normal human observation rather than a research limitation disclaimer. Instead of talking about "the sources available to us at the time of writing," simply state directly that the official site currently doesn't list the price per combination, and advise the player to check at the counter. 

### 3. The "Disambiguation" Transition
**The Pattern:** When AI models detect entities with similar names, they often output a highly mechanical, encyclopedic disambiguation warning, repeating the exact specs of the subject to prove they know the difference.
**The Passage:** *"Да не се бърка с моментната талонна игра „Зодиак“ на БСТ от края на 90-те: днешното ТОТО 2 – Зодиак (теглене 5 от 50 + 1 от 12, от 2014 г.) няма връзка с нея."* (Section: Как се играе)
**Recommendation:** Soften this transition. You don't need to repeat the exact game specs ("теглене 5 от 50 + 1 от 12, от 2014 г.") in brackets right after explaining them in the previous paragraphs. Suggest turning this into a casual, brief aside (e.g., just mentioning that this is a completely different game from the 90s scratch card of the same name) rather than a formal "Do not confuse with..." warning.

### 4. Formulaic FAQ Echoing
**The Pattern:** AI-generated FAQs often repeat the exact premise of the question in the first sentence of the answer, rather than answering conversationally.
**The Passage:** 
*Question:* "Само зодия печели ли нещо?"
*Answer:* "Да, дори без нито едно познато число уцелената зодия носи малка печалба от 10-а група."
**Recommendation:** The answer is good, but it feels slightly repetitive right after the question. Suggest tightening the answer to start directly with the fact (e.g., "Да, тя носи малка печалба от 10-а група, дори да не познаете нито едно число."). This breaks the robotic Q&A rhythm and makes it read more like a human expert answering off the cuff.
