import base64
import hashlib
import json
import random
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from social import github_app, ledger as ledgermod, postiz  # noqa: E402


# --- Postiz: error table, content, provider settings ---------------------------------------

def test_error_table():
    assert postiz.classify("Error validating access token: Session has expired on Tuesday") == "login"
    assert postiz.classify("(#190) The user has not authorized application") == "login"
    assert postiz.classify("REVOKED_ACCESS_TOKEN") == "login"
    assert postiz.classify("Request timed out") == "temporary"
    assert postiz.classify("HTTP 503 Service Unavailable") == "temporary"
    assert postiz.classify("(#4) Application request limit reached") == "temporary"
    assert postiz.classify("(#200) Requires pages_manage_posts permission") == "permanent"
    assert postiz.classify("You are not allowed to create a Tweet with duplicate content.") == "permanent"
    assert postiz.classify("The aspect ratio is not supported") == "permanent"
    assert postiz.classify("something nobody has seen") == "temporary"      # retried at most twice


def test_content_round_trip():
    text = "Ред едно & „кавички“ <важно>.\n\nВтори абзац\nс нов ред.\n\n#рулетка #казино"
    for fmt in ("html", "text"):
        assert postiz.normalize_content(postiz.to_content(text, fmt)) == text
    assert postiz.to_content(text) == ("<p>Ред едно &amp; „кавички“ &lt;важно&gt;.</p><p>Втори абзац<br>с нов ред.</p>"
                                       "<p>#рулетка #казино</p>")
    # what the editor of the tool may give back: same text, other markup
    assert postiz.normalize_content("<p>Ред едно &amp; „кавички“ &lt;важно&gt;.</p>\n<p>Втори абзац<br/>с нов ред.</p>"
                                    "<p>#рулетка&nbsp;#казино</p>") == text
    assert postiz.content_hash("<p>a</p>") == postiz.content_hash("a")


def test_provider_settings():
    assert postiz.provider_settings("x", "x") == {"__type": "x", "who_can_reply_post": "everyone"}
    assert postiz.provider_settings("instagram", "instagram-standalone")["__type"] == "instagram-standalone"
    assert postiz.provider_settings("linkedin-page", "linkedin-page", "Бакара накратко") == {
        "__type": "linkedin-page", "post_as_images_carousel": True, "carousel_name": "Бакара накратко"}
    assert postiz.provider_settings("linkedin-profile", "linkedin") == {"__type": "linkedin"}


def test_client_requests(monkeypatch):
    """The key goes in Authorization with no Bearer prefix; one channel per post, type schedule,
    shortLink false, its own group; the list answer is mapped to the check's shape."""
    sent = []

    class Resp:
        def __init__(self, body):
            self.body = body

        def read(self):
            return json.dumps(self.body).encode()

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

    def fake_urlopen(req, timeout=30):
        sent.append(req)
        if req.full_url.endswith("/posts") and req.get_method() == "POST":
            return Resp([{"postId": "p-1", "integration": "ch-x"}])
        if "/posts?" in req.full_url:
            return Resp({"posts": [{"id": "p-1", "content": "<p>a</p>", "publishDate": "2026-11-04T10:30:00.000Z",
                                    "releaseURL": "https://x.com/i/1", "state": "PUBLISHED",
                                    "integration": {"id": "ch-x", "providerIdentifier": "x"}}]})
        if req.full_url.endswith("/integrations"):
            return Resp([{"id": "ch-x", "name": "@vk", "identifier": "x", "disabled": False, "refreshNeeded": True}])
        return Resp({"id": "up-1", "path": "https://social.example/uploads/a.jpg"})

    monkeypatch.setattr(urllib.request, "urlopen", fake_urlopen)
    c = postiz.Postiz("http://postiz:5000/api/public/v1", "secret-key")
    assert c.create("ch-x", "2026-11-04T10:30:00Z", "<p>a</p>", [{"id": "up-1", "path": "u"}],
                    {"__type": "x", "who_can_reply_post": "everyone"}, "px-vk-0300-p1-x-1-1") == "p-1"
    req = sent[-1]
    assert req.get_header("Authorization") == "secret-key"
    body = json.loads(req.data)
    assert body["type"] == "schedule" and body["shortLink"] is False and body["date"] == "2026-11-04T10:30:00Z"
    assert len(body["posts"]) == 1 and body["posts"][0]["group"] == "px-vk-0300-p1-x-1-1"
    assert body["posts"][0]["integration"] == {"id": "ch-x"} and body["posts"][0]["value"][0]["image"][0]["id"] == "up-1"
    assert c.posts("2026-11-02T00:00:00Z", "2026-11-05T00:00:00Z") == [{
        "id": "p-1", "group": None, "channel_id": "ch-x", "provider": "x", "content": "<p>a</p>",
        "date": "2026-11-04T10:30:00.000Z", "state": "PUBLISHED", "release_url": "https://x.com/i/1", "error": ""}]
    assert "startDate=2026-11-02T00%3A00%3A00Z" in sent[-1].full_url
    assert c.integrations()[0]["needs_reconnect"] is True
    up = c.upload("vk-0300-p1-x-1-1.jpg", b"\xff\xd8jpeg")
    assert up == {"id": "up-1", "path": "https://social.example/uploads/a.jpg"}
    assert sent[-1].get_header("Content-type").startswith("multipart/form-data; boundary=")
    assert b'name="file"; filename="vk-0300-p1-x-1-1.jpg"' in sent[-1].data


