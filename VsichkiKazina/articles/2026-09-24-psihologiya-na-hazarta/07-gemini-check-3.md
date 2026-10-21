# Gemini Step-7 external check — pass 3 (after Humaniser pass 2 / cap)

Command: `python3 scripts/gemini_check.py 05b-final-draft.md`

**Verdict: Shows AI patterns, 80% confidence.** → human-likeness = 100 − 80 = **20**

Pass 2 humaniser applied the pass-2 recs: removed both "not X, but Y" contrasts (intro + conclusion), fixed the awkward "генератор, чиито понятия" link, trimmed the closing 3-link wrap-up to 2 organic links, deleted "Това не е случайност в дизайна", and reworked the loss-chasing synthesis to show the combination narratively instead of announcing it. The prose is cleaner and less formulaic; the detector score is unchanged (20), which is expected for this niche (BG casino copy baseline ~20–25 human-likeness, per prior-run logs).

KEEP-BEST decision (MAX_GEMINI_PASSES reached): human-likeness across versions — initial 15, pass 1 humanised 20, pass 2 humanised 20. The pass-2 humanised version ties the top score AND is the cleanest text, so it is kept as final. All untouchables preserved (numbers, Clark 2009 / Langer citations, links, 18+, RG block, affiliate footer, byline, brand, dates); em-dash 0. Below the 80 PASS threshold → recorded `ai 80`, flagged for optional human style-polish at Step 6 (factual + compliant; style-only gap).
