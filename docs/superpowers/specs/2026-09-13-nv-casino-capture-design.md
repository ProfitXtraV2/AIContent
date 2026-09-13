# NV Casino capture play + review-template upgrade — Design

**Date:** 2026-09-13 · **Status:** approved by Georgi (session)
**Repos:** `ProfitXtraV2/WebPortals` (site + template), `ProfitXtraV2/AIContent` (articles)

## Goal

Capture the large branded search demand for NV Casino (a gray, Curaçao-licensed casino we
cannot and will not affiliate-link) with an honest warning-style review page and two blog
articles, funneling every CTA to our Betano deal. While building the new review page, adopt
the parts of slotcatalog's competitor review template that beat ours (richer spec data,
casino-specific FAQ, top providers/games block) and roll those upgrades out to all 15
existing `/casino/*` pages.

Keyword opportunity (Ahrefs, global EN, slotcatalog ranks top-3 with a bare catalog page):
`nv casino` 408K/KD31 · `nvcasino` 210K/KD26 · `nv casino online` 44K/KD33 ·
`nv cazino` 18K/KD19 · `nv cassino` 13K · long tail (`nv casink`, `nvcasino.`).
Our page is Bulgarian and targets the BG SERP for these terms plus „нв казино" variants.

## Compliance stance (load-bearing)

- NV Casino has **no НАП license** → we never link to it, never show a "Играй сега" for it.
- The page is a **warning review**: „популярно, но нелицензирано в България — играйте при
  лицензиран оператор“. This is also the safe framing for our pending НАП affiliate license.
- Every CTA is an **honestly labeled Betano recommendation** (`/go/betano/?src=nv-*`,
  `rel="nofollow sponsored noopener"`). No dark patterns: the button says Betano, not NV.
