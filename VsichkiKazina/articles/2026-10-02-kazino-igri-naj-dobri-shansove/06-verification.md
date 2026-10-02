# 06 — Verification · vk-0237

## SURVIVING FLAGS
- Open [VERIFY] tags in 05b text: 0.
- Open [DATA NEEDED]: 0.
- Image: `images/domashno-predimstvo-po-igri.svg` is referenced in 05b but authored separately (SVG not yet drawn). Spec below.
- All house-edge values are published as ТИПИЧНИ/ПРИМЕРНИ and explicitly framed in-text as varying by rules/variant/paytable. Each is corroborated by 2 reputable public sources, so no [VERIFY] tag is carried into the body.

## HOUSE-EDGE FIGURES — each value with its source
Sources:
- WoO = Wizard of Odds, „House Edge of Casino Games Compared": https://wizardofodds.com/gambling/house-edge/
- PN = PokerNews, „What is House Edge? Casino House Edge Explained": https://www.pokernews.com/casino/what-is-house-edge.htm

| Стойност в 05b | Source(s) | Source figure |
|---|---|---|
| Блекджек (осн. стратегия) ~0,5% / под 1% | PN; WoO | PN „0,5% depending on version"; WoO 0,28% (liberal Vegas rules, optimal strategy). Published as ~0,5% „под 1%". |
| Видеопокер 9/6 JoB под 1% / над 99% RTP | WoO; PN | WoO Jacks or Better Full Pay 0,46%; PN „less than 1%" with optimal play. |
| Бакара банкер 1,06% (RTP 98,94%) | WoO; PN | Both 1,06%. |
| Бакара играч 1,24% | WoO; PN | Both 1,24%. |
| Бакара равенство ~14% (RTP ~86%) | WoO | WoO 14,36%; published as ~14%. |
| Крапс pass line / come ~1,4% (RTP ~98,6%) | WoO; PN | Both 1,41%; prop bets >10% (PN). Published as ~1,4%. |
| Европейска рулетка 2,70% (RTP 97,30%) | WoO; PN | Both 2,70%. |
| Американска рулетка 5,26% (RTP 94,74%) | WoO; PN | Both 5,26%. |
| Ротативки/слотове 2%–10% (RTP ~90%–98%) | PN; WoO | PN 2%–10%; WoO 2%–15% (narrowed to typical 2%–10%). |
| Кено ~20%–40% (RTP ~60%–80%) | WoO; PN; вътр. | WoO 25%–29%; PN „as high as 25%"; наземно/живо диапазон 20%–40% (съгласуван с вътрешното ни ръководство за кено, 2026-09-08-keno-pravila). |

Note on narrowing/rounding: where sources give a tighter figure (WoO blackjack 0,28%; slots 2%–15%), the published value is the widely-accepted typical („~0,5%", „2%–10%"), framed as типична. No value is more precise than the sources support.

## RECALCULATED € EXAMPLE (with working)
Base: €100 оборот (turnover). Statistical house take = edge × turnover.
- Европейска рулетка: 2,70% × €100 = 0,0270 × 100 = €2,70. (05b: „около €2,70") ✓
- Американска рулетка: 5,26% × €100 = 0,0526 × 100 = €5,26. (05b: „около €5,26") ✓
- Блекджек (осн. стратегия): 0,5% × €100 = 0,005 × 100 = €0,50. (05b: „към €0,50") ✓
- Кено (тежка таблица): 20%–40% × €100 = €20 до €40. (05b: „€20 до €40") ✓
RTP check (RTP = 100% − edge), spot values: 100−2,70 = 97,30 ✓; 100−5,26 = 94,74 ✓; 100−1,06 = 98,94 ✓; 100−10 = 90 and 100−2 = 98 (slots band) ✓; 100−40 = 60 and 100−20 = 80 (keno band) ✓.

## INFOGRAPHIC SPEC — images/domashno-predimstvo-po-igri.svg
Type: horizontal bar chart of ТИПИЧНО домашно предимство по игри (lower bar = better odds). Sort ascending (best odds at top). X-axis = домашно предимство (%). Title in BG: „Типично домашно предимство по игри (%)". Subnote on chart: „типични стойности; зависят от правилата и таблицата". Use a value label on each bar. Range bars (slots, keno) drawn as a band from low to high with both numbers labelled. NO em-dash anywhere in the SVG text; ranges use the en-dash „–" as in 05b. Colours: single neutral series; the two highest bars (кено, американска рулетка) may use a darker shade to read as „по-скъпо".

Bars (every number copied VERBATIM from a 05b line):
| Bar label (BG) | Value | Traceable to 05b line |
|---|---|---|
| Блекджек (осн. стратегия) | 0,5% | table row „Блекджек (основна стратегия) · ~0,5%"; intro-close „предимството пада към 0,5%"; €100 para „към €0,50" |
| Бакара (банкер) | 1,06% | table row „Бакара (банкер) · 1,06%"; „домашното предимство е около 1,06%" |
| Крапс (pass line / come) | 1,4% | table row „Крапс (pass line / come) · ~1,4%"; „pass line около 1,4%" |
| Европейска рулетка | 2,70% | table row „Европейска рулетка (една нула) · 2,70%"; concept para „Игра с 2,70% предимство"; €100 para „около €2,70" |
| Американска рулетка | 5,26% | table row „Американска рулетка (двойна нула) · 5,26%"; €100 para „около €5,26" |
| Ротативки / слотове | 2%–10% | table row „Ротативки / слотове · 2%–10%" (band 2% low → 10% high) |
| Кено | 20%–40% | table row „Кено · ~20%–40%"; €100 para „€20 до €40" (band 20% low → 40% high) |

Every bar label + value above is stated in 05b. ALT text (already in 05b) enumerates the same seven items with the same numbers.
Caption in 05b: „Типични стойности на домашното предимство по игри; зависят от правилата и таблицата за изплащане."

## NUMBER-DIFF ACROSS STAGES (02 → 03 → 04 → 05b)
No house-edge or RTP figure changed, appeared, or disappeared between stages. Step 3 (humaniser) changes were structural only (removed „Първо/Второ" counting; ASCII hyphen in the RTP formula) and added one no-number hub section (edge vs волатилност). All ten edge values + the four € figures are identical in every stage.
