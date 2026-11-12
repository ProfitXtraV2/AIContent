"""Hand-over of one post to the publishing tool (product spec F5, B7, I2; tech spec flow 6).

At the first check inside the post's window (3 hours to 30 minutes before its slot):
  1. the post is still allowed: approved by a merge of someone of the team, every check passes on the
     approved text, the brand is not paused, the channel is connected and enabled, the article
     is not un-approved, its version still matches, and the page is live;
  2. its files on main equal the files at the approving merge, else "Needs fix: text differs
     from approved";
  3. the live link is filled in (posts with a link): an allowed address that answers 200, else
     "Held: no live link";
  4. the live page shows every number and quoted phrase of the post, else "Held: live page
     differs" with the missing lines;
  5. the payload is the approved text with exactly one substitution, [[LINK]] → the tagged
     live address, and this is asserted;
  6. the approved visuals are uploaded and the post is created: one channel per call, type
     schedule, shortLink false, its own group;
  7. an intent row is written before the create and the Postiz post ID after it, so a crash
     never hands a post over twice;
  8. the audit gets the approved text, the payload and every check result.
"""
import hashlib
import json
from datetime import timedelta
from pathlib import Path

from social import checks, github, links, liveness, pack as packmod, pagetext, postiz


class AssertionFailed(Exception):
    pass


def _soon(now):
    """The ISO time two minutes from now: a post's own time before it is sent at once."""
    return (now + timedelta(minutes=2)).strftime("%Y-%m-%dT%H:%M:%SZ")


