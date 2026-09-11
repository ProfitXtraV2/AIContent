# 06 — Verification checklist (for the human, Step 6) · Zahnarztkosten von der Steuer absetzen

Reprocessed under the tiered verification policy (`DentalVia/pipeline/reference/verification-policy.md`,
approved 2026-09-11) by the verify-assist pass on 2026-09-11. The statutory rate claims (§ 33 EStG) were
checked against the primary statute and resolved where the source confirms them verbatim; case-law /
portal-sourced claims stay for the human. This is general information, not Steuerberatung. Nothing was
resolved by reasoning or a secondary source, and no claim or number was altered.

STATUS: still NOT publishable until the REMAINING flags are confirmed by the human. Merge = approve stays human.

## Count summary
**Was 12 flags (12 [VERIFY]) → resolved 8 (Tier A: 0, Tier B: 8), remaining 4 for human.**

## RESOLVED

### Tier B — confirmed against § 33 EStG (fetched gesetze-im-internet.de/estg/__33.html, 2026-09-11; marker removed)
| Claim in article | § 33 EStG passage | Exact quote | Result |
|---|---|---|---|
| Zahnarztkosten = außergewöhnliche Belastung nach **§ 33 EStG**; nur der Teil über der zumutbaren Belastung senkt die Steuer | Abs. 1 | „Erwachsen einem Steuerpflichtigen zwangsläufig größere Aufwendungen als der überwiegenden Mehrzahl der Steuerpflichtigen … (**außergewöhnliche Belastung**)" — die ESt wird ermäßigt, indem der Teil der Aufwendungen abgezogen wird, „der die dem Steuerpflichtigen **zumutbare Belastung** (Absatz 3) übersteigt" | CONFIRMED → resolved. (Statute confirms the § 33 framework + threshold mechanism. That medizinisch notwendige Krankheitskosten qualify is settled EStR 33.4 / BFH doctrine — the citation itself is correct.) |
| Schwelle **zwischen 1 und 7 %** des Gesamtbetrags der Einkünfte | Abs. 3 | Table ranges from 1 to 7 vom Hundert | CONFIRMED → resolved |
| Gestaffelt nach **drei Einkommensstufen** | Abs. 3 | „bis 15 340 EUR" / „über 15 340 EUR bis 51 130 EUR" / „über 51 130 EUR" | CONFIRMED → resolved |
| Alleinstehend ohne Kinder, oberste Stufe = **7 %** | Abs. 3 | ohne Kinder (Grundtarif) über 51 130 EUR = **7 %** | CONFIRMED → resolved |
| Verheiratet ohne Kinder, oberste Stufe = **6 %** | Abs. 3 | ohne Kinder (Splitting) über 51 130 EUR = **6 %** | CONFIRMED → resolved |
| 1–2 Kinder, oberste Stufe = **4 %** | Abs. 3 | ein oder zwei Kinder, über 51 130 EUR = **4 %** | CONFIRMED → resolved |
| 1–2 Kinder, mittlere Stufe = **3 %** | Abs. 3 | ein oder zwei Kinder, über 15 340 bis 51 130 EUR = **3 %** | CONFIRMED → resolved |
| 1–2 Kinder, unterste Stufe = **2 %** | Abs. 3 | ein oder zwei Kinder, bis 15 340 EUR = **2 %** | CONFIRMED → resolved |

(Statute reference for completeness — 3+ Kinder = 1/1/2 %; not stated in the article. The article's
„Beispiel-Satz"/„Beispielwerte" framing in the table and caption was left untouched.)

### Tier A — example-framed price figures
None. This how-to states statutory rates, not market prices; the rate figures were resolved under Tier B above.

## REMAINING FOR HUMAN (flags stay in the text)

| Claim in article | Flag | Best source found / note | What the human must check |
|---|---|---|---|
| „**Seit 2017** … kein pauschaler Prozentsatz mehr; **stufenweise** berechnet" | [VERIFY: gestaffelte Berechnung seit 2017] | BFH, Urteil vom 19.01.2017, **VI R 75/14** (stufenweise Berechnung der zumutbaren Belastung). § 33 EStG statute text does not state „stufenweise" or „seit 2017" — this is BFH interpretation, not fetchable as a verbatim statute quote. | Confirm the stufenweise-Berechnung and the 2017 origin against BFH VI R 75/14 (or the BMF-Anwendung). Tier C: case-law date claim. |
| „Laut Finanztip … Grenze um bis zu **664,70 €** (Stand 2024)" | [VERIFY: 664,70 €, Finanztip Stand 2024] | Finanztip is a **portal/secondary source** (policy forbids resolving against blogs/portals), and the figure is **Stand 2024** (predates 2026). No primary source carries this exact euro figure. | Tier C — cannot be resolved by a primary source. Human: re-verify or re-source the 664,70 € figure (and consider whether „Stand 2024" is still current), or attribute clearly as Finanztip's own estimate. |
| Auslandsbehandlung wird „**grundsätzlich wie eine Behandlung in Deutschland**" als außergewöhnliche Belastung anerkannt | [VERIFY: Auslandsbehandlung deutsche Rechtslage/BFH] | § 33 EStG contains no location restriction, but „Ausland wie Inland" for medical costs rests on BFH/EStR case law, not the statute text. | Tier C — confirm against BFH case law / EStR (Krankheitskosten im Ausland). Statute alone does not name Auslandsbehandlung. |
| Anrechenbar sind auch **notwendige Reise- und Übernachtungskosten** im Zusammenhang mit der Behandlung | [VERIFY] | EStR / BFH on Nebenkosten (Fahrt-/Übernachtungskosten) als Teil der Krankheitskosten — not in § 33 EStG statute text. | Tier C — confirm the deductibility of travel/accommodation costs against EStR/BFH. |

## Worked example (in 06 only, deliberately NOT added to the article)
- zumutbare-Belastung threshold: 7 % × 40.000 € Gesamtbetrag der Einkünfte = 2.800 € (single, no kids, top
  bracket). Only self-borne costs above 2.800 € reduce the tax. Arithmetic illustration only; figures are the
  statutory rates confirmed above.

## Byline / compliance (verify present, do not change)
- Byline: **Georgi Todorov**, Patientenkoordinator (kein Steuerberater). Rotation: 3rd article of run.
- Medical disclaimer verbatim at end ✓ · Mediation-transparency line verbatim in CTA block ✓ · Brand "Dentalvia" ✓.
- „Keine Steuerberatung" stated; cosmetic dentistry stated NOT deductible. Compliance/framing untouched by verify-assist.

## Gemini external check (Step 7)
- gemini-3.1-pro-preview: human-likeness 15 → 25 → 25 across 2 passes, keep-best pass 2 (`ai 25`). Two Gemini
  recs rejected as brand/pipeline violations (first-person „ich"; converting prose to a new bullet list).
  Style-only; no fact/flag/compliance touched. (Unchanged by verify-assist.)

## Images (Step 8)
- 2 images (concept hero WebP + zumutbare-Belastung SVG). Gemini hero 72 / infographic 75 — both sub-80 solely
  due to the mis-loaded VK "Bulgarian ALT" requirement; German ALT correct, data matches, layout clean → both
  kept. Every figure traces verbatim to 05b. Not touched by verify-assist. (Maintainer note in 08-image-review-1.md:
  point the review script at DentalVia's step-8 prompt.)

## Brand Gate (Step 5)
- PASS — total 92/100; zero criticals (blocking check #2 Risiken/Kontraindikation and /garantie/ N/A for a tax
  how-to). See 05-gate-report.md.
