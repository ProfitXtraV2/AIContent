# 07 — Gemini external check · pass 1 (initial draft)

Script: `python3 scripts/gemini_check.py 05b-final-draft.md`
Run: 2026-10-26

**Verdict: Shows AI patterns, 75% confidence.** → human-likeness = 100 − 75 = **25** (< target 80) → iterate.

## Gemini verbatim verdict + recommendations

This article is highly accurate, well-researched, and strictly adheres to compliance and responsible gambling guidelines. However, it exhibits several classic LLM structural fingerprints. The writing relies heavily on didactic contrasts (explaining things by stating what they are *not*), artificial antithesis (setting up a premise just to knock it down), and formulaic parallelism in the conclusion. It reads like a very well-prompted AI that was instructed to be factual and avoid fluff, but it still falls back on robotic, predictable sentence rhythms.

### 1. Artificial Antithesis (The "Setup and Knockdown")
- Flagged: *"Логиката подсказва, че повече линии значат повече шансове. Сметката показва друго."* (Intro)
- Rec: Remove the dramatic setup; combine into a single direct statement (20 lines offer more simultaneous ways to win, but the RTP is actually lower than the 5-line version) without personifying "logic" and "math."

### 2. Didactic Contrast ("Not X, but Y")
- Flagged: *"...връща средно за милиони завъртания, не обещание за твоята сесия."* (RTP); *"Шансът да влезеш расте с размера на залога, не с умение или стратегия..."* (Jackpot Cards)
- Rec: Trim the negative clauses; state the affirmative fact.

### 3. Narrated Emotion / Presumptive Generalization
- Flagged: *"...няма безплатни завъртания, и това изненадва играчи, свикнали всеки нов слот да ги предлага."* (Scatters)
- Rec: Remove the assumption about players being "surprised"; state the mechanics objectively.

### 4. Formulaic Parallelism (Binary Conclusion)
- Flagged: *"Ако търсиш носталгията... Ако търсиш по-добри шансове... няма ги."* (Conclusion)
- Rec: Break the "Ако търсиш... Ако търсиш..." symmetry into a single cohesive sentence.

### 5. Repetitive Mechanical Phrasing
- Flagged: *"...при пет линии един залог покрива пет начина..., при двадесет покриваш двадесет."* (5×3 section)
- Rec: Condense; a single bet here funds 20 fixed paylines, increasing cost per spin.

**Compliance note from Gemini:** the RG "not X but Y" in the волатилност section and the boilerplate are correctly placed — DO NOT touch them. Disclosures and 18+ markers intact and correct.
