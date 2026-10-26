# 07 — Gemini external check · pass 2 (after humaniser pass 1)

Script: `python3 scripts/gemini_check.py 05b-final-draft.md`
Run: 2026-10-26

**Verdict: Shows AI patterns (Hybrid / Heavily Prompted), 65% confidence.** → human-likeness = 100 − 65 = **35** (< target 80; up from 25). Iterate once more (pass 2, within MAX_GEMINI_PASSES=2).

## Gemini verbatim verdict + recommendations

This is a highly sophisticated text. ... The vocabulary is highly idiomatic and grounded ("сухи серии", "грамадните удари", "мести средната сметка"), which usually points to a human writer or a very heavy human edit. However, the underlying *structure* and *thematic rhythm* give it away as likely AI-generated (or written by a human strictly following an AI-like SEO template): over-explaining math like a textbook, summarizing every feature in the conclusion, and obsessively repeating the core comparison (5-line RTP/cost) in almost every paragraph.

### 1. Thematic Repetition ("Hammering")
- Evidence: intro "...по-широкото покритие идва и с по-висок общ залог, с който го плащаш."; 5x3 "По-широко и по-скъпо, а математическото предимство остава на страната на казиното."; RTP "...при същия бюджет плащаш по-голям залог на спин срещу малко по-ниско средно връщане."; conclusion "...по-скъпа негова версия с по-ниско обявено връщане."
- Rec: keep the comparison in the RTP section only; strip the redundant cost-moralizing from the 5x3 section (let mechanics be mechanics).

### 2. Textbook Math Breakdown
- Evidence: "...тоест 100 − 95.88 = 4.12%. При €1000 оборот това значи средно връщане от €958.80..."
- Rec: remove the literal equation; state the 4.12% house edge directly; weave the €1000 example conversationally (keep the figures).

### 3. "Checklist" Conclusion
- Evidence: "Двадесетте линии и разширяващият се wild я правят по-жива... прогресивът и рисковата игра добавят адреналин, но нито едно от тях не мести 4.12%..."
- Rec: cut the feature recap; start the conclusion with the verdict ("Остава си носталгична класика...").

### 4. Clunky Phrasing / Translation Artifact
- Evidence: "Тук е и честната разлика с оригинала."
- Rec: change "честната разлика" → "основната / съществената разлика".

**Compliance note from Gemini:** RG language, 18+ markers, affiliate disclosures, and RTP/math figures are perfectly placed and compliant — do not alter or remove them.