def _canonical(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def approval_hash(pack_dir, entry):
    """sha256 of what was approved for one post: its .md, its visuals and its own entry in
    pack.json (link mode, tags, sources, visuals list). Stored at merge (boundary 3)."""
    h = hashlib.sha256()
    h.update(packmod.post_files_hash(pack_dir, entry["post_id"], entry.get("visuals")).encode())
    h.update(b"\0" + _canonical(entry).encode("utf-8"))
    return h.hexdigest()


def payload_text(approved_text, address, network, link):
    """(text sent, tagged address or None). Exactly one substitution, asserted (flow 6 step 5)."""
    if link.get("mode") != "placeholder":
        if links.LINK in approved_text:
            raise AssertionFailed("the approved text holds [[LINK]] but the post has no link")
        return approved_text, None
    if approved_text.count(links.LINK) != 1:
        raise AssertionFailed("the approved text must hold [[LINK]] exactly once")
    tagged = links.tagged(address, network, link.get("campaign") or "", link.get("content") or "")
    text = approved_text.replace(links.LINK, tagged)
    if text.replace(tagged, links.LINK, 1) != approved_text or text.count(tagged) != 1:
        raise AssertionFailed("the payload differs from the approved text by more than the link")
    return text, tagged


def _results(result, post_id):
    return [r for r in result["posts"].get(post_id, [])]


def hand_over(run, rec):
    """Hand one planned post over. Returns the outcome: scheduled | needs_fix | held | planned
    (kept for the next check, for example when the tool could not be reached)."""
    pid = rec["post_id"]
    slot = rec["planned_slot_utc"]
    pack_dir = Path(run.root) / run.rel_social / "packs" / rec["pack_id"]
    audit = {"slot_utc": slot, "checks": []}

    # 2. the files on main equal the approved files
    try:
        pack = packmod.load(pack_dir)
        entry = packmod.post_meta(pack, pid)
    except (OSError, ValueError):
        pack, entry = None, None
    now_hash = approval_hash(pack_dir, entry) if entry and pid in pack["posts"] else None
    if now_hash != (rec.get("approval") or {}).get("approved_files_sha256"):
        run.set_state(rec, "needs_fix", "needs_fix:text_differs_from_approved", event="hand-over stopped",
                      detail="the post's files on main differ from the files at the approving merge")
        return "needs_fix"

    # 1. still allowed: a merge by someone who still has write access, and every check on the approved text
    try:
        allowed = run.team.has(rec["approval"].get("merged_by"))
    except github.GitHubError:
        run.github_ok = False
        run.audit(rec, "hand-over waits", why="GitHub could not be reached")
        return "planned"
    if not allowed:
        run.set_state(rec, "needs_fix", "needs_fix:merged_by_other", event="hand-over stopped")
        return "needs_fix"
    if pack["meta"].get("source", {}).get("article_version") and rec.get("matched_version"):
        pack["meta"]["source"]["article_version"] = rec["matched_version"]
    result = checks.run(pack, run.check_ctx(pack))
    own = _results(result, pid)
    audit["checks"] = own
    failing = [r["check"] for r in own if not r["ok"]]
    if failing or not own:
        run.set_state(rec, "needs_fix", "needs_fix:check_failed", event="hand-over stopped",
                      detail=", ".join(failing) or "no check result", checks=own)
        return "needs_fix"
    account = run.settings.account(rec["account_id"])
    channel = run.channels.get((account or {}).get("postiz_channel_id"))
    if not channel or channel.get("disabled") or channel.get("needs_reconnect"):
        run.set_state(rec, "held", "held:reconnect_account" if channel and channel.get("needs_reconnect")
                      else "held:channel_disabled", event="hand-over stopped")
        return "held"

    # 3. the live link
    link = entry.get("link") or {}
    address = None
    if link.get("mode") == "placeholder":
        address = run.link_address(rec, entry)
        ok, why = (links.allowed(address, run.brand_key, run.settings.brand, run.ops)
                   if address else (False, "no address"))
        got = run.site.fetch(address) if ok else None
        if not ok or not got["ok"]:
            why = why or (got or {}).get("error") or "does not answer"
            run.set_state(rec, "held", "held:no_live_link", event="hand-over stopped", detail=f"{address}: {why}")
            return "held"
        audit["link"] = {"address": address, "status": got["status"], "final": got["url"]}

    # 4. the live page
    missing, pages = run.live_page_missing(rec, pack["posts"][pid])
    audit["live_page"] = {"pages": pages, "missing": missing}
    if missing:
        run.set_state(rec, "held", "held:live_page_differs", event="hand-over stopped", missing_lines=missing)
        return "held"

    # 5. the payload: the approved text with the link filled in, nothing else
    approved = rec["approved"]["text"]
    try:
        text, tagged = payload_text(approved, address, rec["network"], link)
    except AssertionFailed as e:
        run.set_state(rec, "needs_fix", "needs_fix:text_differs_from_approved", event="hand-over stopped", detail=str(e))
        return "needs_fix"
    visuals = [pack_dir / "visuals" / v["file"] for v in entry.get("visuals") or []]
    if not visuals or not all(f.exists() for f in visuals):
        run.set_state(rec, "held", "held:no_visual", event="hand-over stopped")
        return "held"
    content = postiz.to_content(text, run.env.content_format)
    carousel = rec.get("format") == "carousel" and rec["network"] == "linkedin-page"
    settings = postiz.provider_settings(rec["network"], channel["identifier"],
                                        (pack["posts"][pid].get("image_text") or [rec.get("title") or pid])[0]
                                        if carousel else None)
    attempt = len(rec.get("handover_history") or []) + 1
    group = f"px-{pid}-{attempt}"

    # 7. the intent, before anything is created
    rec["handover"] = {"intent_utc": run.iso, "slot_utc": slot, "channel_id": channel["id"], "postiz_group": group,
                       "content_hash": postiz.content_hash(content),
                       "payload_hash": hashlib.sha256(text.encode("utf-8")).hexdigest(),
                       "postiz_post_id": None, "dry_run": bool(run.env.dry_run)}
    run.db.save(rec)
    run.db.commit()

    # 6. upload and create
    try:
        images = [run.env.postiz.upload(f.name, f.read_bytes()) for f in visuals]
    except postiz.PostizError as e:
        rec["handover"] = None
        run.audit(rec, "hand-over failed", detail=f"upload: {e}", kind=e.kind)
        run.db.save(rec)
        return "planned"
    # at once: a post now, or a post whose own time is (almost) here
    now = bool(rec.get("post_now")) or (bool(rec.get("at_utc")) and (slot or "") <= _soon(run.now))
    try:
        post_id = run.env.postiz.create(channel["id"], run.iso if now else slot, content, images, settings, group,
                                        "now" if now else "schedule")
    except postiz.PostizError as e:
        if e.kind != "temporary":
            rec["handover"] = None                    # refused: nothing was created
        run.audit(rec, "hand-over failed", detail=f"create: {e}", kind=e.kind)
        run.db.save(rec)
        return "planned"
    rec["handover"].update({"postiz_post_id": post_id, "utc": run.iso})
    run.set_state(rec, "scheduled", "", event="handed over" + (" (dry run: nothing was sent)" if run.env.dry_run else ""),
                  approved_text=approved, payload_text=text, link_tagged=tagged,
                  payload={"type": "now" if now else "schedule", "date": run.iso if now else slot,
                           "shortLink": False, "channel_id": channel["id"],
                           "group": group, "settings": settings, "images": [i["id"] for i in images]},
                  **audit)
    run.db.commit()
    return "scheduled"


def page_texts(site, urls):
    """(visible texts, unreachable urls) of the pages a post draws on."""
    texts, down = [], []
    for url in urls:
        got = site.fetch(url)
        if got["ok"]:
            texts.append(pagetext.visible_text(got["text"]))
        else:
            down.append(url)
    return texts, down


def live_missing(site, urls, fields, names):
    """What the live pages do not show (flow 6 step 4); an unreachable page counts as differing."""
    texts, down = page_texts(site, urls)
    missing = [f"page did not answer: {u}" for u in down]
    if texts:
        missing += liveness.missing_on_pages(fields, texts, names)
    return missing