- Verified NV facts only (slotcatalog + NV's public site): operator Kaurum Limited, Curaçao
  license 8048/JAZ, founded 2024, ~2 400+ games / 65+ providers, welcome package up to
  €2000 + 225 FS at **x40** wagering (FS x30), min deposit €10, min withdrawal €45, crypto
  accepted, 24/7 chat/email support incl. Bulgarian. During research, check the НАП
  blocked-sites register for nvcasino domains and state only the verified outcome.

## 1. Review page — `/casino/nv-casino/` (WebPortals)

Built on the existing review template (Betano page is the reference) **after** the template
upgrades in §3, so it is born in the new format.

- **Hero**: NV logo (`assets/img/brands/nv-casino.png`, sourced from their public brand
  asset), overall dial **≈5.6/10**. Red badge **„Без лиценз от НАП“** replaces the license
  badge. Hero CTA block = „Нашата препоръка: Betano — 100% до €1500 + 150 FS“ →
  `/go/betano/?src=nv-verdict`.
- **Score bars**: Легалност 0 · Бонуси ~55 · Игри ~85 · Дизайн ~75 · Плащания ~60 ·
  Поддръжка ~70. Overall ≈5.6 (check `/kak-ocenyavame/` weighting; legality dominates).
- **Spec table** (new richer format): license + „невалиден за България“, operator, founded
  year, games/providers counts, bonus + wagering, min deposit/withdrawal, payment methods
  (incl. crypto — no `/depoziti-i-teglenia/` anchors for methods we don't cover there),
  currencies, support languages/channels.
- **Prose**: why it's searched; what a Curaçao license does/doesn't protect (no НАП
  recourse, NRA domain-blocking status as verified); bonus math x40 vs Betano x25; games;
  payments (€45 min withdrawal called out); support; closing section **„По-добра
  алтернатива“** with the Betano CTA. Winbet-style alt-modal backs any secondary buttons.
- **SEO/structured data**: title ~ „NV Casino — ревю 2026: законно ли е в България?“;
  Review JSON-LD with the low rating + negativeNotes; casino-specific FAQPage JSON-LD
  (has-НАП-license?, законно ли е да играя?, как се теглят пари?, по-добра алтернатива?);
  BreadcrumbList + WebPage JSON-LD; OG image at `assets/img/og/nv-casino.webp` (same
  Gemini-bg + Pillow-Cyrillic approach as article OG images); sitemap upsert.
- **Linking**: NOT in the homepage toplist or `sravni-kazina` (unlicensed). Inbound links
  from the two blog articles and from `/zakonno-li-e/`.

## 2. Blog articles — AIContent pipeline, run manually this session

Both follow the normal pipeline (`VsichkiKazina/pipeline` + `automation/daily-run.md`
steps): research → draft per `pipeline/markets/bg/author.md` → Step-7 Gemini text check →
Step-8 images → one PR per article. Merge = approve → cloud publisher → FTP, as usual.

1. **„NV Casino — законно ли е в България?“** → category `regulations-taxes`.
   Legality/is-it-legit intent. Verified NRA-register facts, НАП official link (follow),
   links to `/casino/nv-casino/` and Betano funnel.
2. **„NV Casino бонус: какво реално означава 100% до €2000 при x40 превъртане“** →
   category `bonuses-vip`. Bonus-hunter intent; wagering math (x40 deposit+bonus vs Betano
   x25); same funnel.

Images per policy: 1 concept hero + 1 SVG infographic each (e.g. wagering-cost comparison,
numbers verbatim from the article's 05b). Topic rows are recorded in `topic-backlog.md` as
`written` so the autopilot doesn't duplicate them.

## 3. Template upgrades → all 15 existing `/casino/*` pages

Adopted from slotcatalog; applied to the NV page and rolled out to: 8888, admiralbet,
alphawin, bet365, betano, elitbet, everbet, inbet, livescorebet, magicbet, mrbit, palmsbet,
sesame, slotino, winbet.

- **Richer spec table**: add rows — година на основаване (BG market entry where relevant),
  валути, езици/канали на поддръжка, лицензна юрисдикция (НАП for all licensed pages).
- **Casino-specific FAQ**: replace the 5 identical generic questions with 5 per-casino
  Q&As grounded in that page's own facts + research; regenerate FAQPage JSON-LD to match.
- **Top providers/games block**: „Топ доставчици и игри в X“ — only research-verified
  providers/titles from the operator's public lobby.
- **Integrity rule (hard)**: any row/block that can't be verified is omitted — never
  invented. Numbers must match what the page already asserts or what research confirms.
- **Execution**: Betano is upgraded by hand first as the reference implementation (step 1
  of the order of work); the remaining 14 pages go to parallel subagents, one per casino
  page; each researches (existing page prose + operator public site) and edits its page. All diffs reviewed centrally before a
  single commit. Pushing WebPortals `main` auto-deploys via the FTP Action — all upgraded
  pages + the new review go live on that push (normal publisher flow).

## Order of work

1. Template upgrades (structure + one reference implementation on the Betano page).
2. NV Casino review page (born in new format) + OG image + sitemap.
3. 15-page rollout via parallel subagents + central diff review.
4. Two articles through the pipeline (PRs in AIContent).
5. Verify: local render/HTML checks, JSON-LD validity, Gemini SEO gate ≥80 for articles,
   spot-check live pages after deploy.

## Error handling / risks

- **Fact gaps**: omit unverifiable rows (integrity rule) rather than block the rollout.
- **NV facts drift** (gray casinos change terms often): state „към септември 2026“ on
  volatile numbers; the review's warning stance doesn't depend on exact bonus figures.
- **NRA register check may 403 from automation** (seen in topic-backlog #2): if blocked,
  phrase legality claims from the statute (unlicensed = illegal to offer) without claiming
  register-row specifics, and flag for human verification in the PR description.
- **Deploy blast radius**: 16 pages in one push; the FTP Action only uploads changed files,
  and each page is independently renderable — a bad page can be fixed forward with a
  follow-up push.

## Success criteria

- `/casino/nv-casino/` live, indexable, targeting the branded cluster, zero NV outlinks,
  all CTAs → `/go/betano/`.
- 2 article PRs open in AIContent passing Step-7 (human ≥80) with Step-8 images.
- All 15 existing review pages carry the richer spec table, per-casino FAQ (+ JSON-LD),
  and a verified top-providers block (or a logged omission).
