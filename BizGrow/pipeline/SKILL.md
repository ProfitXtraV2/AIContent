---
name: bizgrow-content-pipeline
description: "BizGrow page pipeline — PAUSED at onboarding on 2026-11-15, manual trigger only, do not run until the owner un-pauses it in writing. BizGrow is a practical AI and automation consultancy for small businesses in Bulgaria (Next.js static site, Bulgarian at /, English at /en/). Rewrites an existing page (page-rewrite) or drafts a page listed in BizGrow/keyword-map.md (new-page), as a Markdown content file with TOML front matter that a human ports into the site's TypeScript dictionaries. B2B claim rules, professional voice in formal „Вие“ (plain professional English on /en/). Synthesis → Outline → Author → Professional edit → SEO → Brand Gate → light re-check → verification + content file → Gemini check, then STOPS for the human."
---

> ## ⏸ PAUSED — at onboarding on 2026-11-15
> **Manual trigger only. Do not run this pipeline, and do not schedule it, until the owner
> un-pauses it in writing.** On 2026-11-15 the owner's session asked for the BizGrow pipeline
> only ("do NOT write any site copy yet"). If you were asked to run it and there is no written
> un-pause from the owner (dated after 2026-11-15), stop and say so. How to un-pause: see the
> banner at the top of `BizGrow/automation/daily-run.md`.

# BizGrow Content Pipeline (port of the ELLE Dental professional-register line)
# Single brand: BizGrow — AI and automation consultancy for small businesses in Bulgaria.

This file tells Claude how to run the pipeline for the BizGrow site. The agent files in
`agents/`, the market authors in `markets/bg/author.md` and `markets/en/author.md`,
`reference/site-rules.md` and `reference/verification-policy.md` are the brand's production
instructions: load and follow them, do not paraphrase them.

Single brand, two locales (`bg` default at `/`, `en` at `/en/`), single gate. No `BRAND:`
parameter, no byline, no persona.

## Why this brand uses the professional register, not the casino humaniser (owner decision 2026-11-15)

The VsichkiKazina/DentalVia humaniser makes reviews read like a person wrote them: burstiness,
fragments, opinions, an "imperfection budget", informal drops and asides, and a /60
human-likeness score. ELLE Dental replaced that with a professional clinic register
(2026-11-11). BizGrow takes the ELLE Dental machinery and sets the register for a B2B
consultancy talking to small-business owners ("professional version", owner decision
2026-11-15):

- Formal **„Вие“** throughout the Bulgarian pages, capitalised in direct address
  (Вие/Ви/Вас/Ваш/Вашия). No „ти“ forms anywhere, including headings, CTAs and FAQ. The current
  site copy uses „ти“ („Открий“, „твоят бизнес“, „попълваш“); every page-rewrite converts it.
- Complete sentences, clear and concrete; no slang, no fragments as a style device, no
  burstiness, no opinions or verdict lines, no hype („революционен“, „магия“ …), no jargon
  without a plain explanation on first use.
- `agents/humaniser.md` keeps ONLY the de-AI checks (banned AI vocabulary, em-dashes,
  signposting, triads, „не A, а B“, boilerplate, filler) and replaces the /60 score with a
  professional-quality check.
- Not YMYL-medical: ELLE Dental's clinical safety, urgent-care and doctor-review rules are
  removed. In their place: **B2B claim rules** (no invented numbers; an outcome figure only when
  it is labelled as an estimate or example, or sourced; no guarantees of rankings, leads,
  revenue or savings; GDPR statements only as the owner states them).
- The Brand Gate checks the facts allowed list, banned claims, the register (no „ти“), CTA rules
  and one-term-per-page against `BizGrow/keyword-map.md`.
- The Gemini step 7 judges "reads as professionally written by a consultancy's copywriter",
  not "human-written".

Do not import burstiness, fragment, opinion, imperfection or informal-register rules from the
other brands, and do not import ELLE Dental's medical rules, into any BizGrow stage.

## Non-negotiable principles