def test_fake_and_dry_run():
    f = postiz.FakePostiz([{"id": "ch-fb", "identifier": "facebook"}])
    a = f.create("ch-fb", "2026-11-04T10:30:00Z", "a", [], {}, "g-1")
    b = f.create("ch-fb", "2026-11-04T17:30:00Z", "b", [], {}, "g-2")
    f.delete(a)                                          # deletes its group only: one post per group
    assert list(f.items) == [b]
    d = postiz.DryRun(f)
    assert d.create("ch-fb", "2026-11-05T10:30:00Z", "c", [], {}, "g-3").startswith("dry-")
    d.delete(b)
    assert list(f.items) == [b] and [w["call"] for w in d.writes] == ["create", "delete"]


# --- GitHub App: RS256 with the standard library ----------------------------------------------

def _prime(bits, rng):
    while True:
        n = rng.getrandbits(bits) | (1 << (bits - 1)) | 1
        if all(n % p for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)) and _probable_prime(n, rng):
            return n


def _probable_prime(n, rng, rounds=20):
    d, s = n - 1, 0
    while d % 2 == 0:
        d, s = d // 2, s + 1
    for _ in range(rounds):
        x = pow(rng.randrange(2, n - 2), d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def _der_int(v):
    b = v.to_bytes((v.bit_length() + 8) // 8, "big")
    return b"\x02" + _der_len(len(b)) + b


def _der_len(n):
    return bytes([n]) if n < 128 else bytes([0x80 | ((n.bit_length() + 7) // 8)]) + n.to_bytes((n.bit_length() + 7) // 8, "big")


def _test_key():
    """A throwaway 1024-bit RSA key, made here (no key is kept in the repository)."""
    rng = random.Random(20261019)
    e = 65537
    while True:
        p, q = _prime(512, rng), _prime(512, rng)
        phi = (p - 1) * (q - 1)
        if p != q and phi % e:
            break
    n, d = p * q, pow(e, -1, phi)
    ints = [0, n, e, d, p, q, d % (p - 1), d % (q - 1), pow(q, -1, p)]
    body = b"".join(_der_int(i) for i in ints)
    der = b"\x30" + _der_len(len(body)) + body
    b64 = base64.b64encode(der).decode()
    label = "RSA " + "PRIVATE" + " KEY"                    # built here, so this file holds no key header
    pem = f"-----BEGIN {label}-----\n" + "\n".join(b64[i:i + 64] for i in range(0, len(b64), 64)) + f"\n-----END {label}-----\n"
    return pem, n, e


def test_app_jwt_and_token():
    pem, n, e = _test_key()
    key = github_app.load_key(pem)
    assert key[0] == n and key[1] == e
    token = github_app.app_jwt(12345, key, now=1_800_000_000)
    head, payload, sig = token.split(".")
    pad = lambda s: s + "=" * (-len(s) % 4)  # noqa: E731
    assert json.loads(base64.urlsafe_b64decode(pad(head))) == {"alg": "RS256", "typ": "JWT"}
    assert json.loads(base64.urlsafe_b64decode(pad(payload))) == {"iat": 1_799_999_940, "exp": 1_800_000_540, "iss": "12345"}
    # the signature verifies with the public key: s^e mod n is the PKCS#1 v1.5 encoding of the hash
    s = int.from_bytes(base64.urlsafe_b64decode(pad(sig)), "big")
    em = pow(s, e, n).to_bytes(128, "big")
    digest = hashlib.sha256(f"{head}.{payload}".encode()).digest()
    assert em == b"\x00\x01" + b"\xff" * (128 - 3 - 19 - 32) + b"\x00" + bytes.fromhex("3031300d060960864801650304020105000420") + digest
    try:
        from cryptography.hazmat.primitives import hashes, serialization
        from cryptography.hazmat.primitives.asymmetric import padding
    except ImportError:
        pass
    else:
        pub = serialization.load_pem_private_key(pem.encode(), password=None).public_key()
        pub.verify(base64.urlsafe_b64decode(pad(sig)), f"{head}.{payload}".encode(), padding.PKCS1v15(), hashes.SHA256())
    calls = []
    got = github_app.installation_token(12345, 678, pem, post=lambda url, headers: calls.append((url, headers)) or
                                        {"token": "ghs_x", "expires_at": "2026-11-04T11:00:00Z"})
    assert got == ("ghs_x", "2026-11-04T11:00:00Z")
    assert calls[0][0] == "https://api.github.com/app/installations/678/access_tokens"
    assert calls[0][1]["Authorization"].startswith("Bearer ey")


# --- ledger export --------------------------------------------------------------------------------

def test_ledger_export(tmp_path):
    db = ledgermod.Ledger(":memory:")
    rec = {"post_id": "vk-0300-p1-fb-1", "brand": "vsichkikazina", "pack_id": "vk-0300-p1", "state": "scheduled",
           "approved": {"text": "long approved text"}, "handover": {"utc": "t", "postiz_post_id": "pz1", "content_hash": "h",
                                                                   "intent_utc": "t", "channel_id": "ch-fb"},
           "approval": {"pr": 301, "merged_by": "AmigoNiko", "merge_sha": "m", "merged_at": "t", "approved_files_sha256": "x"}}
    db.save(rec)
    db.audit("2026-11-04T08:10:00Z", "vsichkikazina", rec["post_id"], "handed over", payload_text="a")
    db.audit("2026-12-01T08:10:00Z", "vsichkikazina", rec["post_id"], "published")
    written, last = ledgermod.export(db, "vsichkikazina", tmp_path, "2026-12-01T08:10:00Z", [], {})
    data = json.loads((tmp_path / "ledger.json").read_text(encoding="utf-8"))
    post = data["posts"][0]
    assert "approved" not in post and post["handover"] == {"utc": "t", "postiz_post_id": "pz1"}
    assert post["approval"]["merged_by"] == "AmigoNiko" and data["last_check_utc"] == "2026-12-01T08:10:00Z"
    assert sorted(p.name for p in (tmp_path / "audit").iterdir()) == ["2026-11.jsonl", "2026-12.jsonl"]
    assert last == 2
    db.set("audit_exported:vsichkikazina", last)
    db.audit("2026-12-01T09:10:00Z", "vsichkikazina", rec["post_id"], "x")
    ledgermod.export(db, "vsichkikazina", tmp_path, "2026-12-01T09:10:00Z", [], {})
    lines = (tmp_path / "audit" / "2026-12.jsonl").read_text(encoding="utf-8").splitlines()
    assert [json.loads(x)["event"] for x in lines] == ["published", "x"]     # appended, nothing twice
