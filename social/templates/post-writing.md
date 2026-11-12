# Writing social posts — {{brand_name}}

How the drafting agent writes the posts of a pack for {{brand_name}} ({{site}}). The brand:
{{topic_about}} Read the source first: the library item (`library/{{brand_key}}/<slug>/article.md`
and `item.json`) or, for a keyword request with no fitting article and for a free topic, the
sources: the brand's own live pages, the pages and texts the request names in `sources`, and our
library articles. Then write one post per active account and save the draft JSON below;
`make_pack.py build` does the rest (IDs, links, images, checks). Never write a post you cannot
back with the source.

A **free topic** (`request_kind: topic`) is a post about the topic in the request's own words.
Gather its facts from the request's `sources` first, then from our library articles that cover
the topic. Its angle and tone come from the request's `angle`.

## What every post is

- **Language:** {{language_name}}, in every field people read (text, image text, alt text).
- **One idea, one angle.** Every post of a pack has a different angle: the key takeaway, a
  question, one number or fact, myth vs fact, a short checklist. No two posts share an opening
  line. A follow-up (posts per article 2 or more) takes another angle again.
- **Faithful to the source.** Every number, price, percentage, date and claim appears exactly as
  in the source, with the same formatting. No new facts. For every sentence that carries a
  number, a quote or a claim, record the exact source sentence under `sources` (copied word for
  word from the article or the recorded page line). Allowed without a source: slide counters
  like `3/6`, numbers inside a name the source uses, and the link.
- **The brand's rules for this topic:**
{{writing_rules}}
- **The compliance line:** {{compliance_rule}}
- **Voice:** follow the brand's `voice_notes` in `settings.md` (and an account's `tone_override`
  where it has one). Emoji: at most 2 where the account says `light`, none where it says `none`
  (LinkedIn: none). No em-dashes (—).

## Per network

| Network | Write | Hashtags | Link |
|---|---|---|---|
| Facebook | 300–700 characters, a hook in the first line | 0–3 | `[[LINK]]` once, on its own line before the compliance line |
| Instagram | hook in the first 125 characters, 600–1,500 in all | 3–5, brand hashtags included | none: end with one line saying the link is in the profile — never a web address |
| X | 280 with the link (the link counts 23, emoji 2) | 1–2 | `[[LINK]]` once |
| LinkedIn Page | 600–1,300, plain and professional, no emoji | 3–5 | `[[LINK]]` once |

`[[LINK]]` is filled with the article's live address and its tags when the post goes out; write
it exactly like that, once. An account set to `Link: none` gets no `[[LINK]]`. For a request with
no page of ours that fits, set `"no_link_reason": "no link: no fitting page"`.

## Image text and the art

- `image_text` is the text set on the image, exactly as people will read it:
  - a **single image**: one line, the image title, at most about 8 words;
  - a **carousel** (Facebook, Instagram, LinkedIn Page) when the work item's `format` (the
    request's, else the account's) is `carousel`, or `auto` and the source has at least 2
    distinct key points. Write exactly N lines, one per slide, N = the work item's `slides` (the
    request's, else the account's; 5 by default): the cover title (the hook), then N−2 points
    (one short sentence each, a number only from the source), then the closing slide: an
    invitation to read the whole article when the post links to one, else a call to save or
    share. When the source truly has fewer points, write fewer lines (never fewer than 3).
- The pictures follow the house style in `../style/style.md`: read it before you write these two.
  - `art_idea`, in English: the post's ONE idea as one concrete, textless scene for the cover (or
    the single image). {{art_rules}}
  - `slide_ideas`, for a carousel only, in English: one scene per point slide, in order (N−2 of
    them), each the picture of that slide's point, small and simple.
- `alt_text`: what the image shows, specifically; no number the source lacks.
- `english`: the post's English reference, for the reviewers only and never published:
  `text` is the post text and `image_text` the image text lines, in the same order. Translate
  faithfully; never summarise, soften or improve. Keep `[[LINK]]` as it is.

## The draft JSON

Save one file per pack and run `python3 scripts/social/make_pack.py build <file> --brand {{brand_key}} --pr-body <file>`.

```json
{
  "brand": "{{brand_key}}",
  "source": {"kind": "article", "item_id": "{{prefix}}-0001"},
  "request_id": null,
  "angle": "the pack's angle in one line",
  "earlier_angles": [],
  "posts": [
    {
      "account_id": "fb-{{brand_key}}",
      "role": "launch",
      "angle": "one number",
      "text": "…\n\n[[LINK]]{{compliance_example}}",
      "hashtags": ["#one", "#two"],
      "image_text": ["The image title"],
      "alt_text": "What the image shows",
      "english": {"text": "…", "image_text": ["The image title"]},
      "art_idea": "one concrete scene, in English",
      "slide_ideas": [],
      "sources": [{"line": "The exact source sentence.", "where": "The section"}]
    }
  ]
}
```

- `source.kind`: `article` (an article, its queue ID), `intro` (a section intro on request), or
  `page` for a keyword request or a free topic, answered from its sources:
  `{"kind": "page", "request_id": "{{prefix}}-req-001", "pages": [{"url": "https://…", "lines": ["…"]}],
  "texts": [{"ref": "sources/<file>.md", "lines": ["…"]}]}` with the exact lines you quote from
  each source. A page or file the request does not name is not a source. Set `"target_page"` on
  each post that links to one of our pages (never to a page that is not ours).
- `request_id`: the request a pack answers.
- `role`: `launch`, `follow-up` or `request`; `earliest`: a request's earliest date, if any.
- `earlier_angles`: for an article's second or later pack, the angles of its earlier packs.
