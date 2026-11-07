# 07 — Gemini check · pass 2 (after humaniser pass 1)

**Verdict (verbatim):** Shows AI patterns, 75% confidence.
→ Normalized HUMAN-LIKENESS = 100 − 75 = **25**. Improved from 15 (pass 1 now best). Still < 80 → one more humaniser pass (last, MAX_GEMINI_PASSES=2).

Gemini flagged (style-only; money/RG section + footer explicitly praised, DO NOT TOUCH):
1. **Leftover AI image-prompt in hero ALT (the "smoking gun"):**
   `![Плоска илюстрация ... в сдържани тонове, без клубни гербове, без лога, без хора]` reads as
   a literal image-generator prompt (flat illustration / muted tones / negative prompts), not
   real alt-text. → Rewrite as plain descriptive BG alt-text of what is visible.
2. **"Wikipedia summary" staccato rhythm** in §2 (Какво е): uniform sentence length/dry cadence →
   vary length, weave the first-season + first-winner facts into a more fluid line.
3. **Formulaic Q&A subheadings** (perfectly symmetric chronological breakdown reads like a
   generated FAQ) → consolidate some micro-sections, give headings editorial flavor.
4. **Mechanical transition** "Когато шестте кръга приключат, класацията се разделя на три." →
   soften to a journalist's phrasing.

Note from Gemini: "The ## На пари... section and the RG disclosures are excellent... Do not touch
this section or the footer. Focus edits entirely on the sports-information sections above it."

**Action (humaniser pass 2):** fix hero ALT to descriptive text; re-cadence §2; reflavor the
format heading and MERGE advancement + prize into one section; soften the transition. Numbers,
links, RG, dates, names preserved. Re-run gemini_check.py (check 3). Keep-best so far = pass 1 (25).
