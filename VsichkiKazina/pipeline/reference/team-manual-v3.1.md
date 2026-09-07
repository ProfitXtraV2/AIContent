# **Betting Family Content Production — Team Manual v3.0**

*The complete operating guide: LibreChat setup, step-by-step production, canon maintenance. New team members: read fully once (~25 min). Daily use: Section 4 + the cheat sheet.*

**Version 3.0 | Last updated: [DATE] | Owner: Plamen** **Changes from v2.0:** LibreChat deployment instructions; process diagram; NeuronWriter added to Step 0; canon workflow explained in full (CANON ADDITIONS); Gemini step reframed as time-limited calibration probe; multi-market structure (local duos + global Model Desk).

## **1. WHAT THIS SYSTEM IS**

We produce betting content (bookie reviews, guides, news, match analysis) across seven markets using a chain of specialised LLM agents in LibreChat. Each agent does one job. Humans own two things the machine never owns: **fact verification** and **final judgment**.

Every published article must be: (a) factually verified by a human against primary sources, (b) written in a consistent local author voice, (c) semantically complete for its target query, (d) compliant with brand, E-E-A-T and responsible gambling rules, and (e) checked for AI-writing fingerprints by two independent evaluators.

## **2. THE PROCESS DIAGRAM**

           ┌─────────────────────────────────────────────────────┐

            │  STEP 0 · HUMAN · Brief & sourcing                  │

            │  query + market + NeuronWriter export               │

            │  + full text of top 2-3 local SERP articles         │

            └────────────────────────┬────────────────────────────┘

                                     ▼

            ┌─────────────────────────────────────────────────────┐

            │  STEP 1 · AGENT · BetFam Synthesis                  │

            │  original SME draft + fact inventory + report       │

            │  ⚑ flags born here: [VERIFY] [CONFLICT]             │

            └────────────────────────┬────────────────────────────┘

                       human reads report (5 min)

                                     ▼

            ┌─────────────────────────────────────────────────────┐

            │  STEP 1.5 · AGENT · BetFam Outline/Architect        │

            │  solves STRUCTURE before any prose is written:      │

            │  H1-H4, per-section facts/terms/direction/shape,    │

            │  deliberately varied section shapes (anti-template) │

            └────────────────────────┬────────────────────────────┘

                                     ▼

            ┌─────────────────────────────────────────────────────┐

            │  STEP 2 · AGENT · BetFam Author — [market]          │

            │  follows the outline · writes full persona prose    │

            │  reads persona canon (attached) → article in voice  │

            │  outputs CANON ADDITIONS list                       │

            └────────────────────────┬────────────────────────────┘

                                     ▼

            ┌─────────────────────────────────────────────────────┐

            │  STEP 3 · AGENT · BetFam Humaniser                  │

            │  fingerprint score /60 → rewrite only if ≤ MIXED    │

            └────────────────────────┬────────────────────────────┘

                                     ▼

            ┌─────────────────────────────────────────────────────┐

            │  STEP 4 · AGENT · BetFam SEO                        │

            │  entity audit vs NeuronWriter terms → optimise      │

            │  + title tag + meta + internal links                │

            └────────────────────────┬────────────────────────────┘

                                     ▼

            ┌─────────────────────────────────────────────────────┐

            │  STEP 5 · AGENT · BetFam Brand Gate                 │

            │  scorecard /100 → PASS / PASS WITH FIXES / FAIL ────┼──► FAIL: fix at the

            └────────────────────────┬────────────────────────────┘    failing step,

                                     ▼                                  re-run forward

            ┌─────────────────────────────────────────────────────┐

            │  STEP 5B · AGENT · BetFam Humaniser (light re-check)│

            │  narrow scan only — em-dash/signposting/connectives │

            │  catches tells SEO/Brand Gate may have reintroduced │

            │  usually returns unchanged · seconds to run         │

            └────────────────────────┬────────────────────────────┘

                                     ▼

            ┌─────────────────────────────────────────────────────┐

            │  STEP 6 · HUMAN · Verification (~15 min, MANDATORY) │

            │  resolve ALL ⚑ flags vs primary sources             │

            │  re-verify odds/bonuses/licences · recalc one maths │

            │  claim · read aloud                                 │

            └────────────────────────┬────────────────────────────┘

                                     ▼

            ┌─────────────────────────────────────────────────────┐

            │  STEP 7 · AGENT · BetFam External Check (Gemini)    │

            │  recommendations ONLY ──► back through Humaniser    │

            │  (calibration probe — log disagreements)            │

            └────────────────────────┬────────────────────────────┘

                                     ▼

            ┌─────────────────────────────────────────────────────┐

            │  STEP 8 · HUMAN · Publish & log                     │

            │  template blocks · NeuronWriter score check         │

            │  CANON ADDITIONS → canon file → RE-UPLOAD to agents │

            │  content log entry · set +2-week revision           │

            └─────────────────────────────────────────────────────┘

   RULES THAT SPAN THE DIAGRAM

   ⚑ flags pass through untouched until a HUMAN resolves them (Step 6)

   ✋ untouchables at every step: facts · odds · RG lines · 18+ · disclosures ·

      counter-arguments · dates

   ▣ one article = one chat per agent · one owner Step 0→8 · markets sealed

