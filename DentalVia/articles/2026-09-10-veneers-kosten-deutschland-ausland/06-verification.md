# 06 — Verification checklist (for the human, Step 6) · Veneers-Kosten DE vs. Ausland

Reprocessed under the tiered verification policy (`DentalVia/pipeline/reference/verification-policy.md`,
approved 2026-09-11) by the verify-assist pass on 2026-09-11. Tier-A example-framed price markers were
removed in 05b; Tier-B claims were checked against a primary source; Tier-C flags stay in the text for the
human. Nothing here was resolved by reasoning or a secondary source, and no claim or number was altered.

STATUS: still NOT publishable until the REMAINING flags below are confirmed by the human. Merge = approve
stays the human act.

## Count summary
**Was 30 flags (28 [VERIFY] + 1 [CONFLICT] + 1 [DATA NEEDED]) → resolved 22 (Tier A: 22, Tier B: 0),
remaining 8 for human.**

## RESOLVED

### Tier A — example-framed price figures (marker removed; guard is the framing itself, no source needed)
All figures below are framed „ab ca. … €" / „Beispiel(paket/werte)" with „Stand 09/2026" (table header or
inline). Per policy Tier A these carry their guard in the framing; the inline [VERIFY] marker was removed.
The numbers themselves were NOT changed.

| Claim (as written) | Framing present |
|---|---|
| 6 Keramik-Veneers DE ab ca. 3.000–6.000 € (intro) | „ab ca." + „Stand 09/2026" |
| Komposit-Veneer DE ab ca. 250–500 € | „ab ca." + table „Stand 09/2026" |
| Keramik-Veneer DE ab ca. 700–1.500 € | „ab ca." + table „Stand 09/2026" |
| Standard-Keramik DE teils ab 500–1.000 € | „teils ab" + table „Stand 09/2026" |
| Non-Prep/Lumineers DE ab ca. 700–1.500 € | „ab ca." + table „Stand 09/2026" |
| Same-Day DE ab ca. 350–600 € | „ab ca." + table „Stand 09/2026" |
| Türkei ab ca. 250–350 € / Zahn | „ab ca." + table „Stand 09/2026" |
| Ungarn ab ca. 250–350 € (teils bis 800 €) / Zahn | „ab ca." + table „Stand 09/2026" |
| Polen ab ca. 330–550 € / Zahn | „ab ca." + table „Stand 09/2026" |
| Kroatien/Tschechien ab ca. 350–580 € / Zahn | „ab ca." + table „Stand 09/2026" |
| Sofia (Bulgarien) ab ca. 350–500 € / Zahn | „ab ca." + table „Stand 09/2026" |
| Deutschland (Referenz) ab ca. 700–1.500 € / Zahn | „ab ca." + table „Stand 09/2026" |
| Emax Sofia Beispielwerte um 450–522 € | „Beispielwerte" — framing completed: added „(Stand 09/2026)". (The source CONFLICT on this figure is a separate marker and STAYS — see REMAINING.) |
| 6 Keramik-Veneers DE ab ca. 3.000–6.000 € (Paket-Absatz) | „ab ca." + „Stand 09/2026" |
| 6–8 OK ab ca. 4.200 €–12.000 € | „ab ca." |
| 8 Keramik-Veneers DE ab ca. 4.800 € | „ab ca." + „Stand 09/2026" |
| 8 Veneers Türkei ab ca. 1.800 € | „ab ca." + table „Beispielpaket, Stand 09/2026" |
| 8 Veneers Kroatien ab ca. 2.650 € | „ab ca." + table „Beispielpaket, Stand 09/2026" |
| 8 Veneers Ungarn ab ca. 3.100 € | „ab ca." + table „Beispielpaket, Stand 09/2026" |
| 8 Veneers Deutschland ab ca. 4.800 € | „ab ca." + table „Beispielpaket, Stand 09/2026" |
| 8 Veneers England ab ca. 6.500 € | „ab ca." + table „Beispielpaket, Stand 09/2026" |
| 16 Veneers Beispielpakete ab ca. 3.000–5.600 € | „Beispielpakete" + „ab ca." |

### Tier B — confirmed against a fetched primary source
None. The one legal claim checked (GKV/Festzuschuss) could not be verbatim-confirmed for veneers — see REMAINING.

## REMAINING FOR HUMAN (flags stay in the text)

