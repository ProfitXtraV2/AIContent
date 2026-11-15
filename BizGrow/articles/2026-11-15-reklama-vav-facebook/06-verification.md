# 06-VERIFICATION: /reklama-vav-facebook/ (bg, new-page, 2026-11-15)

Deliverables:
- `content/reklama-vav-facebook.md` (porting source, TOML front matter, `status = "draft"`)
- `content/reklama-vav-facebook.port.json` (`ContentPage` object, `status: "published"` as instructed by the launching session; strings generated from the content file, so they are identical)

## SOURCES FETCHED

| id | URL | status | method |
|---|---|---|---|
| S1–S3 | https://www.facebook.com/business/ads/pricing | 200 on 2026-11-15 with plain `curl` (a browser user-agent got 400); text read with WebFetch | page title „Facebook and Instagram Ads Pricing & Cost: An Overview | Meta for Business“ |

## RESOLVED-TO-OWNER-ITEMS (claim, URL, quote)

All three [VERIFY] facts are supported. Markers removed, sentences kept unchanged, source added to `[[sources]]`, owner items F1–F3 written.

- **F1 / S1 (`kak-raboti`)**: „Според Meta бюджетът е основният инструмент за контрол на разходите за реклама. Бюджетът може да бъде дневен или общ. Дневният бюджет е средната сума, която се харчи на ден за дадена кампания, а общият е сумата за целия период на кампанията.“
  Quotes: „Your budget is your most valuable cost control tool when creating an ad.“; daily budget: „This is the average amount you're willing to spend on an ad set or campaign per day.“; lifetime budget: „This is the amount you're willing to spend over the entire run of an ad or campaign.“ Supported (the page says „дадена кампания“ where Meta says „ad set or campaign“: a simplification, not a change of meaning).
- **F2 / S2 (`razhodi`, FAQ 1)**: objective plays a large role in cost; cost also depends on ad quality, bidding strategy, performance goal and type of budget.
  Quotes: „Your ad campaign's objective plays a large role in impacting the cost of your ads.“; „Several factors can contribute to your ad campaign's cost. These include:“ „ad specifications (ad quality, bidding strategy, and performance goal)“ „type of budget (daily or lifetime) and objective (e.g. target local audiences, increase sales, etc.).“ Supported.
- **F3 / S3 (`kak-raboti`, FAQ 4)**: „Рекламата може да бъде спряна временно или прекратена по всяко време.“
  Quote: „You can cancel or pause your ad at any time.“ Supported.

## OWNER ITEMS RAISED (10)

1. F1 new fact (budget = cost control; daily vs lifetime), source + quote.
2. F2 new fact (cost factors), source + quotes; folds in gate M2 (Meta terms unglossed) and M4 („минимален бюджет“ light reading).
3. F3 new fact (pause/cancel any time), source + quote.
4. OC1 OPEN: ad budget paid to Meta separate from or included in BizGrow's fee; folds in gate M1 (possible two-cost reading in `razhodi` / FAQ 1).
5. OC2 who decides the ad budget size.
6. OC3 whose ad account / access (Business Manager, Pixel); not on the page.
7. OC4 pricing of ongoing ad management vs canon one-off price + monthly support.
8. OC5a H1 change: keyword-map „Реклама във Facebook и Instagram“ → „Платена реклама във Facebook и Instagram“ (fallback: keyword-map H1).
9. OC5b placements beyond Facebook/Instagram (Messenger, Audience Network).
10. M5 cross-page: /reklama/ keyword-map H1 still names Facebook.

No „ти“ → „Вие“ conversions (new page); no example scenarios kept (I20 n/a).

## REMAINING FOR HUMAN

- No [LINK NEEDED] / [DATA NEEDED] markers existed. Nothing removed from the text.
- Gate M3 (mixed script „фейсбук“ + „Instagram“ in title/meta/lead/H2) was accepted by the gate as an SEO choice; no owner item, noted here only.
- Gate M6 (`vizii` / FAQ 6 slightly generic) left as is.
- `curl` with a browser user-agent returns 400 while plain `curl` returns 200; the policy check was done with plain `curl` + WebFetch text.

## PORTING NOTES

- New page, no existing dictionary keys change; every `dictionary_key` is "". The site renders it from the `ContentPage` object (`site/src/content/types.ts`), so no new `Dictionary` keys are needed.
- The hero has no section entry in the JSON: `h1` + `lead` + `eyebrow` carry it. Section `kakvo-pravim` uses `closing` for the /reklama/ link line under the bullets; `proces` has `paragraphs: []`, `steps` (4) and `closing` with the booking CTA. `cena` holds `{{EMAIL}}` bare and the second booking CTA.
- JSON `status` is "published" per the launching session; the content file stays `status = "draft"` (pipeline rule). Owner items F1–F3 and OC1–OC5 are still open; publishing before OC1/OC5a are decided is the owner's call.
- `/reklama/` (sibling article) still says Facebook in its H1/title; see M5.
- conversion-links.md already lists /reklama-vav-facebook/; no update needed.

## SELF-CHECK (python3.14 tomllib + json, `_tmp/selfcheck.py`)

| check | result |
|---|---|
| TOML parses | PASS |
| title ≤ 60 incl. „ | BizGrow“ (49) | PASS |
| meta_description 120–160 (154) | PASS |
| meta contains primary keyword | PASS |
| JSON meta equals TOML | PASS |
| primary keyword in title | PASS |
| primary keyword in H1 (Latin variant „Facebook“, OC5a) | PASS |
| primary keyword in first 100 words (lead sentence 1) | PASS |
| primary keyword in one H2 (`kak-raboti`, definite form „платената“) | PASS |
| [[sections]] ↔ body ids and headings, same order | PASS |
| JSON section ids equal body ids (minus hero) | PASS |
| zero em-dashes (md + JSON) | PASS |
| zero bracketed markers | PASS |
| zero „ти“ forms („защото те зависят“ = 3rd-person „they“, reviewed) | PASS |
| zero „доклад“ | PASS |
| zero delivery periods (48 часа, седмиц, за дни) | PASS |
| zero banned words (§2) | PASS |
| zero PRICE / OFFER / TESTIMONIAL | PASS |
| numbers: only canon „30“ (минутен разговор) | PASS |
| every link in conversion-links.md (#cena own anchor) | PASS |
| related = 3 allowed paths, not / nor self | PASS |
| {{BOOKING_URL}} ×2, {{EMAIL}} ×1 | PASS |
| max one booking CTA per section | PASS |
| no hard-coded email / URL in body | PASS |
| inventory I1–I19 present (I20 n/a) | PASS |
| no statement on budget separate/included | PASS |
| JSON strings exact vs content file | PASS |
| JSON required ContentPage keys | PASS |
| decision / checked fields empty | PASS |

**29/29 PASS.**

Counts: body words (sections only, excl. hero lead and FAQ) 479; lead 37; FAQ 249 (8 Q&A).

new facts: 3
owner items added: 10
