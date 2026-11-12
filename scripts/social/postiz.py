"""The publishing tool's public API: Postiz, self-hosted (tech spec, Third-party services 1;
flows 4, 6, 7 and 8). Standard library only.

Only the publishing check and the control loop use it, inside the guest. They call Postiz on
the internal Docker network (POSTIZ_API_URL, for example http://postiz:5000/api/public/v1),
never through the tunnel, where Caddy answers /api/public/* with 403. The key (POSTIZ_API_KEY)
goes in the Authorization header with no "Bearer" prefix. Nothing else in the product holds it.

    Postiz(url, key).integrations()            GET    /integrations
                    .upload(name, data)        POST   /upload          (multipart field "file")
                    .create(...)               POST   /posts           (one channel, its own group)
                    .posts(start, end)         GET    /posts?startDate&endDate
                    .delete(post_id)           DELETE /posts/{id}      (deletes the post's whole group)

Every post is created in a group of its own, so a pull-back removes only that post.

FakePostiz has the same methods and keeps everything in memory (tests, --fake-postiz). DryRun
passes reads through and only records writes (DRY_RUN=1: plan and log, create nothing).
"""
import hashlib
import html
import json
import re
import urllib.error
import urllib.parse
import urllib.request
import uuid
from datetime import datetime, timedelta, timezone

# Our network names → the provider identifiers a channel may have in Postiz. The provider
# settings' __type is the channel's own identifier (instagram or instagram-standalone).
PROVIDERS = {"facebook": ("facebook",), "instagram": ("instagram", "instagram-standalone"), "x": ("x",),
             "linkedin-page": ("linkedin-page",), "linkedin-profile": ("linkedin",)}
STATES = ("QUEUE", "PUBLISHED", "ERROR", "DRAFT")


class PostizError(Exception):
    """kind: temporary (unreachable, timeout, 5xx, rate limit) | auth (our key rejected) |
    permanent (the request itself was refused)."""

    def __init__(self, message, kind="temporary", status=None):
        super().__init__(message)
        self.kind, self.status = kind, status


# --- the fixed table for a post's error text (flow 8) --------------------------------------

ERROR_TABLE = [
    ("login", re.compile(r"reconnect|refresh(?:[ _-]?needed|[ _-]token)|access[ _-]?token|session has expired|"
                         r"token (?:has )?expired|expired token|revoked|invalid_grant|re-?authori[sz]|"
                         r"re-?authenticat|\(#190\)|code\W{0,3}190\b|unauthori[sz]ed|\b401\b", re.I)),
    ("temporary", re.compile(r"time[d ]?\s?out|etimedout|econnreset|econnrefused|socket hang up|rate[ _-]?limit|"
                             r"limit reached|too many requests|\b429\b|\b5\d\d\b|internal server error|"
                             r"bad gateway|service unavailable|temporar|try again|overloaded|unavailable", re.I)),
    ("permanent", re.compile(r"permission|not allowed|not permitted|disallowed|forbidden|\b403\b|polic|violat|"
                             r"abusive|spam|duplicate|invalid media|media (?:type|format)|unsupported|too long|"
                             r"too large|aspect ratio|invalid|\b400\b", re.I)),
]


def classify(error_text):
    """temporary | permanent | login, from the error text the network gave (flow 8). Login
    errors are looked for first, then temporary ones; an error the table does not know counts
    as temporary, so it is retried at most twice and then becomes Failed."""
    text = str(error_text or "")
    for kind, rx in ERROR_TABLE:
        if rx.search(text):
            return kind
    return "temporary"


# --- content ----------------------------------------------------------------------------

_TAGS = re.compile(r"<(?:p|br|div|span|strong|em|b|i|u|a|ul|ol|li|h[1-6])\b[^>]*>|</(?:p|div|li|h[1-6]|span|"
                   r"strong|em|b|i|u|a|ul|ol)>", re.I)


def to_content(text, fmt="html"):
    """The post text as Postiz content. html: one <p> per paragraph, <br> for single line
    breaks, entities escaped (the shape the Postiz editor itself stores). text: as it is.
    Which one gives back exactly the text sent is setup check V4."""
    t = str(text or "").replace("\r\n", "\n").replace("\r", "\n").strip()
    if fmt == "text":
        return t
    paragraphs = [p.strip() for p in re.split(r"\n[ \t]*\n", t) if p.strip()]
    return "".join("<p>" + html.escape(p, quote=False).replace("\n", "<br>") + "</p>" for p in paragraphs)


def normalize_content(value):
    """Content as plain text, for comparing what the tool holds with what was approved:
    HTML stripped, entities decoded, line breaks and trailing spaces normalised."""
    t = str(value or "").replace("\r\n", "\n").replace("\r", "\n")
    if _TAGS.search(t):
        t = re.sub(r"[ \t]*<br\s*/?>[ \t]*", "\n", t, flags=re.I)
        t = re.sub(r"</(?:p|div|h[1-6]|li)>\s*<(?:p|div|h[1-6]|li)\b[^>]*>", "\n\n", t, flags=re.I)
        t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(t).replace(" ", " ").replace(" ", " ")
    t = "\n".join(line.rstrip() for line in t.split("\n"))
    return re.sub(r"\n{3,}", "\n\n", t).strip()