## **3. LIBRECHAT SETUP (one-time, per market)**

### **3.1 The agents to create**

In LibreChat → Agents → Create Agent. For each: paste the agent file's body (everything BELOW the --- frontmatter block — the frontmatter is not for LibreChat) into **Instructions**.

| **LibreChat agent name** | **Source file** | **Model / temp** | **Attach files** |
| --- | --- | --- | --- |
| BetFam Synthesis | serp-synthesis-agent.md | Claude Sonnet / 0.4 | — |
| BetFam Outline/Architect | AGENT_outline_architect.md | Claude Sonnet / 0.5 | — |
| BetFam Comment Moderator | AGENT_comment_moderator.md | Claude Sonnet / 0.2 | — |
| BetFam Lexical Corpus Builder | AGENT_lexical_corpus_builder.md | Claude Sonnet / 0.4 | (periodic, human-run, not in per-article pipeline) |
| BetFam Author — [MARKET] (v2.0) | author-agent.md + that market's full persona master prompts pasted below it | Claude Sonnet / 0.9 | persona_canon_[market].md + persona_canon_modeldesk.md |
| BetFam Humaniser | ai-humanisation-agent.md | Claude Sonnet / 0.9 | same canon files as the Author agent |
| BetFam SEO | seo-copywriter-agent.md | Claude Sonnet / 0.4 | — |
| BetFam Brand Gate | betfam-brand-agent.md | Claude Sonnet / 0.3 | betting_family_brand_master_prompt.md (localised version) |
| BetFam External Check | AGENT_gemini_external_check.md | **Gemini** / 0.3 | — |

**Per-market cloning:** each market gets its OWN Author and Humaniser agents with ONLY that market's persona prompts and canon attached (+ the global Model Desk canon). Never attach another market's canon — this physically enforces market sealing. Synthesis, SEO, Brand Gate and External Check are shared across markets (Brand Gate gets the localised brand file per market).

### **3.2 Knowledge files — the RAG warning**

Attached files in LibreChat may be retrieved as chunks (RAG), not full text. Therefore:

- **Persona master prompts and brand rules go INTO Instructions** (always fully active), never only as attachments.

- **Canon files are fine as attachments** — chunk retrieval of the relevant persona's memories is the desired behaviour.

- Test your install once: ask the Author agent to quote a specific Tier 3 rule from the canon. If it can't, ask the admin about full-context file options.

### **3.3 Versioning**

All prompt files live in the git repo — that is the source of truth. To patch a prompt: commit in git → update the LibreChat agent's Instructions → bump the version in the agent's name. The content log records prompt versions per article; "which version wrote this?" must always be answerable.

## **4. PRODUCING ONE ARTICLE (step by step)**

Rule for every step: **new chat, select the agent from the dropdown, paste the input.** One article = one chat per agent. Never two articles in one chat.

### **STEP 0 — Brief ****&**** sourcing (human, ~20 min)**

- Pick target query + market. **Check the content map:** if we already rank for this or a sibling query → update that article instead.

- Run the query through **NeuronWriter** (correct language/location). Export: term/entity list, PAA questions, competitor list, competitive score range (note the average of positions 1-3).

- Take the **full text** of the top 2-3 local-language sources (NeuronWriter terms carry no facts — the synthesis agent needs actual claims).

- Assemble the brief:

QUERY: [exact query]            MARKET: [language / country]

BYLINE: [persona / editorial]   (see guide below — leave blank to let the agent infer)

INTENT NOTE: [one line]

NEURONWRITER TERMS: [paste term/entity export]

PAA QUESTIONS: [paste]

