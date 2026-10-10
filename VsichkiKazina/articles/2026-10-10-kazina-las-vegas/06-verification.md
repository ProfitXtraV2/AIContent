# 06 — Verification checklist (Step 6 — HUMAN-OWNED) — vk-0276

Article: `05b-final-draft.md` — „Казино в Лас Вегас: колко задържа къщата и какво трябва да знае българският играч"
Type: guide (editorial voice, byline Георги Тодоров) · Brand Gate: PASS WITH FIXES 85 → 92/100
Prepared 10.10.2026. **FLAGS STAY IN THE TEXT** — only the human resolves them against primary sources.

## Surviving flags (5 × [VERIFY], 0 × [DATA NEEDED], 0 × [CONFLICT])
| # | Flag (verbatim key) | Where | Primary source to check | What the source shows now |
|---|---|---|---|---|
| 1 | база на win % за кено в отчета на NGCB | „Защо 11.91% …" | NGCB Gaming Revenue Report Aug 2026, intro p.1 + p.11: https://www.gaming.nv.gov/siteassets/content/about/gaming-revenue/monthly-revenue-report---august-2026.pdf | Keno is listed under „Table, Counter and Card Games" (12 mo. 30.47%); the intro says the „Win Percent for games" is adjusted for credit play (i.e. drop-based like tables). Likely drop-based → confirm and either keep the caveat or say so plainly. |
| 2 | колко разпространени са масите 6:5 на Стрипа | „Блекджек, който плаща 6:5" | https://www.casino.org/vitalvegas/question-answered-can-casinos-pay-6-5-blackjacks/ | Source confirms $12 vs $15 and +1.39%; prevalence on the Strip is not quantified in the fetched source → text already says „на част от масите"; remove flag only if a source is accepted. |
| 3 | 30% удържане и освобождаванията … IRS Pub. 515 (2026) | „Данък върху печалба в САЩ…" | https://www.irs.gov/publications/p515 → „Gambling winnings (income code 28)" + „Tax treaties" | Read 10.10.2026: 30% chapter-3 withholding for NRAs unless treaty-exempt; „No tax is imposed on nonbusiness gambling income a nonresident alien wins playing blackjack, baccarat, craps, roulette, or big-6 wheel"; treaty list includes **Bulgaria**; W-8BEN with U.S. or foreign TIN required for treaty benefit. Text matches. |
| 4 | начин за възстановяване на удържания 30% данък | same section | IRS (Form 1040-NR / ITIN procedure) — not fetched | Not sourced; keep flag or cut the clause. |
| 5 | данъчно третиране в БГ на печалба от казино в САЩ | same section | ЗДДФЛ (lex.bg) / НАП | Not sourced. Note: our /blog/danaci-pechalbi-onlajn-kazino/ covers only BG-licensed online winnings (article says so). |

## Time-sensitive / to-confirm claims (no flag, but check at publish)
- NGCB 12-month figures (01.09.2025–31.08.2026, Strip): slots 7.75% (1¢ 10.53%, 25¢ 11.44%, $1 7.17%, $25 8.12%, $100 5.67%, multi 7.62%); tables: Twenty One 11.91%, Craps 16.90%, Roulette 17.92%, Baccarat 15.80%, 3-Card Poker 31.11%, UTH 22.48%, Keno 30.47%; 59 licensees, avg 35 133 slots; total win $8,985,031k / slots $5,035,369k / games $3,949,662k — **verified against the PDF page 11 on 10.10.2026**. A newer monthly report (September 2026) may be out by publish date → refresh or keep the dated wording.
- NRS 463.350 (under 21: no play/wager, no loitering; misdemeanor): https://nevada.public.law/statutes/nrs_463.350 (official text: https://www.leg.state.nv.us/nrs/nrs-463.html).
- NJ: 21+ and physical location in NJ for internet gaming — NJ DGE responsible-gaming reports (https://www.nj.gov/oag/ge/).
- Roulette edges 2.70% / 5.26% / 7.89% (0-00-1-2-3) / 7.69%: https://wizardofodds.com/games/roulette/basics/ (verified 10.10.2026).
- Starburst RTP 96.08% — own page https://vsichkikazina.bg/blog/starburst/ („Официалният RTP на Starburst е 96.08%").
- ЗХ: чл. 3, чл. 41 ал. 1, чл. 17 ал. 6 (24 ч., от 01.08.2026), глоба 500–2000 лв. (чл. 9 ал. 14 + чл. 97а ал. 2), регистър на уязвимите лица чл. 10г (мин. 12 месеца), НАП 0700 18 700, 5% бюджет — from `source-packs/nap-gambling-law-and-rg-2026-10-10.md`. **Fine is in лв.** (as sourced) — check whether the current ЗХ text states euro amounts after the euro changeover.
- Footer: Brand Gate left the 1-Aug-2026 affiliate-licensing disclosure to the [BRAND BOILERPLATE] slot (article has no commercial links). Sibling drafts carry it inline → human decides; verbatim text is in `pipeline/agents/brand-gate-vsichkikazina.md`.

## Recalculation (working shown)
- Penny slots return per $100: 100 − 10.53 = **$89.47** ✓ (table). All slots: 100 − 7.75 = **$92.25** ✓.
- Strip average vs Starburst: Starburst keeps 100 − 96.08 = 3.92 per 100; 7.75 / 3.92 = **1.977… ≈ 1.98** ✓ („почти двойно").
- Roulette: 1/37 = 2.7027% → **2.70%**; 1/19 = 5.263% → **5.26%**; 1/13 = 7.692% → **7.69%** ✓.
- 6:5 on $10: 10 × 6/5 = **$12**; 3:2: 10 × 3/2 = **$15**; difference $3 ✓.

## External checks
- Step 7 Gemini (text): check 1 „Likely human-written … 65%" (hl 65) → humaniser pass 1 → check 2 „Highly likely human-written … 90%" (hl 90) **PASS**. Passes applied: 1. Keep-best = pass 1 (90). gemini = `human 90`.
- Step 8 images: **images: 3 (hero 100, infographic slots 100, infographic table rules 100)** — review 1 score 95 PASS (one fix: removed the „Wizard of Odds" credit not named in the text), review 2 score 100 PASS. No integrity failures.

## Never
Flags not resolved by the pipeline. Not posted, not merged, not deployed.
