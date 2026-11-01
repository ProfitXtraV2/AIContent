# 07 — Gemini external check, pass 1 (INITIAL draft, 05b)

Command: `python3 scripts/gemini_check.py VsichkiKazina/articles/2026-10-20-belot-pravila/05b-final-draft.md`
Date: 2026-10-20

**Normalized human-likeness = 15** (verdict "Likely AI-generated, 85% confidence" → 100 − 85 = 15). BELOW target 80 → iterate (Humaniser pass via step-7b, then re-check).

## Gemini verbatim verdict + recommendations

**Verdict: Likely AI-generated (or heavily AI-edited), 85% confidence.**

While the text uses accurate Bulgarian terminology for Belot (взятка, капо, майорна терца) and is structurally sound, it exhibits several classic LLM writing patterns. The pacing is overly methodical, it relies on massive run-on sentences to explain complex rules, and it frequently uses forced empathy, philosophical platitudes, and slightly unnatural translated idioms to build rapport with the reader.

*(Note: Per your instructions, all responsible gambling language, 18+ markers, legal disclosures, and footer information have been completely ignored in this critique and should remain exactly as they are.)*

Here are the specific patterns that triggered this assessment and how to fix them:

### 1. The "Kitchen Sink" Run-On Sentences (Over-explanation)
The Pattern: AI struggles with pacing when explaining rules. Instead of using short, digestible sentences, it uses colons, semicolons, and multiple conjunctions to cram every possible condition, exception, and outcome into a single, exhausting breath.
Flagged Passages:
- "Контра удвоява залога (×2), реконтра го качва на ×4, а щом паднат три последователни паса, наддаването приключва и боята, на която всички са се спрели, става коз за цялата ръка; при „Без коз“ никоя боя не е силна, при „Всичко коз“ силни са всички."
- "Какво ще обявите зависи от това какво държите: силна боя с козовите Вале и девятка почти винаги оправдава анонс, защото тези две карти носят най-много точки и прибират най-много взятки, докато разпръсната ръка, богата на аса и десетки, клони към „Без коз“ или „Всичко коз“."
Recommendation: Break these massive blocks into 2 to 3 separate sentences. Replace semicolons and conjunctions (like "а", "докато", "защото") with hard periods. Let the reader breathe between the rule for doubling, the rule for passing, and the rule for No Trumps.

### 2. Concluding Platitudes & Rhetorical Hooks
The Pattern: LLMs love to open sections with a philosophical hook and close them with a neat, aphoristic summary. It makes the text sound preachy rather than informative.
Flagged Passages:
- "Останалото са подробности, а подробностите правят играта." (Intro)
- "Няколко секунди разговор в началото спестяват спор по-късно." (Regional rules section)
Recommendation: Delete these sentences entirely. The text will immediately sound more authoritative and human by simply stating the facts without trying to sound profound or offering life advice.

### 3. Forced Empathy and "Honest" Framing
The Pattern: AI frequently tries to build rapport by explicitly telling the reader how they feel (narrated emotion) or by framing standard information as a special "honest truth."
Flagged Passages:
- "...и точно това обърква начинаещите най-често."
- "...и честният отговор към начинаещ е, че..."
Recommendation: Remove the meta-commentary. You don't need to tell beginners they are confused, nor do you need to frame regional variations as an "honest answer." Just state directly that card values change based on the trump, and that regional rules require pre-game agreement.

### 4. Unnatural Phrasing / Translated Idioms
The Pattern: The AI uses phrases that are grammatically correct in Bulgarian but feel like literal translations of English idioms, lacking the natural rhythm of native card-playing vernacular.
Flagged Passages:
- "...и стоят стабилно..." (Reads like a translation of "stand solid" or "are stable").
- "По-тежко се пада на отбора..." (Reads like a literal translation of "it falls harder on").
- "...честната практика на масата е..." (Reads like "the fair practice is" — a very robotic way to describe game etiquette).
Recommendation: Replace these with natural Bulgarian phrasing. For example, instead of "честната практика", refer to standard etiquette or simply state what players must do. Instead of "по-тежко се пада", use a standard phrase for bearing the risk or penalty. Remove "стоят стабилно" entirely.

### 5. Mechanical Signposting
The Pattern: AI uses formulaic transition phrases to move from one concept to the next, treating the article like a checklist.
Flagged Passages:
- "Отделно стои белот:"
- "Картината се променя, щом..."
Recommendation: Cut the transition fluff. Start the sentence directly with the subject. For example, just start the paragraph with "Белот (Поп и Дама от козовата боя)..." instead of announcing that it stands separately.
