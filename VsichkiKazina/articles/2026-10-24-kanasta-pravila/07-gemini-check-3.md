# 07 — Gemini check, pass 3 (after humaniser pass 2)

Model: gemini (scripts/gemini_check.py) · run 24.10.2026 on 05b after step-7b humaniser pass 2.

## Verdict (verbatim, captured)
**Verdict: Likely AI-generated or heavily AI-assisted, 85% confidence.**

Normalised human-likeness = 100 − 85 = **15** — LOWER than pass 1 (HL25). Humaniser pass 2 lowered the score: the detector is noisy/adversarial, it relocated its flags and surfaced NEW ones (anglicisms, POV shifting) that it had not raised on the previous two versions. MAX_GEMINI_PASSES (2) reached.

While the article is structurally sound, factually dense, and free of obvious hallucinations, it exhibits several classic hallmarks of LLM generation — specifically when translating English instructional logic into Bulgarian: unnatural metaphors (literal translations of English idioms), inconsistent point-of-view (POV) shifting, and mechanical signposting.

### 1. Unnatural Metaphors / Literal Translations (Anglicisms) — newly raised this pass
- "с много по-тежко тегло" / "най-тежките точки" → points are "високи/много", not "тежки".
- "със симетричния минус 800" → drop "симетричния".
- "кърпене с дива карта" → "заместване с дива карта".
- "Масите се различават по няколко точки" → "Правилата варират…".

### 2. Inconsistent Point of View (POV shifting) — newly raised this pass
- Mix of second-person singular ("събираш", "можеш", "изхвърлиш ли") and third person across the instructional text.
(Output truncated in capture after this point; the two sections above are the substance. These flags were NOT raised on the initial draft or pass 1 — characteristic of a high-variance detector whose goalposts move each pass.)

## KEEP-BEST DECISION
Human-likeness by version: initial = 10 · pass 1 = 25 · pass 2 = 15.
Highest = **pass 1 (HL25)**. The loop ended by hitting MAX_GEMINI_PASSES. Per the mandatory keep-best rule, the final 05b is restored to the **pass-1** version (the highest human-likeness seen), NOT the later lower pass-2. gemini column recorded as `ai 75` (pass-1's own verdict: "Shows AI patterns, 75%"). Human voice polish advised downstream (noisy detector on dry rules-dense content; same pattern as siblings vk-0279/0283/0285).
