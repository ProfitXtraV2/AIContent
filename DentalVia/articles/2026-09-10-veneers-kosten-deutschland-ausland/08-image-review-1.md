# Step 8 — Gemini image review · Pass 1 (verbatim)

Model: gemini-3.1-pro-preview (multimodal) · run 10.09.2026
Images reviewed: veneer-kosten-vergleich-hero.webp; veneer-kosten-pro-zahn-deutschland-ausland-vergleich.svg; veneer-paketpreis-8-veneers-laendervergleich.svg

## SCORE: 90 — Verdict: PASS

## Specific problems
- Language/Typo (SVG 1 & SVG 2): both infographics contain a Denglish error in their footer text — the
  English word "dated" is used instead of a German equivalent.
  · SVG 1: "...Alle Preise sind dated Beispiele"
  · SVG 2: "...dated Beispiele, kein Festpreis."
- Layout/Line length (SVG 2): the footer at y=312 is a single ~125-char line running close to the right
  edge; risks clipping on wider default fonts.

## Concrete fixes
- SVG 1: change "dated Beispiele" → German ("Beispielwerte" / "Preisbeispiele (Stand 09/2026)").
- SVG 2: change "dated Beispiele" → German; split the long footer into two lines for safe margins.

## Integrity/hygiene
No fabricated logos, no fake screenshots, no people/faces, no clinical procedures, no before/after teeth,
flat illustration only; infographic numbers match the article (per-tooth and 8-veneer package tables) with
"Stand 09/2026" labels present. PASS on integrity; the "dated" wording is the only defect → fixed in pass 2.
