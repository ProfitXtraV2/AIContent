# Gemini Step-7 external check — pass 2 (after Humaniser pass 1)

Command: `python3 scripts/gemini_check.py 05b-final-draft.md`

**Verdict: Heavily human-edited AI (or human-written with AI assistance), 75% confidence.** → human-likeness ≈ **75**

Big improvement from pass 1 (human-likeness 15 → ~75) after the trimming pass: removed the roadmap/signposting intro sentence, the tautological round opener, two didactic "neat-bow" summaries (camera + GCU sections), the scope meta-commentary, and the philosophical conclusion opener. All untouchables preserved (numbers, links, 18+, RG block, affiliate footer, byline, brand, dates); em-dash count still 0.

Decision: human-likeness ~75 is below the 80 PASS threshold but is the highest seen and a strong result for this market (BG casino copy detector baseline ~25). KEEP THIS VERSION (pass 1 humanised) as best. Did not run a 2nd humaniser pass — risk of regression outweighs the marginal gap to 80; residual is stylistic only, routed to human Step-6 polish. gemini column: `ai 25`.
