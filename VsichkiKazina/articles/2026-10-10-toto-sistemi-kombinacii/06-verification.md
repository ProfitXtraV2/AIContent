# 06 — Verification — „Тото системи и комбинации: колко струва система в 6/49 и увеличава ли шанса"

Queue: vk-0270 · Type: guide (lottery math / EV explainer) · Byline: Георги Тодоров (editorial voice)
Scope: guides-only safe. Pure combinatorics + publicly reported ticket prices. NO affiliate links, NO
operator promotion, NO number picks / „winning systems". Flags STAY in the text for the human (Step 6).
toto.bg / info.toto.bg and nra.bg are behind a Radware bot-CAPTCHA (re-confirmed 10.10.2026: info.toto.bg
→ validate.perfdrive.com) — primary BST pages could not be fetched; facts come from the source packs
(BG-browser reads 10.10.2026) and reachable secondary sources below.

## SURVIVING [VERIFY] FLAGS (4 — human must confirm on toto.bg / in a тото пункт before publish)
1. **Current price per combination: 6/49 0,90 €, 6/42 0,80 €, 5/35 0,60 € (редовен тираж).**
   Derivation: euro prices from 01.01.2026 = 0,80 / 0,70 / 0,60 € (totosimulator.com EUR tables; search
   snippet of the toto.bg 6/49 rules: „с 01.01.2026 г. залогът за една комбинация е в размер на 0.80 евро")
   + „стойността на една комбинация … се увеличава с 0,10 евро" in 6/49 and 6/42 from тираж 57 (23.07.2026).
   · https://www.marica.bg/biznes-zona/tototo-vdiga-cenite-i-dvata-djakpota (04.07.2026)
   · https://sportal.bg/news-2026070612365703048 (06.07.2026)
   · https://totosimulator.com/toto-palno-kombinirane-649/ · /toto-palno-kombinirane-642/ · /toto-palno-kombinirane-535/ (undated, EUR, pre-July prices)
   · Context (лв era): https://www.marica.bg/balgariq/obshtestvo/tototo-tiho-vdigna-cenite-s-10-do-20-stotinki (21.11.2025: 1,60 / 1,40 / 1,20 лв)
   · Search snippets of https://info.toto.bg/chesto-zadavani-vaprosi agree (6/49 0.90 EUR; 6/42 0.80 EUR) — page not fetchable.
   · 5/35: no July change reported in either news source → 0,60 € assumed unchanged.
   **IMPACT:** if any price differs, EVERY € figure must be recomputed: both 6/49 tables + infographic,
   lead (189,00 €), meta (6,30–831,60 €), 33× ratio, budget paragraph (831,60 €), and the
   12 585 434 € / 12 585 434,40 € equivalence (= 13 983 816 × price).
2. **6/49 special-draw price 1,00 €** — only from a search snippet of the info.toto.bg FAQ.
3. **Max system size BST accepts on one slip** — calculators go to 14; BST limit unconfirmed.
4. **Does one 5/35 combination take part in BOTH draws (I и II теглене)?** — unconfirmed; the text gives
   odds „за едно теглене" only (5/35 two draws per тираж confirmed by the toto.bg source pack + bgdnes.bg).

Non-blocking (audit only, not in text): SEO noted [DATA NEEDED] on submission channels for a системен фиш
(пункт / онлайн). Template placeholders `[Author bio: Георги Тодоров]` and `[About Всички Казина boilerplate]`
are publisher-expanded slots.

## TIME-SENSITIVE CLAIMS (sources)
- От 01.01.2026 залозите в тотото са само в евро — btvnovinite.bg (https://btvnovinite.bg/bulgaria/i-tototo-s-gaf-za-evroto-na-1-januari-prevalutiraha-dzhakpota-no-zad-sumata-pak-pishe-leva.html) + source pack.
- Тираж 57/2026 = 23.07.2026, +0,10 € in 6/49 and 6/42 — marica.bg 04.07.2026, sportal.bg 06.07.2026.
- Prize groups 6/5/4/3 and example payouts in тираж 76 (5 → 2211,00 €, 4 → 39,20 €, 3 → 4,80 €) —
  https://www.bgdnes.bg/sport/article/23636783 (28.09.2026). Payouts are pari-mutuel (vary per draw) —
  https://bgprognozi.info/toto/6-49/ .
- Two draws a week (четвъртък/неделя), 5/35 = two draws — VsichkiKazina/source-packs/bst-toto-2026-10-10.md (toto.bg, 10.10.2026).
- НАП: budget ≤ 5% of net income; „стратегиите за добър късмет" don't raise chances; регистър на уязвимите лица
  (чл. 10г ЗХ), min 12 months, 0700 18 700 — source-packs/nap-gambling-law-and-rg-2026-10-10.md
  (https://nra.bg/wps/portal/nra/gambling/responsible.gambling and /Suveti-za-razumno-zalagane).
- Солидарност 0888 99 18 66 and the 1-Aug-2026 affiliate-licensing footer — brand-gate template (verbatim).
- Not stated anywhere (deliberately): prize-fund share %, tax rates (linked to /blog/danaci-pechalbi-onlajn-kazino/).

## FIGURE CHECK (recalculated with python3, working shown)
C(49,6) = 49·48·47·46·45·44 / 720 = 10 068 347 520 / 720 = **13 983 816** ✓
Система 10: C(10,6) = C(10,4) = 10·9·8·7 / 24 = **210** combinations; cost 210 × 0,90 € = **189,00 €** ✓;
jackpot odds 13 983 816 / 210 = 66 589,6 → „≈ 1 към 66 590" ✓.
Per-euro equivalence: 66 589,6 draws ÷ 104 draws/year = 640,3 → „около 640 години" ✓;
66 589,6 × 189 € = 13 983 816 × 0,90 € = **12 585 434,40 €** ✓.
Brand Gate independently re-ran all table/odds/multi-tier counts (C(h,j)·C(N−h,6−j)) — 0 errors; the gate
filled the 6/42 система 9 odds: 5 245 786 / 84 = 62 449,8 → „≈ 1 към 62 450" ✓.
Number diffs between text-editing stages (02→03→04→05→05b): no number lost or changed; only additions were
the gate's 62 450, dates 10.10.2026, helpline and footer (all template/verified).

## EXTERNAL CHECK (Step 7, Gemini)
- external check: skipped (Gemini unavailable — cloud backfill pending). `scripts/gemini_check.py` → `GEMINI_UNAVAILABLE: GEMINI_API_KEY not set` (exit 2).
- In-pipeline humanisation: Stage 3 HUMAN-LIKE 49/60 (pass-through). content-queue `gemini` = `skipped`.

## IMAGES (Step 8)
- images: 1 (infographic, review skipped — Gemini unavailable; cloud backfill pending).
  `images/toto-6-ot-49-sistemi-kombinacii-cena-shans-infografika.svg` — 6/49 system size (6…12) × combinations ×
  cost × jackpot odds + per-€ formula. All 30 numeric tokens in the SVG programmatically traced to 05b (100%).
  No logos/faces/glamorised winning; 18+ line present. Bulgarian ALT + caption in 05b.
- Layout: svg_layout_lint.py not found locally (neither the WebPortals publisher path nor AIContent scripts);
  instead rendered to PNG with headless Chrome at 760×600 and inspected: no overlap, no clipping, ≥16 px margins.
- No AI hero (skipped per instructions; data article → infographic preferred).

## BRAND GATE
PASS WITH FIXES — 89/100 before fixes, 96/100 after (Personality 19 · Tone 14 · E-E-A-T 18 · Trust 11 · Lang&Style 13 · RG 14).
Byline Георги Тодоров, brand „Всички Казина", dates 10.10.2026, RG footer + 18+ verbatim, no affiliate links
(explicit disclosure line), internal links all LIVE in sitemap 10.10.2026: /blog/progresivni-dzhakpoti/,
/zakonno-li-e/, /blog/danaci-pechalbi-onlajn-kazino/, /blog/responsible-gambling/, /otgovorna-igra/.

## HUMAN ACTION QUEUE (Step 6)
Confirm the 4 [VERIFY] items on toto.bg (rules pages / FAQ) or in a тото пункт — above all the current
per-combination prices, because every € figure depends on them — then remove the brackets. Do NOT publish
with [VERIFY] tags live.
