# 05-gate-report — /saveti/google-biznes-profil/ (Step 5, Brand Gate)

Inputs read: 00-current.md, 00-inventory.md, 00-brief.md, 04-seo.md, keyword-map.md (row + all sibling primaries), conversion-links.md, site-rules.md, verification-policy.md, markets/bg/author.md (canon + voice), brand-gate-bizgrow.md, step-5-brand-gate.md.

```
BRAND COMPLIANCE SCORECARD — /saveti/google-biznes-profil/ (bg)
Verdict: PASS (moderate language fixes applied, no criticals)
Total: 91/100 → 93/100 after fixes
Voice 18/20 | Language 13/15 → 14/15 | Trust & claims 18/20 → 19/20 | Usefulness 14/15 | Anti-AI 14/15 | SEO 14/15
```

## ARTICLE RULE CHECKS (python, _tmp/gate_check.py)

| rule | result |
|---|---|
| question-led H2s 6–8 | PASS: 8, all questions |
| body 900–1,400 words excl. lead + FAQ + flag markers | PASS: 920 (gate count; Step 4 reported 934 with a different tokenisation; both in range) |
| FAQ 4–6 | PASS: 6, each 1–2 sentences, none repeats a heading verbatim |
| exactly one booking CTA on the page | PASS: 1 („Запазете безплатна диагностика“ → `{{BOOKING_URL}}`, #bizgrow) |
| eyebrow „Съвети“ | PASS |
| summary ≤160 | PASS: 148 |
| no `service` key | PASS |
| related = 3 sibling paths from conversion-links.md | PASS: /socialni-mrezhi/, /ai-asistent/, /seo-optimizacia/ |
| title ≤60 incl. „ | BizGrow“ | PASS: 54 |
| meta 120–160 | PASS: 140, contains the main term |
| max 3 sourced facts | PASS (see MODERATE 1): F1, F2, F3 per the brief's grouping |
| UI labels only verbatim from 00-brief passages | PASS: „Добавете бизнеса си в Google“, „Заявяване на този бизнес“ (both verbatim in S1); „Google Карти“, „Търсене“ are product names |
| no delivery periods | PASS: only „30-минутен разговор“; „до 5 работни дни“ is Google's sourced review time, not a BizGrow delivery period; „Срокът зависи от решението и го посочваме в офертата.“ verbatim |
| „оферта“, never „доклад“ | PASS: „доклад“ 0 |
| em-dashes / exclamation marks | PASS: 0 / 0 |

## BLOCKING CHECKS

1. NOTHING LOST (new page, inventory carriers): PASS. I1 single CTA in #bizgrow; I2 /diagnostika/ (#bizgrow); I3 /socialni-mrezhi/ („поддържа профила жив“, #bizgrow); I4 /ai-asistent/ (#ocenki); optional `{{EMAIL}}` present once; I5 monthly upkeep with posts, photos, information; I6 ratings/comments watched, reply prepared for approval; I7 free diagnosis + 30-minute call → оферта with prioritised fixes and clear one-off prices, timing line verbatim; I8 „Диагностиката не Ви обвързва с нищо. Работим без дългосрочни договори.“
2. FACTS ALLOWED LIST: PASS. Every BizGrow statement is canon (profile upkeep monthly; replies prepared for approval; AI assistant answering in Messenger/Instagram/WhatsApp outside working hours and taking the contact when it cannot help; process; no long-term contracts). No vendor, team, price, client or count.
3. BANNED CLAIMS: PASS. „безплатн*“ 2× (both the diagnosis); no „отзив*“ in visible copy; no guarantee words; ranking explicitly not promised („никой не може да обещае конкретно място в Картите“); no hype, price, offer or urgency.
4. NUMBERS: PASS. 30 (canon, call), 5 (Tier B, `[VERIFY]` S2, body + FAQ 2). No other figures.
5. HYPOTHETICAL LABEL: N/A (no example scenarios).
6. GDPR WORDING: N/A (GDPR not mentioned; the „лични данни“ line in #ocenki is reply etiquette, not a compliance claim).
7. REGISTER: PASS. Zero „ти“ forms (regex hits were word endings such as „Карти“). Courtesy forms capitalised. FAQ questions use the reader's first person („ми“, „мен“), which is correct.
8. CTA RULES: PASS. One booking CTA, approved wording, token only; email only as `{{EMAIL}}`; no urgency.
9. ONE TERM PER PAGE: PASS. „бизнес профил в гугъл“ once each in title, lead (first 100 words), one H2 (#syzdavane), plus meta; H1 is the keyword-map H1. No sibling primary (ai автоматизация, ai асистент as heading target, автоматизация на бизнес процеси, seo копирайтинг, маркетинг в социалните мрежи, реклама в гугъл, seo оптимизация, локално seo, копирайтър, ключови думи, безплатна диагностика за бизнеса) in title, H1 or any H2. „AI асистент“ appears only as body link text to its own page.
10. LINKS & ANCHORS: PASS. /ai-asistent/, /socialni-mrezhi/, /diagnostika/ (3 contextual, within 1–3), all in conversion-links.md; no external body links (business.google.com/add deliberately not shown, flagged).
11. BIZGROW VOICE: PASS. No fragment paragraphs, rhetorical questions, verdict lines, slang or hype; jargon („AI асистент“) explained on first use.

CRITICAL (blocks): none.

## MODERATE (fixed or noted)

1. Sourced-fact count (noted, not changed): F1 bundles two statements from S1 (found in Search and Maps after adding and verifying; adding/claiming without monetary payment) and F2 two from S2 (ownership; options depend on business type). Counted as 3 facts per the brief's suggested grouping. The claim steps and the ownership-request sentence in #zayavyavane are procedural paraphrase of S1; Step 6 should cite S1 for them. Added as a FLAGS note and an owner item.
2. Language, lead (fixed): „Google бизнес профил е информацията …“ → „Google бизнес профилът е информацията …“ (subject needs the full article).
3. Language + scope, #bizgrow (fixed): „Нищо не се публикува, преди да го одобрите.“ (clitic „го“ does not agree with „нищо“) → „Нищо не се публикува без Вашето одобрение.“ Meaning of inventory I6 kept. The sentence also covers profile posts and photos, while canon states approval explicitly for replies and for the content tool → owner item.
4. Language, #danni (fixed): „дали сте отворени“ next to „отварят профила“ (repetition) → „дали работите в момента“.
5. SEO voice, lead (noted, not changed): „В търсачката хората го търсят и като „бизнес профил в гугъл“ или „гугъл бизнес профил“.“ reads slightly like a keyword note but is accurate and carries the main term in the first 100 words; left for the owner's colloquial-spelling decision (existing flag).
6. Repetition (noted): the no-ranking-promise idea appears in #kakvo-e and FAQ 4; acceptable because FAQ answers must stand alone.

## VOICE NOTES (protect in Step 6)
- Keep the calm advisory tone, the step lists, the no-ranking-promise sentence and the closing order: upkeep → diagnosis → оферта → timing line → no commitment → CTA → email.
- Keep „оценки и коментари“ throughout until the owner decides item 7.

---