1. **AI TEXT IS A DRAFT.** Nothing goes live until the human ports it into the site and the
   owner approves it. The pipeline never edits the `biz-grow` repo.
2. **ONLY CANON FACTS ABOUT BIZGROW.** Services, process, audience and policies come only from
   the canon in `markets/bg/author.md` (owner-confirmed 2026-11-15). Prices, team names, legal
   data, address, phone, client names and case results are UNKNOWN and are never stated.
3. **NO INVENTED NUMBERS.** Every figure is either canon (48 часа, 30 минути, обикновено до 2
   седмици), a clearly labelled hypothetical example/estimate, or a sourced external fact in
   `[[sources]]` (max 3 new sourced facts per page, `reference/verification-policy.md`).
4. **EXAMPLE SCENARIOS STAY HYPOTHETICAL.** Any "what the result looks like" content keeps an
   explicit label that it is an example, not a client result.
5. **NO GUARANTEES.** No promise of rankings, traffic, leads, revenue, savings or response times
   beyond canon. Banned claims and hype per `reference/site-rules.md` §2.
6. **NOTHING LOST ON A REWRITE.** Every CTA, `{{TOKEN}}`, anchor, canon fact, label and FAQ on
   the current page survives every stage (inventory diff at every editing stage), unless the
   brief lists it under REMOVE-BY-BRIEF with the owner's instruction.
7. **ONE MAIN TERM PER PAGE.** From `BizGrow/keyword-map.md`; no page targets another page's term.
8. **FRESH CONTEXT PER STAGE; ORDER IS FIXED; FIX THE FACTORY**: each stage is a separate
   subagent reading only its inputs; a Gate FAIL is fixed at the failing stage and re-run
   forward, never hand-patched.
9. **THE PIPELINE NEVER WRITES TO THE SITE REPO.** It delivers `content/<slug>.md` in a PR here;
   a human ports it into `site/src/i18n/dictionaries/{bg,en}.ts` and the page components, then
   runs the site's lint, type check and build.

## Brand constants (BizGrow)

- Business: BizGrow, practical AI and automation consultancy/agency for small businesses in
  Bulgaria. Brand name always in Latin script „BizGrow“ (in BG text it is marked `lang="en"` by
  the site; the pipeline just writes „BizGrow“).
- Site: Next.js static export. Bulgarian (default) at `/`, English at `/en/`. Copy lives in typed
  dictionaries `site/src/i18n/dictionaries/bg.ts` and `en.ts` in the `biz-grow` repo
  (`desislavamit/biz-grow`; local `~/Work/biz-grow`). Brand spec: `docs/ai-consultancy-spec.md`.
- Language: Bulgarian, formal „Вие“ (capitalised), BizGrow professional voice; English pages in
  plain professional English (`markets/en/author.md`). No em-dashes in either language.
