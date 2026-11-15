# 06-verification — / (home, bg) — 2026-11-15

Inputs: 05b-final-draft.md (no changes vs the Brand Gate Phase 2 page), 00-current.md, 00-inventory.md,
reference/verification-policy.md, reference/site-rules.md, templates/content-file-template.md, keyword-map.md.
Assembled by one script from one data structure so `content/home.md` and `content/home.port.json` carry
identical strings (scratchpad build.py / check.py, Python 3.14 with tomllib).

## RESOLVED-TO-OWNER-ITEMS
- [VERIFY] markers: 0. New external facts: 0. `[[sources]]`: none.
- [OWNER CONFIRM] markers in 05b: 9 → 10 `[[owner_items]]` (gate list items 1-8, 11; item 9 "optional GDPR FAQ" folded into the FAQ owner item).
- „за дни, не месеци“ (hero.body, hero.overlayUnit): not canon → per policy "the text says only what is known", the
  author/gate fallback „обикновено до 2 седмици“ is used verbatim; restoring the phrase is an owner item.
- Example rows E1-E3 kept verbatim with the label; owner item.

## REMAINING FOR HUMAN
- `#faq` anchor has no row in BizGrow/conversion-links.md (shared file, not edited by this run). Add it.
- Home dictionary has no `related` key, so the port JSON has none (the brief's "related = 3 paths" rule applies to ContentPage objects, not to the home `Dictionary`). If the human wants a related strip on home, suggested paths: /ai-asistent/, /avtomatizacii/, /diagnostika/.
- `a11y.home` „BizGrow – начало“ contains an en-dash (unchanged UI string, not an em-dash); optional change to „BizGrow, начало“.

## PORTING NOTES
- Changed keys: meta.title/description/ogTitle/ogDescription; hero.line1/line2/body/imageAlt/overlayUnit; metrics (all 3); losses.title/items; services.title/items; process.lead/steps[*].body; results.title; reasons.lead; cta.body.
- Unchanged keys (copied verbatim from bg.ts @ 528ad25): a11y, page, nav, hero.primary/secondary/imageSrc/overlayLabel, results.note/rows, reasons.title/items, cta.title/button, contact, footer, meta.ogLocale.
- NEW type fields in `site/src/i18n/types.ts`: `losses.link: { label: string; href: string }`; `services.items[].href: string`; top-level `faq: { title: string; items: { question: string; answer: string }[] }`. en.ts needs the same keys (en-home run).
- Components: Services cards become links (href); Losses renders `link`; new FAQ section between CtaBand and Contact with `id="faq"` (and FAQPage structured data if wanted); process step bodies and FAQ answers contain `[label](/diagnostika/)` and need RichText rendering.
- `hero.overlayValue` stays omitted (overlay is a phrase).

## SELF-CHECK
| check | result |
|---|---|
| TOML parses (tomllib) | PASS (9 sections, 7 faq, 10 owner_items) |
| title ≤ 60 incl. " \| BizGrow", no em-dash | PASS (43) |
| meta_description 120-160, contains main term | PASS (149, „AI автоматизация“) |
| primary_keyword = keyword-map term | PASS („ai автоматизация“) |
| main term in title / H1 / first 100 words / one H2 | PASS (title 1, H1 line 1, hero body sentence 1, #services H2) |
| sections ↔ body blocks (id, heading, order) | PASS |
| em-dashes (md + json) | PASS (0) |
| bracketed markers | PASS (0) |
| „ти“ forms / lowercase courtesy forms | PASS (0 / 0) |
| banned claims, hype, PRICE/OFFER/TESTIMONIAL | PASS (0) |
| numbers: canon (30 мин, 48 ч, 2 седмици, 0) or labelled example (24/7, 10 часа, 80%) | PASS |
| example label in #results | PASS |
| inventory items present | PASS (C1-C6, T1-T2, 8 anchors + #faq, F1-F9, N3-N8, L1; L2 replaced by canon fallback → owner item; N1/N2/questionnaire/„Решения по поръчка“ REMOVE-BY-BRIEF) |
| links only from conversion-links.md | PASS (/ai-asistent/, /avtomatizacii/, /seo-statii/, /socialni-mrezhi/, /reklama/, /seo-optimizacia/, /diagnostika/, #services) ; #faq anchor new (see above) |
| tokens | PASS ({{BOOKING_URL}} ×3 in body + nav/hero/cta/contact keys; {{EMAIL}} in contact) |
| port JSON strings identical to content file | PASS (all changed strings present verbatim; only unchanged UI chrome is not in the md) |

Counts: new facts: 0; owner items added: 10. Body word count (content file body incl. FAQ and form labels): 793.
