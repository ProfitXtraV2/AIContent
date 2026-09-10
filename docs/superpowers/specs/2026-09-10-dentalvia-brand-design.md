# DentalVia brand — design

**Date:** 2026-09-10
**Status:** approved by user (conversation), pending spec review
**Goal:** add a second, fully self-contained brand project to AIContent for
**dentalvia.de** — a German-language dental-tourism mediation agency (German
patients → treatment at partner Elle Dental Clinic, Sofia). Full automation is
built but **not scheduled**; the user triggers runs manually for now.

## Decisions made

| Decision | Choice |
|---|---|
| Scope | Full autonomous clone of the VsichkiKazina setup, minus scheduling |
| Repo layout | Sibling folder `DentalVia/` inside AIContent (per README "Adding a new brand") |
| Pipeline | **Own pipeline copy** under `DentalVia/pipeline/` — not shared bindings. Dental is a different vertical (health/YMYL, not gambling) |
| Languages | German (primary market `de`), English (secondary market `en`, on request only) |
| Byline | Rotates between **Georgi Todorov** and **Mario Yordanov**, alternating per article |
| Publishing | Out of scope — pipeline ends at approved markdown after PR merge; site is not ready |
| Scheduling | Out of scope — no cloud routine created; manual trigger documented |

## Layout

```
DentalVia/
  pipeline/
    SKILL.md                       dentalvia-content-pipeline (same stage discipline)
    agents/                        synthesis, outline-architect, humaniser,
                                   seo-copywriter, external-check-gemini,
                                   brand-gate-dentalvia (NEW — see Compliance)
    markets/de/author.md           German dental patient-guide voice + inline canon
    markets/en/author.md           English counterpart
    prompts/                       step-1 … step-8 templates, adapted
    templates/00-brief-template-dentalvia.md
  automation/
    daily-run.md                   adapted clone (see Automation)
    learn-run.md                   AI-tell dictionary loop for German copy
    backfill-images.md             step-8 infographic/hero backfill
    build-dashboard.md             per-brand dashboard build
  articles/                        per-article working dirs (00-brief → 05b-final, log.md)
  content-queue.md                 buffer state + byline-rotation tracker
  topic-backlog.md                 seed backlog (dental-tourism topics)
  research-topics.md               Ahrefs research state
  conversion-links.md              internal-link set + consultation CTAs
                                   (replaces affiliate-links.md)
```

Shared, brand-agnostic infrastructure stays shared: `scripts/`
(`ahrefs_enrich.py`, `gemini_check.py`, `gemini_image_gen.py`, …), `published/`
feed conventions, PR-per-article review flow (merge = approve).

## Brand constants

- **Brand:** DentalVia (dentalvia.de). Mediation agency, not a clinic: arranges
  consultation, travel, accommodation, aftercare; treatment by Elle Dental
  Clinic, Sofia. Fixed prices guaranteed in writing is the core promise.
- **Markets:** `de` primary — Ahrefs `country=de`, German keywords, German copy.
  `en` secondary — no autonomous keyword research; written only when a brief
  requests it.
- **Content types:** treatment guides (implants, All-on-4/All-on-6, crowns,
  bridges, veneers, root canal, bone augmentation, dentures, whitening), cost
  comparisons DE↔BG, dental-tourism how-tos (travel, logistics, aftercare),
  clinic-choice / "is treatment abroad safe" guides.
- **Byline:** alternates Georgi Todorov ↔ Mario Yordanov. `content-queue.md`
  records who signed last; the brand gate flags a wrong or team byline.
- **Internal links / CTAs:** pulled from the live dentalvia.de sitemap during
  implementation into `conversion-links.md`; conversion goal is the free
  consultation request (lead gen), not affiliate revenue.

## Compliance gate (brand-gate-dentalvia.md) — the big rewrite

German health content is YMYL; the gambling gate does not transfer. New gate
checks, all blocking:

1. **No healing/success guarantees** (Heilmittelwerbegesetz discipline): no
   "schmerzfrei", "100% Erfolg", "hält ein Leben lang" claims; success rates
   only with a cited source.
2. **Risks mentioned:** every treatment article names the material risks and
   the cases where the treatment is not indicated.
3. **Medical disclaimer** on every article: content is informational and
   "ersetzt keine zahnärztliche Beratung/Untersuchung".
4. **Prices as dated examples:** "ab X €, Stand MM/YYYY"; savings claims
   ("bis zu 70 % günstiger") must state the comparison basis.
5. **Sourced medical claims:** primary references only (dental associations,
   peer-reviewed studies, implant manufacturers, regulators).