- Content types: `page-rewrite` (an existing page: `/` or `/en/`) | `new-page` (only an address
  listed in `BizGrow/keyword-map.md` with status `planned`, i.e. approved by the owner or the
  owner's session).
- Gate: `agents/brand-gate-bizgrow.md`. Market authors: `markets/bg/author.md`,
  `markets/en/author.md`.
- Links: `BizGrow/conversion-links.md` (pages, section anchors, `{{BOOKING_URL}}`, `{{EMAIL}}`).
- Keyword map: `BizGrow/keyword-map.md` (one main term per address; filled by the owner's
  session; empty at onboarding).
- Output: `content/<slug>.md`, Markdown with TOML front matter (title, meta_description, h1,
  slug, locale, primary_keyword, secondary_keywords, [[sections]], [[faq]], [[sources]],
  [[owner_items]]). Format in `reference/site-rules.md` §8 and
  `templates/content-file-template.md`. A human ports it into the TS dictionaries.

## Working directory layout (one per page)

articles/{YYYY-MM-DD}-{slug}/
  00-brief.md            (from templates/00-brief-template-bizgrow.md)
  00-current.md          (page-rewrite: the current copy, verbatim, from the dictionary file(s)
                          and page component(s), with the biz-grow commit sha)
  00-inventory.md        (every CTA, token, anchor, canon fact, number, label, FAQ and
                          hypothetical-example label on the current page)
  01-synthesis.md
  01.5-outline.md
  02-draft.md
  03-humanised.md        (professional-quality report + edited page)
  04-seo.md              (audit, title, meta, FAQ, links)
  05-gate-report.md
  05b-final-draft.md     (light re-check output; still carries flags)
  06-verification.md     (sources fetched, owner items raised, self-check table)
  content/{slug}.md      (THE DELIVERABLE: Markdown + TOML front matter, no flags)
  07-gemini-check-N.md   (Step 7 verdicts)
  log.md

Slugs: `home` = `/` (bg), `en-home` = `/en/` (en). New pages use the slug listed in
`keyword-map.md`, with an `en-` prefix for English.

## Running one page

STEP 0 — BRIEF. Confirm the pause has been lifted in writing (else stop). Read the current copy
from the `biz-grow` repo (`desislavamit/biz-grow`, branch `main` unless the owner names another):
`site/src/i18n/dictionaries/<locale>.ts`, the page component(s) that render it
(`site/src/components/*.tsx`, `site/src/app/(bg|en)/…/page.tsx`), `site/src/i18n/config.ts`
(booking URL and email that the tokens stand for) and `docs/ai-consultancy-spec.md`. Write
`00-current.md` (verbatim + commit sha) and `00-inventory.md`. Fill `00-brief.md` (main term from
`BizGrow/keyword-map.md`, Ahrefs metrics from `topic-backlog.md`, buyer questions from a web
search of the main term in the page's language). If the site repo cannot be read for a
page-rewrite, STOP. If the page has no main term in `keyword-map.md`, STOP and ask for one.

STEPS 1 → 5b — sequential, each a FRESH-CONTEXT stage:
1    agents/synthesis.md              prompts/step-1-synthesis.md
1.5  agents/outline-architect.md      prompts/step-1.5-outline.md
2    markets/<locale>/author.md       prompts/step-2-author-editorial.md
3    agents/humaniser.md              prompts/step-3-humaniser.md      (edit only if NEEDS EDIT)
4    agents/seo-copywriter.md         prompts/step-4-seo.md
5    agents/brand-gate-bizgrow.md     prompts/step-5-brand-gate.md     (FAIL → fix upstream)
5b   agents/humaniser.md              prompts/step-5b-humaniser-light.md
Between every stage that edits text, DIFF THE INVENTORY: every `00-inventory.md` item must still
be present with the same meaning; any missing or weakened item halts the page for review.

STEP 6 — VERIFICATION + CONTENT FILE: `prompts/step-6-content-file.md`. Checks sources, turns
flags into `[[owner_items]]`, assembles `content/<slug>.md`, runs the self-check.

STEP 7 — GEMINI PROFESSIONAL-REGISTER CHECK:
`python3 scripts/gemini_check.py <dir>/05b-final-draft.md --brand bizgrow`
(`prompts/step-7-gemini-check.md`). Below 80 → `prompts/step-7b-apply-gemini-recs.md` via a fresh
humaniser pass, Gate re-check, rebuild the content file, re-check; ≤ 2 passes; keep the best.
Unavailable → log `skipped`, continue.
**Where it works:** `GEMINI_API_KEY` exists only in the cloud routine environment, not on the
local machine. A local manual run therefore logs `external check: skipped (no GEMINI_API_KEY
locally)`. To get the check for a local run, use the one-shot RemoteTrigger pattern used for the
other brands (snapshot the page into this repo on a branch, trigger a one-off cloud run that
executes only Step 7, read its verdict back), with a pinned judge model.

STEP 8 — IMAGES: none by default (`prompts/step-8-images.md`).

THEN STOP. The human reviews the PR, ports `content/<slug>.md` into the site's dictionaries and
components, runs `npm run lint`, `npx tsc --noEmit` and `npm run build` there, and sends the
page and its `[[owner_items]]` to the owner. Merge of the AIContent PR records that the draft
was accepted for porting; it never means "approved by the owner" or "live".
