---
name: profitxtra-content-pipeline
description: "ProfitXtra multi-brand article production pipeline (Content Framework v2, ported from LibreChat). Use whenever the user asks to produce, draft, or run the pipeline on an article for any ProfitXtra brand — for the Betting Family brand: bookmaker reviews, betting guides, news, or match analysis in any market (Global EN, DE, DK, SE, FI, NO, NL, CA). Runs Synthesis → Outline → Author → Humaniser → SEO → Brand Gate → light re-check as sequential fresh-context stages with file handoffs, then STOPS for mandatory human fact verification. Also covers comment moderation and lexical corpus building. MULTI-BRAND: brand=betfam (default — behavior unchanged) or brand=vsichkikazina (Всички Казина, vsichkikazina.bg — independent Bulgarian online-casino comparison site: casino reviews, bonus/wagering guides, licence news, comparisons; output in Bulgarian; no sports predictions). Every brief must declare its brand."
---

# ProfitXtra Content Pipeline (Cowork port of Content Framework v2)
# Multi-brand: Betting Family (betfam) + Всички Казина (vsichkikazina).

Source of truth for process detail: reference/team-manual-v3.1.md. This SKILL.md
tells Claude how to run that process in Cowork. The agent instruction files in
agents/ are pasted VERBATIM from the production LibreChat agents (exported
2026-09-06) — do not paraphrase them; load and follow them.

## Non-negotiable principles (from the manual — never bend)

1. FLAGS BLOCK PUBLISH. [VERIFY] / [DATA NEEDED] / [CONFLICT] flags pass through
   every stage untouched. Only the HUMAN resolves them, at Step 6, against
   primary sources. Claude never resolves a flag by guessing — not even with
   web search. Web search may be used to PRE-ASSEMBLE a verification report
   (find the primary-source URL for each flag), but the flag stays in the text
   until the human confirms.
2. UNTOUCHABLES at every stage: facts, odds, RG lines, 18+ markers, disclosures,
   counter-arguments, dates. Rephrase for voice allowed; removal never.
3. FRESH CONTEXT PER STAGE. Each stage must judge the text cold. Run each stage
   as a separate subagent/task that reads ONLY its input files — never give the
   Humaniser or Brand Gate the conversation history of the stages before it.
4. ORDER IS FIXED. Voice before SEO; gate after every editor; only the 5b light
   re-check runs after the gate, scoped to em-dash/signposting/connective/
   table/list cleanup. Nothing else edits after the gate.
5. MARKETS ARE SEALED. A DE article loads markets/de/ only (plus the global
   Model Desk canon). Never load another market's persona or canon files.
6. FIX THE FACTORY. Brand Gate FAIL → fix at the failing stage and re-run
   forward from there; never hand-patch the final text around the gate.
7. ONE OWNER. One pipeline run = one article = one working directory.

## Brand parameter (multi-brand)

Every brief MUST declare its brand: `BRAND: betfam` or `BRAND: vsichkikazina`.
A brief without a brand line → ask the user; never assume. The brand parameter
changes ONLY the file bindings and constants below — the pipeline stages, order,
principles, flags discipline, and working-directory layout are identical for
both brands.

BRAND = betfam (default — current behavior, completely unchanged):
- Gate (Stage 5): agents/brand-gate.md
- Markets: Global EN, DE, DK, SE, FI, NO, NL, CA → markets/{mkt}/author.md
  (plus the global Model Desk canon per the sealing exception)
- Content types: bookmaker reviews, betting guides, news, match analysis/predictions

BRAND = vsichkikazina (Всички Казина — vsichkikazina.bg):
- Gate (Stage 5): agents/brand-gate-vsichkikazina.md
- Market: bg ONLY → markets/bg/author.md (Stage 2). Canon is inline in that
  file. The Model Desk exception does NOT apply — this brand has no Model Desk
  and NO sports predictions of any kind; a brief requesting match tips under
  this brand is out of scope and is returned, not run.
- Output language: Bulgarian. Currency €. Regulator НАП.
- Content types: review / guide / news / comparison.
- Internal links come from this approved set only: /kak-ocenyavame/
  /zakonno-li-e/ /otgovorna-igra/ /depoziti-i-teglenia/
  /bonus-category/welcome-bonus/ /kazino-igri/
- Voice corpus files (when built): markets/bg/VOICE_BG_{type}.md, loaded at
  Stages 1.5 and 2 exactly like BetFam voice files.

