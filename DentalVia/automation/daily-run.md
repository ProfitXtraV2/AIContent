# Daily Run — DentalVia Content Autopilot

> **MANUAL TRIGGER — NOT SCHEDULED.**
> This run is NOT scheduled. Trigger: open a Claude Code session in the repo and say:
> *run DentalVia/automation/daily-run.md*. Do not register a routine for it.

You are running the daily content autopilot for **dentalvia.de**. Work only inside
this repo. Brand is hard-locked: `BRAND: dentalvia` (German output, €, DGI/DGZMK/
KZBV/GKV context, no clinical guarantees, approved internal-link set only from
`DentalVia/conversion-links.md`). Follow the pipeline in `DentalVia/pipeline/`
VERBATIM — never paraphrase its agent files.

## Constants
- BUFFER_TARGET = 10   (a FLOOR, not a cap — the buffer of written-but-unposted articles
  should never sit below this. There is NO upper limit: keep producing quality content and
  let the library grow. The buffer only guides urgency, never stops production.)
- MAX_PER_RUN = 3       (new articles to write per run — always aim for this many, every run,
  regardless of how full the buffer already is; small batches keep clear of the rate limit)
- GEMINI_TARGET_CONFIDENCE = 80   (Step 7 accepts at "human-written ≥ 80%"; 80 is acceptable)
- MAX_GEMINI_PASSES = 2            (max Humaniser re-passes driven by Gemini before handing to human)
- IMAGE_MIN_PER_ARTICLE = 1        (Step 8: every article ships at least one image; more when they earn it)
- IMAGE_TARGET_SCORE = 80          (Step 8 accepts a Gemini image-review score ≥ 80, no integrity failure)
- MAX_IMAGE_PASSES = 2             (max regenerate/fix passes per image driven by Gemini review)

