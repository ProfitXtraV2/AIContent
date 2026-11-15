# Step 7 — External cross-model check (Gemini) — BizGrow

Canonical prompt sent to Gemini (a different model family than the writer) by
`python3 scripts/gemini_check.py <article>/05b-final-draft.md --brand bizgrow`.
**Recommendations only**: if needed, the page is edited by a fresh pass of
`agents/humaniser.md` via `step-7b-apply-gemini-recs.md`, never by Gemini directly.
**Availability:** `GEMINI_API_KEY` is set only in the cloud routine environment. A local run gets
exit code 2 and logs `external check: skipped`; see `SKILL.md` STEP 7 for the one-shot cloud
pattern.

Like ELLE Dental, this check does NOT ask "does it read as human-written". It asks whether the
page reads as professionally written by a B2B consultancy's copywriter (owner decision
2026-11-15: "professional version", formal „Вие“, no slang, no hype).

## PROMPT (verbatim — send with the finished page appended)

Act as a senior copy editor for a reputable B2B consultancy, fluent in Bulgarian and English, with deep knowledge of LLM writing patterns. You will be given a finished website page for BizGrow, a practical AI and automation consultancy for small businesses in Bulgaria. The page is in Bulgarian (formal „Вие“) or in English. Evaluate whether it reads as professionally written by the consultancy's copywriter for small-business owners: clear, concrete, calm, respectful, complete well-formed sentences, plain explanations of technical terms, a clear and predictable structure, comparable to the website of a reputable professional-services firm.

Flag two kinds of problem:
- Machine-writing tells: em-dashes, signposting lead-ins („Причината е проста:“, „Ето как:“, "Here's the thing:"), „не A, а B“ or "not just X, but Y" antitheses ending paragraphs, demonstrative crutches („Именно тази“, „точно затова“), stock connectives („освен това“, „в заключение“, „заслужава да се отбележи“, "moreover", "it's worth noting"), habitual groups of three, AI vocabulary ("delve", "leverage", "seamless", "unlock", „отключете потенциала“), translated-sounding metaphors, filler and hedging stacks, agency boilerplate („решения, съобразени с Вашите нужди“, "tailored solutions"), restating summaries.
- Unprofessional register: in Bulgarian any informal „ти“ form (singular verbs, „твоят“, „теб“, singular imperatives) or lowercase formal pronouns in direct address; chatty or salesy tone, hype words („революционен“, „магия“, "game-changing", "revolutionary"), exclamation marks, urgency or scarcity wording, one-line fragment paragraphs used for effect, rhetorical questions, opinions or verdict lines, slang, unexplained jargon, grammar or agreement errors, calques.

Do NOT flag as problems: a predictable section order, lists for services and steps, short labels on cards and buttons, question-form headings, even sentence length, honest qualifiers such as „обикновено“, „в повечето случаи“, "usually", or a clearly labelled example scenario.

Give me:

- A verdict with a confidence level, in exactly one of these forms: "Reads as professionally written, X% confidence" or "Shows AI or informal patterns, Y% confidence".
- The specific passages that triggered your assessment — quote the exact text and name the pattern.
- Concrete recommendations to make it read as professional consultancy copy — specific, actionable, tied to the passages you flagged, style only.

IMPORTANT — hard rules:

- Do NOT change, question, or second-guess any fact, number, example label, name, link, call to action or date. Your job is style and register only, not fact-checking.
- Do NOT suggest adding numbers, results, guarantees, client names, prices or any new claim.
- Do NOT rewrite the page yourself. Recommendations only — never output a rewritten version.
- Do NOT suggest removing any {{TOKEN}} placeholder (such as {{BOOKING_URL}} or {{EMAIL}}) or any label saying an example is hypothetical. If a [VERIFY]/[OWNER CONFIRM]/[DATA NEEDED] flag survives, note it as a process issue and do not touch it.

## Accept / iterate policy (used by daily-run.md Step 7)
- Normalise to one PROFESSIONAL score (0–100, higher = better): "Reads as professionally written,
  X%" → X; "Shows AI or informal patterns, Y%" → 100 − Y.
- **PASS** at professional score **≥ 80**.
- Otherwise apply the recommendations via a FRESH `agents/humaniser.md` pass
  (`step-7b-apply-gemini-recs.md`), a quick Brand Gate re-check, then re-run this check. Up to
  `MAX_GEMINI_PASSES` (2). Keep the highest-scoring version seen, never a later lower one.
- Record in the queue `gemini` column as `human <score>` if ≥ 80, else `ai <100−score>` (the
  dashboard's existing badge format; "human" here means "passed the professional check").
- Unavailable (exit 2, e.g. no `GEMINI_API_KEY` locally) → log `skipped`, `gemini` column
  `skipped`, continue.
