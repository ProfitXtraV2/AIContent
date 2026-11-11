# Step 7 — External cross-model check (Gemini) — ELLE Dental

Canonical prompt sent to Gemini (a different model family than the writer) by
`python3 scripts/gemini_check.py <article>/05b-final-draft.md --brand elledental`.
**Recommendations only**: if needed, the page is edited by a fresh pass of
`agents/humaniser.md` via `step-7b-apply-gemini-recs.md`, never by Gemini directly.

Unlike VsichkiKazina/DentalVia, this check does NOT ask "does it read as human-written". It
asks whether the page reads as professionally written by a clinic's medical writer (owner
decision 2026-11-11: the pages must sound like a professional clinic, not friends chatting).

## PROMPT (verbatim — send with the finished page appended)

Act as a senior medical editor for a reputable private dental clinic, fluent in Bulgarian, with deep knowledge of LLM writing patterns. You will be given a finished Bulgarian patient-information page for ELLE Dental Clinic (elledental.bg), a dental clinic in Sofia. Evaluate whether it reads as professionally written by a clinic's medical writer: calm, precise, respectful, formal „Вие“, complete well-formed sentences, clear and predictable structure, comparable to a good national health service leaflet or a reputable private clinic website.

Flag two kinds of problem:
- Machine-writing tells: em-dashes, signposting lead-ins („Причината е проста:“, „Какво означава това:“), „не A, а B“ antitheses ending paragraphs, demonstrative crutches („Именно тази“, „точно затова“), stock connectives („освен това“, „в заключение“, „заслужава да се отбележи“), translated-sounding metaphors, filler and hedging stacks, boilerplate phrases, restating summaries.
- Unprofessional register: chatty or conversational tone, one-line fragment paragraphs, rhetorical asides, opinions or verdict lines, colloquial wording („минете на преглед“, „няма как“, „държите на“), sentences starting with „И“ or „Но“ for effect, exclamation marks, grammar or agreement errors, calques.

Do NOT flag as problems: a predictable section order, lists for steps, symptoms and risks, question-form headings, even sentence length, or medical safety qualifiers such as „обикновено“, „при повечето пациенти“, „лекарят ще прецени“.

Give me:

- A verdict with a confidence level, in exactly one of these forms: "Reads as professionally written, X% confidence" or "Shows AI or informal patterns, Y% confidence".
- The specific passages that triggered your assessment — quote the exact Bulgarian text and name the pattern.
- Concrete recommendations to make it read as professional clinic copy — specific, actionable, tied to the passages you flagged, style only.

IMPORTANT — hard rules:

- Do NOT change, question, or second-guess any medical fact, warning, risk, contraindication, number, source, link, name or date. Your job is style and register only, not fact-checking.
- Do NOT rewrite the page yourself. Recommendations only — never output a rewritten version.
- Do NOT suggest removing or softening any warning, risk or contraindication, the heading „Кога да се обадите веднага“, the placeholder {{URGENT_CARE}} or any other {{TOKEN}}. If a [VERIFY]/[DATA NEEDED] flag survives, note it as a process issue and do not touch it.

## Accept / iterate policy (used by daily-run.md Step 7)
- Normalise to one PROFESSIONAL score (0–100, higher = better): "Reads as professionally written,
  X%" → X; "Shows AI or informal patterns, Y%" → 100 − Y.
- **PASS** at professional score **≥ 80**.
- Otherwise apply the recommendations via a FRESH `agents/humaniser.md` pass
  (`step-7b-apply-gemini-recs.md`), a quick Brand Gate re-check, then re-run this check. Up to
  `MAX_GEMINI_PASSES` (2). Keep the highest-scoring version seen, never a later lower one.
- Record in the queue `gemini` column as `human <score>` if ≥ 80, else `ai <100−score>` (the
  dashboard's existing badge format; "human" here means "passed the professional check").
