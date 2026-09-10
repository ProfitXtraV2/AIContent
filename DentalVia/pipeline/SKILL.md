---
name: dentalvia-content-pipeline
description: "DentalVia single-brand article production pipeline (Content Framework v2, ported from the ProfitXtra/VsichkiKazina line). Use whenever the user asks to produce, draft, or run the pipeline on an article for dentalvia.de — a German-language dental-tourism mediation agency (German/Austrian/Swiss patients → partner clinic Elle Dental Clinic in Sofia). Content types: German-language guides, comparisons, how-tos, and news on dental treatment, implants, veneers, crowns, costs, insurance reimbursement, and treatment travel to Sofia. Output in German (Sie form) only. Runs Synthesis → Outline → Author → Humaniser → SEO → Brand Gate → light re-check as sequential fresh-context stages with file handoffs, then STOPS for mandatory human fact verification. DentalVia is NOT a clinic — it arranges consultation, travel, and aftercare; the partner clinic performs the treatment."
---

# DentalVia Content Pipeline (Cowork port of Content Framework v2)
# Single-brand: DentalVia (dentalvia.de) — German dental-tourism mediation agency.

This SKILL.md tells Claude how to run the pipeline in Cowork for dentalvia.de. The
agent instruction files in agents/ and the market author in markets/de/ are the
brand's production instructions — do not paraphrase them; load and follow them.

DentalVia is a SINGLE-brand skill: there is no `BRAND:` parameter. Every brief
runs against the one brand, the one market (de), the one gate. Briefs need no
brand line.

## Non-negotiable principles (never bend)

1. FLAGS BLOCK PUBLISH. [VERIFY] / [DATA NEEDED] / [CONFLICT] flags pass through
   every stage untouched. Only the HUMAN resolves them, at Step 6, against
   primary sources. Claude never resolves a flag by guessing — not even with
   web search. Web search may be used to PRE-ASSEMBLE a verification report
   (find the primary-source URL for each flag), but the flag stays in the text
   until the human confirms.
2. UNTOUCHABLES at every stage: facts, prices, risk statements, contraindications,
   the medical disclaimer, the mediation-transparency line, sources, dates.
   Rephrase for voice allowed; removal never.
3. FRESH CONTEXT PER STAGE. Each stage must judge the text cold. Run each stage
   as a separate subagent/task that reads ONLY its input files — never give the
   Humaniser or Brand Gate the conversation history of the stages before it.
4. ORDER IS FIXED. Voice before SEO; gate after every editor; only the 5b light
   re-check runs after the gate, scoped to em-dash/signposting/connective/
   table/list cleanup. Nothing else edits after the gate.
5. THE MARKET IS SEALED. This brand serves the German market only. Stage 2 loads
   markets/de/author.md and nothing else. Canon is inline in that file. Never
   load another brand's or market's author, gate, or canon files.
6. FIX THE FACTORY. Brand Gate FAIL → fix at the failing stage and re-run
   forward from there; never hand-patch the final text around the gate.
7. ONE OWNER. One pipeline run = one article = one working directory.

## Brand constants (DentalVia — dentalvia.de)

WHO WE ARE: DentalVia is a German-language dental-tourism MEDIATION AGENCY. We
connect German, Austrian, and Swiss patients with our partner clinic, Elle Dental
Clinic in Sofia (Bulgaria), and organise the consultation, the travel, and the
aftercare around the treatment. WE ARE NOT A CLINIC and NOT a dental practice.
The partner clinic performs every treatment; DentalVia arranges the journey.
This distinction is load-bearing and never blurred in copy.

- Gate (Stage 5): agents/brand-gate-dentalvia.md
- Market: de ONLY → markets/de/author.md (Stage 2). Canon is inline in that
  file. This brand has no persona-tester mode: nobody at DentalVia treats or
  examines patients, so Stage 2 is ALWAYS editorial mode (see below).
- Output language: German only, formal address ("Sie" form), matching the live
  site. Currency €. Reference market: Germany (statutory-insurance context
  KZBV/GKV; professional bodies DGI/DGZMK).
- Brand name: always written exactly **DentalVia** in published copy.
- Content types: guide | comparison | howto | news.
- Byline/author rotation: ALWAYS one of **Georgi Todorov** or **Mario Yordanov**,
  alternating per article and tracked in `DentalVia/content-queue.md` — the next
  article takes whichever name the most recent row did NOT use; the first
  article is **Georgi Todorov**. Both are patient coordinators, NOT dentists.
  Never a team/editorial byline; never any clinical credential or fabricated
  treatment experience for either author. The Brand Gate flags any other byline.
- COMPLIANCE LINES (verbatim, both German, never reworded, never dropped):
  · Medical disclaimer, at the end of every article:
    „Dieser Beitrag dient der allgemeinen Information und ersetzt keine zahnärztliche Beratung, Diagnose oder Behandlung."
  · Mediation transparency, in the CTA/footer block of every article:
    „Wir sind eine Vermittlungsagentur und vermitteln Zahnbehandlungen bei einer Partnerklinik in Sofia. Die Behandlung führt die Partnerklinik durch; wir organisieren Beratung, Reise und Betreuung."
