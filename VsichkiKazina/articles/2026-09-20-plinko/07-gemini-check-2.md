# 07 — Gemini Step-7 external check, pass 2 (Plinko)

Command: `python3 scripts/gemini_check.py VsichkiKazina/articles/2026-09-20-plinko/05b-final-draft.md` (after humaniser pass 1)
Model: gemini-3.1-pro-preview · Exit 0

## Verbatim verdict
**Verdict: Likely human-written, 85% confidence.** → human-likeness = **85**. PASS (≥ 80).

"Exceptionally well-crafted and avoids almost all the classic pitfalls of AI-generated Bulgarian text. Highly idiomatic, natural phrasing (e.g. 'бавно топене', 'ситни връщания', 'парите вече са вътре', 'нечий късмет вечерта'). Avoids hyperbolic tone." A few minor residual SEO-mill patterns noted (concept re-statement across the risk/RTP sections; a short parallel BGaming/Spribe comparison) but not blocking.

## Keep-best decision
- Initial draft: human-likeness 20 (Shows AI patterns 80%).
- Humaniser pass 1: human-likeness 85 (Likely human-written 85%). ← highest seen, PASS.
- KEEP pass 1 (current 05b). gemini column: **human 85**.
- Loop ends on PASS after 1 humaniser pass (cap MAX_GEMINI_PASSES=2 not reached). Residual minor notes left as-is (style-only, non-blocking; facts/RG untouched).
