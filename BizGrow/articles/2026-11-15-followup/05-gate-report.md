# 05 · Step 5 Brand Gate: follow-up 2026-11-15 (items A, B, C)

Inputs: 04-seo/{saveti,home-cards,reklama}.json, 00-brief.md, 00-current.md, 00-inventory.md (incl. REMOVE-BY-BRIEF R1–R4), 03-report.md, 04-seo.md, baseline `_tmp/reklama.current.json`; rules from agents/brand-gate-bizgrow.md, markets/bg/author.md (canon incl. service 6), site-rules.md, verification-policy.md, keyword-map.md, conversion-links.md.

Scripted checks over every string field of all three outputs: em-dashes 0, en-dashes 0, exclamation marks 0, price patterns 0, „ти“ forms 0, lowercase courtesy pronouns 0, banned words (гарант*/лидер/най-добр*/hype/промоци*/отзив*/сертифиц*/„доклад“/delivery periods/100%) 0, „безплатн*“ only with „диагностика“. Numbers: only „30-минутен“ (canon, diagnosis call) ×2 on /reklama/. Links and tokens all from conversion-links.md.

/reklama/ reviewed as a diff against the baseline: 14 strings changed, 1 paragraph removed (sections[2].paragraphs[1], by R2). Home cards: 5 live cards are byte-identical to 00-current (icon, title, body, href); new copy = 3 new cards, /reklama/ card, services_title, nav „Съвети“.

Outputs: 05-gate/saveti.json (1 edit), 05-gate/home-cards.json (copy), 05-gate/reklama.json (copy).

---

## A. /saveti/

```
BRAND COMPLIANCE SCORECARD — /saveti/ (bg)
Verdict: PASS
Total: 92/100
Voice 18/20 | Language 14/15 | Trust & claims 19/20 | Usefulness 13/15 | Anti-AI 14/15 | SEO 14/15
BLOCKING CHECKS: 1 N/A (new page; hub inventory items present: label „Съвети“, path, tool "hub",
  no service, sections [], faq [], 3 related) | 2 PASS (no BizGrow fact beyond „безплатна
  диагностика“) | 3 PASS | 4 PASS (no figures) | 5 N/A | 6 N/A | 7 PASS | 8 PASS (no booking CTA;
  /diagnostika/ link, no urgency) | 9 PASS (primary „—“; no address's main term in title/meta/
  h1/eyebrow/lead/summary) | 10 PASS (/diagnostika/, /avtomatizacii/, /seo-statii/,
  /seo-optimizacia/) | 11 PASS after polish
CRITICAL: none
MODERATE (fixed): lead s1 ran about 38 words with a colon list → split into two sentences
  („…малък бизнес. Статиите показват как да използвате…“); meaning, link and explanations of
  AI/SEO unchanged.
OWNER ITEMS: G-A1 (below)
VOICE NOTES: first sentence states what the page offers; AI and SEO explained on first use.
```

## B. Home #services cards + nav

```
BRAND COMPLIANCE SCORECARD — / #services cards, nav (bg)
Verdict: PASS
Total: 93/100
Voice 18/20 | Language 14/15 | Trust & claims 19/20 | Usefulness 14/15 | Anti-AI 14/15 | SEO 14/15
BLOCKING CHECKS: 1 PASS (B1: 5 live cards identical to 00-current; /reklama/ card href kept,
  title/body Google-only; B2: services.more/nav cta untouched, nav „Услуги“, „Процес“,
  „Свържете се с нас“ unchanged, „Съвети“ → /saveti/ between „Процес“ and „Свържете се с нас“)
  | 2 PASS (site card: build + maintenance = canon service 6, short monthly report = canon
  process step 4; shop card: product descriptions for whole collections and abandoned-cart
  messages = canon capabilities, framed „можем да добавим“; both ad cards = canon service 4)
  | 3 PASS | 4 PASS (no figures) | 5 N/A | 6 N/A | 7 PASS | 8 N/A (no CTAs in scope)
  | 9 PASS (services_title keeps home's own term; each card names and links its own page)
  | 10 PASS (all 9 hrefs in conversion-links.md) | 11 PASS
CRITICAL: none
MODERATE: none
MINOR (no edit): Facebook card opens with definite „Маркетинг специалистът“, relying on the
  /reklama/ card directly above; reads correctly in the fixed order.
OWNER ITEMS: G-B1, G-B2 (below)
VOICE NOTES: card bodies are 1–2 complete sentences; no platforms, periods or prices.
```

## C. /reklama/

