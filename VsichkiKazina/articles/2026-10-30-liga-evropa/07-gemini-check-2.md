# 07 — Gemini Step-7 check, pass 2 (after humaniser pass 1)

Script: `python3 scripts/gemini_check.py 05b-final-draft.md` · 2026-10-30

VERDICT (verbatim): **Likely AI-generated or heavily AI-assisted (85% confidence)** → HUMAN-LIKENESS = 100 − 85 = **15**.

NOTE: HL DROPPED 35 → 15 after applying pass-1 recs. Gemini's detector is behaving adversarially/unstably on this evergreen format-guide (same observed on sibling vk-0314 Ефбет Лига: „детектор нестабилен"). Each round of cuts makes it flag harder. Keep-best so far = INITIAL draft (HL 35). Will apply one more (final, pass 2) humaniser pass on the defensible recs, re-check, then keep the highest-HL version seen.

Recommendations (pass 2, style-only):
1. Neat-bow wrap-ups → cut: intro „Точно затова турнирът отдавна не е утешителна награда, а сериозен коридор…"; „Така една и съща таблица събира и грандовете…"; „Именно заради това правило от 2024/25…".
2. Unsolicited advice → „…вместо да се помни наизуст." remove; state plainly.
3. Mechanical enumeration → blend the three qualification routes into one flowing sentence.
4. Dramatic phrasing → intro „една особеност, която я отличава…" state directly; „никой не е доминирал така, както Севиля" → objective record statement.
RG section + footer: untouched (mandated).

--- FULL VERBATIM OUTPUT ---
**Verdict: Likely AI-generated or heavily AI-assisted (85% confidence)**

While the text is grammatically flawless, highly informative, and well-localized, it suffers from the classic "LLM cadence." The article relies heavily on formulaic paragraph structures—specifically the "Topic Sentence -> Explanation -> Neat Summary Bow" loop. It also features unsolicited advisory padding and slightly overdramatized hooks that AI uses to sound engaging.

### Flagged Passages & AI Patterns

1. The "Neat Bow" Paragraph Wrap-ups (Formulaic Structure)
* Quote 1: „Точно затова турнирът отдавна не е утешителна награда, а сериозен коридор към върха на европейския футбол."
* Quote 2: „Така една и съща таблица събира и грандовете, и по-малките имена, а всеки резултат мести мястото в общото подреждане."
* Quote 3: „Именно заради това правило от 2024/25 клубът шампион не остава да защитава титлата в Лига Европа, а се качва едно ниво нагоре."

2. Unsolicited Advisory Tone (AI Helpfulness)
* Quote: „...затова за актуалната разбивка е по-разумно да се гледа официалният сайт на УЕФА, вместо да се помни наизуст."

3. Mechanical Enumeration (Robotic Signposting)
* Quote: „Част от местата отиват при носителите на националните купи, други се печелят чрез класирането във вътрешните първенства. Трета група идва „отгоре"..."

4. Narrated Drama / Cliché Hooks
* Quote 1: „...Лига Европа има една особеност, която я отличава от повечето големи надпревари..."
* Quote 2: „...никой не е доминирал така, както Севиля."

### Concrete Recommendations
* Break the summary loop: Delete the repetitive wrap-up sentences at the end of paragraphs (e.g. delete „Именно заради това правило..." without losing information).
* Cut the unsolicited advice: remove „е по-разумно да се гледа официалният сайт на УЕФА, вместо да се помни наизуст." Simply state the allocation depends on UEFA coefficients and changes annually.
* Fluidize the signposting: blend domestic cup winners, league standings, and Champions League drop-downs into a single flowing list.
* Tone down the dramatic phrasing: intro — state directly that the Europa League is unique because the winner does not defend their title; titles — change „никой не е доминирал така, както Севиля" to an objective record statement.

A Note on Compliance/Responsible Gambling: the „На пари, отдалеж" section and footer disclosures are mandated compliance/RG text; per hard rules, no changes recommended. All 18+ markers, RG language, and licensing disclosures remain exactly as they are.
