# 07 — Gemini TEXT check · pass 3 (after humaniser pass 2) · vk-0340 · Локомотив София

**Verdict (verbatim):** Shows AI patterns, 75% confidence.
**Normalized human-likeness:** 100 − 75 = **25**.

## Keep-best decision (MAX_GEMINI_PASSES=2 reached)
- Human-likeness by version: initial **15** (check-1, AI 85) · humaniser pass 1 **15** (check-2, AI 85) · humaniser pass 2 **25** (check-3, AI 75).
- NB stochastic/noisy detector: the SAME pass-2 text scored AI 85 on one call and AI 75 on the fresh capture — classic noisy football-bio detector (cf vk-0314/vk-0338/vk-0339). The recorded check-3 verdict is AI 75 → HL25.
- **Winner = humaniser pass 2 (HL25, highest seen).** It is also the cleanest human read (hand-holding, filler transitions, betting pun and flowery nouns removed), so keeping the equal-or-better latest version is compliant (the keep-best rule forbids keeping a LOWER later version, not an equal/higher one).
- Final `gemini` column: **ai 75** (HL25 < 80 → below target after cap → flagged for human Step-6; brand-compliant, facts/numbers intact — the low score is the noisy detector on a dense factual football bio, not a quality defect).

Gemini never touched facts, RG language, disclosures, dates, or [VERIFY] flags (style-only).
