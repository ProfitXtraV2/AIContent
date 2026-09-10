# 06 — Verification checklist (for the human, Step 6) · Veneers-Kosten DE vs. Ausland

STATUS: NOT publishable until every flag below is confirmed against a primary source and resolved by a
human. Flags remain IN the article text. Claude does not resolve flags.

## Byline / compliance (verify present, do not change)
- Byline: **Georgi Todorov**, Patientenkoordinator (no clinical credential). Rotation: first article of run.
- Medical disclaimer verbatim at end ✓ · Mediation-transparency line verbatim in CTA block ✓ · Brand "Dentalvia" ✓.

## Price flags — all are dated examples ("ab X €", "Stand 09/2026"); confirm current figures + dates
| Claim in article | Value (as written) | Suggested primary/secondary source to confirm |
|---|---|---|
| Komposit-Veneer DE / Zahn | ab ca. 250–500 € [VERIFY] | zahnkosten-rechner.de/ratgeber/veneers-kosten/ ; zukunftzahn.de veneers-arten |
| Keramik-Veneer DE / Zahn | ab ca. 700–1.500 € [VERIFY] | zukunftzahn.de ; implantate.com/was-kosten-veneers... |
| Standard-Keramik DE / Zahn | teils ab 500–1.000 € [VERIFY] | zahnkosten-rechner.de |
| Non-Prep/Lumineers DE / Zahn | ab ca. 700–1.500 € [VERIFY] | zahnkosten-rechner.de |
| Same-Day/Veneers-to-Go DE / Zahn | ab ca. 350–600 € [VERIFY] | zahnkosten-rechner.de |
| 6 Keramik-Veneers DE gesamt | ab ca. 3.000–6.000 € [VERIFY] | qunomedical.com/de/guides/veneers-kostenueberblick |
| 6–8 Keramik OK gesamt | ab ca. 4.200 €–12.000 € [VERIFY] | zukunftzahn.de |
| 8 Keramik-Veneers DE Paket | ab ca. 4.800 € [VERIFY] | qunomedical.com |
| 8 Veneers Türkei/Kroatien/Ungarn/DE/England | ab ca. 1.800 / 2.650 / 3.100 / 4.800 / 6.500 € [VERIFY] | qunomedical.com/de/guides/veneers-kostenueberblick |
| Ausland/Zahn: Türkei/Ungarn 250–350 €, Polen 330–550 €, Kroatien/Tschechien 350–580 € [VERIFY] | as written | veneer-vergleich.de/veneers-in-ungarn/ ; dentfix.de |
| Sofia (Bulgarien)/Zahn | ab ca. 350–500 € [VERIFY] | dentaly.org (Bulgaria) ; local Sofia clinic Kostenvoranschlag |
| Emax Sofia | Beispielwerte 450–522 € [VERIFY] | 123.clinic emax-veneers/bulgaria |
| 16 Veneers Paket-Beispiel | ab ca. 3.000–5.600 € [VERIFY] | qunomedical.com |

### [CONFLICT] to resolve
- Sofia/Emax Bulgaria price: one source ~350 $, another ~522 € (currency + spread mismatch). **Human: obtain
  an actual dated Sofia partner-clinic Kostenvoranschlag in € and replace the example with a single sourced range.**

## Recalculated savings example (working shown)
- 8 Keramik-Veneers, like-for-like vs. the named German reference (ab ca. 4.800 €):
  · Ungarn ab ca. 3.100 €  → 4.800 − 3.100 = **1.700 €** below DE (article: "rund 1.700 €") ✓
  · Türkei ab ca. 1.800 €  → 4.800 − 1.800 = **3.000 €** below DE (article: "rund 3.000 €") ✓
  Maths correct. (Figures themselves stay [VERIFY].)

## Non-price / medical flags
| Claim | Flag | Source to confirm |
|---|---|---|
| Schmelzabtrag ca. 0,3–0,7 mm bei Präparation | [VERIFY] | zahnkosten-rechner.de ; DGÄZ/DGZMK ästhetische Zahnmedizin |
| Haltbarkeit: Komposit 5–8 / Keramik 10–15 / Lumineers 10–20 / Same-Day 5–10 Jahre | [VERIFY] | zahnkosten-rechner.de ; qunomedical.com |
| Ablauf in der Regel 2 Reisen (Non-Prep teils 1) | [VERIFY: genaue Reisenzahl je Fall] | partner-clinic process / case-dependent |
| Kontraindikation Bruxismus ohne Aufbissschiene | [VERIFY] | DGZMK/DGÄZ guideline (named source) |
| Kontraindikationen allgemein (zu wenig Schmelz, Karies/Parodontitis zuerst behandeln) | [DATA NEEDED: benannte fachliche Quelle] | **Human: cite a DGZMK/DGÄZ or peer-reviewed source** |
| GKV übernimmt Veneers nicht, kein Festzuschuss | [VERIFY: KZBV/GKV-Grundsatz] | KZBV/GKV ; § 55 SGB V context (ästhetische Leistung ausgeschlossen) |
| PKV/Zusatz nur bei entsprechendem Tarif | [VERIFY] | individual PKV terms |

## Gemini external check (Step 7)
- Model gemini-3.1-pro-preview. Initial 05b: "Shows AI patterns 85%" → human-likeness 15.
- 2 Humaniser passes applied (07-gemini-check-1/2/3.md). All three passes scored human-likeness 15 (tied).
- Keep-best: pass 2 retained. Queue `gemini` = **ai 15** (below target 80 after cap). Residual driven largely
  by the required inline flags + compliance boilerplate + data-table prose; not resolvable without breaching
  pipeline rules. Style-only; no fact/flag/compliance touched.

## Images (Step 8)
- images: 3 (1 concept hero WebP + 2 data infographics SVG). Best Gemini image-review score **90 (PASS)**;
  SVGs re-reviewed 85 (PASS) after German-label + margin fixes. No integrity or dental-hygiene failure.
  Every infographic figure traces verbatim to 05b; "Stand 09/2026" + "Beispielwerte" labels present; German.

## Brand Gate (Step 5)
- PASS WITH FIXES, total 93/100 (see 05-gate-report.md; all 8 blocking checks PASS; 2 mechanical em-dash
  fixes in meta placeholders only).