6. **Byline check:** exactly one of the two rotating authors.
7. **Untouchables** as in the base pipeline: facts, prices, dates, disclaimers,
   counter-arguments survive every stage; `[VERIFY]`/`[DATA NEEDED]`/`[CONFLICT]`
   flags block publish until the human resolves them at Step 6.

Removed from the gambling gate: RG/18+ lines, licence framing, affiliate
disclosure (replaced by a mediation-model transparency line: DentalVia
arranges, the partner clinic treats).

## Automation (built, not started)

`automation/daily-run.md` mirrors the VsichkiKazina daily run: Ahrefs keyword
research (`country=de`, German dental/dental-tourism seed terms) → opportunity
scoring → cannibalization clustering (one pillar per cluster) → refill buffer
to `BUFFER_TARGET = 10` → 7-stage pipeline per article → Gemini step-7
AI-detection gate (target "human-written ≥ 80 %", ≤ 2 humaniser passes, keep
best) → step-8 infographic + concept-hero images with Gemini review → one PR
per article. Falls back to web research when Ahrefs is unavailable.

**No `CronCreate`/routine is registered.** The run doc starts with the manual
trigger instructions; scheduling later = pointing a new routine at
`DentalVia/automation/daily-run.md`.

## Keyword strategy

Mechanism inherited unchanged from the VsichkiKazina run: Ahrefs v3
(`country=de`) → volume/KD/intent/trend → deterministic Opportunity score;
web-research fallback (`checked=web`, never halt, never fabricate); human
`topic-backlog.md` enriched but never overridden; AI bank in
`research-topics.md`; anti-cannibalization clustering at research time (one
pillar per intent cluster, near-dupes folded in).

DentalVia-specific weighting — research targets five German dental-tourism
keyword families, by conversion value:

1. **Treatment + cost/abroad** (money): "Zahnimplantate Kosten",
   "All-on-4 Kosten", "Zähne machen lassen im Ausland", "Veneers Bulgarien
   Preise".
2. **Destination comparisons**: capture existing Ungarn/Türkei demand
   ("Zahnimplantate Türkei Risiken", "Zahnersatz Ungarn Erfahrungen") and make
   Bulgaria's case (EU, patient rights, prices, proximity).
3. **Trust & safety**: "Zahnarzt Ausland seriös", "Gewährleistung Zahnersatz
   Ausland".
4. **Insurance/reimbursement**: "Heil- und Kostenplan im Ausland",
   "Krankenkasse Zuschuss Zahnersatz Ausland".
5. **Treatment education** (TOFU): "Knochenaufbau Ablauf", "Wurzelbehandlung
   oder Implantat".

Adjustments for the vertical:
- **German compounding/synonyms**: cluster variant forms as one intent
  ("Zahnimplantat"/"Implantat"/"Zahnersatz"/"dritte Zähne"; "Kosten"/"Preise"/
  "Erfahrungen" modifiers) so the cannibalization guard holds.
- **Young-domain bias**: dentalvia.de has low authority — prioritise low-KD
  long-tail first; high-KD head terms stay in the bank as long-term pillars
  rather than being written early.
- **English**: no autonomous keyword research; `en` articles on request only.

The seed `topic-backlog.md` is written from these families; the first manual
run validates it against live Ahrefs `country=de` data.

## Dashboard

DentalVia gets its own page on the existing GitHub Pages site:

- **URL: `https://profitxtrav2.github.io/AIContent/dentalvia/`**
  (`docs/dentalvia/index.html`), same look as the VsichkiKazina dashboard at
  the site root.
- `scripts/build_dashboard.py` becomes brand-aware (brand → queue path + output
  path): DentalVia data lands in `docs/data/dentalvia/status.json`; the
  VsichkiKazina paths and page stay byte-for-byte where they are so nothing
  breaks for the existing routine.
- The two pages cross-link in the header (brand switcher). No merged
  cross-brand aggregate view — each brand has its own page.

## Testing / verification

- Dry-run one article end-to-end manually (brief → 05b + gate report + Gemini
  check) before declaring the pipeline usable.
- Verify the seeded backlog topics against real Ahrefs `country=de` data on the
  first manual run.
- Existing `scripts/tests` stay green; any script change needed for
  brand-awareness (dashboard/feed paths) gets a test.

## Out of scope

- Publishing/deploy (renderer, FTP) — until the site stack is ready.
- A merged cross-brand dashboard view (each brand gets its own page instead).
- English keyword research automation.
- Any change to the VsichkiKazina folder, pipeline, or its scheduled routines.
