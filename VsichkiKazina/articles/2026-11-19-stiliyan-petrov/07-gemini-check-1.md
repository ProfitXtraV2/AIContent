# 07 — Gemini text check · pass 1 (INITIAL draft)

Command: `python3 scripts/gemini_check.py 05b-final-draft.md`
Exit: 0

## Verdict (verbatim)
**Verdict: Shows AI patterns, 90% confidence**
→ human-likeness = 100 − 90 = **10** (below GEMINI_TARGET_CONFIDENCE 80) → iterate.

## Recommendations (verbatim summary)
1. **Prompt echo / over-signposting** — delete intro sentence „Тази статия проследява кариерата
   му по завършени факти…"; remove „Всички стойности следват текста на статията" from the image
   caption; remove „Прогнози на кого да заложиш обаче няма да намериш тук." (keep all RG/compliance
   text + links untouched).
2. **Formulaic transitions** — cut „Следващата спирка е Англия." (start with the date/transfer);
   drop „Паралелно с клубовете върви и най-дългата линия…" (start directly with the 105/8 record).
3. **Manufactured drama / clichés** — remove „преди Западът да почука на вратата"; remove
   „кариерата му спира по начин, който никой не очаква."; remove „Новината надхвърля футбола."
4. **„Not just X, but Y" conclusion** — rewrite final sentence without the „biggest match off the
   pitch" trope; remove the „one half / the other half" framing in „Какво остава".

(Gemini is style-only; it must not touch facts, RG language, disclosures, dates, byline, brand.)

→ Action: fresh Humaniser pass (step-7b), preserve every untouchable (105, 8, 4 titles, №19,
dates 30.03.2012 / 02.08.2012 / 09.05.2013 / 26.05.2013, 1979/1996/1999/2006/2013, links, RG,
18+, affiliate footer, byline Георги Тодоров, brand Всички Казина).
