---
name: elledental-content-pipeline
description: "ELLE Dental (elledental.bg) page pipeline — PAUSED by the owner on 2026-11-11, manual trigger only, do not run until the owner un-pauses it in writing. Bulgarian dental clinic in ж.к. Света Троица, София (Д-р Елена Манолова, Д-р Теодора Янчева). Rewrites one of the site's 28 existing pages (page-rewrite) or, only on owner approval, drafts a new page (new-page), as a WebPortals-ready content/<slug>.md file (TOML front matter) for doctor review. YMYL medical rules, professional clinic voice in formal „Вие“. Synthesis → Outline → Author → Professional edit → SEO → Brand Gate → light re-check → verification + content file → Gemini check, then STOPS for the human and the doctor."
---

> ## ⏸ PAUSED — by owner on 2026-11-11
> **Manual trigger only. Do not run this pipeline, and do not schedule it, until the owner
> un-pauses it in writing.** The owner asked: "add this site to contentAI pipeline, but pause
> it for now". If you were asked to run it and there is no written un-pause from the owner
> (dated, after 2026-11-11), stop and say so. How to un-pause: see the banner at the top of
> `ElleDental/automation/daily-run.md`.

# ELLE Dental Content Pipeline (port of Content Framework v2 — DentalVia line)
# Single-brand: ELLE Dental Clinic (elledental.bg) — a real dental clinic in Sofia.

This file tells Claude how to run the pipeline for elledental.bg. The agent files in `agents/`,
the market author in `markets/bg/author.md` and `reference/site-rules.md` are the brand's
production instructions: load and follow them, do not paraphrase them.

Single brand, single market (bg), single gate. No `BRAND:` parameter, no byline, no persona.

## Why this brand departs from the VsichkiKazina / DentalVia humaniser (owner decision 2026-11-11)

The inherited humaniser is built to make casino reviews read like a person wrote them:
burstiness, fragments, opinions and verdicts, an "imperfection budget", informal drops and
asides, and a /60 human-likeness score. Applied to the ELLE Dental pages, it produced text the
owner described as reading "like friends chatting, not a professional medical clinic". So for
this brand:

- `agents/humaniser.md` keeps ONLY the de-AI checks (banned AI vocabulary, signposting,
  boilerplate repeated across pages, „не A, а B“, filler and hedging stacks — never medical
  safety wording) and replaces the /60 score with a professional-quality check (correctness,
  clarity, register consistency, readability, no AI tells).
- `markets/bg/author.md` defines the binding **ELLE VOICE**: professional patient information
  from a modern clinic, like a good national health service leaflet; complete sentences, mostly
  12–25 words; paragraphs of 2–4 sentences; lists for steps, symptoms and risks; predictable
  structure; third-person clinic voice or a sparing neutral „ние“.
- `agents/outline-architect.md` uses a predictable patient-information order instead of
  deliberately varied section shapes.
- The Brand Gate checks the ELLE VOICE (blocking check 10, Pillar 1).
- The Gemini step 7 judges "reads as professionally written by a clinic's medical writer", not
  "human-written".

Do not import burstiness, fragment, opinion, imperfection or informal-register rules from the
other brands into any ELLE Dental stage.

## Non-negotiable principles

1. **AI TEXT IS A DRAFT.** A page is reviewed only when Д-р Елена Манолова has actually reviewed
   it and the human sets `reviewed_by` / `reviewed_on`. The pipeline never sets them, never
   fills a clinical item's decision, never writes "Медицински преглед".
