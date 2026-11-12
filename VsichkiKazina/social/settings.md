# Social settings — Всички Казина

Brand and account settings for social posts (product spec D1–D4). Read by the drafting run,
the PR checks and the publishing check (`scripts/social/settings.py`).

**Change them in the dashboard's Settings tab** (or with a PR). A change counts once someone with
write access to this repository merges its PR; the person who made it may merge it. A change that
reaches `main` any other way is ignored: the last approved settings stay in force and the
dashboard warns "settings changed without approval". No passwords or keys ever go in this file.

- `social` can be switched `on` only after the identities are verified (`identities_verified`).
- An account can be `active` only after its visible test post (`test_post_seen`: date, who saw
  it, how) and, for Instagram, once its profile link is set (`profile_link_set`).
- Slots are local times in `time_zone`: `daily 12:30, 19:30`, `mon-fri 10:00, 18:30`,
  `mon,wed,fri 09:00`, several rules separated by `;`.
- `format`: `carousel` (a cover, one slide per point, a closing slide; Facebook, Instagram and
  LinkedIn Page), `single` (one image) or `auto` (a carousel when the article has the points for
  one). `slides`: how many slides a carousel has, 3–10 (default 5). A request can set both for
  its own posts.
- `art`: `every slide` (a carousel's point slides get their own picture too, in the house
  style of `style/style.md`) or `cover` (only the cover is drawn; the points are text slides,
  cheaper). Every picture counts against `image_budget_usd`.
- Word lists are comma-separated and used by the advertising check (B5).

## Brand

| key | value |
|---|---|
| social | off |
| pause | off |
| time_zone | Europe/Sofia |
| language | bg |
| voice_notes | Спокойно и фактологично, предимно учтиво „вие“; без хайп думите от брандбука; без тирета (—). |
| compliance_long | 18+ Хазартът може да пристрасти. Играйте отговорно. |
| compliance_short | 18+ Играйте отговорно. |
| eligible_types | guide, comparison, review, news |
| allowed_link_areas | /blog/ |
| operator_names_manual |  |
| address_pattern | https://vsichkikazina.bg/blog/{slug}/ |
| brand_hashtags |  |
| image_budget_usd | 60 |
| art | every slide |
| packs_per_run | 5 |
| analytics_source | ahrefs |
| identities_verified |  |
| offer_words | бонус, бонуса, бонуси, бонусът, бонусите, оферта, оферти, промоция, промоции, промо код, бонус код, кешбек, cashback, free spins, фрий спинове, безплатни завъртания, безплатни спинове, джакпот оферта, welcome bonus |
| register_words | регистрирай се, регистрирайте се, регистрирай се сега, направи депозит, направете депозит, депозирай, депозирайте, вземи бонуса, вземете бонуса, вземи своя бонус, играй сега, играйте сега, sign up, register now, deposit now, claim now |
| allowed_number_names | 20 Super Hot, 40 Super Hot, Gates of Olympus 1000, 5 Dazzling Hot, 100 Super Hot |

## Accounts

| account_id | network | postiz_channel_id | active | posts_per_article | followup_delay_days | format | slides | max_hashtags | link | slots | max_per_day | emoji | tone_override | test_post_seen | profile_link_set |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| fb-vsichkikazina | facebook |  | off | 1 | 14 | carousel | 5 | 3 | in post | daily 12:30, 19:30 | 2 | light |  |  |  |
| ig-vsichkikazina | instagram |  | off | 1 | 14 | carousel | 5 | 5 | profile | daily 12:30, 19:30 | 2 | light |  |  |  |
| x-vsichkikazina | x |  | off | 1 | 14 | single |  | 2 | in post | daily 12:30, 19:30 | 2 | light |  |  |  |
| li-vsichkikazina | linkedin-page |  | off | 1 | 14 | auto | 5 | 5 | in post | daily 12:30, 19:30 | 2 | none |  |  |  |
