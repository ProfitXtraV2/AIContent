# 05b · Step 5b Humaniser light re-check: follow-up 2026-11-15 (items A, B, C)

Inputs: 05-gate/{saveti,home-cards,reklama}.json, 05-gate-report.md, 00-inventory.md, baseline
`_tmp/reklama.current.json`. Rules: prompts/step-5b-humaniser-light.md, agents/humaniser.md,
markets/bg/author.md, reference/site-rules.md.

Scope: only strings that are new or changed against the live copy (gate polish on /saveti/ lead,
3 new home cards + /reklama/ card + services_title + nav „Съвети“, the 14 changed /reklama/
strings). Unchanged /reklama/ strings are live owner-approved copy and were left alone.

Scripted scan over every string of all three files: em-dashes 0, en-dashes 0, exclamation
marks 0, „ти“ forms 0, lowercase вие/ви/вас/ваш 0, „доклад“ 0, delivery periods 0, price
patterns 0, banned connectives/signposts/hype 0, „безплатн*“ only with „диагностика“, digits only
in `updated`, „30-минутен“ (canon, ×2) and „B2B“. Question marks only in FAQ questions.

## Verdicts

| Item | Verdict | Edits |
|---|---|---|
| A. /saveti/ | PUBLISH-READY, unchanged | none. Gate split of the lead reads correctly; s2 lists three real topics (not a habitual triad); AI and SEO explained on first use. |
| B. Home cards + nav | PUBLISH-READY, unchanged | none. New card bodies are complete sentences, formal „Вие“, no periods/prices/platforms; „Съвети“ nav label fine. |
| C. /reklama/ | PUBLISH-READY, unchanged | none. Changed strings (title, meta, label, summary, eyebrow, H1, lead, specialist p1, „Планиране“ bullet, facebook-instagram heading and paragraph, FAQ 6 answer, service) are grammatical, formal, free of AI tells. |

Noted, not edited (taste, not an error):
- /reklama/ specialist p1 repeats „поема“ (s1 baseline, s3 „като поема планирането“); already
  logged by the gate as MINOR.
- Home Facebook card „Резултатите получавате с конкретни числа.“ is correct; definite
  „Маркетинг специалистът“ relies on the /reklama/ card above (gate MINOR).
- Both JSONs carry `"status": "published"` as in the baseline/site schema; not a pipeline
  approval marker, left untouched.

## /reklama/ inventory re-check (05b vs 00-inventory)

- Section ids (8, order unchanged): specialist, kak-raboti, facebook-instagram, za-kogo, otchet,
  proces, cena, diagnostika. PASS.
- FAQ: 8 entries, all 8 questions verbatim. PASS.
- C1 proces CTA „Запазете безплатна диагностика“ → {{BOOKING_URL}} · C2 diagnostika „Запазете
  час“ → {{BOOKING_URL}} · C3 {{EMAIL}} in diagnostika · C4 /diagnostika/ in proces step 1 ·
  C5 /seo-optimizacia/ in kak-raboti p4 · C6 /socialni-mrezhi/ in facebook-instagram and FAQ 5.
- C7 lead/specialist/FAQ 5 · C8 lead, otchet, FAQ 4 · C9 lead, summary, bullet 3, otchet, FAQ 4 ·
  C10 specialist p1 · C11 bullet 4 · C12 facebook-instagram s3 + FAQ 5 · C13 za-kogo (3
  situations + 6 bullets) · C14 proces 4 steps, „оферта“, no period · C15 cena p1, FAQ 1 ·
  C16 cena p1, lead, FAQ 7 · C17 „Работим по GDPR.“ in cena · C18 FAQ 8 timing line verbatim ·
  C19 kak-raboti p1, cena p2, FAQ 1, FAQ 3 · C20 kak-raboti p2, cena p2, FAQ 1 · C21 kak-raboti
  p3, FAQ 2 · C22 kak-raboti p1/p4, FAQ 3.
- related: /reklama-vav-facebook/, /seo-optimizacia/, /diagnostika/ (R4 applied).

Inventory diff 05-gate → 05b: none (all three files byte-identical to 05-gate; JSON valid).
Inventory diff baseline → 05b: only the brief's REMOVE-BY-BRIEF R1, R2, R4 changes recorded in
05-gate-report.md; no new loss.

## Outputs

- 05b/saveti.json (copy of 05-gate)
- 05b/home-cards.json (copy of 05-gate)
- 05b/reklama.json (copy of 05-gate)