def content_hash(value):
    return hashlib.sha256(normalize_content(value).encode("utf-8")).hexdigest()


def provider_settings(network, identifier, carousel_name=None):
    """The provider settings of one post (`settings.__type` is the channel's identifier).
    X needs who_can_reply_post; a LinkedIn Page carousel goes as a document of images."""
    s = {"__type": identifier}
    if network == "x":
        s["who_can_reply_post"] = "everyone"
    elif network == "instagram":
        s.update({"post_type": "post", "collaborators": []})
    elif network == "facebook":
        s["post_type"] = "post"
    if carousel_name and network == "linkedin-page":
        s.update({"post_as_images_carousel": True, "carousel_name": carousel_name[:100]})
    return s


def _iso(dt):
    if isinstance(dt, str):
        return dt
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")


def _post_out(p):
    """A post of GET /posts in the shape the check uses."""
    integ = p.get("integration") or {}
    return {"id": p.get("id"), "group": p.get("group"), "channel_id": integ.get("id") or p.get("integrationId"),
            "provider": integ.get("providerIdentifier") or integ.get("identifier"),
            "content": p.get("content") or "", "date": p.get("publishDate") or p.get("date"),
            "state": str(p.get("state") or "").upper(), "release_url": p.get("releaseURL") or "",
            "error": p.get("error") or ""}


def _channel_out(c):
    return {"id": c.get("id"), "name": c.get("name", ""), "identifier": c.get("identifier") or c.get("providerIdentifier"),
            "disabled": bool(c.get("disabled")),
            # V9 records which flag the pinned version returns for an expired login.
            "needs_reconnect": bool(c.get("refreshNeeded") or c.get("inBetweenSteps") or c.get("needsReconnect")),
            "profile": c.get("profile", ""), "customer": (c.get("customer") or {}).get("id")}


