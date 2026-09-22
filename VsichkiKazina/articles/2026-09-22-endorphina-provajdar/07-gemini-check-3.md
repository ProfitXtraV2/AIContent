# 07 — Gemini external check, pass 3 (after Humaniser pass 2) — Endorphina

Model: gemini-3.1-pro-preview · script: scripts/gemini_check.py
**Verdict: Likely human-written with AI assistance (or heavily structured AI with excellent human editing) — 75% confidence.** → human-likeness = **75**. → below the PASS bar (80), but the best of all versions.

Big jump: HL 15 (initial) → 25 (pass 1) → **75 (pass 2)**. Gemini: "strong, highly readable text… stripped out the most egregious AI clichés… refreshingly cynical and realistic about casino math, which is rare for raw AI output," praising „Тези правила обаче са писани в полза на казиното." Remaining minor nits: a couple of transition/vocabulary-loop tells and a caption echo — diminishing returns on a noisy provider-profile detector (cf. the Amusnet EGT profile, which also resisted the 80 bar).

## Keep-best decision (mandatory)
MAX_GEMINI_PASSES (2) reached. Human-likeness by version: initial **15**, humaniser-1 **25**, humaniser-2 **75**. Highest = **75** = the current 05b (humaniser pass 2). Keep it. Since 75 < 80, content-queue `gemini = ai 25` (verbatim scale: 100 − 75). The [VERIFY] flag and every untouchable remain intact. No later, lower version kept.
