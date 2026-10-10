# 06 — Verification report — vk-0269 „Тото Зодиак"

> For the human at Step 6. FLAGS STAY IN THE TEXT of `05b-final-draft.md` until you confirm them
> against primary sources. Autopilot did NOT resolve any flag. Do not publish with live tags.

**Status:** drafted · Brand Gate PASS WITH FIXES **91/100** (85 → 91 after fixes) · 0 em-dashes ·
~1 650 words raw (≈1 350 prose excl. table/flags) · byline Георги Тодоров · brand „Всички Казина" · 18+ + RG present.

## Surviving flags (9) — with where to check

| # | Flag (verbatim) | Where to verify | What we found |
|---|---|---|---|
| 1 | [VERIFY: актуален размер към датата на публикуване] — джакпот 1 500 000,00 евро | https://www.toto.bg/ (results board) | Source pack (BG browser, 10.10.2026): jackpot Зодиак към тираж 79 (08.10.2026) = 1 500 000.00 euro. Time-sensitive; update or keep the „към тираж 79" date. |
| 2 | [VERIFY: съответствие номер ↔ зодиакален знак] | toto.bg rules / paper slip | Results show the sign as a number (тираж 79: зодия 9; тираж 76: Z = 9). No source maps number → sign. Text does not claim a mapping. |
| 3 | [VERIFY: цена на комбинация за Зодиак] | toto.bg game page / any БСТ пункт | Not found in bg.wikipedia or any fetched source. Text states no price. |
| 4 | [CONFLICT: БНТ 18:45 vs Facebook след 19:00] | toto.bg „Информация" block; facebook.com/SportTotoBG | Pack lists Зодиак in BOTH the БНТ (Thu/Sun 18:45) list and the Facebook (after 19:00) list; bg.wikipedia says БНТ 1. Text follows toto.bg Facebook line. |
| 5 | [DATA NEEDED: праг за изплащане в пункт и ред за големи печалби] | toto.bg rules / БСТ | Not sourced. Either fill from БСТ rules or delete the sentence. |
| 6 | [VERIFY: сумите за тираж 76 …] | https://www.lotteryextreme.com/toto2/results(27.09.2026) (secondary aggregator); cross-check on toto.bg archive | Fetched 10.10.2026: 4+Z €3 000.00 (3), 4 €300.00 (15), 3+Z €60.00 (33), 3 €6.00 (410), 2+Z €3.00 (578), 1+Z €1.00 (2 708), 2 €0.50 (5 849), Z €0.60 (4 030); total 13 626 winners, €27 724.50. |
| 7 | [VERIFY: дял на фонда за печалби от постъпленията] | БСТ game rules (Правила за ТОТО 2) | Not found anywhere reachable. Text gives no percentage. |
| 8 | [VERIFY: кои групи са фиксирани …] | БСТ rules | bg.wikipedia „Зодиак (хазартна игра)" says fixed groups 3–8, but lists 10 groups; tirage-76 payouts for 9/10 look fixed. |
| 9 | [VERIFY: 65/35, таванът 15% и правилата за прехвърляне …] | БСТ rules | Source: https://bg.wikipedia.org/wiki/Зодиак_(хазартна_игра) (fetched 10.10.2026) — remainder 65% група 1 / 35% група 2; 15% cap per fixed group; rollover rules as written. |

## Time-sensitive / sourced claims (no flag)
- Format 5 от 50 + 1 от 12; start 17.08.2014 — bg.wikipedia „Зодиак (хазартна игра)" + „Български спортен тотализатор" (хронология).
- Тираж 79 (08.10.2026): 1, 6, 7, 20, 24; зодия 9 — toto.bg via `source-packs/bst-toto-2026-10-10.md`.
- Two draws/week; bet acceptance windows (график от 08.12.2022): odd Sun 19:20 → Thu 18:00, even Thu 19:20 → Sun 18:00; payout release within 1 h after the broadcast; online winnings auto-credited; ePay.bg / карта през БОРИКА — toto.bg via pack.
- ЗХ: лотарийни игри (тото, лото, бинго, кено) = хазарт; чл. 3 лиценз от изп. директор на НАП; държавата — само за спорт/култура/здравеопазване/образование/социално дело; непълнолетни забранени; 5% от нетните доходи; регистър чл. 10г; 0700 18 700 — `source-packs/nap-gambling-law-and-rg-2026-10-10.md` (nra.bg, BG browser).
- Affiliate-licensing footer (1 Aug 2026 regime) — verbatim from the brand gate spec.
- Moment/scratch „Зодиак" (late 1990s) disambiguation — bg.wikipedia „Български спортен тотализатор" chronology (1997–1999 „Тото шанс за всички"; 2000 „Зодиак + 6/45").

## Figure recalculation (working shown, python3-checked)
C(50,5) = 50·49·48·47·46 / 5! = 254 251 200 / 120 = **2 118 760**; × 12 зодии = **25 425 120** → jackpot 1 на 25 425 120.
Per group (k numbers matched): ways = C(5,k)·C(45,5−k), ×1 with sign, ×11 without.
- 5 без зодия: 1·1·11 = 11 → 25 425 120 / 11 = 2 311 374.55 → „2 311 375" ✓
- 4 + зодия: 5·45 = 225 → 113 000.53 → „113 001" ✓ · 4: 2 475 → 10 272.78 → „10 273" ✓
- 3 + зодия: 10·990 = 9 900 → 2 568.19 ✓ · 3: 108 900 → 233.47 ✓
- 2 + зодия: 10·14 190 = 141 900 → 179.18 ✓ · 2: 1 560 900 → 16.29 → „16,3" ✓
- 1 + зодия: 5·148 995 = 744 975 → 34.13 ✓ · само зодия: 1 221 759 → 20.81 → „20,8" ✓
- Any prize: 25 425 120 − (8 194 725 + 13 439 349) = 3 791 046 → 14.91% ≈ 1 на 6.71 ✓
- vs 6/49: 25 425 120 / 13 983 816 = 1.818 → „около 1,8 пъти" ✓
- ~244 000 years: 25 425 120 / (2 × ~52 draws/yr) ≈ 243 600–244 500 ✓ (order of magnitude illustration)
- Tirage 76: winners paid €0,50–€3 = 578 + 2 708 + 5 849 + 4 030 = 13 165 → „над 13 000" ✓

## External checks
- **Step 7 Gemini text check:** external check: skipped (Gemini unavailable — cloud backfill pending). `gemini_check.py` → `GEMINI_UNAVAILABLE: GEMINI_API_KEY not set`. Passes applied: 0.
- **Step 8 images:** images: 1 (SVG infographic, review skipped — Gemini unavailable, cloud backfill pending). `images/toto-zodiak-shans-pechalba-grupi-infografika.svg` — 10 prize groups + odds, every figure verbatim from 05b; rendered to PNG locally (Quick Look) and inspected: no overlap/clipping. `svg_layout_lint.py` not found locally → manual render check only.

## Internal links (all present in live sitemap 10.10.2026)
/zakonno-li-e/ · /blog/danaci-pechalbi-onlajn-kazino/ · /blog/keno-pravila/ · /otgovorna-igra/. No affiliate links. No sibling lottery drafts linked (not live).

## Human notes
- Footer has two near-duplicate 18+ lines (RG untouchable for the pipeline) — consider merging at publish.
- Optional: add Солидарност helpline if the brand template uses it (gate did not add, no-new-numbers rule).
- `[СЛОТ: За автора …]` / `[СЛОТ: За Всички Казина …]` are publisher slots.
