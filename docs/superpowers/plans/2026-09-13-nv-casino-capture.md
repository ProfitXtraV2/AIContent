# NV Casino Capture Play Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship a warning-style NV Casino review at `/casino/nv-casino/` funneling to Betano, upgrade the review-page format (richer spec table, per-casino FAQ, top-providers block) across all 15 existing casino pages, and produce 2 NV Casino blog articles through the AIContent pipeline.

**Architecture:** Static-HTML site (WebPortals repo, `VsichkiKazina/`, deployed by FTP GitHub Action on push to `main`) + content pipeline (AIContent repo, PR-per-article, merge=approve). Review pages are hand-built HTML following the Betano page as canonical structure; blog articles go through `VsichkiKazina/pipeline/` stages verbatim.

**Tech Stack:** Plain HTML/CSS (existing `assets/css/style.css`), JSON-LD, Python 3 (stdlib + Pillow) for validation/OG image, `gh` CLI for PRs, pipeline scripts `gemini_check.py` / `gemini_image_gen.py` / `gemini_image_review.py`.

## Global Constraints

- **Never link to NV Casino** — no aff link, no bare domain link, no "Играй сега" for NV. Every CTA on NV-related pages goes to `/go/betano/?src=nv-<placement>` with `rel="nofollow sponsored noopener" target="_blank"`.
- **Integrity rule (hard):** any fact/row/block that can't be verified is OMITTED, never invented. NV facts must be verified against NV's public pages (reachable locally — the cloud geo-block does not apply to this session) or clearly attributed „към септември 2026 г.".
- NV verified base facts (re-verify in Task 3): operator Kaurum Limited, Curaçao licence 8048/JAZ, founded 2024, ~2 400+ games / 65+ providers, welcome package up to €2000 + 225 FS at **x40** wagering (FS x30), min deposit €10, min withdrawal €45, crypto accepted, 24/7 chat/email incl. Bulgarian.
- Scoring methodology (from `/kak-ocenyavame/`): Законност 25% · Бонуси 20% · Игри 20% · Плащания 15% · Удобство(Дизайн) 10% · Поддръжка 10%. NV bars: Легалност 0, Бонуси 55, Игри 85, Дизайн 75, Плащания 60, Поддръжка 70 → **overall 5.2**.
- Brand copy rules: brand written **Всички Казина**; byline **Георги Тодоров**; 18+ badge + „Хазартът може да пристрасти. Играйте отговорно." on every casino card/CTA block; article rules per `pipeline/markets/bg/author.md` + brand gate.
- Article content only on `content/<date>-<slug>` PR branches, never on AIContent `main`; board files (content-queue, topic-backlog, docs/) on `main`.
- WebPortals: work on `main` (publisher flow), **single push at the end** (Task 7) — push = live deploy via FTP Action.
- Repos: `/Users/georgitodorov/Work/WebPortals` (site), `/Users/georgitodorov/Work/CoWork/ContentWrite/AIContent` (content). Both on `main`, pull before starting.

---

### Task 1: Review-format reference doc + Betano reference implementation

**Files:**
- Create: `WebPortals/VsichkiKazina/_publisher/review-format.md` (canonical structure doc)
- Modify: `WebPortals/VsichkiKazina/casino/betano/index.html`

**Interfaces:**
- Produces: the three new blocks' exact HTML shapes (spec rows, FAQ, providers block) that Tasks 3 and 6 copy verbatim; `review-format.md` documenting them.

- [ ] **Step 1: Pull latest WebPortals main**

```bash
git -C /Users/georgitodorov/Work/WebPortals pull --rebase
```

- [ ] **Step 2: Research Betano facts** (WebFetch betano.bg public pages + existing page prose): year Betano entered the BG market, accepted currencies, support channels + languages, top providers/games actually in its lobby. Record each fact with source URL in a scratch note. Facts that can't be verified → omit that row.

- [ ] **Step 3: Add new spec-table rows to `casino/betano/index.html`** — insert after the existing „Оператор" row, values from Step 2 research (shapes below; drop any unverified row):

```html
<tr><th scope="row">Лицензна юрисдикция</th><td>България (НАП)</td></tr>
<tr><th scope="row">На БГ пазара от</th><td>2019 г.</td></tr>
<tr><th scope="row">Валути</th><td>EUR</td></tr>
<tr><th scope="row">Поддръжка</th><td>Чат на живо и имейл, на български</td></tr>
```