- Internal links + CTA rules come from `DentalVia/conversion-links.md` ONLY:
  2–5 approved internal links per article; the CTA block targets /kontakt/
  („Kostenlose Beratung"). Never invent a URL; use `[LINK NEEDED: <topic>]` for a
  page not in that registry. There is no affiliate programme — no affiliate links.
- NO FABRICATED CLINICAL EXPERIENCE: neither author has clinical qualifications.
  No „ich habe behandelt/untersucht" claims, no first-person medical judgement,
  no invented patient story with identifying detail — ever. Authority comes from
  organisational experience (travel, pricing, clinic process, logistics).

## Working directory layout (create per article)

articles/{article-slug}/
  00-brief.md            (input — human-provided or assembled with approval)
  01-synthesis.md        (report + draft)
  01.5-outline.md
  02-draft.md            (+ CANON ADDITIONS noted at the bottom)
  03-humanised.md        (+ fingerprint report)
  04-seo.md              (+ audit, title, meta, [LINK] insertions)
  05-gate-report.md      (scorecard; article updated in place if PASS WITH FIXES)
  05b-final-draft.md     (light re-check output — the pre-verification text)
  06-verification.md     (flag checklist with primary-source links, for the human)
  log.md                 (stage-by-stage run log: versions, scores, verdicts)

## Running one article

STEP 0 — BRIEF (human-owned; Claude assists).
If the user provides the brief, use it. If asked to assemble it: web-search the
target query in German, fetch the FULL TEXT of the top 2-3 German-language
results, and fill the brief template in prompts/step-1-synthesis.md. NeuronWriter
terms and PAA come from the user (Claude has no NeuronWriter access — ask for the
export; proceed with "none provided" only if the user says to). Write 00-brief.md
and show it for a quick confirm before running the chain.

STEPS 1 → 5b — run sequentially, each as a FRESH-CONTEXT stage:
For each stage: load the matching agents/*.md file (or markets/de/author.md at
Stage 2) as the stage's instructions, fill the matching prompts/*.md template with
the input files listed in the layout above, produce the output file, and append
one line to log.md. Between every stage that edits text, DIFF ALL NUMBERS: extract
every numeric token (prices, percentages, dates, success/survival rates, distances,
durations) from input and output and compare — any changed or missing number halts
the run for review. This replaces the manual's "spot-check 3 figures" with a full
check.

Stage → agent file → prompt template:
1    agents/synthesis.md          prompts/step-1-synthesis.md
1.5  agents/outline-architect.md  prompts/step-1.5-outline.md
2    markets/de/author.md         prompts/step-2-author-editorial.md
3    agents/humaniser.md          prompts/step-3-humaniser.md
4    agents/seo-copywriter.md     prompts/step-4-seo.md
5    agents/brand-gate-dentalvia.md  prompts/step-5-brand-gate.md
5b   agents/humaniser.md          prompts/step-5b-humaniser-light.md

Stage-2 mode: ALWAYS EDITORIAL. There is no tester/persona routing on this brand —
nobody reviews implants or examines patients hands-on, so no persona ever writes
from clinical experience. The article carries the rotating byline (Georgi Todorov
or Mario Yordanov, per content-queue.md) but is written in the neutral, warm
patient-guide „Sie" voice defined in markets/de/author.md. All facts / E-E-A-T /
compliance / anti-AI-style rules apply in full.
Stage-3 rule: rewrite only if verdict ≤ MIXED (< 48/60); HUMAN-LIKE passes through.
Stage-5 rule: FAIL → report to the user which stage the scorecard blames, fix
there, re-run forward. Never continue past a FAIL.

STEP 6 — STOP. MANDATORY HUMAN VERIFICATION. Claude's job here is to make the
human's 15 minutes fast, not to replace them: write 06-verification.md listing
every surviving flag and every time-sensitive or medical claim (prices, „Stand
MM/JJJJ" dates, success/survival rates, insurance-reimbursement figures, source
citations) with the primary-source URL found via web search (professional body,
manufacturer, KZBV/GKV, peer-reviewed study) and what the source currently shows.
Recalculate one price/savings claim and show the working. Then hand over: the
human resolves flags, edits 05b-final-draft.md, and says "verified" to continue.
NEVER present 05b output as publishable.

STEP 7 — EXTERNAL CHECK. The original uses a Gemini agent as a cross-model
calibration probe. Cowork cannot call Gemini. Options, in order of fidelity:
(a) the user runs Step 7 in LibreChat and pastes the recommendations back —
then apply prompts/step-7b-apply-gemini-recs.md via a fresh Humaniser stage and
do a quick Brand Gate re-check; (b) run agents/external-check-gemini.md as a
fresh-context Claude subagent that sees ONLY the final article (weaker: same
model family as the writer — say so in log.md); (c) skip, per the manual's own
plan to retire this step after ~30-50 articles. Ask the user which, remember
the answer for the session. Never apply an external rewrite directly —
recommendations only, through the Humaniser.

STEP 8 — PUBLISH & LOG (human-owned; Claude assists). Assemble the template
blocks (rotating byline, author-bio slot, boilerplate, published/updated dates,
the verbatim medical disclaimer, the verbatim mediation-transparency line in the
CTA block). If CANON ADDITIONS ≠ "none" (rare), append the rows to
markets/de/author.md — the file is live, no re-upload dance. Append the article
row to content-queue.md (id, type, byline, query, keywords, volume/kd, folder,
prompt versions, humanisation score, gate score, external verdict, dates) and
flip the rotating byline for the next article.

## Revision cycle (core content, every 2 weeks)

Re-verify time-sensitive facts against live sources (web search + verification
report, human confirms): prices („Stand MM/JJJJ"), insurance-reimbursement
figures, cited success/survival rates, source availability. Update "last updated"
only if something changed. Check against current canon. Substantive edits → quick
Brand Gate re-run. Log it.

## Fresh-context discipline (reminder)

Never chain the stages in one conversation. Each editing stage — Author,
Humaniser, SEO, Brand Gate, 5b light re-check — runs as its own task that reads
only its declared input files, so it judges the text cold and cannot inherit an
earlier stage's rationalisations. This is what makes the gate trustworthy.
