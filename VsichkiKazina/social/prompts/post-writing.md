# Writing social posts — Всички Казина

How the drafting agent writes the posts of a pack (product spec B1–B9, C3, C4). Read the source
first: the library item (`library/vsichkikazina/<slug>/article.md` and `item.json`) or, for a
keyword request with no fitting article and for a free topic, the sources: the brand's own live
pages, the pages and texts the request names in `sources`, and our library articles. Then write
one post per active account and save the draft JSON below; `make_pack.py build` does the rest
(IDs, links, images, checks). Never write a post you cannot back with the source.

A **free topic** (`request_kind: topic`) is a post about the topic in the request's own words,
e.g. „7 грешки при рулетката“. Gather its facts from the request's `sources` first, then from
our library articles that cover the topic. Its angle and tone come from the request's `angle`.

## What every post is

- **One idea, one angle.** Every post of a pack has a different angle: the key takeaway, a
  question, one number or fact, myth vs fact, a short checklist. No two posts share an opening
  line. A follow-up (posts per article 2 or more) takes another angle again.
- **The only calls to action are to read the guide, or to save or share the post.** No "register", "deposit", "claim", "play
  now", no bonus or offer, no operator name — not in the text, the image text, the hashtags or
  the alt text. Not even a bonus guide's example amounts: talk about how a term works.
- **Faithful to the source (B4).** Every number, price, percentage, date and claim appears
  exactly as in the source, with the same formatting (`€1 000` stays `€1 000`, `~1,06%` stays
  `~1,06%`, `x40` stays `x40`). No new facts. For every sentence that carries a number, a quote
  or a claim, record the exact source sentence under `sources` (copied word for word from the
  article or the recorded page line). Allowed without a source: `18+`, slide counters like
  `3/6`, numbers inside a name the source uses („20 Super Hot“), and the link.
- **The compliance line, word for word,** at the end of every post:
  „18+ Хазартът може да пристрасти. Играйте отговорно.“ On X the short form
  „18+ Играйте отговорно.“ is enough.
- **Voice (B3, B9):** Bulgarian, calm and factual, mostly the polite „вие“. None of the brand
  book's hype words (see `VsichkiKazina/pipeline/agents/brand-gate-vsichkikazina.md`), the
  AI-tell dictionary of `VsichkiKazina/pipeline/agents/humaniser.md`, **no em-dashes (—)**.
  Emoji: at most 2 where the account says `light`, none where it says `none` (LinkedIn: none).

## Per network (B2)

| Network | Write | Hashtags | Link |
|---|---|---|---|
| Facebook | 300–700 characters, a hook in the first line | 0–3 | `[[LINK]]` once, on its own line before the compliance line |
| Instagram | hook in the first 125 characters, 600–1,500 in all | 3–5, brand hashtags included | none: end with „Линкът е в профила ни.“ — never a web address |
| X | 280 with the link (the link counts 23, emoji 2) | 1–2 | `[[LINK]]` once |
| LinkedIn Page | 600–1,300, plain and professional, no emoji | 3–5 | `[[LINK]]` once |

`[[LINK]]` is filled with the article's live address and its tags when the post goes out; write
it exactly like that, once. An account set to `Link: none` gets no `[[LINK]]`. For a keyword
request with no editorial page that fits, set `"no_link_reason": "no link: no fitting page"`.

## Image text and the art

- `image_text` is the text set on the image, exactly as people will read it, in Bulgarian:
  - a **single image**: one line, the image title, at most about 8 words;
  - a **carousel** (Facebook, Instagram, LinkedIn Page) when the work item's `format` (the
    request's, else the account's) is `carousel`, or `auto` and the source has at least 2
    distinct key points. Write exactly N lines, one per slide, N = the work item's `slides` (the
    request's, else the account's; 5 by default): the cover title (the hook: it makes people
    swipe), then N−2 points (one short sentence each, a number only from the source), then the
    closing slide: „Прочетете цялото ръководство“ when the post links to an article, else a call
    to save or share („Запазете поста за по-късно“). The domain and „18+“ are added on it. When
    the source truly has fewer points, write fewer lines (never fewer than 3) rather than pad.
- The pictures follow the house style in `../style/style.md`: read it before you write these two
  (its STYLE block goes to the image model word for word, and the review checks it).
  - `art_idea`, in English: the post's ONE idea as one concrete, textless scene for the cover (or
    the single image), in the guide's words: what the brand's fox does and with which object
    when the fox helps, else the object alone (e.g. "the fox in a lab coat weighs two piles of
    identical gold tokens on a balance scale that tips slightly to one side" for the house edge).
    Never humans, screens, logos, money raining; the fox never plays, bets or celebrates.
  - `slide_ideas`, for a carousel only, in English: one scene per point slide, in order (N−2 of
    them: not the cover, not the closing slide), each the picture of that slide's point, small and
    simple (one object or the fox with one object). With the brand's `art` setting `every slide`
    each point slide gets its picture; without `slide_ideas` the points are text slides.
- `alt_text`, in Bulgarian: what the image shows, specifically; no number the source lacks.
- `english`: the post's English reference, for the reviewers only and never published:
  `text` is the post text and `image_text` the image text lines, in the same order. Translate
  faithfully; never summarise, soften or improve: a reviewer who reads only the English must
  see exactly what the post says, its numbers, its call to action and the compliance line
  included. Keep `[[LINK]]` as it is. Hashtags and alt text are not translated.

## The draft JSON

Save one file per pack and run `python3 scripts/social/make_pack.py build <file> --pr-body <file>`.

```json
{
  "brand": "vsichkikazina",
  "source": {"kind": "article", "item_id": "vk-0300"},
  "request_id": null,
  "angle": "the pack's angle in one line",
  "earlier_angles": [],
  "posts": [
    {
      "account_id": "fb-vsichkikazina",
      "role": "launch",
      "angle": "one number",
      "text": "…\n\nПрочетете цялото ръководство: [[LINK]]\n\n18+ Хазартът може да пристрасти. Играйте отговорно.",
      "hashtags": ["#бакара", "#казиноигри"],
      "image_text": ["Три залога в бакара"],
      "alt_text": "Две карти на везни: изборът между Банко и Пунто",
      "english": {"text": "…\n\nRead the full guide: [[LINK]]\n\n18+ Gambling can be addictive. Play responsibly.",
                  "image_text": ["Three bets in baccarat"]},
      "art_idea": "the fox in a suit points at two playing cards on a balance scale, one side slightly heavier",
      "slide_ideas": [],
      "sources": [{"line": "Банко 1:1 минус 5% комисиона.", "where": "Трите залога"}]
    }
  ]
}
```

- `source.kind`: `article` (an article, its queue ID), `intro` (a section intro on request), or
  `page` for a keyword request or a free topic, answered from its sources:
  `{"kind": "page", "request_id": "vk-req-012", "pages": [{"url": "https://…", "lines": ["…"]}],
  "texts": [{"ref": "sources/2026-10-24-ruletka.md", "lines": ["…"]}, {"ref": "vk-0012", "lines": ["…"]}]}`
  with the exact lines you quote from each source (each is confirmed in its source before it
  counts). `pages`: our live pages, and the web addresses the request names. `texts`: the text
  files the request names (`sources/…`) and our library articles (their queue ID). A page or file
  the request does not name is not a source. Set `"target_page"` on each post that links to one
  of our pages (never to a page that is not ours).
- `request_id`: the request a pack answers, also when it is drafted from an article (A2, A4).
- `role`: `launch`, `follow-up` or `request`; `earliest`: a request's earliest date, if any.
- `earlier_angles`: for an article's second or later pack, the angles of its earlier packs.