- [ ] **Step 4: Add top-providers block** — new `<section class="wrap prose">` after „Казино игри и доставчици" prose section:

```html
<h3>Топ доставчици и игри в Betano</h3>
<p>Сред 25-те студия в каталога най-силно присъствие имат <a href="/slot-igri/">…verified providers…</a> — включително заглавия като …verified flagship titles…</p>
```

(Names strictly from Step 2 research. If lobby can't be verified, skip the block and log the omission.)

- [ ] **Step 5: Replace generic FAQ with Betano-specific FAQ** — rewrite the 5 `<details class="faq__item">` entries with per-casino Q&As grounded in the page's own facts (licence №s, x25 wagering, €5 min deposit, 24h e-wallet withdrawals, no crypto), and regenerate the `FAQPage` JSON-LD `<script>` in `<head>` to match the new Q&As exactly.

- [ ] **Step 6: Validate**

```bash
python3 - <<'EOF'
import json, re, html
src = open('/Users/georgitodorov/Work/WebPortals/VsichkiKazina/casino/betano/index.html').read()
for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', src, re.S):
    json.loads(m.group(1))  # raises on invalid
faq_html = len(re.findall(r'<details class="faq__item">', src))
print("JSON-LD OK, FAQ items:", faq_html)
EOF
```

Expected: `JSON-LD OK, FAQ items: 5`, no exception.

- [ ] **Step 7: Write `_publisher/review-format.md`** — short doc: section order, the three new blocks with their HTML shapes, FAQ JSON-LD sync rule, integrity/omission rule, unlicensed-variant notes (red badge, no operator CTA, alt-funnel).

- [ ] **Step 8: Commit (no push)**

```bash
git -C /Users/georgitodorov/Work/WebPortals add VsichkiKazina/casino/betano/index.html VsichkiKazina/_publisher/review-format.md
git -C /Users/georgitodorov/Work/WebPortals commit -m "review-format: richer spec table, per-casino FAQ, providers block (Betano reference)

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

### Task 2: NV brand + OG assets

**Files:**
- Create: `WebPortals/VsichkiKazina/assets/img/brands/nv-casino.png` (or `.webp`/`.svg` fallback)
- Create: `WebPortals/VsichkiKazina/assets/img/og/nv-casino.webp` (1200×630)

**Interfaces:**
- Produces: logo path used by Task 3 hero (`width=160 height=88` display slot) and OG image path for Task 3 `<head>`.

- [ ] **Step 1: Fetch NV Casino's public logo** (their site's press/brand asset or site header image; nominative fair use in a review). Convert/resize so it fits the 160×88 hero slot on white/light background.
- [ ] **Step 2: If no usable logo can be fetched**, author a simple typographic SVG brand mark ("NV Casino", dark text) at `assets/img/brands/nv-casino.svg` — never fabricate their actual mark.
- [ ] **Step 3: Generate OG image** — reuse `_publisher/og_image.py` (`generate_og_image(title, slug, site_root, category_key)`) with title „NV Casino — ревю и лицензна проверка", slug `nv-casino`; requires `GEMINI_API_KEY` in env. Fallback if unavailable: Pillow-only render matching existing OG style (branded background colour `#FAF8F3`, Cyrillic title, „Всички Казина" brand line).
- [ ] **Step 4: Verify** file sizes (<100 KB preferred for logo, OG ≤ ~200 KB), dimensions 1200×630 for OG:

```bash
python3 -c "from PIL import Image; i=Image.open('/Users/georgitodorov/Work/WebPortals/VsichkiKazina/assets/img/og/nv-casino.webp'); print(i.size)"
```

Expected: `(1200, 630)`.
- [ ] **Step 5: Commit (no push)** — `git add` both assets, message `assets: NV Casino brand + OG image`.

### Task 3: NV Casino review page

**Files:**
- Create: `WebPortals/VsichkiKazina/casino/nv-casino/index.html`
- Modify: `WebPortals/VsichkiKazina/sitemap.xml` (add URL)
- Modify: `WebPortals/VsichkiKazina/zakonno-li-e/index.html` (one inbound link)

**Interfaces:**
- Consumes: Task 1 block shapes + Task 2 asset paths.
- Produces: live URL `/casino/nv-casino/` that Task 4/5 articles link to.

- [ ] **Step 1: Verify NV facts first-hand.** WebFetch NV Casino's public T&C/bonus/payments pages and the slotcatalog page; confirm or correct every Global-Constraints fact. Check the НАП blocked-sites register for nvcasino domains (`https://nra.bg` register pages). If the register is unreachable, phrase legality from the statute (unlicensed = не може законно да предлага хазарт на български играчи) without claiming register-row specifics, and note „flagged for human verification" in the commit body.
- [ ] **Step 2: Build the page** by copying `casino/betano/index.html` chrome (head, header, nav, footer, scripts) and replacing content per the warning variant:
  - `<title>NV Casino — ревю 2026: законно ли е в България?</title>`; meta description states no-НАП-licence + our recommendation; canonical `https://vsichkikazina.bg/casino/nv-casino/`; OG/twitter images → `/assets/img/og/nv-casino.webp`.
  - Hero (`section.hero .verdict`): NV logo; H1 = title; **no** `verdict__bonus` for NV — instead a warning line; red badge replaces НАП badge; dial shows 5.2:

```html
<p class="verdict__bonus">Без лиценз от НАП — не препоръчваме регистрация</p>
<a class="btn btn--cta" href="/go/betano/?src=nv-verdict" rel="nofollow sponsored noopener" target="_blank">Играй в Betano (лицензиран)</a>
<p class="compliance">
<span class="badge badge--age">18+</span>
<span class="badge badge--warn">Без лиценз от НАП — лиценз само от Кюрасао</span>
<span class="compliance__note">Хазартът може да пристрасти. Играйте отговорно.</span>
</p>
...
<span class="rating-dial rating-dial--lg" data-dial="" style="--score-final: 52">5.2</span>
```

  (Check `assets/css/style.css` for an existing warn/negative badge class; if none, add `.badge--warn` — red-toned, same shape as `.badge--nap` — in a small `<style>`-free way: append the rule to `style.css` and bump its `?v=` query in this page only if the site convention requires; otherwise reuse an existing red-ish class.)
  - Score bars in Betano order with values 0 / 55 / 85 / 75 / 60 / 70.
  - Spec table (new format from Task 1) — rows: Лиценз от НАП → **„Не — работи с лиценз от Кюрасао (8048/JAZ), невалиден за България"**; Лицензна юрисдикция → Кюрасао; Оператор → Kaurum Limited; Основано → 2024 г.; Казино бонус → „до €2000 + 225 FS (пакет от 3 депозита)"; Превъртане → **x40 (бонус), x30 (FS)**; Казино игри → 2 400+; Доставчици → 65+; Мин. депозит → €10; Мин. теглене → **€45**; Методи на плащане → plain text list (Visa, Mastercard, Skrill, Neteller, банков превод, MiFinity, крипто BTC/ETH/LTC/USDT) — **no** `/depoziti-i-teglenia/` anchor links for methods that page doesn't cover; Валути; Поддръжка (24/7 чат/имейл, вкл. български).
  - Prose sections (each funnels honestly, no scare-mongering, numbers verbatim from verified facts): „Какво е NV Casino и защо се търси толкова" · „Лицензът: какво означава Кюрасао вместо НАП" (no ЗХ protection, no НАП recourse, NRA blocking as verified in Step 1) · „Бонусът: до €2000 + 225 FS — но при x40" (worked € example: превъртане на €100 бонус = €4 000 залози; vs Betano x25) · „Игри и доставчици" (+ providers block: Pragmatic Play, Hacksaw Gaming, Yggdrasil, NoLimit City, Spribe — re-verify) · „Плащания: крипто, но €45 минимално теглене" · „Поддръжка" · closing „**По-добрата алтернатива: Betano**" with comparison sentence + CTA `?src=nv-content`.
  - Pros/cons block: pros (широк каталог 65+ доставчика; крипто плащания; 24/7 чат вкл. на български) / cons (без лиценз от НАП — без защита за БГ играчи; x40 превъртане; €45 минимално теглене).
  - „Сравни с" cards: Betano (9.4) + Mr Bit (8.8) copied from Betano page pattern, `?src=nv-alternatives`.
  - FAQ (5 items + matching FAQPage JSON-LD), exact questions: „Има ли NV Casino лиценз от НАП?" · „Законно ли е да играя в NV Casino от България?" · „Как се теглят пари от NV Casino?" · „Какъв е бонусът на NV Casino и какви са условията?" · „Коя е по-добра алтернатива на NV Casino?" — answers 2–4 sentences each, grounded ONLY in Step-1 verified facts, last one recommending Betano.
  - JSON-LD: Review (ratingValue 5.2, negativeNotes = the cons, positiveNotes = the pros), WebPage, BreadcrumbList, FAQPage. **No Organization sameAs to NV.**
  - Sticky CTA + alt-modal: reuse Betano's, labelled for Betano (`?src=nv-sticky`, `?src=nv-modal`).
- [ ] **Step 3: Validate** — same JSON-LD/FAQ python check as Task 1 Step 6 against the new file; additionally:

```bash
grep -c 'nvcasino\|nv-casino\.' /Users/georgitodorov/Work/WebPortals/VsichkiKazina/casino/nv-casino/index.html
```

Expected: `0` outbound NV links (asset paths `nv-casino.png/webp` are fine — the grep pattern above excludes them; adjust to check `href` values only: `grep -o 'href="[^"]*"' … | grep -i nv` → only internal/asset hits).
- [ ] **Step 4: Sitemap upsert** — add `<url><loc>https://vsichkikazina.bg/casino/nv-casino/</loc>…</url>` matching existing casino entries' shape (lastmod today).
- [ ] **Step 5: Inbound link** — in `zakonno-li-e/index.html`, at the natural spot about unlicensed sites, add one sentence linking `/casino/nv-casino/` as a worked example.
- [ ] **Step 6: Commit (no push)** — message `casino: NV Casino warning review (no NAP licence, Betano funnel)`, body lists verified-fact sources + any human-verification flags.

### Task 4: Rollout to remaining 14 casino pages (parallel subagents)

**Files:**
- Modify: `WebPortals/VsichkiKazina/casino/{8888,admiralbet,alphawin,bet365,elitbet,everbet,inbet,livescorebet,magicbet,mrbit,palmsbet,sesame,slotino,winbet}/index.html`

**Interfaces:**
- Consumes: Task 1 block shapes + `review-format.md`.

- [ ] **Step 1: Dispatch one subagent per page** (parallel, batches of 4–5). Prompt template per agent:

```
Upgrade the casino review page <ABS_PATH>/index.html to the new review format.
Reference implementation: /Users/georgitodorov/Work/WebPortals/VsichkiKazina/casino/betano/index.html
Format doc: /Users/georgitodorov/Work/WebPortals/VsichkiKazina/_publisher/review-format.md
Do exactly three upgrades, nothing else:
1. Spec table: add rows Лицензна юрисдикция / На БГ пазара от / Валути / Поддръжка
   after the Оператор row. Values ONLY from (a) facts already stated in this page's prose,
   (b) the operator's own public site (WebFetch). OMIT any row you cannot verify.
2. Replace the 5 generic FAQ <details> items with 5 casino-specific Q&As grounded in THIS
   page's facts (licence №, wagering, min deposit, withdrawal times, standout feature),
   AND regenerate the FAQPage JSON-LD in <head> to match the new Q&As verbatim.
3. Add a "Топ доставчици и игри в <Casino>" h3 + paragraph inside the games prose section,
   naming only providers/titles verifiable from the page or the operator's public lobby.
   If unverifiable, SKIP the block and say so in your report.
Hard rules: never invent numbers/facts; keep every existing number, link, badge, CTA,
JSON-LD block untouched except the FAQPage one; Bulgarian copy; brand written "Всички Казина".
Validate before finishing: python3 JSON-LD parse of every <script type="application/ld+json">
block + exactly 5 <details class="faq__item">.
Return: list of rows added, rows omitted (+why), FAQ questions used, providers block
included yes/no, validation output.
```

- [ ] **Step 2: Central review** — for each page `git diff` review: FAQ JSON-LD ↔ visible FAQ sync, no touched numbers elsewhere, no invented facts (spot-check 2–3 claims per page against sources named in the agent report), JSON-LD validation rerun centrally across all 14 files (same python loop, glob `casino/*/index.html`).
- [ ] **Step 3: Fix or re-dispatch** any page that fails review.
- [ ] **Step 4: Commit (no push)** — one commit: `review-format: roll out richer spec table + per-casino FAQ + providers block to all casino pages`.

### Task 5: Article 1 — „NV Casino — законно ли е в България?" (AIContent pipeline)

**Files:**
- Create: `AIContent/VsichkiKazina/articles/2026-09-13-nv-casino-zakonno-li-e/*` (on branch `content/2026-09-13-nv-casino-zakonno-li-e`)
- Modify (main): `AIContent/VsichkiKazina/content-queue.md`, `VsichkiKazina/topic-backlog.md`

**Interfaces:**
- Consumes: live-URL-to-be `/casino/nv-casino/` (Task 3) for internal links; `/go/betano/` funnel; keyword data from Ahrefs screenshot (nv casino 408K/KD31 global, nvcasino 210K/KD26, nv cazino 18K/KD19, nv casino online 44K/KD33 — BG volumes to be pulled if `AHREFS_API_KEY` available, else recorded `checked=web`).
- Produces: PR #N; queue row `drafted`.

- [ ] **Step 1: Board rows (main).** Add `topic-backlog.md` rows (priority 3 and 4, type `review`… actually type `guide`/`news` is wrong — use `review` for legality piece? Use `guide`: the piece is an educational legality explainer, not an operator review page) — concretely: priority 3 | guide | „NV Casino — законно ли е в България" | nv casino, нв казино, nv casino законно | status `in-progress session` note „written in-session 13.09". Add matching `content-queue.md` row: fresh id, `status: in-progress`, `type: guide`, folder `2026-09-13-nv-casino-zakonno-li-e`, source `backlog`. Commit board to `main` (no article content).
- [ ] **Step 2: Branch + brief.** `git checkout -b content/2026-09-13-nv-casino-zakonno-li-e`. Assemble `00-brief.md` from `pipeline/templates/00-brief-template-vsichkikazina.md`: sources = НАП register/statute pages, NV public T&C, our new review page facts (Task 3 Step 1 research is reusable), slotcatalog. Angle: „търсиш NV Casino → ето правния статус + какво рискуваш + лицензираната алтернатива". Primary keyword `nv casino` (BG SERP), secondary „нв казино", „nv casino законно ли е". Internal links: `/casino/nv-casino/`, `/zakonno-li-e/`, `/otgovorna-igra/`; operator recommendation Betano → affiliate rule (Step 4).
- [ ] **Step 3: Run pipeline stages 1 → 1.5 → 2 → 3 → 4 → 5 → 5b** as FRESH-CONTEXT subagents per `automation/daily-run.md` §4, each loading only its `pipeline/agents/*.md` + `pipeline/prompts/step-*.md` inputs (brand gate = `brand-gate-vsichkikazina.md`, author = `markets/bg/author.md`). DIFF ALL NUMBERS between stages; changed number → halt, fix at failing stage, re-run forward.
- [ ] **Step 4: Affiliate link.** Betano's first prominent mention links its `affiliate_url` from `VsichkiKazina/affiliate-links.md` if a row exists with `status: active`; the local registry table is EMPTY → per registry rule insert `[LINK NEEDED: Betano]`… **unless** the registry rule's known-good site link applies: the site's own `/go/betano/` redirect is the canonical affiliate URL (per registry header „reuse the site's own /go/<brand> URLs"). Add the missing registry row first (on `main`, board commit): `| Betano | https://vsichkikazina.bg/go/betano/ | welcome bonus | active | /casino/betano/ | 2026-09-13 |`, then link normally. NEVER a bare betano.bg link.
- [ ] **Step 5: Step-7 Gemini check loop** — `python3 scripts/gemini_check.py <article>/05b-final-draft.md`; PASS at human-likeness ≥80; ≤2 humaniser passes via `step-7b-apply-gemini-recs.md`; keep-best mandatory; commit trail per daily-run (initial draft → check → humaniser pass → …, separate commits). If `GEMINI_API_KEY` unset locally: check `env | grep -i gemini`; if truly absent log `external check: skipped (Gemini unavailable)` and continue.
- [ ] **Step 6: Step-8 images** — 1 SVG infographic (e.g. „Лицензиран vs нелицензиран оператор: какво получаваш" checklist, or the x40 wagering math — numbers verbatim from 05b) + optional Gemini concept hero (textless metaphor, e.g. паспорт/печат metaphor for licensing); review via `gemini_image_review.py`, PASS ≥80, ≤2 passes, keep-best, integrity-fail → drop; commit trail per daily-run.
- [ ] **Step 7: `06-verification.md` + `log.md`** — surviving flags, time-sensitive claims with source URLs, one recalculated figure with working (the x40 → €4 000 example), Gemini verdicts, image scores.
- [ ] **Step 8: PR.** Push branch; `gh pr create` — title = the query, body per daily-run §7 (type, gate score, humanisation verdict, flags, images+score, link to 06-verification). Update queue row on `main`: `status: drafted`, `drafted_date`, `pr: #<n>`, `gemini: <result>`; backlog row → `written`.

### Task 6: Article 2 — „NV Casino бонус: какво реално означава 100% до €2000 при x40" (AIContent pipeline)

**Files:**
- Create: `AIContent/VsichkiKazina/articles/2026-09-13-nv-casino-bonus-usloviya/*` (branch `content/2026-09-13-nv-casino-bonus-usloviya`)
- Modify (main): same board files.

**Interfaces:**
- Consumes: same verified NV bonus facts (x40/x30, €2000+225FS, €10/€45 limits); Betano x25 comparison; affiliate registry row from Task 5 Step 4.
- Produces: PR #M; queue row `drafted`.

- [ ] **Step 1–8: identical procedure to Task 5** with: category `bonuses-vip`; primary keyword „nv casino бонус" (+ „nv casino bonus", fallback `checked=web`); brief angle = bonus-hunter lands here → worked € math of x40 (депозит €100 + бонус €100 → залози €8 000 при deposit+bonus base — VERIFY the wagering base from NV T&C in the brief; if base unclear, present both readings labelled) vs Betano x25; infographic = the wagering comparison SVG with the exact numbers from 05b; anti-cannibalization note: links (not duplicates) to the existing wagering guide `2026-09-07-kak-raboti-razigravaneto` topic and the NV review page.

### Task 7: Deploy + verify everything

**Files:**
- Modify: `AIContent` main board (`content-queue.md` final states, `docs/` dashboard), `run-status.json` untouched (not a scheduled run).

- [ ] **Step 1: Final WebPortals review** — `git -C /Users/georgitodorov/Work/WebPortals log --oneline main..` sanity, full-glob JSON-LD validation across `casino/*/index.html`, `grep` NV pages for forbidden outbound NV hrefs.
- [ ] **Step 2: Push WebPortals main** (this deploys via FTP Action):

```bash
git -C /Users/georgitodorov/Work/WebPortals push origin main
gh run watch --repo ProfitXtraV2/WebPortals $(gh run list --repo ProfitXtraV2/WebPortals --workflow ftp-deploy.yml -L1 --json databaseId -q '.[0].databaseId')
```

Expected: workflow success.
- [ ] **Step 3: Live spot-checks** — WebFetch `https://vsichkikazina.bg/casino/nv-casino/` (200, warning badge present, CTA hrefs `/go/betano/`), one upgraded page (e.g. `/casino/winbet/` FAQ changed), sitemap contains the new URL.
- [ ] **Step 4: AIContent dashboard refresh** — `python3 scripts/build_dashboard.py`, commit board + docs to `main`, push.
- [ ] **Step 5: Report** — summarize live URLs, PR numbers, omissions/flags for human verification (esp. NRA register if it was unreachable), and remind: merging the two PRs approves them into the publisher drip (1/day).

---

## Self-review notes

- Spec coverage: §1 review page → Task 2+3; §2 articles → Tasks 5–6; §3 template+rollout → Tasks 1+4; order-of-work + verify → Task 7. Covered.
- The `.badge--warn` CSS may not exist — Task 3 Step 2 includes the check-and-add instruction.
- Affiliate registry empty-table contradiction resolved explicitly (Task 5 Step 4: add the `/go/betano/` row per the registry's own header guidance).
- Blog-article publish depends on the review page being live first — guaranteed by Task ordering (WebPortals push in Task 7 Step 2 happens before PRs merge, since merging is the human's step).
