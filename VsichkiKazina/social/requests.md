# Social requests and commands — Всички Казина

Add a row here in GitHub's web editor and commit it straight to `main`, the way the keyword
backlog is edited. Leave `id`, `status`, `reason` and `pack_id` empty: the board workflow
gives each new row its ID within minutes, and the drafting run and the publishing check fill
in the rest.

**Requests** ask for posts (product spec A2, A4):
- `kind`: `keyword` (posts about a keyword), `article` (an older article: its ID or slug),
  `intro` (a section intro: its ID or slug, e.g. `hub-intro-casino-payments`) or `topic` (a free
  topic in your own words, e.g. `7 грешки при рулетката`; its facts come from the `sources` and
  from our articles).
- `target`: the keyword(s), the ID, the slug or the topic. `angle`: optional note (the hook, the
  tone). `format`: optional `carousel` or `single` (empty = the account's). `slides`: optional,
  3–10 slides in a carousel (empty = the account's, 5 by default).
- `sources`: optional, for a keyword or a topic: web addresses and text files under
  `sources/` (e.g. `sources/2026-10-24-ruletka.md`), comma-separated. The post may take facts
  from them; each fact is checked word for word against its source.
- `target_page`: optional page of ours to link to. `accounts`: optional, e.g.
  `fb-vsichkikazina, x-vsichkikazina` (empty = every active account). `earliest`: optional date,
  `YYYY-MM-DD`.

**Commands** change posts that are already approved (F6):
- `fix <post ID>`: the post goes into a fix PR (also brings back a "Failed" post).
- `cancel <post ID>`: cancels a post that is not yet in the publishing tool.
- `not before <post ID> <date>`: moves a post that is not yet in the publishing tool.
- `post now <post ID>`: sends an approved post at once instead of at its slot (every check still
  applies; a post already in the tool is pulled back and sent at once).
- `post at <post ID> <YYYY-MM-DD HH:MM>`: sends it at that day and time (the brand's time zone)
  instead of at its slot, with the same rules.
- `post now` and `post at` also take a pack ID (e.g. `vk-0300-p1`): every post of the pack. Written
  while the pack's PR is still open, the line waits for the merge, so the time is chosen before it.

## Requests

| id | kind | target | angle | format | slides | sources | target_page | accounts | earliest | status | reason | pack_id | added |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Commands

| id | command | post_id | date | status | note |
|---|---|---|---|---|---|
