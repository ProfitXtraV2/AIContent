# Daily Run — VsichkiKazina Content Autopilot

You are running the daily content autopilot for **vsichkikazina.bg**. Work only
inside this repo. Brand is hard-locked: `BRAND: vsichkikazina` (Bulgarian output,
€, НАП, no sports predictions, approved internal-link set only). Follow the
pipeline in `VsichkiKazina/pipeline/` VERBATIM — never paraphrase its agent files.

## Constants
- BUFFER_MINIMUM = 10   (a FLOOR, not a cap — the buffer of written-but-unposted articles
  should never sit below this. There is NO upper limit: keep producing quality content and
  let the library grow. The buffer only guides urgency, never stops production.)
- MAX_PER_RUN = 3       (new articles to write per run — always aim for this many, every run,
  regardless of how full the buffer already is; small batches keep clear of the rate limit)

## Resume / idempotency (a failed run must self-heal on the next fire)
This run may be re-fired at any time (schedule fires 3×/day; a prior run may have died on a
429 rate limit). It MUST be safe to re-run and MUST continue, not restart:
- **First, reconcile leftovers.** Before selecting new topics, look for `content-queue.md`
  rows with `status: in-progress` (an article a previous run started but didn't finish).
  For each: if its `content/<slug>` branch already has a complete `05b`, finish it (Gemini
  Step-7 → PR → set `drafted`); otherwise complete the writing from where it left off. Only
  after all in-progress rows are resolved do you select NEW topics for this run's batch.
- **Never duplicate.** An article already `drafted`/`approved`/`posted` (or with an open PR)
  is done — never rewrite it. Dedup every new candidate against the queue + sitemap as usual.
- **Rate-limit behavior.** If you hit a 429 mid-run, commit whatever is safely complete
  (drafted rows + their PRs), leave the rest `in-progress`, end the heartbeat as `idle`, and
  STOP cleanly — the next scheduled fire resumes from the in-progress rows.
- GEMINI_TARGET_CONFIDENCE = 80   (Step 7 accepts at "human-written ≥ 80%"; 80 is acceptable)
- MAX_GEMINI_PASSES = 2            (max Humaniser re-passes driven by Gemini before handing to human)

## CURRENT CONTENT SCOPE (guides-only autopilot)
Until a BG-reachable source route exists (proxy/scraping-API or human source packs), the
cloud environment CANNOT reach operator T&C pages or the НАП register (geo-block: 403 /
connection reset). Therefore, for now:
- **Write only `guide`-type topics** (and any topic that needs NO operator-specific or НАП
  primary source — evergreen education, worked-€ math, concept explainers).
- When selecting topics (step 3), **skip `review` / `comparison` / `news`** items that
  depend on operator terms/licence data. Do NOT attempt them (they will fail on geo-block).
  Leave them in the backlog with a note `needs source pack / BG route`; fill the batch
  with guides instead. Never fabricate operator facts to force one through.
- **Game & provider explainers ARE in scope — do NOT defer them.** Specific slots (e.g.
  „Sweet Bonanza", „20 Super Hot"), game types (бакара, кено, крас игри), and provider
  profiles (Pragmatic Play, Amusnet/EGT) are `guide`-type and writable. Their facts — RTP,
  volatility band, mechanics/features, max win, provider background — come from the
  **provider's own site + international game databases**, NOT from geo-blocked BG operator
  T&C or the НАП register. Write them as educational how-it-works guides (they are NOT
  operator reviews and need no operator licensing/bonus terms). Source every specific figure
  (e.g. an exact RTP %) from a reachable page; if one cannot be verified, mark it `[VERIFY]`
  — never fabricate. So high-opportunity slot/provider keywords should be WRITTEN, not
  skipped. (Only truly operator/НАП-list-dependent topics like a ranked "лицензирани казина"
  table are deferred — but the same intent can be a writable "how to check a licence" guide.)
- This scope is a single switch: when full operator sourcing is solved, allow all types again.

## Brand conventions (every article)
- Byline/author is ALWAYS **Георги Тодоров** — never "Екипът на Всички Казина" or a
  team/editorial byline (even editorial-voice guides are signed Георги Тодоров).
- Write the brand name exactly **Всички Казина** in published copy (no transliteration).
- If an article reads as over-structured / AI-patterned, apply
  `pipeline/prompts/step-7b-apply-gemini-recs.md` through a fresh Humaniser pass (break
  symmetry, drop narrative signposts, de-count headers/lists, cut synthesizing summaries),
  preserving every number, link, RG line, disclosure and date. The Brand Gate enforces
  the byline and brand-name rules.

## What goes where (data model)
- **Article content** (`VsichkiKazina/articles/<slug>/*`) goes on a **PR branch** only,
  for human review. Never commit article files to `main`.
- **Board files** are operational tracking and ARE committed to `main` so the dashboard
  is always accurate: `content-queue.md`, `topic-backlog.md`, `research-topics.md`,
  `docs/data/run-status.json`, and the `docs/` dashboard. Committing these to `main` is
  expected — it is not article content.

## Live progress reporting (drives the dashboard step tracker)
Keep a `progress` object in `run-status.json` current. **This is what animates the stage
tracker** — the dashboard hides the tracker when `stage_index` is `null`, so you MUST set
it, not leave it null. Cadence, at EACH stage boundary of the current article (a quick,
one-file commit + push — do this even though you're mid-article; it is cheap and expected):

`progress = {"phase":"writing","article_index":<1-based>,"article_total":<batch size>,
"article_slug":"<slug>","stages":["Synthesis","Outline","Author","Humaniser","SEO",
"Brand Gate","Light re-check","Verification","PR"],"stage_index":<0-based index of the
stage you are STARTING now>,"stage":"<that stage's name>"}`.

- Set `stage_index` to `0` (Synthesis) before the first stage, then bump it to `1,2,3…`
  as each stage completes and the next begins. Push after each bump.
- Use the exact stage names above. The dashboard reads this file fresh via the GitHub API,
  so updates appear within ~seconds (Pages build latency does not apply).
- If you genuinely cannot push per stage, at minimum bump `stage_index` once per completed
  stage; never leave it `null` for the whole article (that shows only "writing…").

## Procedure

1. **Sync + start heartbeat.** Get up-to-date `main` (the human may have merged
   approvals, marked articles `posted`, or edited `topic-backlog.md`). Write
   `run-status.json` `{"state":"running","run_started_utc":"<now>","run_finished_utc":null,
   "articles_written":null,"prs_opened":[],"run_url":"<this run's URL if known>",
   "note":"daily run","progress":{...as above, stage null}}` and push to `main`.

2. **Set the batch size.** Run `python3 scripts/build_dashboard.py` and read
   `docs/data/status.json`. This run writes **`batch = MAX_PER_RUN` NEW articles**, ALWAYS —
   even if the buffer is already ≥ BUFFER_MINIMUM. The minimum is a floor, NOT a cap: never
   stop producing just because the buffer is "full". The ONLY thing that lowers the count is
   quality — if there aren't `MAX_PER_RUN` genuinely distinct, non-cannibalizing, on-strategy
   topics available after dedup/research, write fewer (quality over quota; never pad). If the
   buffer is BELOW the minimum, treat filling it as extra-urgent but still cap this run at
   MAX_PER_RUN. (Only skip writing if there are truly zero valid distinct topics left.)

3. **Select up to `batch` topics:**
   a. Take up to `batch` rows with `status: open` from `topic-backlog.md`, in priority
      order (do NOT change their status yet — only the write outcome sets it, step 5).
      **Backlog is a commitment:** every `open` backlog keyword MUST eventually become a
      written article (it should show up in "Articles for review"). Prioritise the backlog
      ahead of research candidates and keep attempting its open rows across runs until each
      reaches `written` (with its PR noted). Never silently drop an open backlog item; if
      current scope/sourcing blocks it (e.g. a review needing operator data under the
      guides-only scope), keep it `open` with a `blocked: <reason>` note so it is revisited
      the moment it is unblocked.
   b. If fewer than `batch`, top up from `research-topics.md` `status: candidate` rows,
      **highest-Opportunity first**. Read the computed Opportunity from `docs/data/status.json`
      (each research row has `opportunity.score`/`band`) and pick candidates in DESCENDING
      opportunity order — Strong before Good before Moderate before Weak; break ties by
      higher `volume`. (Rows with no volume/kd → no Opportunity → lowest priority; write them
      only when nothing scored is left.) This still respects dedup + anti-cannibalization
      (step d/d2) — skip a high-opportunity candidate if its cluster is already covered.
   c. If still short, research more (НАП register, competitor BG sites, BG gambling news)
      and append candidates to `research-topics.md`. NEVER invent weak topics to hit the
      number — write fewer instead.
   d. **Dedup (exact)** each candidate against `content-queue.md` (any status) AND the live
      sitemap `https://vsichkikazina.bg/sitemap.xml` — drop anything already covered.
   d2. **Anti-cannibalization (keyword-cluster, not just URL).** Do NOT create a new article
      that targets essentially the same primary keyword / search intent as an existing or
      already-queued article, or as another candidate in this same batch. Group candidates
      into keyword clusters (e.g. all "без депозит" variants, or "безплатни казино игри"
      variants) and write **ONE pillar per cluster**, choosing the highest-opportunity
      member; the near-duplicates become sections or internal links inside that pillar, not
      separate pages. Also skip candidates that overlap heavily with an existing article
      (e.g. a "срок за разиграване" standalone when the wagering guide already covers it) —
      route them as a section/link instead. When unsure, prefer fewer, clearly distinct
      pillars over many overlapping ones.
   e. For each selected topic add a `content-queue.md` row: fresh `id`, `status: in-progress`,
      `type`, `query`, `keywords_or_terms` (the keywords you will actually target),
      `volume` + `kd` (copy the target keyword's Ahrefs metrics from research/backlog so the
      dashboard can show Vol/KD/Opportunity per article), `source` = `backlog` or `research`,
      `folder` = `<TODAY>-<slug>`.

4. **Write each article** in `VsichkiKazina/articles/<TODAY>-<slug>/` (TODAY = today's date;
   get it with `date -u +%Y-%m-%d`):
   - Assemble `00-brief.md` from `pipeline/templates/00-brief-template-vsichkikazina.md`
     (web-search + fetch top 2-3 BG sources). If sources are unreachable and the type
     needs them (review/comparison/news), STOP this article and mark it `failed` — never
     fabricate operator terms, licences, or figures.
   - Run stages **1 → 1.5 → 2 → 3 → 4 → 5 → 5b** as FRESH-CONTEXT subagents, each reading
     only its inputs, loading `pipeline/agents/*.md` + `pipeline/prompts/*.md`. Brand
     bindings: gate = `pipeline/agents/brand-gate-vsichkikazina.md`; author =
     `pipeline/markets/bg/author.md` (+ VOICE_BG_review.md for reviews).
   - DIFF ALL NUMBERS between text-editing stages; any changed/missing number → halt this
     article, mark `failed`, log why.
   - Brand Gate FAIL → fix at the failing stage and re-run forward; never hand-patch.
   - **Affiliate links:** if the article recommends/references a specific operator (reviews,
     comparisons, bonus/deposit pieces), link that operator's first prominent mention to its
     `affiliate_url` from `VsichkiKazina/affiliate-links.md` (`status: active` only). If the
     operator is missing from that registry, insert `[LINK NEEDED: <operator>]` — NEVER invent
     an affiliate URL or link a bare operator domain. Keep the affiliate-disclosure footer.
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
       `pipeline/prompts/step-7b-apply-gemini-recs.md` (preserve EVERY untouchable: numbers,
       links, RG lines, 18+, disclosures, dates, byline, brand; never paste Gemini's text),
       then a quick Brand Gate re-check, then re-run `gemini_check.py`. Repeat up to
       `MAX_GEMINI_PASSES` (2).
     · **KEEP THE BEST STATE (mandatory).** Record the **human-likeness** of the INITIAL
       draft and of EVERY pass (the `07-gemini-check-<pass>.md` files preserve the verdicts).
       A Humaniser pass can *lower* human-likeness (e.g. 75 → 70 → 65). When the loop ends —
       by PASS or by hitting the cap — the final `05b` MUST be the version with the
       **highest human-likeness seen**, even if that is the untouched original or an earlier
       pass. NEVER keep a later, lower version just because it came last. Commit the winner as
       `content(<slug>): keep best version (pass <k>, <human-likeness>%)` and record it in the
       `gemini` column: `human <hl>` if human-likeness ≥ 80, else `ai <100−hl>` (i.e. the
       winning version's own verdict, verbatim scale).
     · Gemini must NEVER touch facts, RG language, disclosures, or `[VERIFY]` flags — it is
       style-only; recommendations only.
     · **Commit-history discipline (audit trail on the PR branch).** Keep every iteration as
       its own commit so the PR shows draft → Gemini feedback → revision → re-check:
         1. Commit the initial draft (whole `articles/<slug>/`): `content(<slug>): initial draft`.
         2. After each Gemini check, save Gemini's verbatim verdict + recommendations to
            `articles/<slug>/07-gemini-check-<pass>.md` and commit:
            `gemini(<slug>): check <pass> — <verdict> (<needs changes|PASS>)`.
         3. After applying the recommendations via the Humaniser, commit the revised `05b`:
            `content(<slug>): humaniser pass <pass> (apply Gemini recs)`.
         4. Repeat 2–3 until PASS or `MAX_GEMINI_PASSES`. Each Gemini feedback and each Claude
            revision is a SEPARATE commit — never squash them. The `07-gemini-check-*.md` files
            persist in the article dir as the record.
     · **Record the result in the article's `content-queue.md` `gemini` column** so the
       dashboard shows it: `human <conf>` if it passed (e.g. `human 84`), `ai <conf>` if it
       ended below 80 after the cap (e.g. `ai 68`), or `skipped` if Gemini was unavailable.
       The dashboard turns `human ≥80` into a green ✓ "approved by Gemini" badge (shown on
       both Articles-for-review and Articles-ready-to-deploy).
   - Assemble `06-verification.md`: surviving flags + time-sensitive claims with
     primary-source URLs; recalculate one figure with working shown. FLAGS STAY IN THE
     TEXT. Record the Gemini verdict (final confidence + passes applied) in
     `06-verification.md` and one line per stage in `log.md`.

5. **Record the outcome (board on `main`):**
   - Success → `content-queue.md` row `status: drafted`, fill `drafted_date`. If the topic
     came from `topic-backlog.md`, set that backlog row `status: written` (drops it from
     the Backlog-keywords tab). If from `research-topics.md`, set that row `status: used`.
   - Failure → `content-queue.md` row `status: failed` with a `notes` reason. If from
     backlog, set that backlog row `status: failed` (stays visible, flagged for retry).
   - **Do NOT resolve flags, post, or merge.** The human owns Step 6 and publishing.

6. **Keyword research + analysis (Ahrefs, with web fallback) → refresh dashboard.**

   **Data source, in order (never halt on failure):**
   - PREFERRED — **Ahrefs API**: base `https://api.ahrefs.com/v3`, header
     `Authorization: Bearer $AHREFS_API_KEY`, market **country = `bg`**. (If unsure of the
     exact endpoint/field names, read `https://docs.ahrefs.com` at runtime — do not invent
     endpoints.) For each keyword pull: search **volume**, **keyword difficulty (kd)**,
     search **intent**, and a **trend** signal (up/flat/down from volume history). Mark
     `checked = ahrefs`.
   - FALLBACK — if `$AHREFS_API_KEY` is unset, or Ahrefs returns errors / is unreachable /
     out of units: **DO NOT STOP**. Estimate via web research (WebSearch/WebFetch: related
     searches, autosuggest, competitor headings, People-Also-Ask). Fill what you can; mark
     `checked = web`; leave `volume`/`kd` blank if you cannot estimate them credibly (never
     fabricate precise numbers — an estimate must be labelled as such in the suggestion).

   **a. AI backlog (`research-topics.md`, 11-col schema):** discover/refresh candidate
   BG gambling keywords (data-first, casino-weighted). For each row fill `type, query,
   researched_keywords, volume, kd, intent, trend, checked, suggestion, status,
   date_researched`. `suggestion` is a one-line rating/verdict (e.g., "силен: голям обем,
   ниска трудност" or "слаб обем, пробвай дълга опашка X"). The dashboard computes the
   Opportunity band/score from volume+kd, so keep those accurate.

   **Apply anti-cannibalization WHEN RESEARCHING (not just when writing):** cluster every
   new keyword by primary intent and keep only **one pillar candidate per cluster** in the
   bank. DROP a candidate outright if its cluster is already covered by (i) an existing or
   queued article (`content-queue.md` / the live sitemap), (ii) an `open` human backlog
   keyword, or (iii) a pillar already in this bank. Near-duplicates are recorded in the
   pillar's `suggestion` as "fold-in: <kw>", never added as separate candidate rows. The
   bank must never accumulate two candidates that would compete for the same query.

   **b. Analyse the human backlog (`topic-backlog.md`, enriched 11-col):** for every row
   with `status: open`, look the keyword up (Ahrefs, else web) and fill `volume, kd,
   intent, checked` and `ahrefs_note` — a short verdict + suggestion ("добър избор" /
   "нисък обем; обмисли '<по-силна алтернатива>'"). NEVER change the human's `priority`,
   `type`, `query`, `keywords_or_terms`, or `status` — only enrich the metric columns.

   Then run `python3 scripts/build_dashboard.py` to regenerate `status.json`.

7. **Open one PR per written article — content only.** Branch `content/<TODAY>-<slug>`
   contains ONLY `VsichkiKazina/articles/<slug>/*` (the article). PR title = the article
   query (prefix `[FAILED] ` if it failed) ; body summarises type, gate score, humanisation
   verdict, surviving-flag count, and links `06-verification.md`. Request review from the
   repo owner. Then set that article's `content-queue.md` `pr` column to `#<PR number>`.

8. **Commit the board to `main`** (`content-queue.md`, `topic-backlog.md`,
   `research-topics.md`, `docs/`) and end the heartbeat: `run-status.json`
   `{"state":"idle", "run_started_utc":"<start>","run_finished_utc":"<now>",
   "articles_written":<N drafted>,"prs_opened":[<pr numbers>],"run_url":"<url>",
   "note":"<summary>","progress":{...,"phase":"done","stage":null}}`. Push to `main`.

## Never
- Never commit article files to `main` (they go via PR). Never present `05b` as final,
  resolve a flag, post, or merge.
- Never load BetFam or another market's files. Never write sports predictions.
- Never fabricate a topic, comment, testimonial, or any operator fact to hit a number.
