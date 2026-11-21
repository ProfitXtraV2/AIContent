# 07 — Gemini Step-7 external check, pass 2 (Clover Chance)

Command: `python3 scripts/gemini_check.py .../05b-final-draft.md` (after humaniser pass 1)
Model: gemini-3.1-pro-preview · Exit 0

## Verbatim verdict
**Verdict: Likely human-written, 90% confidence.** → human-likeness = **90**. PASS (≥ 80).

"Reads exceptionally well and avoids almost all common LLM pitfalls. Natural Bulgarian gambling slang ('вързан върху', 'гониш', 'седят върху сходни слотове', 'джакпот слой'). The transparency meta-commentary ('конкретни числа за тях няма да прочетеш тук') is a strong human indicator — a human who hit a research dead-end and chose transparency, whereas AI would hallucinate numbers."

## Keep-best decision
- Initial draft: human-likeness 20 (Shows AI patterns 80%).
- Humaniser pass 1 (broke colon/semicolon rhythm, varied one heading): human-likeness 90 (Likely human-written 90%). ← highest, PASS.
- KEEP pass 1 (current 05b). gemini column: **human 90**. 0 number-drift; both [VERIFY] flags intact.
- Loop ends on PASS after 1 humaniser pass (cap 2 not reached).
