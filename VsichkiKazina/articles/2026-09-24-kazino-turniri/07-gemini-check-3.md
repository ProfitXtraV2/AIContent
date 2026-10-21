# Gemini Step-7 external check — pass 3 (after Humaniser pass 2 / cap)

Command: `python3 scripts/gemini_check.py 05b-final-draft.md`

**Verdict: Shows AI patterns, 75% confidence.** → human-likeness = 100 − 75 = **25**

Pass 2 humaniser applied the pass-2 recs: removed the four signposting openers in the "Капаните" section (paragraphs now start on the point), replaced personifications ("бюджет не обича" → "изпразва бюджета бързо", "тих начин" → "скрит начин", dropped the "витрина" showcase metaphor), deleted the narrated-emotion sentence about the leaderboard's "attractive force", and turned "Един пример с примерни числа." into "Например (числата са примерни):". All illustrative numbers kept verbatim and still labelled примерни.

KEEP-BEST decision (MAX_GEMINI_PASSES reached): human-likeness across versions — initial 15, pass 1 humanised ~mid, pass 2 humanised 25. The pass-2 humanised version is the highest AND cleanest, kept as final. All untouchables preserved (numbers, links, 18+, RG block, affiliate footer, byline, brand, dates); em-dash 0. Below the 80 PASS threshold → recorded `ai 75`, flagged for optional human style-polish at Step 6 (factual + compliant; style-only gap).