KNOWN ISSUES IN SOURCES: [anything stale/wrong you spotted, or "none"]

SOURCES:

--- SOURCE 1 [URL] --- [full text]

--- SOURCE 2 [URL] --- [full text]

**BYLINE guide — which mode for which content:**

| **Content type** | **Byline** |
| --- | --- |
| Bookmaker reviews (Betano, bet365…) | **persona** — lived testing is the credibility; a neutral review is just a spec sheet |
| Match analysis, tactical previews | **persona** |
| Model picks, predictions, transparency reports | **persona** (always Model Desk / Vasquez) |
| Strategy / system / concept guides ("what is a Martingale", "how do Asian handicaps work") | **editorial** — reference content, neutral |
| News | **editorial** |
| Neutral comparison / reference / legal-regulatory pages | **editorial** |

Editorial mode = the neutral "Betting Family Editorial Team" house voice: no author personality, no first person, no invented experience — but every brand, E-E-A-T, fact and responsible-gambling rule still fully applies. Neutral, not compliance-light.

### **STEP 1 — BetFam Synthesis**

Paste the brief. You get: synthesis report + original draft + persona suggestion. **Before moving on (5 min):** read the [CONFLICT] flags and the "claims excluded as dubious" list — confirm you agree. If any passage feels like it echoes a source: *"**Rewrite section X from scratch — it tracks Source N too closely.**"*

### **STEP 1.5 — BetFam Outline/Architect**

Paste the Synthesis report + draft + the original brief. You get a structural skeleton: H1, section-by-section facts/terms/direction/length-shape, signature element placement, opening/closing direction. **This is the agent that actually fixes the ****"****every paragraph reads the same****"**** problem** — it assigns deliberately uneven section shapes before any prose exists, so Author isn't simultaneously inventing structure and writing voice. Skim it for one thing: does the section-shape variety look genuinely uneven (not three same-shaped sections in a row)? If it looks too uniform, ask it to vary two sections before moving on.

### **STEP 2 — BetFam Author — [market]**

**Persona mode:** Paste the outline + the draft + use the saved "Step 2 Author (PERSONA)" prompt. Fill in persona name and market. Override the synthesis agent's suggestion if you disagree — bookmaker product content ALWAYS goes to the wallet persona. **Editorial mode:** Use the "Step 2 Author (EDITORIAL)" prompt. You get the article. **Check:**