class Postiz:
    def __init__(self, url, key, timeout=30):
        self.url, self.key, self.timeout = url.rstrip("/"), key, timeout

    def _call(self, method, path, body=None, params=None, raw=None, content_type=None):
        url = self.url + path + ("?" + urllib.parse.urlencode(params) if params else "")
        data = raw if raw is not None else (json.dumps(body).encode("utf-8") if body is not None else None)
        headers = {"Authorization": self.key, "Accept": "application/json", "User-Agent": "px-social"}
        if data is not None:
            headers["Content-Type"] = content_type or "application/json"
        req = urllib.request.Request(url, data=data, method=method, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                got = resp.read()
                return json.loads(got) if got else None
        except urllib.error.HTTPError as e:
            detail = ""
            try:
                detail = e.read().decode("utf-8", "replace")[:300]
            except OSError:
                pass
            kind = "auth" if e.code == 401 else "temporary" if e.code == 429 or e.code >= 500 else "permanent"
            raise PostizError(f"{method} {path}: HTTP {e.code} {detail}".strip(), kind, e.code) from None
        except (urllib.error.URLError, TimeoutError, OSError, ValueError) as e:
            raise PostizError(f"{method} {path}: {e}", "temporary") from None

    def integrations(self):
        return [_channel_out(c) for c in self._call("GET", "/integrations") or []]

    def upload(self, filename, data):
        boundary = "pxsocial" + uuid.uuid4().hex
        ctype = "image/png" if filename.lower().endswith(".png") else "image/jpeg"
        body = (f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{filename}\"\r\n"
                f"Content-Type: {ctype}\r\n\r\n").encode("utf-8") + data + f"\r\n--{boundary}--\r\n".encode("utf-8")
        got = self._call("POST", "/upload", raw=body, content_type=f"multipart/form-data; boundary={boundary}") or {}
        if not got.get("id") or not got.get("path"):
            raise PostizError("upload: no id or path in the answer", "permanent")
        return {"id": got["id"], "path": got["path"]}

    def create(self, channel_id, date_utc, content, images, settings, group, post_type="schedule"):
        body = {"type": post_type, "date": _iso(date_utc), "shortLink": False, "tags": [],
                "posts": [{"integration": {"id": channel_id}, "group": group,
                           "value": [{"content": content, "image": list(images)}], "settings": settings}]}
        got = self._call("POST", "/posts", body)
        first = got[0] if isinstance(got, list) and got else got if isinstance(got, dict) else {}
        pid = (first or {}).get("postId") or (first or {}).get("id")
        if not pid:
            raise PostizError("create: no post id in the answer", "permanent")
        return pid

    def posts(self, start_utc, end_utc):
        got = self._call("GET", "/posts", params={"startDate": _iso(start_utc), "endDate": _iso(end_utc)}) or {}
        return [_post_out(p) for p in (got.get("posts") if isinstance(got, dict) else got) or []]

    def delete(self, post_id):
        self._call("DELETE", f"/posts/{urllib.parse.quote(str(post_id))}")


def _parse(ts):
    t = str(ts).replace("Z", "").split(".")[0]
    return datetime.strptime(t[:19], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc)


class FakePostiz:
    """Postiz in memory. `advance(now)` plays the tool's part: due posts on enabled channels
    are published (or fail, as set with `fail_next`); a post deleted before its time is gone."""

    def __init__(self, channels=None):
        self.channels = [dict({"disabled": False, "needs_reconnect": False, "profile": "", "customer": None}, **c)
                         for c in channels or []]
        self.items, self.uploads, self.calls = {}, {}, []
        self.down, self.fail_next, self.publish_delay_min = False, {}, {}
        self._n = 0

    def _id(self, prefix):
        self._n += 1
        return f"{prefix}{self._n:04d}"

    def _check(self, method):
        self.calls.append(method)
        if self.down:
            raise PostizError(f"{method}: connection refused", "temporary")

    def channel(self, channel_id):
        return next((c for c in self.channels if c["id"] == channel_id), None)

    def integrations(self):
        self._check("integrations")
        return [dict(c) for c in self.channels]

    def upload(self, filename, data):
        self._check("upload")
        uid = self._id("up")
        self.uploads[uid] = {"name": filename, "sha256": hashlib.sha256(data).hexdigest()}
        return {"id": uid, "path": f"https://social.example.test/uploads/{uid}-{filename}"}

    def create(self, channel_id, date_utc, content, images, settings, group, post_type="schedule"):
        self._check("create")
        if not self.channel(channel_id):
            raise PostizError(f"create: no channel {channel_id}", "permanent", 400)
        pid = self._id("pz")
        self.items[pid] = {"id": pid, "group": group, "channel_id": channel_id,
                           "provider": self.channel(channel_id)["identifier"], "content": content,
                           "date": _iso(date_utc), "state": "QUEUE", "release_url": "", "error": "",
                           "images": list(images), "settings": dict(settings), "type": post_type}
        return pid

    def posts(self, start_utc, end_utc):
        self._check("posts")
        a, b = _parse(_iso(start_utc)), _parse(_iso(end_utc))
        return [{k: v for k, v in p.items() if k not in ("images", "settings", "type")}
                for p in self.items.values() if a <= _parse(p["date"]) <= b]

    def delete(self, post_id):
        self._check("delete")
        group = (self.items.get(post_id) or {}).get("group")
        for pid in [k for k, v in self.items.items() if k == post_id or (group and v["group"] == group)]:
            del self.items[pid]

    # what happens in the tool between checks
    def advance(self, now):
        if self.down:                                  # the tool is off: nothing goes out
            return
        for p in self.items.values():
            ch = self.channel(p["channel_id"]) or {}
            if p["state"] != "QUEUE" or ch.get("disabled") or ch.get("needs_reconnect"):
                continue
            delay = timedelta(minutes=self.publish_delay_min.get(p["id"], 0))
            if now >= _parse(p["date"]) + delay:
                if p["id"] in self.fail_next:
                    p["state"], p["error"] = "ERROR", self.fail_next.pop(p["id"])
                else:
                    p["state"] = "PUBLISHED"
                    p["release_url"] = f"https://{p['provider']}.example.test/p/{p['id']}"
                    if delay:
                        p["date"] = _iso(_parse(p["date"]) + delay)

    def add_foreign(self, channel_id, content, date_utc):
        """A post someone made in the tool directly."""
        pid = self._id("pz")
        self.items[pid] = {"id": pid, "group": "manual-" + pid, "channel_id": channel_id,
                           "provider": (self.channel(channel_id) or {}).get("identifier"), "content": content,
                           "date": _iso(date_utc), "state": "QUEUE", "release_url": "", "error": ""}
        return pid

    def to_json(self):
        return {"channels": self.channels, "items": self.items, "uploads": self.uploads, "n": self._n}

    @classmethod
    def from_json(cls, data):
        f = cls()
        f.channels, f.items, f.uploads, f._n = data["channels"], data["items"], data["uploads"], data["n"]
        return f


class DryRun:
    """DRY_RUN=1: reads go to the tool, writes are only recorded (the check plans and logs
    hand-overs but creates nothing)."""

    def __init__(self, inner):
        self.inner, self.writes, self._n = inner, [], 0

    def integrations(self):
        return self.inner.integrations()

    def posts(self, start_utc, end_utc):
        return self.inner.posts(start_utc, end_utc)

    def upload(self, filename, data):
        self._n += 1
        self.writes.append({"call": "upload", "file": filename, "bytes": len(data)})
        return {"id": f"dry-up-{self._n}", "path": f"dry-run/{filename}"}

    def create(self, channel_id, date_utc, content, images, settings, group, post_type="schedule"):
        self._n += 1
        self.writes.append({"call": "create", "type": post_type, "channel_id": channel_id, "date": _iso(date_utc), "group": group,
                            "content_sha256": content_hash(content), "images": len(images)})
        return f"dry-{self._n}"

    def delete(self, post_id):
        self.writes.append({"call": "delete", "id": post_id})