| Claim in article | Flag | Best source found / pre-fetched quote | What the human must check |
|---|---|---|---|
| Emax Sofia Preis 450–522 € — Quellen nennen teils ~350 $, teils ~522 € | [CONFLICT] | no single authoritative source; partner-clinic Kostenvoranschlag | Obtain an actual dated Sofia partner-clinic Kostenvoranschlag in € and replace the example with one sourced range. Currency ($ vs €) must be reconciled. |
| Auslandsbehandlung „in der Regel in zwei Reisen", Non-Prep teils in einer | [VERIFY: genaue Reisenzahl je Fall] | partner-clinic process (case-dependent) — no primary source | Confirm against the partner clinic's actual workflow; case-dependent. |
| Schmelzabtrag etwa 0,3–0,7 mm bei klassischer Präparation | [VERIFY] | DGZMK/DGÄZ ästhetische Zahnmedizin guideline (not a fetchable exact-figure quote) | Confirm the 0,3–0,7 mm range against a named dental-society/clinical source. Tier C: medical procedure detail. |
| Haltbarkeit: Komposit 5–8 / Keramik 10–15 / Lumineers 10–20 / Same-Day 5–10 Jahre | [VERIFY] | clinical longevity data (DGZMK / peer-reviewed); not price → Tier A N/A | Confirm durability ranges against a clinical source. Tier C: outcome/longevity claim. |
| Kontraindikation Bruxismus ohne Aufbissschiene (Kaukräfte überlasten Schalen) | [VERIFY] | DGZMK/DGÄZ guideline | Tier C (medical risk/contraindication) — human-mandatory. Cite a named source. |
| Weitere Kontraindikationen (zu wenig Schmelz, Karies/Parodontitis zuerst behandeln) | [DATA NEEDED: benannte fachliche Quelle] | DGZMK/DGÄZ or peer-reviewed source | Tier C — cite a named clinical source for the contraindication list. |
| GKV übernimmt Veneers nicht, kein Festzuschuss | [VERIFY: KZBV/GKV-Grundsatz] | § 55 SGB V (gesetze-im-internet.de/sgb_5/__55.html), fetched 2026-09-11: „Versicherte haben … Anspruch auf befundbezogene Festzuschüsse bei einer **medizinisch notwendigen** Versorgung mit **Zahnersatz**". | Statute confirms Festzuschüsse require *medizinisch notwendige Versorgung mit Zahnersatz*; it does NOT name veneers. Flag STAYS (Tier C) because resolving „Veneers = ästhetisch → kein Festzuschuss" needs the classification step, which only the human may confirm. Quote pre-attached for confirm-by-reading. |
| PKV/Zusatz leistet nur bei Tarif mit ästhetischen Leistungen | [VERIFY] | individual PKV-Tarifbedingungen — no single primary source | Tier C — depends on the reader's own tariff; cannot be resolved by a public source. |

## Recalculated savings example (working shown — figures stay as dated examples)
- 8 Keramik-Veneers vs. the named German reference (ab ca. 4.800 €):
  · Ungarn ab ca. 3.100 € → 4.800 − 3.100 = **1.700 €** below DE (article: „rund 1.700 €") ✓
  · Türkei ab ca. 1.800 € → 4.800 − 1.800 = **3.000 €** below DE (article: „rund 3.000 €") ✓
  Maths correct; figures themselves remain dated examples.

## Byline / compliance (verify present, do not change)
- Byline: **Georgi Todorov**, Patientenkoordinator (no clinical credential). Rotation: first article of run.
- Medical disclaimer verbatim at end ✓ · Mediation-transparency line verbatim in CTA block ✓ · Brand "Dentalvia" ✓.
- Compliance lines, risk section, example framing and images were NOT touched by verify-assist.

## Gemini external check (Step 7)
- Model gemini-3.1-pro-preview. Initial 05b: "Shows AI patterns 85%" → human-likeness 15; 2 humaniser passes
  (15/15/15, keep-best pass 2). Queue `gemini` = ai 15. Residual driven by required inline flags + compliance
  boilerplate + data-table prose; style-only, no fact/flag/compliance touched. (Unchanged by verify-assist.)

## Images (Step 8)
- 3 images (1 concept hero WebP + 2 data infographics SVG). Best Gemini image-review 90 (PASS); SVGs 85 (PASS).
  Every infographic figure traces verbatim to 05b; "Stand 09/2026" + "Beispielwerte" labels present; German.
  Not touched by verify-assist.

## Brand Gate (Step 5)
- PASS WITH FIXES, total 93/100 (see 05-gate-report.md; all 8 blocking checks PASS).