Brands are sealed like markets are sealed: never load one brand's gate, author,
canon, or voice files while running the other. Shared stages (Synthesis,
Outline, Humaniser, SEO, corpus builder, moderation) are brand-agnostic and
load per-brand references only through the bindings above.

## Working directory layout (create per article)

articles/{article-slug}/
  00-brief.md            (input — human-provided or assembled with approval)
  01-synthesis.md        (report + draft + persona suggestion)
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
target query in the target language/market, fetch the FULL TEXT of the top 2-3
local-language results, and fill the brief template in prompts/step-1-synthesis.md.
NeuronWriter terms and PAA come from the user (Claude has no NeuronWriter access —
ask for the export; proceed with "none provided" only if the user says to).
Write 00-brief.md and show it for a quick confirm before running the chain.

STEPS 1 → 5b — run sequentially, each as a FRESH-CONTEXT stage:
For each stage: load the matching agents/*.md file as the stage's instructions,
fill the matching prompts/*.md template with the input files listed in the layout
above, produce the output file, and append one line to log.md. Between every
stage that edits text, DIFF ALL NUMBERS: extract every numeric token (odds,
amounts, dates, percentages) from input and output and compare — any changed or
missing number halts the run for review. This replaces the manual's
"spot-check 3 figures" with a full check.

Stage → agent file → prompt template:
1    agents/synthesis.md          prompts/step-1-synthesis.md
1.5  agents/outline-architect.md  prompts/step-1.5-outline.md
2    markets/{mkt}/author.md      prompts/step-2-author-persona.md or -editorial.md
3    agents/humaniser.md          prompts/step-3-humaniser.md
4    agents/seo-copywriter.md     prompts/step-4-seo.md
5    agents/brand-gate.md         prompts/step-5-brand-gate.md
5b   agents/humaniser.md          prompts/step-5b-humaniser-light.md

Stage-2 mode: reviews / match previews / predictions → PERSONA (bookmaker
product content always goes to the wallet persona; numbers content always to
the Model Desk / Vasquez). Guides / news / neutral reference → EDITORIAL.
Stage 2 also loads markets/{mkt}/persona_canon.md and the global
markets/modeldesk/persona_canon.md; Stage 3 loads the same canon files.
Stage-3 rule: rewrite only if verdict ≤ MIXED (< 48/60); HUMAN-LIKE passes through.
Stage-5 rule: FAIL → report to the user which stage the scorecard blames, fix
there, re-run forward. Never continue past a FAIL.

STEP 6 — STOP. MANDATORY HUMAN VERIFICATION. Claude's job here is to make the
human's 15 minutes fast, not to replace them: write 06-verification.md listing
every surviving flag and every time-sensitive claim (odds, bonuses, licence
identifiers, dates) with the primary-source URL found via web search (operator's
own site, regulator register, official league source) and what the source
currently shows. Recalculate one probability/odds/edge claim and show the
working. Then hand over: the human resolves flags, edits 05b-final-draft.md,
and says "verified" to continue. NEVER present 05b output as publishable.

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
blocks (byline, bio slot, boilerplate, dates, 18+/RG line with the market's
resource, affiliate disclosure). If CANON ADDITIONS ≠ "none" (rare), append the
rows to markets/{mkt}/persona_canon.md — the file is live, no re-upload dance.
Append the article row to content-log.md (article ID, query, market, persona,
prompt versions, humanisation score, gate score, external verdict, dates,
next revision = +2 weeks for core content).

## Side workflows

Comment moderation: agents/comment-moderator.md + prompts/comment-moderation.md.
Real reader comments only — never generate or improve comment content.
Lexical corpus building: agents/lexical-corpus-builder.md + prompts/lexical-corpus-analysis.md.
Output goes to markets/{mkt}/VOICE_{mkt}_{type}.md and is then loaded at
Stages 1.5 and 2.

## Revision cycle (core content, every 2 weeks)

Re-verify time-sensitive facts against live sources (web search + verification
report, human confirms). Update "last updated" only if something changed. Check
against current canon. Substantive edits → quick Brand Gate re-run. Log it.

## Not yet ported

markets/de/ is exported (canon is inline in author.md); the other 7 markets are pending — the 8 per-market Author agents
(~34-41k chars each, incl. personas and routing) and any canon files still live
in LibreChat and are exported one market per session. Until a market's author.md
exists here, Stage 2 for that market must run in LibreChat.