```
BRAND COMPLIANCE SCORECARD — /reklama/ (bg)
Verdict: PASS
Total: 92/100
Voice 18/20 | Language 14/15 | Trust & claims 19/20 | Usefulness 14/15 | Anti-AI 14/15 | SEO 13/15
BLOCKING CHECKS:
 1 PASS: C1–C22 present (CTAs ×2 {{BOOKING_URL}}, {{EMAIL}}, /diagnostika/, /seo-optimizacia/,
   /socialni-mrezhi/ in body and FAQ 5; C12 „Брандирани визии, публикации и рекламни
   материали … всеки месец“ in section facebook-instagram + FAQ 5); 8 section ids unchanged;
   8 FAQ questions verbatim. Removed only by brief: R1 (FB/IG out of title, meta, label,
   summary, h1, lead, service, „Планиране“ bullet), R2 (old sections[2] para 2 dropped, section
   now 3 sentences), R3 (FAQ 6 kept, repointed), R4 (related[0] = /reklama-vav-facebook/).
 2 PASS: changed strings state only canon (specialist plans/runs/tracks, reports with numbers,
   monthly creatives); „към какви търсения да бъдат насочени“ describes Google Ads search
   targeting already explained on the page (ключови думи, S1), no vendor/tool/period added.
 3 PASS | 4 PASS (only „30-минутен“ ×2, canon) | 5 N/A | 6 PASS („Работим по GDPR.“)
 7 PASS (FAQ questions „рекламирам“, „платя“ are the buyer's own 1st-person voice)
 8 PASS (one booking CTA in proces, one in diagnostika; approved wording; no urgency)
 9 PASS: main term „реклама в гугъл“ in title, meta, lead s1, H2 kak-raboti; H1 „Реклама в
   Google с маркетинг специалист“ (Latin script, as baseline). No /reklama-vav-facebook/ term
   in title/meta/H1/H2/label/summary/service/eyebrow; FB/IG appear only in the 3-sentence
   pointer section (H2 „Кампании извън Google“), FAQ 6 (question verbatim + repointed answer)
   and the two anchor texts to /reklama-vav-facebook/. „seo оптимизация“ only inside its own
   page's anchor; „ключови думи“ once as an unchanged jargon explanation (not targeted).
 10 PASS (/seo-optimizacia/, /reklama-vav-facebook/ ×2, /socialni-mrezhi/ ×2, /diagnostika/,
   tokens; related /reklama-vav-facebook/, /seo-optimizacia/, /diagnostika/)
 11 PASS
Facebook/Instagram-as-channel check (brief): PASS. Nothing outside section facebook-instagram
  (3 sentences, pointer + creatives) and FAQ 6 presents FB/IG as a channel of this page.
CRITICAL: none
MODERATE: none
MINOR (no edit): specialist para repeats „поема“ (s1 baseline, s3 baseline + „управлява
  кампаниите в Google Ads“); eyebrow „Google Ads с маркетинг специалист“ is a UI label, fine.
Title 48 chars, meta 157 chars (contains main term).
OWNER ITEMS: G-C1–G-C5 (below)
VOICE NOTES: unchanged owner-approved strings (kak-raboti, za-kogo, otchet, proces, cena,
  diagnostika, FAQ 1–5, 7–8) protected; no edits made.
```

---

## Blocking table

| # | Check | /saveti/ | home cards | /reklama/ |
|---|---|---|---|---|
| 1 | Nothing lost | N/A (new) | PASS | PASS (R1–R4 applied) |
| 2 | Facts allowed list | PASS | PASS | PASS |
| 3 | Banned claims | PASS | PASS | PASS |
| 4 | Numbers | PASS | PASS | PASS |
| 5 | Hypothetical label | N/A | N/A | N/A |
| 6 | GDPR wording | N/A | N/A | PASS |
| 7 | Register „Вие“ | PASS | PASS | PASS |
| 8 | CTA rules | PASS | N/A | PASS |
| 9 | One term per page | PASS | PASS | PASS |
| 10 | Links & anchors | PASS | PASS | PASS |
| 11 | BizGrow voice | PASS (after polish) | PASS | PASS |

## Fixes applied (Phase 2)

1. 05-gate/saveti.json `lead`: „…собственици на малък бизнес: как да използвате…“ → „…собственици на малък бизнес. Статиите показват как да използвате…“ (sentence split; JSON valid; keys, path, link unchanged).
2. 05-gate/home-cards.json, 05-gate/reklama.json: copied unchanged from 04-seo.

## Owner items (for Step 6)

- G-A1. /saveti/ H1 „Съвети за малкия бизнес“ differs from keyword-map h1 „Съвети“ (H1 change → owner confirm).
- G-B1. Three new home cards (Изработка на сайт, Онлайн магазини, Реклама във Facebook и Instagram), the Google-only /reklama/ card and services_title „AI автоматизация, сайтове, съдържание и реклама на едно място“ are new copy for approval. Site card ties „кратък месечен отчет“ to website maintenance (canon process step 4 applied to service 6): confirm.
- G-B2. Both ad cards use icon "chart" (set by the brief); owner may pick a distinct icon.
- G-C1. keyword-map.md row /reklama/ still lists h1 „Реклама в Google и Facebook с маркетинг специалист“; update to the Google-only H1 (not edited here).
- G-C2 (= 04 O1). „google ads специалист“ not used: would imply a platform specialisation the canon does not state.
- G-C3 (= 04 O2). H1 uses Latin „Google“, title/lead/H2 use „Гугъл“; owner may unify.
- G-C4 (= 04 O3). „ключови думи“ in kak-raboti p2 could link to /saveti/klyuchovi-dumi/ once live.
- G-C5. Section id `facebook-instagram` kept (inventory requires unchanged ids) while its heading is now „Кампании извън Google“; renaming the id needs a brief. The removed baseline sentence „…без да Ви е нужен дизайнер на щат“ (owner-approved wording) was dropped under R2; confirm.
