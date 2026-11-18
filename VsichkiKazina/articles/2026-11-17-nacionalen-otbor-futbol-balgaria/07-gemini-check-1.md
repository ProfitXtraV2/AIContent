# 07 — Gemini External Check · Pass 1 (on initial 05b)

Tool: `scripts/gemini_check.py` (GEMINI_API_KEY set; API ONLINE — 402 outage cleared).
Date: 2026-11-17.

## Verbatim verdict

**Verdict: Shows AI patterns, 85% confidence.** (re-run wording: „Shows strong AI patterns, 85% confidence.")

Normalized HUMAN-LIKENESS = 100 − 85 = **15** → below GEMINI_TARGET_CONFIDENCE (80).
Action: iterate (Humaniser pass 1 via step-7b), then re-check. Record 15 as the initial-draft score for keep-best.

## Verbatim recommendations

While the article is grammatically flawless, well-structured, and strictly adheres to the requested
factual constraints, it suffers heavily from "AI voice." The text relies on classic LLM writing tropes:
heavy signposting, melodramatic framing of historical facts, philosophical thematic wrapping, and overly
polished, antithetical punchlines.

### 1. Pattern: Signposting & Meta-Discourse
- Flagged: „Тук проследяваме пътя по завършени факти, тоест дати, мачове и резултати. Няма да намериш
  текущи класирания, състави или прогнози какво предстои." (Intro)
- Flagged: „Профилите на отделните играчи са тема за себе си и живеят в самостоятелни текстове, затова
  тук имената служат колкото за ориентир, толкова и за покана да ги прочетеш поотделно." (Поколението)
- Recommendation: Delete these meta-explanations. In the intro, end after „...повод за национален разказ,
  а не само за статистика." In the records section, state the records and link the profiles without
  explaining why you aren't going into detail.

### 2. Pattern: Poetic Contrast & Over-Dramatization
- Flagged: „...което превърна всяко ново класиране по-скоро в надежда, отколкото в очакване."
- Flagged: „Пътят към най-светлата страница тръгва от едно гостуване."
- Flagged: „На финалите в Съединените щати отборът направи това, което дотогава изглеждаше немислимо."
- Recommendation: Tone down the melodrama. Replace the „надежда/очакване" contrast with a straightforward
  statement about the team's historical struggles at the finals. Change „най-светлата страница" to
  something grounded (e.g. „Пътят към САЩ '94 започва с..."). Let beating the world champions provide the
  drama without calling it „немислимо".

### 3. Pattern: Philosophizing / Thematic Wrapping
- Flagged: „Това не зачерква европейските участия, а ги подрежда там, където си стоят: като потвърждение,
  че след 1994 г. България още принадлежеше към тимовете, които се класират за големите турнири."
- Recommendation: Cut the philosophical justification. State the facts: the generation was changing, the
  '94 success couldn't be replicated, group-stage exits in '96 and '04. End there.

### 4. Pattern: Formulaic Antithesis (the „mic drop" conclusion)
- Flagged: „Дали някога ще бъде подобрено, се решава на терена, не на талона."
- Recommendation: Break the symmetry. Reword more conversationally and less poetically (e.g. „Следващите
  успехи зависят от играчите на терена, а залозите остават просто допълнение към мача.").

### Process note (hard rules)
Gemini noted the surviving `[VERIFY: точен брой и дали е наравно с Христо Бонев]` tag and the RG language;
it explicitly did NOT suggest removing them. Per daily-run: flags STAY in the text (human resolves at
Step 6); Gemini is style-only. Applied accordingly.