## Resume / idempotency (a failed run must self-heal on the next fire)
This run may be re-fired at any time (a prior run may have died on a 429 rate limit).
It MUST be safe to re-run and MUST continue, not restart:
- **First, reconcile leftovers.** Before selecting new topics, look for `DentalVia/content-queue.md`
  rows with `status: in-progress` (an article a previous run started but didn't finish).
  For each: if its `dv-content/<slug>` branch already has a complete `05b`, finish it (Gemini
  Step-7 → PR → set `drafted`); otherwise complete the writing from where it left off. Only
  after all in-progress rows are resolved do you select NEW topics for this run's batch.
- **Never duplicate.** An article already `drafted`/`approved`/`posted` (or with an open PR)
  is done — never rewrite it. Dedup every new candidate against the queue + sitemap as usual.
- **Rate-limit behavior.** If you hit a 429 mid-run, commit whatever is safely complete
  (drafted rows + their PRs), leave the rest `in-progress`, end the heartbeat as `idle`, and
  STOP cleanly — the next run resumes from the in-progress rows.

## Brand conventions (every article)
- Byline/author rotates between **Georgi Todorov** and **Mario Yordanov** — alternating per
  article, tracked in `DentalVia/content-queue.md`. The next article takes whichever name the
  most recent queue row did NOT use; the very first article uses **Georgi Todorov**. See the
  byline step in the per-article procedure below.
- Write the brand name exactly **Dentalvia** in published copy (site casing).
- Both authors are patient coordinators, NOT dentists. Never a team/editorial byline; never
  a clinical credential or fabricated treatment experience for either author.
- Compliance lines (verbatim, never reworded, never dropped) — see
  `DentalVia/pipeline/agents/brand-gate-dentalvia.md` for enforcement:
  · Medical disclaimer (end of every article):
    „Dieser Beitrag dient der allgemeinen Information und ersetzt keine zahnärztliche
    Beratung, Diagnose oder Behandlung."
  · Mediation transparency (in the CTA/footer block of every article):
    „Wir sind eine Vermittlungsagentur und vermitteln Zahnbehandlungen bei einer
    Partnerklinik in Sofia. Die Behandlung führt die Partnerklinik durch; wir
    organisieren Beratung, Reise und Betreuung."
- If an article reads as over-structured / AI-patterned, apply
  `DentalVia/pipeline/prompts/step-7b-apply-gemini-recs.md` through a fresh Humaniser pass
  (break symmetry, drop narrative signposts, de-count headers/lists, cut synthesizing
  summaries), preserving every number, link, compliance line, disclaimer, and date.
  The Brand Gate enforces the byline, brand-name, and all compliance rules.

## What goes where (data model)
- **Article content** (`DentalVia/articles/<slug>/*`) goes on a **PR branch** only,
  for human review. Never commit article files to `main`.
- **Board files** are operational tracking and ARE committed to `main` so the dashboard
  is always accurate: `DentalVia/content-queue.md`, `DentalVia/topic-backlog.md`,
  `DentalVia/research-topics.md`, `docs/data/dentalvia/run-status.json`, and the
  `docs/` dashboard. Committing these to `main` is expected — it is not article content.

## Live progress reporting (drives the dashboard step tracker)
Keep a `progress` object in `docs/data/dentalvia/run-status.json` current. **This is what
animates the stage tracker** — the dashboard hides the tracker when `stage_index` is `null`,
so you MUST set it, not leave it null. Cadence, at EACH stage boundary of the current
article (a quick, one-file commit + push — do this even though you're mid-article; it is
cheap and expected):

`progress = {"phase":"writing","article_index":<1-based>,"article_total":<batch size>,
"article_slug":"<slug>","stages":["Synthesis","Outline","Author","Humaniser","SEO",
"Brand Gate","Light re-check","Images","Verification","PR"],"stage_index":<0-based index of the
stage you are STARTING now>,"stage":"<that stage's name>"}`.

- Set `stage_index` to `0` (Synthesis) before the first stage, then bump it to `1,2,3…`
  as each stage completes and the next begins. Push after each bump.
- Use the exact stage names above. The dashboard reads this file fresh via the GitHub API,
  so updates appear within ~seconds (Pages build latency does not apply).
- If you genuinely cannot push per stage, at minimum bump `stage_index` once per completed
  stage; never leave it `null` for the whole article (that shows only "writing…").

## Procedure

1. **Sync + start heartbeat.** Get up-to-date `main` (the human may have merged
   approvals, marked articles `posted`, or edited `DentalVia/topic-backlog.md`). Write
   `docs/data/dentalvia/run-status.json`
   `{"state":"running","run_started_utc":"<now>","run_finished_utc":null,
   "articles_written":null,"prs_opened":[],"run_url":"<this run's URL if known>",
   "note":"daily run","progress":{...as above, stage null}}` and push to `main`.

2. **Set the batch size.** Run `python3 scripts/build_dashboard.py dentalvia` and read
   `docs/data/dentalvia/status.json`. This run writes **`batch = MAX_PER_RUN` NEW articles**,
   ALWAYS — even if the buffer is already ≥ BUFFER_TARGET. The target is a floor, NOT a cap:
   never stop producing just because the buffer is "full". The ONLY thing that lowers the
   count is quality — if there aren't `MAX_PER_RUN` genuinely distinct, non-cannibalizing,
   on-strategy topics available after dedup/research, write fewer (quality over quota; never
   pad). If the buffer is BELOW the target, treat filling it as extra-urgent but still cap
   this run at MAX_PER_RUN. (Only skip writing if there are truly zero valid distinct topics
   left.)
   > Note: DentalVia dashboard data lives at `docs/data/dentalvia/status.json` — never read
   > the brandless `docs/data/status.json` (that is VsichkiKazina's). If
   > `python3 scripts/build_dashboard.py dentalvia` rejects the argument (script not yet
   > brand-aware), skip the dashboard refresh and log it — do not run the no-arg command.

3. **Select up to `batch` topics:**
   a. Take up to `batch` rows with `status: open` from `DentalVia/topic-backlog.md`, in
      priority order (do NOT change their status yet — only the write outcome sets it,
      step 5). **Backlog is a commitment:** every `open` backlog keyword MUST eventually
      become a written article. Prioritise the backlog ahead of research candidates and
      keep attempting its open rows across runs until each reaches `written` (with its PR
      noted). Never silently drop an open backlog item; if current scope/sourcing blocks
      it, keep it `open` with a `blocked: <reason>` note so it is revisited the moment it
      is unblocked.
   b. If fewer than `batch`, top up from `DentalVia/research-topics.md` `status: candidate`
      rows, **highest-Opportunity first**. Read the computed Opportunity from
      `docs/data/dentalvia/status.json` (each research row has `opportunity.score`/`band`)
      and pick candidates in DESCENDING opportunity order — Strong before Good before
      Moderate before Weak; break ties by higher `volume`. (Rows with no volume/kd → no
      Opportunity → lowest priority; write them only when nothing scored is left.) This
      still respects dedup + anti-cannibalization (step d/d2) — skip a high-opportunity
      candidate if its cluster is already covered.
   c. If still short, research more (Ahrefs `country=de`, competitor DE dental sites,
      Google autosuggest, PAA) and append candidates to `DentalVia/research-topics.md`.
      NEVER invent weak topics to hit the number — write fewer instead.
   d. **Dedup (exact)** each candidate against `DentalVia/content-queue.md` (any status)
      AND the live sitemap `https://dentalvia.de/sitemap.xml` AND the existing live
      Ratgeber articles listed in `DentalVia/conversion-links.md` (those count as covered
      clusters) — drop anything already covered.
   d2. **Anti-cannibalization (keyword-cluster, not just URL).** Do NOT create a new article
      that targets essentially the same primary keyword / search intent as an existing or
      already-queued article, or as another candidate in this same batch. Group candidates
      into keyword clusters (e.g. all "Zahnimplantate Kosten" variants, all destination
      comparison variants) and write **ONE pillar per cluster**, choosing the
      highest-opportunity member; near-duplicates become sections or internal links inside
      that pillar, not separate pages. Also apply **German compound/synonym clustering**:
      Zahnimplantat / Implantat / Zahnersatz / dritte Zähne cluster as one intent; Kosten /
      Preise / Erfahrungen modifiers cluster as one intent across those roots. When unsure,
      prefer fewer, clearly distinct pillars over many overlapping ones.
   e. For each selected topic add a `DentalVia/content-queue.md` row: fresh `id`,
      `status: in-progress`, `type`, `byline` (leave BLANK at row creation — it is filled
      during that article's step-4 byline step, just before writing begins; the rotation
      reads the most recent NON-EMPTY byline in the queue),
      `query`, `keywords_or_terms` (the keywords you will actually target), `volume` + `kd`
      (copy the target keyword's Ahrefs metrics from research/backlog so the dashboard can
      show Vol/KD/Opportunity per article), `source` = `backlog` or `research`, `folder` =
      `<TODAY>-<slug>`.

4. **Write each article** in `DentalVia/articles/<TODAY>-<slug>/` (TODAY = today's date;
   get it with `date -u +%Y-%m-%d`):

   - **Byline step (before writing).** Read `DentalVia/content-queue.md` and find the most
     recent row that has a `byline` value. This article gets the OTHER name (Georgi Todorov
     ↔ Mario Yordanov). If no prior row exists, use **Georgi Todorov**. Write the chosen
     byline into `DentalVia/articles/<slug>/00-brief.md` and into the queue row's `byline`
     column immediately (so the next article's byline step reads it correctly).

   - Assemble `00-brief.md` from
     `DentalVia/pipeline/templates/00-brief-template-dentalvia.md`
     (web-search + fetch top 2-3 German-language sources). If sources are unreachable and
     the type needs them (price comparisons, insurance data, clinical claims), STOP this
     article and mark it `failed` — never fabricate prices, clinical facts, or figures.

   - Run stages **1 → 1.5 → 2 → 3 → 4 → 5 → 5b** as FRESH-CONTEXT subagents, each reading
     only its inputs, loading `DentalVia/pipeline/agents/*.md` + `DentalVia/pipeline/prompts/*.md`.
     Brand bindings:
     · gate = `DentalVia/pipeline/agents/brand-gate-dentalvia.md`
     · author = `DentalVia/pipeline/markets/de/author.md`
     · Stage 2 is ALWAYS editorial mode (no tester/persona routing on this brand)

   - DIFF ALL NUMBERS between text-editing stages; any changed/missing number → halt this
     article, mark `failed`, log why.

   - Brand Gate FAIL → fix at the failing stage and re-run forward; never hand-patch.

   - **Conversion links:** if the article mentions a specific treatment by name (implants,
     veneers, crowns, root canal, bone grafting, etc.), link that first prominent mention
     to its treatment page from `DentalVia/conversion-links.md`. Every article links 2–5
     internal pages; every article ends with the CTA block targeting `/kontakt/`
     („Kostenlose Beratung"). Long pillars (>1,500 words) may add one mid-article link to
     `/kontakt/`. If an article topic naturally calls for a page not in the registry,
     insert `[LINK NEEDED: <topic>]` — NEVER invent a URL or link to an external domain.
     Keep the compliance footer blocks (disclaimer + transparency line) verbatim.

   - **Verify-assist (before Step 7).** Run the flag-verification pass per
     `DentalVia/pipeline/reference/verification-policy.md` as a FRESH-CONTEXT stage over
     `05b`: fetch each flagged claim's PRIMARY source, resolve confirmed Tier-B flags
     (primary-source quote attached in `06-verification.md`), remove stray Tier-A markers
     (example-framed figures — fix the „Stand MM/JJJJ" framing where needed), keep Tier C
     for the human. `06-verification.md` gets RESOLVED / REMAINING FOR HUMAN sections plus
     a count summary; the PR body cites both counts. Never alter a claim to match a source
     — mismatches become `[CONFLICT]`. (Writing stages 1–2 also load the policy file so
     Tier-A figures are not flagged in the first place.)

   - **Step 7 — external Gemini check (cross-model).** After `05b` is final, run:
     `python3 scripts/gemini_check.py <article>/05b-final-draft.md`. It reads `GEMINI_API_KEY`
     and prints Gemini's verdict + recommendations.
     · **If it exits non-zero / prints `GEMINI_UNAVAILABLE`/`GEMINI_ERROR`** (key unset, API
       down): DO NOT halt — log `external check: skipped (Gemini unavailable)` and continue.
     · **Interpreting the verdict → one HUMAN-LIKENESS score (0–100, higher = better).**
       Gemini phrases it two ways; normalize BOTH before any comparison:
       `"Likely human-written, X%"` → human-likeness = **X**; `"Shows AI patterns, Y%"` →
       human-likeness = **100 − Y**. (So "AI patterns 65%" = 35 human-likeness, which is
       worse than "human-written 70%".) Use human-likeness for the PASS test AND for
       keep-best — NEVER compare the raw confidence numbers across different verdict types.
     · **PASS** when **human-likeness ≥ GEMINI_TARGET_CONFIDENCE (80)** — log
       `external check: Gemini <verdict>` and continue.
     · **Otherwise** (shows AI patterns, or human-written < 80): iterate to improve. Each
       pass: apply Gemini's flagged recommendations through a FRESH Humaniser pass using
       `DentalVia/pipeline/prompts/step-7b-apply-gemini-recs.md` (preserve EVERY untouchable:
       numbers, links, compliance lines, medical disclaimer, transparency line, dates, byline,
       brand name; never paste Gemini's text), then a quick Brand Gate re-check, then
       re-run `gemini_check.py`. Repeat up to `MAX_GEMINI_PASSES` (2).
     · **KEEP THE BEST STATE (mandatory).** Record the **human-likeness** of the INITIAL
       draft and of EVERY pass (the `07-gemini-check-<pass>.md` files preserve the verdicts).
       A Humaniser pass can *lower* human-likeness. When the loop ends — by PASS or by
       hitting the cap — the final `05b` MUST be the version with the **highest
       human-likeness seen**, even if that is the untouched original or an earlier pass.
       NEVER keep a later, lower version just because it came last. Commit the winner as
       `content(<slug>): keep best version (pass <k>, <human-likeness>%)` and record it in
       the `gemini` column: `human <hl>` if human-likeness ≥ 80, else `ai <100−hl>`.
     · Gemini must NEVER touch facts, medical claims, compliance lines, or `[VERIFY]` flags
       — it is style-only; recommendations only.
     · **Commit-history discipline (audit trail on the PR branch).** Keep every iteration as
       its own commit so the PR shows draft → Gemini feedback → revision → re-check:
         1. Commit the initial draft (whole `DentalVia/articles/<slug>/`): `content(<slug>): initial draft`.
         2. After each Gemini check, save Gemini's verbatim verdict + recommendations to
            `DentalVia/articles/<slug>/07-gemini-check-<pass>.md` and commit:
            `gemini(<slug>): check <pass> — <verdict> (<needs changes|PASS>)`.
         3. After applying the recommendations via the Humaniser, commit the revised `05b`:
            `content(<slug>): humaniser pass <pass> (apply Gemini recs)`.
         4. Repeat 2–3 until PASS or `MAX_GEMINI_PASSES`. Never squash these commits.
     · **Record the result in `DentalVia/content-queue.md` `gemini` column** so the
       dashboard shows it: `human <conf>` if it passed, `ai <conf>` if it ended below 80
       after the cap, or `skipped` if Gemini was unavailable.

   - **Step 8 — article images (create + Gemini visual review).** After the text is final,
     give the article **at least `IMAGE_MIN_PER_ARTICLE` (1) image** — more when each earns
     its place. Follow `DentalVia/pipeline/prompts/step-8-images.md` VERBATIM for what to
     make and the hygiene rules. In short:
     · **Prefer a data infographic (hand-authored SVG)** whenever the article has numbers/
       comparisons/steps — every figure copied VERBATIM from `05b` (never introduce a number
       the text doesn't state; label illustrative figures as Beispielwerte). SVG needs no API.
     · **Optionally add a concept-hero** via `python3 scripts/gemini_image_gen.py
       "<english descriptive prompt with hygiene constraints>" \
       DentalVia/articles/<slug>/images/<descriptive-name>.webp 100`. It writes a WebP < 100 KB.
       If it exits non-zero / prints `GEMINI_UNAVAILABLE`/`GEMINI_ERROR`, DO NOT halt — log
       `image gen: skipped (Gemini unavailable)` and ship the infographic alone.
     · **Hygiene (both kinds):** no operator/clinic logos, no fake X-rays or clinical
       screenshots, no invented prices/percentages, no people/faces, no medical procedures
       depicted graphically; descriptive lowercase-hyphenated filename; specific German ALT
       text. Save under `DentalVia/articles/<slug>/images/` and reference each image from
       `05b-final-draft.md` at the natural spot (concept-hero under the H1; infographic
       beside its data) with German ALT and, for infographics, a one-line German caption.
     · **Gemini visual review (per image).** Run `python3 scripts/gemini_image_review.py
       DentalVia/articles/<slug>/05b-final-draft.md <image1> [<image2> …]` (raster images
       reviewed as pixels; SVGs as source so numbers are checked). It prints a 0–100 score
       + verdict + fixes.
       · Unavailable / non-zero exit → log `image review: skipped (Gemini unavailable)` and
         keep the image(s) (do NOT halt).
       · **PASS** when score **≥ IMAGE_TARGET_SCORE (80)** AND no integrity failure
         (a fabricated logo/number/screenshot, a person/face, a clinical procedure depicted
         graphically, or glamorised outcome is an AUTOMATIC fail even at a high score).
       · **Otherwise** iterate: for a hero, regenerate with an improved prompt; for an
         infographic, hand-fix the SVG (numbers still trace to `05b`). Re-run the review.
         Repeat up to `MAX_IMAGE_PASSES` (2).
       · **Keep-best (mandatory):** if still < 80 after the cap, keep the highest-scoring
         version seen. **Integrity failure → never ship a fabrication:** drop that image
         and keep the article's other image(s), or ship the infographic alone.
     · **Commit trail (audit on the PR branch), mirroring Step 7:** commit the created
       image(s) (`content(<slug>): add image(s)`); save each Gemini image verdict verbatim to
       `DentalVia/articles/<slug>/08-image-review-<pass>.md` and commit
       (`image(<slug>): review <pass> — score <n> (<PASS|needs work>)`); then commit any fix
       (`content(<slug>): image fix pass <pass> (apply review)`). Never squash these.
     · **Record it:** note the final image count + best review score in `06-verification.md`
       (e.g. `images: 2 (infographic 88, hero 82)`), and add a short `notes` mention on the
       `DentalVia/content-queue.md` row (e.g. `img:2`). Never let images block the PR — an
       article with zero shippable images still proceeds, logged as `images: none (reason)`.

   - Assemble `06-verification.md`: surviving flags + time-sensitive claims with
     primary-source URLs (DGI/DGZMK, peer-reviewed studies, KZBV/GKV, manufacturers);
     recalculate one price/savings claim with working shown. FLAGS STAY IN THE TEXT.
     Record the Gemini verdict (final confidence + passes applied) in `06-verification.md`
     and one line per stage in `log.md`.

5. **Record the outcome (board on `main`):**
   - Success → `DentalVia/content-queue.md` row `status: drafted`, fill `drafted_date`.
     If the topic came from `DentalVia/topic-backlog.md`, set that backlog row
     `status: written`. If from `DentalVia/research-topics.md`, set that row `status: used`.
   - Failure → `DentalVia/content-queue.md` row `status: failed` with a `notes` reason.
     If from backlog, set that backlog row `status: failed` (stays visible, flagged for
     retry).
   - **Do NOT resolve flags, post, or merge.** The human owns verification and publishing.

6. **Keyword research + analysis (Ahrefs, with web fallback) → refresh dashboard.**

   **Data source, in order (never halt on failure):**
   - PREFERRED — **Ahrefs API**: base `https://api.ahrefs.com/v3`, header
     `Authorization: Bearer $AHREFS_API_KEY`, market **`country=de`**. (If unsure of the
     exact endpoint/field names, read `https://docs.ahrefs.com` at runtime — do not invent
     endpoints.) For each keyword pull: search **volume**, **keyword difficulty (kd)**,
     search **intent**, and a **trend** signal (up/flat/down from volume history). Mark
     `checked = ahrefs`.
   - FALLBACK — if `$AHREFS_API_KEY` is unset, or Ahrefs returns errors / is unreachable /
     out of units: **DO NOT STOP**. Estimate via web research (WebSearch/WebFetch: related
     searches, autosuggest, competitor headings, People-Also-Ask). Fill what you can; mark
     `checked = web`; leave `volume`/`kd` blank if you cannot estimate them credibly (never
     fabricate precise numbers — an estimate must be labelled as such in the suggestion).

   **Keyword weighting — five families (research and prioritisation priority order):**

   1. **Treatment + cost/money keywords** (highest intent, closest to consultation lead):
      „Zahnimplantate Kosten", „All-on-4 Kosten", „Zähne machen lassen im Ausland",
      „Veneers Bulgarien Preise". These convert; prioritise for pillar articles.

   2. **Destination comparisons** (capture Ungarn/Türkei demand, make Bulgaria's case
      honestly): „Zahnimplantate Ungarn", „Zahnimplantate Türkei", „Zahnersatz Bulgarien
      Vergleich". Cover competitor destinations fairly — patient rights, Gewährleistung,
      and proximity are Bulgaria/EU advantages that can be stated honestly without bashing.

   3. **Trust & safety** (high-value mid-funnel; builds authority with sceptical patients):
      „Zahnarzt Ausland seriös", „Gewährleistung Zahnersatz Ausland". These readers need
      reassurance, not a sales pitch — prioritise for guide-type treatment.

   4. **Insurance & reimbursement** (strong intent, Germany-specific regulatory context):
      „Heil- und Kostenplan im Ausland", „Krankenkasse Zuschuss Zahnersatz Ausland".
      Always [VERIFY] with KZBV/GKV sources; never assert figures without a source + date.

   5. **Treatment education (TOFU)** (broad reach, brand awareness, long-term authority):
      „Knochenaufbau Ablauf", „Wurzelbehandlung oder Implantat". Write as educational
      guides (reader is weighing options, not yet booking) — neutral, risk-inclusive,
      links to relevant treatment pages.

   **German compound/synonym clustering rule (apply at research time):**
   Zahnimplantat / Implantat / Zahnersatz / dritte Zähne cluster as one intent — keep only
   ONE pillar candidate per intent cluster. Kosten / Preise / Erfahrungen as modifiers
   cluster as one intent when the root treatment is the same (e.g. „Zahnimplantate Kosten"
   and „Zahnimplantate Preise" are one cluster). DROP a duplicate; record it as
   "fold-in: <kw>" in the pillar's `suggestion`, never add it as a separate row.

   **Young-domain bias:** prefer **low keyword difficulty (KD)**. High-KD head terms (e.g.
   „Zahnimplantat" standalone, „Veneers") stay in `research-topics.md` at `status: candidate`
   with `suggestion: "pillar — wait for authority"` — do NOT queue them yet. The existing
   live Ratgeber articles in `DentalVia/conversion-links.md` count as covered clusters for
   anti-cannibalization; do not research their primary intent as a new candidate.

   **a. AI research bank (`DentalVia/research-topics.md`, 11-col schema):** discover/refresh
   candidate DE dental-tourism keywords. For each row fill `type, query,
   researched_keywords, volume, kd, intent, trend, checked, suggestion, status,
   date_researched`. `suggestion` is a one-line rating/verdict (e.g., "stark: hohes Volumen,
   niedrige Schwierigkeit" or "schwaches Volumen, probiere Long-Tail X"). The dashboard
   computes the Opportunity band/score from volume+kd, so keep those accurate.

   **Apply anti-cannibalization WHEN RESEARCHING (not just when writing):** cluster every
   new keyword by primary intent (including German compound/synonym clustering above) and
   keep only **one pillar candidate per cluster** in the bank. DROP a candidate outright if
   its cluster is already covered by (i) an existing or queued article (`DentalVia/content-queue.md`
   / the live sitemap), (ii) an `open` human backlog keyword, (iii) a live Ratgeber article
   in `DentalVia/conversion-links.md`, or (iv) a pillar already in this bank. Near-duplicates
   are recorded in the pillar's `suggestion` as "fold-in: <kw>", never added as separate
   candidate rows.

   **Zero-volume rule (skip or reword — no dead rows in the bank):** if Ahrefs was
   queried and returns no measurable volume (blank or 0) for the query and all its
   `researched_keywords` variants, do NOT add/keep it as a candidate row. First try to
   **REWORD**: use matching-terms / related-keywords discovery to find a same-intent
   variant with real measured volume and record THAT as the candidate (still one pillar
   per cluster). If no variant in the cluster has measurable volume, **SKIP** the topic
   entirely — at most leave a "fold-in: <kw>" note on an existing volume-bearing pillar.
   Existing `candidate` rows that are `checked = ahrefs` with blank/0 volume are removed
   under the same rule (`used`/`queued` rows stay for the record). `checked = web` rows
   with a credible web-estimated volume may stay while Ahrefs units are exhausted, but
   MUST be re-verified at the next Ahrefs reset — any that then show no measurable
   volume are reworded or dropped the same way.

   **b. Analyse the human backlog (`DentalVia/topic-backlog.md`, enriched 11-col):** for
   every row with `status: open`, look the keyword up (Ahrefs `country=de`, else web) and
   fill `volume, kd, intent, checked` and `ahrefs_note` — a short verdict + suggestion
   (e.g. "gute Wahl, niedriger KD" / "geringes Volumen; erwäge '<stärkere Alternative>'").
   NEVER change the human's `priority`, `type`, `query`, `keywords_or_terms`, or `status`
   — only enrich the metric columns.

   Then run `python3 scripts/build_dashboard.py dentalvia` to regenerate
   `docs/data/dentalvia/status.json`.

7. **Open one PR per written article — content only.** Branch `dv-content/<TODAY>-<slug>`
   contains ONLY `DentalVia/articles/<slug>/*` (the article + its `images/`). PR title =
   the article query (prefix `[FAILED] ` if it failed); body summarises type, gate score,
   humanisation verdict, surviving-flag count, **image count + best image-review score**,
   the byline used, and links `06-verification.md`. Embedding an image preview in the PR
   body is fine. Request review from the repo owner. Then set that article's
   `DentalVia/content-queue.md` `pr` column to `#<PR number>`.

8. **Commit the board to `main`** (`DentalVia/content-queue.md`, `DentalVia/topic-backlog.md`,
   `DentalVia/research-topics.md`, `docs/data/dentalvia/`) and end the heartbeat:
   `docs/data/dentalvia/run-status.json`
   `{"state":"idle", "run_started_utc":"<start>","run_finished_utc":"<now>",
   "articles_written":<N drafted>,"prs_opened":[<pr numbers>],"run_url":"<url>",
   "note":"<summary>","progress":{...,"phase":"done","stage":null}}`. Push to `main`.
   > **Publisher integration comes later.** There is no `build_feed.py` / published-feed
   > step for DentalVia yet — publishing is out of scope for the current automation.
   > When a publisher workflow is added, this step will be updated.

## Never
- Never commit article files to `main` (they go via PR). Never present `05b` as final,
  resolve a flag, post, or merge.
- Never fabricate medical facts, clinical claims, prices, or success rates. Never fabricate
  a topic to hit a number.
- Never resolve flags — FLAGS STAY IN THE TEXT for the human's Step 6 verification.
- Never schedule this run. This run is MANUAL TRIGGER ONLY — do not register a CronCreate,
  routine, or any scheduled automation for it.
- Never load another brand's or market's agent files. Never write sports predictions or
  gambling content.
- Never claim DentalVia or the authors treat, examine, or diagnose patients.
