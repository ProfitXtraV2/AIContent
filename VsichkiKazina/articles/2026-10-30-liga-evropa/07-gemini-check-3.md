# 07 — Gemini Step-7 check, pass 3 (after humaniser pass 2) — PASS

Script: `python3 scripts/gemini_check.py 05b-final-draft.md` · 2026-10-30

VERDICT (verbatim): **Likely human-written (or heavily human-edited), 85% confidence.** → HUMAN-LIKENESS = **85** (≥ target 80 → PASS).

## KEEP-BEST DECISION (loop ends on PASS)
Human-likeness seen across the loop:
- check 1 (initial draft): „Shows AI patterns 65%" → HL 35
- check 2 (after humaniser pass 1): „Likely AI-generated 85%" → HL 15
- check 3 (after humaniser pass 2): „Likely human-written 85%" → HL **85** ← BEST, PASS
Detector was unstable/adversarial (35 → 15 → 85) on this evergreen format guide, but the final version (humaniser pass 2) is both the highest-HL AND a clear PASS. **Current 05b = winner (pass 2, 85%).** Recorded gemini = `human 85`.

Gemini's further (post-PASS) suggestions — consolidate H2s / merge micro-sections / reweave the opening definition — NOT applied: the loop PASSED at 85 and further edits risk lowering it; the scannable H2 structure is intentional for an educational format guide. Facts/numbers/links/RG/dates/byline untouched throughout; RG + footer explicitly praised by Gemini as the strongest proof of human authorship.

--- FULL VERBATIM OUTPUT ---
**Verdict: Likely human-written (or heavily human-edited), 85% confidence.**

This article reads predominantly like the work of a human expert, particularly in the final third. The responsible gambling section, the localized legal nuances (referencing НАП and specific Bulgarian laws), and idiomatic phrases like "На пари, отдалеч" and "малко трезва сметка" are highly characteristic of an experienced, localized human copywriter. AI rarely generates this level of precise, culturally embedded compliance language without sounding robotic.

However, the first two-thirds of the article (the sports facts) suffer from a slightly sterile, encyclopedic tone. While factually dense, it relies on a rigid, prompt-like structure that mimics AI summarization patterns.

### 1. Pattern: Formulaic FAQ-Style Signposting (The "Prompt Outline" Structure)
Flagged: the sequence of H2s (Какво е Лига Европа / Форматът / Кой продължава и кой отпада / Какво печели победителят / Как отборите влизат / Най-титулуваните) reads like a zero-shot AI prompt outline; recommendation: consolidate micro-sections into a more fluid journalistic narrative.

### 2. Pattern: The "Dictionary Definition" Opening
Flagged: „Лига Европа е второто по сила клубно състезание на УЕФА, точно под Шампионската лига и над Лигата на конференциите." Recommendation: weave the hierarchy into the historical context rather than a standalone X-is-Y definition.

### 3. Pattern: The Flattened Bullet List
Flagged: „В турнира се влиза по няколко начина: ... купите ... класирането ... „отгоре"..." Recommendation: add conversational transition; split domestic routes from the Champions League drop-downs.

### A Note on the Compliance & Gambling Sections
The „На пари, отдалеж" section and footer disclosures are excellent, distinctly human, idiomatic and locally tailored. Per the hard rules, do not touch the RG language, 18+ markers, or affiliate disclosures — they are the strongest proof of human authorship.
