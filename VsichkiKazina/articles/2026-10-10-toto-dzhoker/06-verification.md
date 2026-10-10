# 06 — Verification — „Тото Джокер: как работи и какъв е реалният шанс за печалба"

Type: guide (neutral lottery explainer, vk-0266) · Byline: Георги Тодоров (editorial voice)
Scope: no operator promotion, NO affiliate links, no number/position picks. Flags STAY in the text
for the human (Step 6). ~1 470 words body (H1 → signature), 0 em-dashes.

## SURVIVING FLAGS (4 — publish-blocking until the human resolves them)
1. **[VERIFY] Цена €0,20** за комбинация от 3 позиции и 3 цифри (lede).
   · Source: https://info.toto.bg/toto1-i-toto2/toto-2-toto-dzhoker — fetched once 2026-10-10 via
     WebFetch (rules page; „Една комбинация от 3 позиции и 3 цифри струва 0.20 EUR"). Subsequent
     fetches hit the Radware CAPTCHA → human to confirm in a BG browser. Time-sensitive (prices change).
2. **[VERIFY] 1999 г., 63-ти тираж** — introduction of Тото Джокер.
   · Source: https://bg.wikipedia.org/wiki/Български_спортен_тотализатор („63 тираж 1999 г.: Въвежда
     се играта „Тото джокер"" — „игра за познаване на позицията и съответната цифра от фабричния
     номер на фиша"). Single secondary source.
3. **[VERIFY] Draw method / equal likelihood of digits 0–9** (odds section). The rules page confirms
   positions 1–9, three position–digit pairs, two winning groups, but does NOT publish how the
   positions/digits are drawn. All odds are computed under the stated assumption (3 different
   positions out of 1–9, a digit 0–9 each, every outcome equally likely). If BСТ's rules say
   otherwise (e.g. digits drawn from the actual ticket numbers sold), the odds must be recomputed.
   · Check: toto.bg „Вероятности" page (https://www.toto.bg/veroyatnosti — did not render) or the
     official game rules PDF.
4. **[DATA NEEDED] Типични суми на печалбите за I и II група и срок за получаване на печалба**
   (inserted by SEO stage; no source in hand). Human may fill from toto.bg results/rules or delete
   the line (the article is complete without it).

## OTHER CLAIMS TO SPOT-CHECK (sourced, not flagged)
- Can't be played alone; only on ТОТО 1 / ТОТО 2 slips except „ТОТО 2 – Рожден ден"; ≥3 positions
  from 1–9; „АВТОМАТИЧНО" / „ОТКАЗ"; квитанция = proof; I група 3 pairs / II група 2 pairs; 50% of
  receipts to prizes, split equally per group; unwon group money → I група next draw.
  · https://info.toto.bg/toto1-i-toto2/toto-2-toto-dzhoker (fetched 2026-10-10)
- Two draws a week (Thursday/Sunday), live on БНТ from 18:45 ч.; online site offline 18:40–19:10 ч.;
  online Joker winnings credited automatically; results board „Печеливши позиции 2, 3, 5 / Печеливши
  числа 3, 9, 8" (тираж 79, 08.10.2026).
  · https://www.toto.bg/ via source pack `VsichkiKazina/source-packs/bst-toto-2026-10-10.md`
- ЗХ: лотарийни игри (тото, лото, бинго, кено) are gambling; чл. 3 licence from изпълнителния
  директор на НАП; state licence only for sport/culture/health/education/social causes; minors
  excluded; НАП lists of licensed/unlicensed sites; illegal_gambling@nra.bg (no anonymous signals);
  5% of net income budget; „стратегиите за добър късмет" не увеличават шансовете; регистър по чл. 10г,
  min 12 months; 0700 18 700.
  · https://nra.bg/wps/portal/nra/gambling , …/Online-hazat , …/responsible.gambling ,
    …/responsible.gambling/Suveti-za-razumno-zalagane via source pack
    `VsichkiKazina/source-packs/nap-gambling-law-and-rg-2026-10-10.md`
  · Minimum age wording (18 г.) in ЗХ is listed as NOT in the pack → article says only
    „Непълнолетни не могат да участват" (pack §7: ЗХ забранява участието на малолетни и непълнолетни).
- Advance-fee scam description: Revolut BG fraud education page
  https://help.revolut.com/bg-BG/help/security-logging-in/how-do-i-protect-myself-from-fraudsters/fraud-education-advance-fee-scam/
- „Солидарност" 0888 99 18 66 (делнични 10:00–17:00): brand-gate canon RG resource.
- Tax: linked to /blog/danaci-pechalbi-onlajn-kazino/ (not explained in-article). Human: confirm the
  linked piece also fits lottery (тото) winnings, or adjust the anchor sentence.
- Affiliate-licensing footer (1 август 2026 г.; ДВ бр. 69 от 31.07.2026 г.): brand-template footer;
  site licence = заявление подадено, очаква издаване (NOT claimed issued).

## FIGURE CHECK (recalculation with working shown; python3 Fractions + full enumeration)
- Ways to pick 3 positions from 9: C(9,3) = 9·8·7 / 3! = 504 / 6 = **84**.
- **I група:** P(your 3 positions drawn) = 1/84; P(3 digits match) = (1/10)³ = 1/1000 →
  1/84 × 1/1000 = **1/84 000**.
- **II група (exactly 2 pairs):**
  (a) all 3 positions drawn, exactly 2 digits match: 1/84 × 3 × (1/10)² × (9/10) = 27/84 000 = 9/28 000;
  (b) exactly 2 of your positions drawn: C(3,2)·C(6,1) = 3 × 6 = 18 of 84 triples; both digits match
      1/100 → 18/84 × 1/100 = 60/28 000.
  Sum = 69/28 000 = 0.0024643 → **≈ 1 на 406** (28 000 / 69 = 405.8). Share of path (b): 60/69 = 86.96% → „около 87%".
- **Any prize:** 1/84 000 + 69/28 000 = 1/84 000 + 207/84 000 = 208/84 000 = **13/5250 ≈ 1 на 404**.
- Full enumeration over all 84 × 10³ outcomes: P0 + P1 + P2 + P3 = 1 (consistency check passed).
- Systems: 4 позиции → C(4,3) = 4 → €0,80; 5 → C(5,3) = 10 → €2,00; 9 → C(9,3) = 84 → €16,80;
  4 positions: 4/84 000 = 1/21 000.
- EV: 50% × €0,20 = **€0,10**. Year: 2 × 52 = 104 тиража × €0,20 = €20,80 → ≈ €10,40 back;
  II група every 405.8 / 104 = 3.9 years (≈ „четири"); I група 84 000 / 104 = 807.7 → „около 808".
- 6/49 jackpot: C(49,6) = 13 983 816; 13 983 816 / 84 000 = 166.47 → „приблизително 166 пъти".

## GEMINI STEP-7 (text, cross-model)
- external check: skipped (Gemini unavailable — cloud backfill pending). `gemini_check.py` →
  `GEMINI_UNAVAILABLE: GEMINI_API_KEY not set`. content-queue `gemini` = `skipped`.
- Internal humanisation: Stage 3 Phase-1 verdict MIXED 46/60 → light rewrite (4 targeted edits).

## IMAGES (Step 8)
- images: 1 (infographic, review skipped — Gemini unavailable). Hand-authored SVG
  `images/toto-dzhoker-shans-za-pechalba-infografika.svg`: odds per group, system costs, €0,10/€0,20
  split, assumption footnote, 18+. Every figure traced programmatically to 05b. Rendered via headless
  Chrome → no overlap/clipping. No AI hero.

## BRAND GATE
- PASS WITH FIXES: input 84/100 (Personality 18 · Tone 14 · E-E-A-T 17 · Trust 9 · Lang&Style 13 · RG 13)
  → **94/100** after fixes (trust slots, footers, RG block). 0 CRITICAL remaining.
- Internal links (4): /zakonno-li-e/, /blog/keno-pravila/, /blog/danaci-pechalbi-onlajn-kazino/,
  /otgovorna-igra/ (+ /kak-ocenyavame/ in the brand boilerplate). All present in live sitemap 2026-10-10.

## HUMAN ACTIONS BEFORE PUBLISH
Resolve 3 [VERIFY] + 1 [DATA NEEDED]; insert the author bio slot; confirm tax-link fit. Do NOT publish
with live flags.
