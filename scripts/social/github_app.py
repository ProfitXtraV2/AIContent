"""The publishing check's GitHub identity: the GitHub App px-publishing-check (tech spec, Third-
party services 7). Standard library only, so the guest that holds the keys runs no third-party
package.

The App's private key lives only in the guest (/etc/px-social/, readable by px-social alone).
Each run signs a JWT with it (RS256, valid 9 minutes) and exchanges it for an installation token
(valid one hour). The check uses that token for the GitHub API and to push the ledger to main;
it is never written to disk or printed.

    token, expires_at = installation_token(app_id, installation_id, pem_text)
"""
import base64
import hashlib
import json
import re
import time
import urllib.error
import urllib.request

API = "https://api.github.com"
_SHA256_DIGEST_INFO = bytes.fromhex("3031300d060960864801650304020105000420")
_PEM = re.compile(r"-----BEGIN ([A-Z ]+)-----(.*?)-----END \1-----", re.S)


class AppError(Exception):
    pass


def _der(data, i):
    """(tag, value, next index) of one DER element."""
    tag, length = data[i], data[i + 1]
    i += 2
    if length & 0x80:
        n = length & 0x7F
        length = int.from_bytes(data[i:i + n], "big")
        i += n
    return tag, data[i:i + length], i + length


def _elements(seq):
    out, i = [], 0
    while i < len(seq):
        tag, value, i = _der(seq, i)
        out.append((tag, value))
    return out


def load_key(pem_text):
    """(n, e, d, p, q, dp, dq, qinv) of an RSA private key in PEM (PKCS#1 or PKCS#8)."""
    m = _PEM.search(str(pem_text or ""))
    if not m:
        raise AppError("the App key file holds no PEM block")
    der = base64.b64decode("".join(m.group(2).split()))
    tag, seq, _ = _der(der, 0)
    parts = _elements(seq)
    if len(parts) == 3 and parts[1][0] == 0x30 and parts[2][0] == 0x04:      # PKCS#8 wraps PKCS#1
        tag, seq, _ = _der(parts[2][1], 0)
        parts = _elements(seq)
    ints = [int.from_bytes(v, "big") for t, v in parts if t == 0x02]
    if len(ints) < 9:
        raise AppError("not an RSA private key")
    return tuple(ints[1:9])


def sign_rs256(message, key):
    """RSASSA-PKCS1-v1_5 with SHA-256 (RFC 8017 §8.2), using the CRT values of the key."""
    n, e, d, p, q, dp, dq, qinv = key
    k = (n.bit_length() + 7) // 8
    t = _SHA256_DIGEST_INFO + hashlib.sha256(message).digest()
    if k < len(t) + 11:
        raise AppError("the key is too short for RS256")
    m = int.from_bytes(b"\x00\x01" + b"\xff" * (k - len(t) - 3) + b"\x00" + t, "big")
    s1, s2 = pow(m, dp, p), pow(m, dq, q)
    s = s2 + ((qinv * (s1 - s2)) % p) * q
    return s.to_bytes(k, "big")


def _b64(data):
    return base64.urlsafe_b64encode(data).rstrip(b"=")


def app_jwt(app_id, key, now=None):
    now = int(now if now is not None else time.time())
    header = _b64(json.dumps({"alg": "RS256", "typ": "JWT"}, separators=(",", ":")).encode())
    payload = _b64(json.dumps({"iat": now - 60, "exp": now + 540, "iss": str(app_id)}, separators=(",", ":")).encode())
    signing_input = header + b"." + payload
    return (signing_input + b"." + _b64(sign_rs256(signing_input, key))).decode("ascii")


def installation_token(app_id, installation_id, pem_text, api=API, post=None, now=None):
    """(token, expires_at) for the App's installation on AIContent. `post(url, headers)` is
    injectable for tests."""
    jwt = app_jwt(app_id, load_key(pem_text), now)
    url = f"{api}/app/installations/{int(installation_id)}/access_tokens"
    headers = {"Authorization": f"Bearer {jwt}", "Accept": "application/vnd.github+json",
               "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "px-social"}
    if post is None:
        def post(u, h):
            req = urllib.request.Request(u, data=b"", method="POST", headers=h)
            try:
                with urllib.request.urlopen(req, timeout=30) as resp:
                    return json.loads(resp.read())
            except urllib.error.HTTPError as e:
                raise AppError(f"installation token: HTTP {e.code}") from None
            except (urllib.error.URLError, TimeoutError, OSError) as e:
                raise AppError(f"installation token: {e}") from None
    got = post(url, headers) or {}
    if not got.get("token"):
        raise AppError("installation token: no token in the answer")
    return got["token"], got.get("expires_at")
