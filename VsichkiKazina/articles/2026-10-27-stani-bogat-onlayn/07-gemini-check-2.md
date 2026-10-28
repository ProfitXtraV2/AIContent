# 07 — Gemini check, pass 2 (after humaniser pass 1)

Command: `python3 scripts/gemini_check.py 05b-final-draft.md`
Normalized human-likeness: **95** ("Likely human-written, 95% confidence") → ≥ GEMINI_TARGET_CONFIDENCE (80): **PASS**.

Keep-best: pass-1 (HL 95) > baseline (HL 75) → KEEP pass-1. Loop ends on PASS (1 humaniser pass applied). Recorded as `human 95`.

## Gemini verbatim verdict

**Verdict: Likely human-written, 95% confidence.**

This article reads exceptionally well and avoids almost all the classic traps of AI-generated Bulgarian text. It lacks the robotic enthusiasm, flowery adjectives ("вълнуващ", "незабравим"), and formulaic introductions/conclusions ("В днешния дигитален свят...", "В заключение...") that LLMs typically rely on.

The writer uses highly idiomatic, punchy phrasing that AI struggles to replicate naturally in Bulgarian—such as "шепа помощи", "не каса", and the excellent closing thought: "понякога знаеш отговора, а понякога само ти се струва, че го знаеш." The first-person perspective ("за които пиша тук") is also integrated smoothly.

### Process Note: Surviving Editor Tags
Three **[VERIFY: ...]** tags left in the text — flagged for the editorial team, not altered. (KEEP per brand rule — they stay for human Step 6.)

### Further optional polish (NOT applied — already PASS at 95; no further pass needed)
1. „Over-compressed list" — semicolon stacking in the жокери paragraph could be split into shorter sentences. (Optional; style only.)
2. „Formulaic contrast" — the „Едно нещо отличава..." contrast opener of the closing section. (Optional; style only.)

## Decision
PASS at HL 95 on pass 1; keep-best = pass 1. No further humaniser pass (we are above the 80 gate and MAX_GEMINI_PASSES not needed). Facts, [VERIFY] flags, RG lines, links, byline, brand, dates all preserved.
