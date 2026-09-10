# Learn Run — DentalVia (close the Gemini feedback loop)

Periodic maintenance run (weekly, or every ~10 new articles). It mines the **recurring**
patterns Gemini flags across recent articles and proposes them as permanent rules in the
**DE AI-TELL DICTIONARY** inside `DentalVia/pipeline/markets/de/author.md` so future
*first* drafts avoid them — turning per-article fixes into lasting improvement (higher
first-pass scores, fewer Humaniser passes).

It **proposes only** — because it edits the pipeline that shapes ALL future content, it
opens a **PR for human approval** and never commits pipeline changes to `main` directly.

## Procedure

1. **Gather Gemini feedback.** Collect every `07-gemini-check-*.md` from recent articles:
   read them from `DentalVia/articles/*/` on `main` (merged/posted articles) AND from
   all open `dv-content/*` PR branches (`git fetch origin`; `git show <branch>:<path>`).
   Aim for the last ~15–20 articles. Also note each article's final `gemini` score from
   `DentalVia/content-queue.md`.

2. **Extract RECURRING patterns only.** Cluster Gemini's flagged patterns and pick those
   that appear in **≥ 2–3 different articles** (a one-off is not a rule). Capture both:
   - **Named patterns** (symmetrical contrasts, staccato rhythm, didactic imperatives,
     signposting, narrated emotion, over-polished lists, run-on hypothetical sentences,
     translated-sounding German calques, formal A/B dilemma structures), and
   - **Concrete DE phrases/idioms** Gemini repeatedly calls "translated-sounding" or
     unnatural in German patient-guide context (e.g. „darüber hinaus", „des Weiteren",
     „abschließend lässt sich sagen" and similar AI connectives; German equivalents of
     „Moreover / Furthermore / In conclusion").
   For each, keep 2–3 real example quotes + the source article slugs as evidence.

3. **Draft additions** to the existing **AI-TELL DICTIONARY · GERMAN** section of
   `DentalVia/pipeline/markets/de/author.md` (and, where it fits,
   `DentalVia/pipeline/agents/humaniser.md`), in the file's existing format: a short
   "avoid X → prefer Y" rule with a real example in German. Do NOT remove or weaken
   existing rules; ADD. Do NOT touch compliance/untouchable rules (facts, medical
   disclaimer, transparency line, prices, flags). Keep it tight — only well-evidenced,
   recurring tells.

4. **Open an approval PR** on a branch `learn/<date>-ai-tells`, title
   `learn: AI-TELL DICTIONARY update from Gemini feedback (<N> articles)`. PR body: the
   patterns added, their frequency, evidence quotes + source slugs, and a one-line
   rationale each. Request review from the repo owner. Do NOT merge; do NOT commit to
   `main`.

5. **Report.** Final message: how many articles analysed, which recurring patterns were
   found, what was proposed, and the current average first-pass Gemini score (trend).

## After merge (human)
Once the PR is merged, the new tells are live for the next content run.

## Guardrails
- Propose, never auto-apply. Evidence ≥ 2 articles per rule. Cite sources.
- Never edit facts, compliance lines (medical disclaimer, transparency line), medical claims,
  prices, risk statements, contraindications, or the untouchables list.
- Additions are style guidance for the Author/Humaniser only.
- Never commit pipeline changes to `main` — PR only, always.
