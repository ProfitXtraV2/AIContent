# 06 — Verification checklist (for the human, Step 6) · Zahnarztkosten von der Steuer absetzen

STATUS: NOT publishable until every tax figure is confirmed against § 33 EStG / BFH / Finanzamt and the
human resolves the flags. ALL figures are flagged [VERIFY] and stay IN the text. Claude resolves nothing.
This is general information, NOT Steuerberatung.

## Byline / compliance
- Byline: **Georgi Todorov**, Patientenkoordinator (no clinical/tax credential). Rotation: 3rd article of run.
- Medical disclaimer verbatim at end ✓ · Mediation-transparency line verbatim in CTA block ✓ · Brand "Dentalvia" ✓.
- Howto (not cost/comparison) → /garantie/ intentionally omitted. German law only (no Austrian/KPMG figures used).

## Tax figures — confirm each against § 33 EStG / BFH / Finanzamt (German law)
| Claim | Value (as written) | Source to confirm |
|---|---|---|
| Legal basis | § 33 EStG (außergewöhnliche Belastung) [VERIFY] | gesetze-im-internet.de (§ 33 EStG) ; finanztip.de/krankheitskosten |
| zumutbare Belastung range | 1–7 % des Gesamtbetrags der Einkünfte [VERIFY] | finanztip.de ; § 33 Abs. 3 EStG |
| 3 Einkommensstufen | drei Einkommensstufen [VERIFY] | § 33 Abs. 3 EStG |
| Example rates | Alleinstehend o. K. 7 %; Verheiratet o. K. 6 %; 1–2 Kinder 4 %/3 %/2 % (oberste/mittlere/unterste Stufe) [VERIFY each] | finanztip.de ; § 33 Abs. 3 EStG table |
| Staffelung seit 2017 | gestaffelte Berechnung seit 2017 [VERIFY] | BFH-Urteil VI R 75/14 (2017) ; finanztip.de |
| Finanztip figure | senkt die Grenze um bis zu 664,70 € (Stand 2024) [VERIFY] | finanztip.de/krankheitskosten (current value/date) |
| Abroad deductible | medizin. notwendige Zahnbehandlung im (EU-)Ausland als agB, inkl. notw. Reise-/Übernachtungskosten [VERIFY] | BFH-Rechtsprechung ; deutsche Finanzverwaltung |
| Only self-borne share counts | Festzuschuss + Erstattungen zuerst abziehen | § 33 EStG (Eigenbelastung) |

## Recalculated example (illustrative — shows the mechanic; NOT a figure from the article)
Using the article's example rate for a single without children (oberste Stufe, 7 % [VERIFY]):
- Hypothetical Gesamtbetrag der Einkünfte 40.000 € → zumutbare Belastung = 7 % × 40.000 € = 2.800 €.
- Selbst getragener Eigenanteil (nach Festzuschuss/Erstattungen) z. B. 4.000 € → absetzbar = 4.000 − 2.800 = 1.200 €.
Arithmetic confirmed; the 7 % rate itself stays [VERIFY]. (This worked example is for the human's check only
and is deliberately NOT added to the article, which carries no invented euro amounts.)

## Non-figure flags
- Cosmetic dentistry (Bleaching, kosmetische Veneers ohne Krankheitswert) stated as NOT deductible — confirm against § 33 EStG (medizinische Notwendigkeit). ✓ present once.
- Anlage Außergewöhnliche Belastungen; full Eigenanteil eingetragen, Finanzamt zieht zumutbare Belastung selbst ab — confirm current form handling [VERIFY-adjacent].

## Gemini external check (Step 7)
- Model gemini-3.1-pro-preview. Initial 05b: "shows AI patterns 85%" → human-likeness 15.
- 2 Humaniser passes (07-gemini-check-1/2/3.md): human-likeness 15 → 25 → 25; keep-best pass 2. Queue `gemini` = **ai 25**.
- Two of Gemini's recs were REJECTED as brand/pipeline violations: injecting first-person "ich"/"aus meiner
  Erfahrung" (brand forbids default "ich" + first-person experiential claims) and converting prose into a new
  bullet list (pipeline reduces lists, never adds). Residual score driven by required inline flags + verbatim
  compliance boilerplate + the procedural rhythm of a how-to. Style-only; no fact/flag/compliance changed.

## Images (Step 8)
- images: 2 (1 concept hero WebP: tax form + receipts + refund coin; 1 data infographic SVG: zumutbare-
  Belastung example rates). Gemini image-review: hero 72, infographic 75 — both sub-80 SOLELY due to a
  mis-loaded "Bulgarian ALT" requirement from the shared VK review prompt; German ALT is correct here and the
  reviewer confirms both perfectly match the article, the infographic data matches exactly, and layout is
  clean (no clipping/overlap). No integrity/hygiene/layout violation → both kept (keep-best). Every infographic
  figure traces verbatim to 05b; German labels; example rates flagged as Beispielwerte.

## Brand Gate (Step 5)
- PASS, total **92/100**; blocking checks: #2 (Risiken+Kontraindikation) N/A (tax how-to), /garantie/ N/A
  (howto), all others PASS; zero criticals; no fixes needed. See 05-gate-report.md.
