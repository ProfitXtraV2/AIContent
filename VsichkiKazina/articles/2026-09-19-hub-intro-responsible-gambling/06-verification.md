# Verification — hub-intro-responsible-gambling

- type: hub-intro (category-page intro copy for /blog/responsible-gambling/, not a
  standalone article)
- word count (body, excluding Title tag/Meta description header): 358 words — within the
  350–500 hub-intro spec.
- headings: 0 × H1 (correct — hub page renders its own), 2 × H2 (at the spec cap):
  "Какво включва отговорната игра", "Какво да провериш, преди да заложиш".
- images: none (hub-intro spec — no image stage run, no images/ folder created).
- internal links (3, matching the 2–3 spec range):
  1. Money page: [Betano](/casino/betano/) — framed as part of the responsible-play
     point (a НАП-licensed operator is a precondition for self-control tools existing),
     explicitly disclaimed as not a promotional recommendation. Plain on-site internal
     link, not an affiliate redirect (per task brief).
  2. Category article: [страницата за отговорна игра](/otgovorna-igra/) — self-control
     tools / self-exclusion.
  3. Category article: [тук е обяснено къде и как](/zhalbi/) — where to file a complaint.
  All three were pre-verified by the orchestrator against the live sitemap
  (https://vsichkikazina.bg/sitemap.xml) before this run; none were invented here.
- byline: Георги Тодоров (brand override — always this byline, never a team byline).
  The body itself carries no visible byline line (hub-intro is inserted into the category
  page's existing template); the publisher's meta.json author field is hard-set to
  "Георги Тодоров" regardless (scripts/build_feed.py AUTHOR constant).
- brand name: "Всички Казина" not used verbatim in this piece (not required — no forced
  brand mention was needed for a natural intro of this length/topic); spelling rule
  (never a transliteration) was respected in all supporting/process files.
- RG marker line: verbatim "18+ Хазартът може да пристрасти. Играйте отговорно." present
  inline in the opening paragraph.
- helpline: no specific phone number/organisation named, per the task's explicit caution
  for this safety-sensitive category — phrased generically ("специалист по зависимости
  или национална линия за помощ при хазартна зависимост").
- numbers/facts diff: no numeric facts (превъртане/RTP/€ figures) appear anywhere in this
  piece across any stage — nothing to diff for drift; confirmed identical body text from
  02-draft.md through 05b-final-draft.md (0 words/links/facts changed since Step 2).
- [VERIFY] / [DATA NEEDED] flags: none.
- Brand Gate (Step 5): PASS, 92/100, zero criticals (see 05-gate-report.md).
- Step 5b light humaniser re-check: nothing to fix (em-dashes/signposting/tables/lists/
  other tells all absent) — article returned unchanged.
- Step 7 Gemini external check: see 07-gemini-check-*.md files and log.md for the verdict
  and pass count.
