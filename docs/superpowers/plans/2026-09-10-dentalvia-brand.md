# DentalVia Brand Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add the DentalVia brand (dentalvia.de, German dental-tourism content) to the AIContent repo as a fully self-contained sibling of VsichkiKazina — own pipeline, own automation (built but never scheduled), own dashboard page.

**Architecture:** `DentalVia/` mirrors `VsichkiKazina/` file-for-file where the machinery is brand-agnostic (board files, automation run docs, prompts) and replaces the brand-specific layer (brand gate, author voice, canon, links registry) with dental/YMYL equivalents. Shared `scripts/` gain brand-awareness only in `build_dashboard.py`. Spec: `docs/superpowers/specs/2026-09-10-dentalvia-brand-design.md` — read it before any task.

**Tech Stack:** Markdown instruction files (agent/prompt docs), Python 3 stdlib (`scripts/build_dashboard.py` + pytest tests), static HTML/JS dashboard (GitHub Pages `docs/`).

## Global Constraints

- Work on branch `dentalvia-brand`; commit per task; NEVER touch `VsichkiKazina/**` content, `docs/index.html` behavior (only the additive brand-switcher edit in Task 8), or existing `docs/data/status.json` output shape.
- Brand name in copy: exactly **Dentalvia** (as the site writes it). Site: `https://www.dentalvia.de`. Mediation agency, NOT a clinic — partner clinic (Elle Dental Clinic, Sofia) treats; Dentalvia arranges consultation/travel/care. Area served: DE/AT/CH. Contact: beratung@dentalvia.de, +49 89 1234567, /kontakt/.
- Pipeline output language: **German only**. No English authoring anywhere (EN = future publisher-side translation).
- Byline rotates **Georgi Todorov ↔ Mario Yordanov** (exactly these two, never a team byline). Neither is a dentist — NO fabricated clinical credentials or first-person treatment claims, ever.
- Compliance (every article, blocking): no healing/success guarantees ("schmerzfrei", "100 % Erfolg", "hält ein Leben lang" banned; success rates only with cited source); risks + contraindications named; medical disclaimer verbatim: „Dieser Beitrag dient der allgemeinen Information und ersetzt keine zahnärztliche Beratung, Diagnose oder Behandlung."; prices as dated examples („ab X €, Stand MM/JJJJ") with comparison basis for savings claims; mediation-transparency line verbatim (from the live footer): „Wir sind eine Vermittlungsagentur und vermitteln Zahnbehandlungen bei einer Partnerklinik in Sofia. Die Behandlung führt die Partnerklinik durch; wir organisieren Beratung, Reise und Betreuung."
- Images: 1 concept hero (WebP, = OG image) + 1–3 SVG infographics, ≤ 4 total; NO realistic before/after teeth or clinical photos — stylised flat illustration only.
- No scheduling: never run `CronCreate`/routine registration for DentalVia.
- Flags discipline unchanged: `[VERIFY]`/`[DATA NEEDED]`/`[CONFLICT]` block publish; human resolves at Step 6.
- Article PR branches: `dv-content/<YYYY-MM-DD>-<slug>` (distinct from VK's `content/...` so the dashboards can filter).
- Existing live Ratgeber articles (anti-cannibalization — never seed/write these clusters as new pillars): `/ratgeber/was-kostet-ein-zahnimplantat/`, `/ratgeber/ablauf-implantatbehandlung-schritt-fuer-schritt/`, `/ratgeber/anreise-nach-sofia-zahnbehandlung/`, `/ratgeber/seriose-zahnklinik-ausland-erkennen/`, `/ratgeber/zahnersatz-ausland-zuschuss-krankenkasse/`, `/ratgeber/zahnersatz-bulgarien-worauf-achten/`, `/ratgeber/zahnimplantate-materialien-und-systeme/`.

---

### Task 1: Board files (queue, backlog, research bank)

**Files:**
- Create: `DentalVia/content-queue.md`
- Create: `DentalVia/topic-backlog.md`
- Create: `DentalVia/research-topics.md`

**Interfaces:**
- Produces: the three board tables later tasks parse. Queue column order (15 cols, byline after type): `id | status | type | byline | query | keywords_or_terms | volume | kd | source | drafted_date | posted_date | folder | pr | gemini | notes`. Backlog (11 cols) and research (11 cols) use the SAME column sets as VsichkiKazina's current files. Article ids: `dv-0001`… `type` ∈ `guide | comparison | howto | news`.

- [ ] **Step 1: Write `DentalVia/content-queue.md`** — mirror the header prose of `VsichkiKazina/content-queue.md` (read it first), adapted: byline-rotation rule spelled out ("`byline` alternates Georgi Todorov ↔ Mario Yordanov; next article takes whichever name the most recent row did NOT use; first article → Georgi Todorov"), buffer definition (target ≥ 10), `gemini` column meaning. Table header exactly:

```markdown
| id | status | type | byline | query | keywords_or_terms | volume | kd | source | drafted_date | posted_date | folder | pr | gemini | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
```

No data rows (queue starts empty).

- [ ] **Step 2: Write `DentalVia/topic-backlog.md`** — header prose mirrors VK's (human-owned, run enriches `volume|kd|intent|checked|ahrefs_note`, drained top-to-bottom before the research bank; `checked` ∈ ahrefs|web|none), same 11-col header as `VsichkiKazina/topic-backlog.md`. Seed EXACTLY these 10 rows (status `open`, metric cells empty — the first run enriches them):

```markdown
| 1 | guide | All-on-4 Kosten und Erfahrungen: feste Zähne auf vier Implantaten | all-on-4 kosten, feste zähne auf 4 implantaten, all-on-4 erfahrungen |  |  |  | none |  | open | money keyword; site has /festsitzender-zahnersatz/ treatment page — Ratgeber angle: Kosten/Ablauf/für wen, link treatment page as CTA |
| 2 | comparison | Zahnimplantate in der Türkei: Kosten, Risiken und die EU-Alternative | zahnimplantate türkei, zahnimplantate türkei erfahrungen, zahnimplantate türkei risiken |  |  |  | none |  | open | capture Türkei demand, make the EU/Bulgaria case honestly (patient rights, Gewährleistung, proximity) — no bashing |
| 3 | comparison | Zahnersatz in Ungarn oder Bulgarien? Der nüchterne Vergleich | zahnersatz ungarn, zahnersatz ungarn erfahrungen, zahnersatz ungarn kosten |  |  |  | none |  | open | Ungarn is the classic DE dental-tourism destination; fair comparison, Bulgaria advantages where true |
| 4 | guide | Wurzelbehandlung oder Implantat: wann sich welcher Weg lohnt | wurzelbehandlung oder implantat, zahn ziehen oder wurzelbehandlung |  |  |  | none |  | open | decision guide; links /wurzelbehandlung/ and /zahnimplantate/; strictly neutral, risks both ways |
| 5 | guide | Knochenaufbau beim Zahnarzt: Ablauf, Dauer und was es kostet | knochenaufbau kiefer, knochenaufbau kiefer kosten, sinuslift |  |  |  | none |  | open | educational depth vs the commercial /knochenaufbau/ page — anti-cannibal note required in brief |
| 6 | howto | Zahnarztkosten von der Steuer absetzen — auch bei Behandlung im Ausland | zahnarztkosten steuer absetzen, zahnbehandlung steuer |  |  |  | none |  | open | außergewöhnliche Belastung, § 33 EStG; strong trust topic; [VERIFY] all tax figures |
| 7 | guide | Zahnbehandlung unter Sedierung oder Vollnarkose: Möglichkeiten und Kosten | zahnbehandlung vollnarkose, dämmerschlaf zahnarzt, sedierung zahnarzt kosten |  |  |  | none |  | open | Angstpatienten angle; medical risks section mandatory |
| 8 | guide | Provisorium und Übergangszeit: Leben zwischen zwei Behandlungsterminen | provisorium zähne, provisorium wie lange, langzeitprovisorium |  |  |  | none |  | open | pairs with the two-visit treatment model; links /ablauf/ and /reise/ |
| 9 | comparison | Zahnprothese oder Implantat: was im Alter wirklich passt | zahnprothese oder implantat, herausnehmbarer zahnersatz oder implantat |  |  |  | none |  | open | 60+ audience; neutral decision framework; links /zahnprothesen/ /zahnimplantate/ |
| 10 | comparison | Veneers-Kosten 2026: Deutschland und Ausland im Vergleich | veneers kosten, veneers kosten deutschland, veneers ausland |  |  |  | none |  | open | price comparison with dated example prices; anti-cannibal vs /veneers/ (commercial) and /kosten/ |
```

- [ ] **Step 3: Write `DentalVia/research-topics.md`** — header mirrors VK's research bank (Ahrefs `country=de` first, web fallback, never stop; Opportunity from volume+kd; `status` ∈ candidate|queued|used), same 11-col header, zero data rows. Add one line pointing at the five keyword families in the spec's "Keyword strategy" section.

- [ ] **Step 4: Verify** — run:
`python3 - <<'EOF'` … parse each file's table header row, assert cell counts are 15/11/11 and `topic-backlog.md` has 10 data rows … `EOF` (write the small inline check; expected output `OK 15 11 11 10`).

- [ ] **Step 5: Commit** — `git add DentalVia/ && git commit -m "feat(dentalvia): board files — queue with byline rotation, seeded backlog, research bank"`

---

### Task 2: conversion-links.md (internal links + CTA registry)

**Files:**
- Create: `DentalVia/conversion-links.md`

**Interfaces:**
- Produces: the approved internal-link set + CTA rules that the SEO stage (Task 4), brand gate (Task 3) and daily run (Task 6) reference by exact path `DentalVia/conversion-links.md`.

- [ ] **Step 1: Write the file.** Structure mirrors `VsichkiKazina/affiliate-links.md` (read it first) but for lead-gen, not affiliates. Contents:
  - Purpose prose: single source of truth for internal links and consultation CTAs; extracted from the live sitemap 2026-09-10; NO affiliate links exist for this brand; never invent a URL — a needed-but-missing page gets `[LINK NEEDED: <topic>]`.
  - **Approved internal links table** (columns `path | page | use when`), one row per live DE page: `/behandlungen/`, `/zahnimplantate/`, `/festsitzender-zahnersatz/`, `/veneers/`, `/zahnkronen/`, `/zahnbruecken/`, `/zahnprothesen/`, `/wurzelbehandlung/`, `/knochenaufbau/`, `/bleaching/`, `/kosten/`, `/finanzierung/`, `/garantie/`, `/ablauf/`, `/reise/`, `/warum-sofia/`, `/partnerklinik/`, `/ueber-uns/`, `/faq/`, `/ratgeber/`, `/kontakt/`, plus the 7 existing Ratgeber article paths from Global Constraints.
  - **CTA rules:** primary CTA = free consultation → `/kontakt/` (label „Kostenlose Beratung"); one CTA block per article (end of article), optional single mid-article text link for long pillars; phone/WhatsApp only inside the CTA block, never inline in body copy.
  - **Rules** section: every article links ≥ 2 and ≤ 5 internal pages, chosen for relevance; treatment mentions link the matching treatment page on first prominent mention; comparison/cost articles must link `/kosten/` and `/garantie/`.

- [ ] **Step 2: Verify** — `grep -c '^| /' DentalVia/conversion-links.md` → expect ≥ 28 (21 site pages + 7 Ratgeber paths).

- [ ] **Step 3: Commit** — `git commit -am "feat(dentalvia): conversion-links registry (internal links + consultation CTAs)"`

---

### Task 3: Pipeline core — SKILL.md, brand gate, author file

**Files:**
- Create: `DentalVia/pipeline/SKILL.md`
- Create: `DentalVia/pipeline/agents/brand-gate-dentalvia.md`
- Create: `DentalVia/pipeline/markets/de/author.md`

**Interfaces:**
- Consumes: `DentalVia/conversion-links.md` (Task 2); structure templates: `VsichkiKazina/pipeline/SKILL.md`, `VsichkiKazina/pipeline/agents/brand-gate-vsichkikazina.md`, `VsichkiKazina/pipeline/markets/bg/author.md`, and `VsichkiKazina/pipeline/markets/de/author.md` (the BetFam GERMAN author — reuse its German anti-AI style rules / AI-tell dictionary wholesale).
- Produces: single-brand skill with these bindings, used verbatim by Tasks 4–6 — Gate: `pipeline/agents/brand-gate-dentalvia.md`; Author: `pipeline/markets/de/author.md`; stage order 1→1.5→2→3→4→5→5b→(6 human)→7→8 identical to VK; working-directory layout identical (`articles/{slug}/00-brief.md` … `06-verification.md`, `log.md`).

- [ ] **Step 1: Write `DentalVia/pipeline/SKILL.md`.** Copy VK's SKILL.md as the skeleton; make it SINGLE-brand (no `BRAND:` parameter — briefs need no brand line). Frontmatter name `dentalvia-content-pipeline`, description covering: German dental-tourism guides/comparisons/howtos/news for dentalvia.de. Keep verbatim (they are brand-agnostic): the 7 non-negotiable principles, working-directory layout, stage→agent→prompt table, DIFF-ALL-NUMBERS rule, Step 6 human verification, Step 7 external check, fresh-context discipline. Replace the brand block with the Dentalvia constants from Global Constraints (brand facts, byline rotation, compliance lines verbatim, internal links → `DentalVia/conversion-links.md`, German-only output, content types guide/comparison/howto/news, "no fabricated clinical experience" rule). Stage-2 mode: EDITORIAL always (no tester persona — nobody reviews implants hands-on); delete persona-mode routing.

- [ ] **Step 2: Write `DentalVia/pipeline/agents/brand-gate-dentalvia.md`.** Keep the evaluation machinery of `brand-gate-vsichkikazina.md` (scorecard structure, PASS/PASS-WITH-FIXES/FAIL verdicts, untouchables list, flag pass-through) — read it and mirror section-for-section. Replace the Brand Bible and checklist with the dental one. The gate's blocking checks, verbatim in the file:

```markdown
## BLOCKING CHECKS (any failure → FAIL or PASS WITH FIXES; never silently fix facts)
1. HEILVERSPRECHEN: no cure/success guarantees. Banned outright: „schmerzfrei",
   „100 % Erfolg", „garantiert", „hält ein Leben lang", „risikofrei". Success/survival
   rates ONLY with a named primary source + year.
2. RISIKEN: every treatment-bearing article names material risks AND at least one
   case where the treatment is NOT indicated (Kontraindikation).
3. DISCLAIMER (verbatim, end of article): „Dieser Beitrag dient der allgemeinen
   Information und ersetzt keine zahnärztliche Beratung, Diagnose oder Behandlung."
4. TRANSPARENZ (verbatim, in the CTA/footer block): „Wir sind eine Vermittlungsagentur
   und vermitteln Zahnbehandlungen bei einer Partnerklinik in Sofia. Die Behandlung
   führt die Partnerklinik durch; wir organisieren Beratung, Reise und Betreuung."
5. PREISE: every price is a dated example — „ab X €" + „Stand MM/JJJJ"; every savings
   claim states its comparison basis (which treatment, which German reference price).
6. QUELLEN: medical claims cite primary references (Fachgesellschaften wie DGI/DGZMK,
   peer-reviewed studies, manufacturers, KZBV/GKV for insurance topics) — else [VERIFY].
7. BYLINE: exactly „Georgi Todorov" or „Mario Yordanov"; correct rotation vs
   content-queue.md; no team byline; no clinical credentials claimed for either author.
8. LINKS: internal links only from DentalVia/conversion-links.md; 2–5 per article;
   CTA block present, pointing to /kontakt/.
```

- [ ] **Step 3: Write `DentalVia/pipeline/markets/de/author.md`.** Skeleton = `VsichkiKazina/pipeline/markets/bg/author.md` structure (header comments, EDITORIAL mode rules, anti-AI style discipline, inline canon at bottom). Import the GERMAN language layer from BetFam's `VsichkiKazina/pipeline/markets/de/author.md`: its German AI-tell dictionary (phrase + structural tells + connectives) carries over verbatim minus betting-specific entries. New content, written in full:
  - Voice: warm, precise patient-guide German — an informed friend who has organised many treatment journeys, NOT a dentist. Du/Sie decision: **Sie** (matches the live site). Sentence-length variance rules, no marketing superlatives, numbers precise.
  - AUTHOR FACTS (Tier-1 canon, both authors): Georgi Todorov — patient coordinator, organises treatment journeys Germany↔Sofia, speaks from organisational experience (travel, pricing, clinic process). Mario Yordanov — patient coordinator, aftercare/logistics focus. Tier-3 (forbidden): any clinical qualification, any "I treated/examined" claim, any first-person medical judgement, any invented patient story with identifying detail.
  - NATIVE TERMINOLOGY table: German dental terms to prefer (Zahnersatz, Versorgung, Behandlungsplan, Heil- und Kostenplan, Eigenanteil, Festzuschuss, Gewährleistung, Provisorium, Aufbissschiene…) vs generic translations to avoid.
  - Mandatory blocks the author must leave intact: disclaimer + transparency lines (verbatim strings from the gate).

- [ ] **Step 4: Verify** — `grep -L "ersetzt keine zahnärztliche Beratung" DentalVia/pipeline/SKILL.md DentalVia/pipeline/agents/brand-gate-dentalvia.md DentalVia/pipeline/markets/de/author.md` → expect EMPTY output (all three contain the disclaimer string). `grep -c "казино\|casino\|Wette\|betting" DentalVia/pipeline/markets/de/author.md` → expect `0`.

- [ ] **Step 5: Commit** — `git commit -am "feat(dentalvia): pipeline core — skill, dental brand gate, German author"`

---

### Task 4: Pipeline agents, prompts, brief template

**Files:**
- Create: `DentalVia/pipeline/agents/{synthesis,outline-architect,humaniser,seo-copywriter,external-check-gemini}.md`
- Create: `DentalVia/pipeline/prompts/` — all of: `step-1-synthesis.md`, `step-1.5-outline.md`, `step-2-author-editorial.md`, `step-3-humaniser.md`, `step-4-seo.md`, `step-5-brand-gate.md`, `step-5b-humaniser-light.md`, `step-7-gemini-check.md`, `step-7b-apply-gemini-recs.md`, `step-8-images.md`, `step-8-image-review.md`
- Create: `DentalVia/pipeline/templates/00-brief-template-dentalvia.md`

**Interfaces:**
- Consumes: bindings from Task 3's SKILL.md (file names must match its stage table exactly).
- Produces: complete runnable stage set. NOT copied: `step-2-author-persona.md` (editorial-only brand), `comment-moderator.md`, `lexical-corpus-builder.md`, `brand-gate.md` (BetFam) — YAGNI.

- [ ] **Step 1: Copy each source file from `VsichkiKazina/pipeline/` and adapt.** For every file, apply the same transformation checklist: (a) replace brand/market references (Всички Казина→Dentalvia, bg→de, НАП→n/a, casino examples→dental examples); (b) replace RG/18+/affiliate-disclosure requirements with the disclaimer + transparency requirements (verbatim strings from Task 3 Step 2); (c) examples inside prompts use dental data (price table DE↔BG, „Ablauf in 2 Reisen" step sequence) instead of wagering math; (d) `step-8-images.md`: keep the full hero+infographic policy and caps, add the dental hygiene rule — no realistic before/after teeth, no clinical photos, flat illustration only; price graphics carry „Stand MM/JJJJ"; German labels; (e) `step-8-image-review.md` review criteria unchanged plus a check for rule (d). `external-check-gemini.md` and step-7 prompts need only language/brand mentions changed (the check itself is language-agnostic). The humaniser agent keeps its full machinery; its language examples become German (source: BetFam DE author tells).

- [ ] **Step 2: Write the brief template** — copy `templates/00-brief-template-vsichkikazina.md`, drop the BRAND line, add fields: `byline` (from rotation), `anti-cannibal notes` (must list any overlapping live page from conversion-links.md), `target keyword + Ahrefs metrics`, `internal links planned (2–5)`.

- [ ] **Step 3: Verify** — `ls DentalVia/pipeline/prompts | wc -l` → `11`; `grep -rl "vsichkikazina\|Всички Казина\|казино" DentalVia/pipeline/ | grep -v Binary` → EMPTY.

- [ ] **Step 4: Commit** — `git commit -am "feat(dentalvia): pipeline agents, prompts, brief template"`

---

### Task 5: Automation docs (daily-run, learn-run, backfill-images, build-dashboard)

**Files:**
- Create: `DentalVia/automation/daily-run.md`
- Create: `DentalVia/automation/learn-run.md`
- Create: `DentalVia/automation/backfill-images.md`
- Create: `DentalVia/automation/build-dashboard.md`
- Create: `DentalVia/automation/fix-log.md`, `DentalVia/automation/flag-resolution-log.md` (empty log skeletons copied from VK's headers)

**Interfaces:**
- Consumes: everything from Tasks 1–4 by exact path; `scripts/build_dashboard.py dentalvia` CLI (Task 7 — the doc references it; Task 7 implements it).
- Produces: `DentalVia/automation/daily-run.md` — the single entry point the user triggers manually.

- [ ] **Step 1: Write `daily-run.md`** — copy VK's `automation/daily-run.md` section-for-section and adapt:
  - Top of file, before everything: **MANUAL TRIGGER note** — "This run is NOT scheduled. Trigger: open a Claude Code session in the repo and say: *run DentalVia/automation/daily-run.md*. Do not register a routine for it."
  - Constants: `BUFFER_TARGET = 10`, market `country=de`, board paths under `DentalVia/`, article dirs `DentalVia/articles/`, PR branches `dv-content/<TODAY>-<slug>`, heartbeat + dashboard data under `docs/data/dentalvia/` (run `python3 scripts/build_dashboard.py dentalvia`).
  - Byline step (new, in the per-article procedure): before writing, read the queue's most recent byline → this article takes the other name; write it into `00-brief.md` and the queue row.
  - Keyword research section: keep the Ahrefs→web-fallback machinery verbatim; weighting = the five families from the spec's Keyword strategy section (list them in the doc); German compound/synonym clustering rule; young-domain bias (prefer low KD; head terms stay `candidate` with note "pillar — wait for authority").
  - Replace the affiliate-links step with the conversion-links rules (Task 2).
  - Compliance references point at the dental gate checks; RG/18+ lines removed.
  - DELETE the `build_feed.py` / published-feed step (publishing out of scope) — note "publisher integration comes later".
  - Keep: resume/idempotency section, live progress reporting (paths adjusted), DIFF-ALL-NUMBERS, Step-7 Gemini gate incl. score normalization and keep-best rule, Step-8 images, one-PR-per-article, Never section (adapted: never fabricate medical facts/prices; never resolve flags; never schedule this run).
- [ ] **Step 2: Write `learn-run.md`** — VK copy with paths swapped and target = the German AI-tell dictionary inside `DentalVia/pipeline/markets/de/author.md`; approval-PR mechanism unchanged.
- [ ] **Step 3: Write `backfill-images.md`** — VK copy, paths + dental image-hygiene rule (Task 4d).
- [ ] **Step 4: Write `build-dashboard.md`** — VK's 17-line doc adapted: command `python3 scripts/build_dashboard.py dentalvia`, output `docs/data/dentalvia/status.json`, page `docs/dentalvia/index.html`.
- [ ] **Step 5: Verify** — `grep -c "CronCreate\|schedule this" DentalVia/automation/daily-run.md` shows the never-schedule note present; `grep -rl "VsichkiKazina/" DentalVia/automation/` → EMPTY.
- [ ] **Step 6: Commit** — `git commit -am "feat(dentalvia): automation docs (manual daily run, learn, image backfill, dashboard)"`

---

### Task 6: articles/ scaffold + repo docs

**Files:**
- Create: `DentalVia/articles/.gitkeep`
- Modify: `README.md` (repo root — brands section + "Adding a new brand" now points at DentalVia as the worked example)
- Modify: `SETUP.md` (add: DentalVia needs the same `AHREFS_API_KEY`/`GEMINI_API_KEY`; no routine registered)

**Interfaces:**
- Consumes: final layout from Tasks 1–5.

- [ ] **Step 1:** Add `DentalVia/articles/.gitkeep`. Update README: in the intro, "configured for two brands"; add a short DentalVia paragraph (German dental-tourism, manual runs only, German-only pipeline, EN via future publisher); repository-layout tree gains the `DentalVia/` subtree; dashboard section lists both URLs (root + `/dentalvia/`).
- [ ] **Step 2:** Update SETUP.md with the manual-trigger instructions (same wording as daily-run.md's note).
- [ ] **Step 3: Commit** — `git commit -am "docs: register DentalVia brand in README/SETUP"`

---

### Task 7: Brand-aware build_dashboard.py (TDD)

**Files:**
- Modify: `scripts/build_dashboard.py`
- Test: `scripts/tests/test_build_dashboard.py`

**Interfaces:**
- Consumes: DentalVia queue 15-col layout (Task 1).
- Produces: CLI `python3 scripts/build_dashboard.py [brand]`, brand ∈ `vsichkikazina` (default) | `dentalvia`. Module constants `BRANDS` dict and `COLUMNS_DV` (15-col list with `byline` after `type`). No-arg behavior byte-identical to today.

- [ ] **Step 1: Write failing tests** (append to `scripts/tests/test_build_dashboard.py`):

```python
DV_SAMPLE = """# Content Queue — DentalVia
| id | status | type | byline | query | keywords_or_terms | volume | kd | source | drafted_date | posted_date | folder | pr | gemini | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| dv-0001 | drafted | guide | Georgi Todorov | All-on-4 Kosten | all-on-4 kosten | 1300 | 12 | backlog | 2026-09-10 |  | 2026-09-10-all-on-4-kosten | #90 | human 85 |  |
| dv-0002 | in-progress | comparison | Mario Yordanov | Zahnersatz Ungarn oder Bulgarien | zahnersatz ungarn | 700 | 25 | research |  |  | 2026-09-10-zahnersatz-ungarn |  |  |  |
"""

def test_dentalvia_queue_parses_byline():
    rows = bd.parse_queue(DV_SAMPLE, brand="dentalvia")
    assert rows[0]["byline"] == "Georgi Todorov"
    assert rows[1]["byline"] == "Mario Yordanov"
    assert rows[0]["volume"] == "1300"

def test_dentalvia_status_meta_and_paths():
    status = bd.build_status(bd.parse_queue(DV_SAMPLE, brand="dentalvia"),
                             target=10, brand="dentalvia")
    assert status["meta"]["brand"] == "DentalVia"
    assert status["articles_base_url"].endswith("/tree/main/DentalVia/articles/")
    assert status["buffer"]["count"] == 1

def test_default_brand_unchanged():
    rows = bd.parse_queue(SAMPLE)               # no brand arg — VK layout
    status = bd.build_status(rows, target=10)
    assert status["meta"]["brand"] == "VsichkiKazina"
    assert "byline" not in rows[0]
```

- [ ] **Step 2: Run to verify failure** — `python3 -m pytest scripts/tests/test_build_dashboard.py -q` → FAIL (`parse_queue() got an unexpected keyword argument 'brand'`).
- [ ] **Step 3: Implement.** In `build_dashboard.py`: add `COLUMNS_DV = COLUMNS[:3] + ["byline"] + COLUMNS[3:]`; give `parse_queue(md, brand="vsichkikazina")` a brand param choosing specs (`dentalvia` → `[COLUMNS_DV]`, else the existing legacy-spec list); give `build_status(..., brand="vsichkikazina")` a `BRANDS` lookup:

```python
BRANDS = {
    "vsichkikazina": {"dir": "VsichkiKazina", "brand": "VsichkiKazina",
                      "out": ("docs", "data", "status.json")},
    "dentalvia":     {"dir": "DentalVia", "brand": "DentalVia",
                      "out": ("docs", "data", "dentalvia", "status.json")},
}
```

`articles_base_url` and `meta.brand` come from the lookup; `meta.schedule` for dentalvia = `{"note": "manual runs only — not scheduled"}`. `main()` reads `sys.argv[1]` (default `vsichkikazina`, unknown value → `sys.exit("unknown brand …")`) and resolves all paths through `BRANDS`.
- [ ] **Step 4: Run tests** — `python3 -m pytest scripts/tests/ -q` → ALL PASS (old tests prove VK output unchanged).
- [ ] **Step 5: Generate the first data file** — `python3 scripts/build_dashboard.py dentalvia` → writes `docs/data/dentalvia/status.json` (buffer 0/10, 10 backlog rows). Commit script + tests + data: `git commit -am "feat(dashboard): brand-aware build_dashboard with dentalvia support"`

---

### Task 8: DentalVia dashboard page + brand switcher

**Files:**
- Create: `docs/dentalvia/index.html`
- Modify: `docs/index.html` (additive header link ONLY)

**Interfaces:**
- Consumes: `docs/data/dentalvia/status.json` (Task 7), heartbeat `docs/data/dentalvia/run-status.json` (written by future runs; page must handle 404 gracefully — the VK page's existing try/catch pattern already does).

- [ ] **Step 1: Create `docs/dentalvia/index.html`** — copy `docs/index.html`, then: title/header "Dentalvia — Content Dashboard"; `fetch('./data/status.json')` → `fetch('../data/dentalvia/status.json')`; run-status GitHub-API URL path `docs/data/run-status.json` → `docs/data/dentalvia/run-status.json` (and Pages fallback `../data/dentalvia/run-status.json`); PR list: filter fetched PRs to `head.ref.startsWith('dv-content/')`; articles links come from `status.articles_base_url` (already brand-correct); add header brand switcher: `VsichkiKazina ↔ Dentalvia` (`../` and `./`). Buffer target label reads from status.json (unchanged logic).
- [ ] **Step 2: Modify `docs/index.html`** — add the same two-link switcher span in the header (`./` and `./dentalvia/`). Nothing else.
- [ ] **Step 3: Verify** — `python3 -m http.server -d docs 8901 &` then `curl -s localhost:8901/dentalvia/ | grep -c "dentalvia/status.json"` → ≥ 1; open check: `curl -s localhost:8901/ | grep -c "dentalvia"` → ≥ 1; kill the server. (Rendering with live JSON is confirmed by the file:// path structure matching the VK page's, which is in production.)
- [ ] **Step 4: Commit** — `git commit -am "feat(dashboard): dentalvia page + brand switcher"`

---

### Task 9: Full-repo verification + PR

- [ ] **Step 1: Cross-file consistency sweep** — run and require empty/expected output:
  - `grep -rn "vsichkikazina\|Всички Казина" DentalVia/ | grep -vi "not\|unlike"` → EMPTY
  - `grep -rln "ersetzt keine zahnärztliche" DentalVia/pipeline/` → SKILL.md, gate, author (3 files)
  - Every path referenced in `DentalVia/automation/daily-run.md` exists: extract `DentalVia/[A-Za-z0-9/._-]*` matches and `test -e` each.
  - `python3 -m pytest scripts/tests/ -q` → all pass.
- [ ] **Step 2: Push and open PR** — `git push -u origin dentalvia-brand`, then `gh pr create` with title "Add DentalVia brand (German dental-tourism content pipeline)" and a body summarising the spec link, what's included, and the two follow-ups that stay manual: (1) first article dry-run via `DentalVia/automation/daily-run.md`, (2) scheduling later by pointing a routine at that file. End body with the Claude Code attribution footer.
- [ ] **Step 3:** Report PR URL + the manual-trigger instruction to the user. Do NOT merge (merge = approve is the human's act in this repo).

---

## Self-review notes

- Spec coverage: layout→T1/2/6, pipeline core→T3, stages→T4, automation→T5, keyword strategy→T5 Step 1 + T1 seed, images→T4d + T5, dashboard→T7/8, README→T6, no-scheduling→T5/T9, out-of-scope items (publishing, feed, EN, cross-brand aggregate) explicitly excluded in T5 Step 1 and nowhere implemented.
- The first end-to-end article dry-run (spec "Testing") is deliberately NOT a plan task: it is the user's first manual run and writes real content via PR.