2. **NOTHING SAFETY-RELEVANT IS REMOVED.** Every warning, risk, contraindication, number, link,
   `{{TOKEN}}`, source, existing clinical item and the urgent-care block survive every stage
   (inventory diff at every editing stage, like DentalVia's number diff).
3. **NEW MEDICAL FACTS NEED A SOURCE AND A DOCTOR.** Max 3 per page; authoritative source,
   HTTP 200, added to `[[sources]]`; one `[[clinical_items]]` entry each
   (`reference/verification-policy.md`).
4. **NO INVENTION.** No patient stories, testimonials, experience, equipment, materials,
   durations, visit counts or credentials beyond `markets/bg/author.md` canon.
5. **NO PRICES, NO OFFERS, NO GUARANTEES.** Banned terms per `reference/site-rules.md` §2.
6. **THE 28 ADDRESSES NEVER CHANGE.** Links only from `ElleDental/conversion-links.md`.
7. **/botulinov-toksin/ STAYS NEUTRAL.** No booking wording, doctors, Superdoc, „ботокс“, brand
   names or medical-use claims.
8. **FRESH CONTEXT PER STAGE; ORDER IS FIXED; FIX THE FACTORY** (as DentalVia): each stage is a
   separate subagent reading only its inputs; a Gate FAIL is fixed at the failing stage and
   re-run forward, never hand-patched.
9. **THE PIPELINE NEVER WRITES TO WEBPORTALS.** It delivers `content/<slug>.md` in a PR here;
   a human copies it into WebPortals and runs that repo's `check_site.py` and build.

## Brand constants (ELLE Dental — elledental.bg)

- Clinic: ELLE Dental Clinic („ELLE Dental Clinic & Aesthetics“), ЕЛ ДЕНТАЛ КЛИНИК ЕООД,
  ж.к. Света Троица, бл. 145В, вх. Б, партер, София 1309. Phone 0886 034 890; Mon–Sat
  09:00–18:30. No emergency service, no out-of-hours number.
- Doctors: Д-р Елена Манолова (зъболекар; medical reviewer), Д-р Теодора Янчева (лекар по
  дентална медицина). Facts only from the canon in `markets/bg/author.md`.
- Language: Bulgarian, formal „Вие“ (capitalised courtesy forms), ELLE VOICE. No em-dashes.
- Content types: `page-rewrite` (one of the 28 existing pages) | `new-page` (only with the
  owner's written approval naming the page).
- Gate: `agents/brand-gate-elledental.md`. Market author: `markets/bg/author.md`.
- Links: `ElleDental/conversion-links.md` (28 addresses + `/kontakti/#zapazi`).
- Output: a WebPortals-ready `content/<slug>.md` (TOML front matter: title, meta_description,
  h1, slug, type, group, status, last_updated, related, written_by, [[faq]], [[sources]],
  [[clinical_items]]) — not a blog article. Format in `reference/site-rules.md` §9.
- Upstream of truth for site rules: WebPortals `ElleDental/_publisher/` (re-read every run).

## Working directory layout (one per page)

articles/{YYYY-MM-DD}-{slug}/
  00-brief.md            (from templates/00-brief-template-elledental.md)
  00-current.md          (page-rewrite: the live content file, verbatim, with source commit)
  00-inventory.md        (every warning, risk, contraindication, number, link, token, source,
                          clinical item, FAQ on the current page)
  01-synthesis.md
  01.5-outline.md
  02-draft.md
  03-humanised.md        (professional-quality report + edited page)
  04-seo.md              (audit, title, meta, FAQ, links)
  05-gate-report.md
  05b-final-draft.md     (light re-check output; still carries flags)
  06-verification.md     (sources fetched, clinical items raised, self-check table)
  content/{slug}.md      (THE DELIVERABLE: WebPortals-ready content file, no flags)
  07-gemini-check-N.md   (Step 7 verdicts)
  log.md

## Running one page

STEP 0 — BRIEF. Confirm the pause has been lifted in writing (else stop). Fetch the current
content file from `ProfitXtraV2/WebPortals` (`ElleDental/_publisher/content/<slug>.md`; branch
`main` if the ElleDental site is merged, otherwise `feature/elledental-site`) and the
publisher's rule files; write `00-current.md` (verbatim + commit sha) and `00-inventory.md`.
Fill `00-brief.md` (main term from `keyword-map.md`, Ahrefs metrics from `topic-backlog.md`,
patient questions from web search of the main term in Bulgarian). If the WebPortals file cannot
be read, STOP: a page-rewrite without the current page is never attempted.

STEPS 1 → 5b — sequential, each a FRESH-CONTEXT stage:
1    agents/synthesis.md              prompts/step-1-synthesis.md
1.5  agents/outline-architect.md      prompts/step-1.5-outline.md
2    markets/bg/author.md             prompts/step-2-author-editorial.md
3    agents/humaniser.md              prompts/step-3-humaniser.md      (edit only if NEEDS EDIT)
4    agents/seo-copywriter.md         prompts/step-4-seo.md
5    agents/brand-gate-elledental.md  prompts/step-5-brand-gate.md     (FAIL → fix upstream)
5b   agents/humaniser.md              prompts/step-5b-humaniser-light.md
Between every stage that edits text, DIFF THE INVENTORY: every `00-inventory.md` item must still
be present with the same meaning; any missing or weakened item halts the page for review.

STEP 6 — VERIFICATION + CONTENT FILE: `prompts/step-6-content-file.md`. Turns flags into
`[[clinical_items]]`, adds sources, assembles `content/<slug>.md`, runs the self-check.

STEP 7 — GEMINI PROFESSIONAL-REGISTER CHECK:
`python3 scripts/gemini_check.py <dir>/05b-final-draft.md --brand elledental`
(`prompts/step-7-gemini-check.md`). Below 80 → `prompts/step-7b-apply-gemini-recs.md` via a fresh
humaniser pass, Gate re-check, rebuild the content file, re-check; ≤ 2 passes; keep the best.
Unavailable → log `skipped`, continue.

STEP 8 — IMAGES: none for page-rewrite (`prompts/step-8-images.md`).

THEN STOP. The human reviews the PR, copies `content/<slug>.md` into WebPortals, runs its gate,
and passes the page and its `[[clinical_items]]` to Д-р Манолова. Merge of the AIContent PR
records that the draft was accepted for doctor review; it never means "reviewed".