- Persona mode: signature elements present? (Each persona's named device + verdict label / withdrawal test / closer.) Scroll to the bottom: find **CANON ADDITIONS** — in the new default (no-anecdote) it will almost always say "none." If it lists something, save those lines for Step 8. Canon is now read to avoid *contradicting* fixed facts, not to generate new stories.

- Quick scan: does the article invent a personal memory or backstory that wasn't in the brief? If yes, flag it — the no-anecdote default should have prevented it. Real documented testing receipts (withdrawal timestamps, amounts) are fine and expected in reviews; invented life stories are not.

- Editorial mode: no first person, no invented experience, no persona devices, byline reads "Editorial Team", CANON ADDITIONS = "none".

### **STEP 3 — BetFam Humaniser**

Paste the article + *"**Phase 1 evaluation first. Rewrite only if MIXED or worse. Persona: [X].**"* HUMAN-LIKE → move on. Rewrite happened → spot-check 3 numbers against the Step 2 version.

### **STEP 4 — BetFam SEO**

Paste the article + *"**Target query: [query]. Market: [market]. NeuronWriter terms: [paste list]. Audit then optimise; preserve the persona voice.**"* You get audit + optimised article + title/meta + [LINK] insertions. **Reject any insertion that is filler** — a missing entity with no facts behind it should have been [DATA NEEDED].

### **STEP 5 — BetFam Brand Gate**

Paste the article. PASS → continue. PASS WITH FIXES → skim the change log, continue. **FAIL → never hand-patch around the gate**: fix at the step the scorecard blames, re-run forward from there.

### **STEP 5B — BetFam Humaniser (light re-check)**

Paste the article + the "Step 5b Humaniser (Light Re-check)" saved prompt. SEO and Brand Gate both edit/insert text, and either can quietly reintroduce an AI tell into a sentence they touched. This pass scans for: em-dashes (fully removed at this final stage, replaced with hyphen-dashes/commas/colons), signposting lead-ins, banned connectives, freshly repeated paragraph shapes, **over-polished tables** (converts simple-fact tables to prose - keeps tables only where genuine side-by-side comparison is needed), and **excessive bullet lists** (converts short enumerable lists to prose - keeps lists only for real sequential steps or long enumerations). It must not touch facts, SEO insertions, links, title/meta, or any Brand Gate compliance fix - every figure converted from a table/list to prose must survive exactly. If nothing's flagged, it returns unchanged - that happens often. Cheap insurance; takes seconds to a minute.

### **STEP 6 — HUMAN VERIFICATION (~15 min, cannot be skipped or delegated)**

- Resolve **every** [VERIFY] / [DATA NEEDED] / [CONFLICT] against a **primary source** (bookmaker's own site, regulator register, official club/league source). Replace the flag with the verified fact. No flag survives to publish.

- Independently re-verify time-sensitive data even if unflagged: odds, bonus amounts, rollover terms, licence numbers.

- Recalculate one probability/odds/edge claim.

- Read the article aloud — you are the free final fingerprint detector. Press-release passages go back to Step 3, quoted.

### **STEP 7 — BetFam External Check (Gemini) — calibration probe**

Set up once: paste AGENT_gemini_external_check.md into the Gemini agent's Instructions field. Per article, just paste the article — the agent already knows to give a verdict + specific patterns + **recommendations only, no rewrite, no fact changes**.

- Clean verdict → proceed.

- Recommendations → paste them into the **Humaniser**: *"**Apply these external recommendations. Facts, odds, disclosures, RG lines untouchable. Persona: [X].**"* Quick Brand Gate re-check after.

- **Never publish Gemini's own rewritten text.**

- Log agree/disagree vs our Humaniser verdict in the content log. *This step is time-limited: after ~30-50 articles we review the disagreement data and either harvest its patterns into the Humaniser and drop the step, or replace it with a statistical detector.*

### **STEP 8 — Publish ****&**** log**

- Optional: paste the final article into NeuronWriter for the score. Target the competitive range of the current top 3 — **the score is a guardrail, not a target**; never term-stuff to chase 90+. Brand Gate beats NeuronWriter whenever they conflict.

- Assemble in the template: article + byline + author bio + brand boilerplate + dates + 18+/RG line (market's resource) + affiliate disclosure where relevant.

- **Canon logging (same day — usually skipped now):**

- Check the CANON ADDITIONS from Step 2. With the no-anecdote default, this will almost always say "none" — if so, skip the rest of this step entirely.

- If it listed something (a specific invented detail from an explicitly-briefed anecdote): open persona_canon_[market].md → find that persona's Tier 2 table → add a row: next ID, the detail in one sentence, article ID, reuse note.

- **RE-UPLOAD the updated canon file to that market's Author AND Humaniser agents in LibreChat** (edit agent → remove old attachment → upload new). Only re-upload if the file actually changed — uploading an unchanged file wastes time and doesn't help.

- Content log entry: article ID, query, market, persona, prompt versions, humanisation score, Gemini verdict (+agree/disagree), NeuronWriter score, publish date, next revision date (core content = +2 weeks).

## **4.5 TWO AGENTS OUTSIDE THE PER-ARTICLE PIPELINE**

**BetFam Comment Moderator** — used whenever readers submit comments under a published article. Paste a real submitted comment + the article it's under; get back APPROVE / REJECT / FLAG, with a reason. **This agent never writes comment content.** It only triages genuine reader submissions — spam/abuse get rejected, PII gets flagged for redaction, genuine criticism (including criticism of our own articles) gets approved unedited, problem-gambling signals get flagged for a human's supportive reply. Real testimonials/comments only — Betting Family never publishes fabricated reader content under any framing.

**BetFam Lexical Corpus Builder** — run occasionally, not per article, by whoever owns a market's voice quality. Paste in a batch of real native-language betting content (real forum posts, real published reviews, genuine community writing — never AI-generated). It extracts two things: new confirmed AI-tells for that market's AI_TELLS_[market].md, and genuine human voice patterns (real sentence rhythm, real paragraph shapes, how real writers actually express opinion) for a new AUTHENTIC_VOICE_[market].md file. This is the positive complement to the AI-tell ban lists — it gives the Author agent something to emulate, not just things to avoid. Fold its output into the relevant files manually, then re-paste the updated FINAL_author_[market].md into that market's agent.

## **5. THE TWO-WEEK REVISION CYCLE (core content)**

- Re-verify all time-sensitive facts against live sources; update the "last updated" date only if something actually changed.

- Check the article against the **current** canon — post-publish edits are where drift sneaks in.

- Substantive text changes → quick Brand Gate re-run.

- Log the revision.

## **6. GOLDEN RULES (never bend)**

- **Flags block publish.** Resolved by humans with primary sources only.

- **Facts are sacred at every transition.** Spot-check 3 figures after every stage that edits text.

- **Order is fixed.** Voice before SEO; gate after every editor; **one narrow Humaniser re-check (5b) is the only thing permitted after the gate**, scoped to em-dash/signposting/connective cleanup only — it touches nothing else; Gemini recommendations come back through OUR Humaniser; nothing else edits after the gate.

- **Top-ranking ≠ correct.** Read the synthesis report's excluded-claims section every time. NeuronWriter measures similarity to what ranks — our edge is covering that PLUS the gaps it missed.

- **Untouchables:** RG lines, 18+ markers, disclosures, counter-arguments, dates. Rephrase fine; removal never, by anyone, at any step.

- **One owner per article, Step 0→8.** Handoffs lose flags.

- **Canon before invention; log same day; re-upload after logging.** Contradictions are fixed in the article, never in the canon.

- **Markets are sealed.** Local sources, local personas, local canon — agents per market carry only their own files. The Model Desk (Vasquez) is the single global exception, with its single global canon.

## **7. TROUBLESHOOTING**

| **Symptom** | **Likely cause** | **Fix** |
| --- | --- | --- |
| Humanisation score repeatedly MIXED for one persona | Persona prompt drifting | Report to Plamen → patch the Author agent's Instructions, bump version |
| Brand Gate flags the same defect 3 articles running | Upstream prompt gap | Same — fix the factory, not every product |
| Persona tells a memory you don't recognise | Unlogged invention, or stale canon upload | Check canon file vs what's uploaded to the agent; log or re-upload |
| Two articles contradict a memory | Canon not checked / re-upload skipped | Errata log → pick surviving version → align older article at next revision |
| Draft echoes a source's structure | Too few sources / one dominates | Re-run Step 1 with restructure instruction; ensure 2-3 full sources pasted |
| Gemini and Humaniser disagree strongly | Different model blind spots (expected) | Apply Gemini's specific recommendations via our Humaniser; log the disagreement — it's calibration data |
| Agent invents a licence number / withdrawal time | Flag discipline removed or stale prompt version | **Stop the line.** Severity-1: check prompt versions vs content log |
| SEO step added filler paragraphs | Missing entity with no facts available | Reject the insertion — should have been [DATA NEEDED]; note for prompt patching |
| NeuronWriter score low but Brand Gate passed | Gaps strategy working OR genuine entity misses | Check the SEO audit's missing-entities list; if entities were skipped for lack of facts, source the facts — don't stuff terms |

## **8. CHEAT SHEET (print this)**

0 BRIEF      query + market · NeuronWriter export · top 2-3 LOCAL sources (full text)

1 SYNTHESIS  → draft + report. READ conflicts + excluded claims

1.5 OUTLINE  → structure: H1, per-section facts/terms/direction/shape. Check

              shape variety looks genuinely uneven, not repeated

2 AUTHOR     → persona article, following the outline. CHECK signature elements

              + note CANON ADDITIONS

3 HUMANISE   → /60. Rewrite only if ≤ MIXED. Spot-check 3 facts after

4 SEO        → audit vs NW terms + optimised + title/meta. Reject filler

5 BRAND GATE → /100. FAIL = fix upstream, re-run. Never hand-patch around it

5B HUMANISE  → light re-check only (em-dash/signposting/connectives). Usually

              returns unchanged — seconds, not a full re-evaluation

6 HUMAN      → resolve ALL flags vs PRIMARY sources · re-verify odds/bonuses/

              licences · recalc one maths claim · read aloud

7 GEMINI     → recommendations ONLY → back through OUR Humaniser → quick gate

              re-check · log agree/disagree (calibration probe)

8 PUBLISH    → NW score = guardrail not target · template blocks · CANON LOG +

              RE-UPLOAD canon to agents · content log · +2wk revision

ONE ARTICLE = ONE CHAT PER AGENT · ONE OWNER 0→8 · MARKETS SEALED

UNTOUCHABLES: facts · odds · RG · 18+ · disclosures · counter-args · dates

FLAGS BLOCK PUBLISH: [VERIFY] [DATA NEEDED] [CONFLICT]

HUMAN OWNS: Step 0 + Step 6 (+ canon logging). Step 6 is never optional.