"""Post, pack and request IDs (product spec B6, A2).

    vk-0300-p1-fb-1      post: source, pack number, network, number in the pack
    vk-0300-p1           pack
    vk-req-012           request; a request answered without a feed item is the source itself
                         (vk-req-012-p1-ig-1)

An ID is never reused: a new post takes the next number after every number ever given.
"""
import re

from social import brands

NET_CODES = {"fb", "ig", "x", "li"}
SOURCE = r"[a-z]{2}-(?:\d{4}|req-\d{3,})"
POST_ID_RE = re.compile(rf"^(?P<source>{SOURCE})-p(?P<pack>\d+)-(?P<net>fb|ig|x|li)-(?P<k>\d+)$")
PACK_ID_RE = re.compile(rf"^(?P<source>{SOURCE})-p(?P<pack>\d+)$")
REQUEST_ID_RE = re.compile(r"^(?P<prefix>[a-z]{2})-req-(?P<n>\d{3,})$")
ITEM_ID_RE = re.compile(r"^[a-z]{2}-\d{4}$")


def net_code(network):
    return brands.NETWORKS[network]["code"]


def pack_id(source_id, number):
    return f"{source_id}-p{int(number)}"


def post_id(source_id, pack_number, network, k):
    return f"{source_id}-p{int(pack_number)}-{net_code(network)}-{int(k)}"


def parse_post_id(value):
    m = POST_ID_RE.match(str(value or "").strip())
    if not m:
        return None
    return {"source": m["source"], "pack": int(m["pack"]), "net": m["net"], "k": int(m["k"]),
            "pack_id": f"{m['source']}-p{m['pack']}"}


def parse_pack_id(value):
    m = PACK_ID_RE.match(str(value or "").strip())
    return {"source": m["source"], "pack": int(m["pack"])} if m else None


def next_pack_number(source_id, known_pack_ids):
    """The next pack number of a source: one more than any pack it ever had."""
    nums = [p["pack"] for p in map(parse_pack_id, known_pack_ids) if p and p["source"] == source_id]
    return max(nums, default=0) + 1


def next_post_ids(source_id, pack_number, network, count, known_post_ids):
    """`count` new post IDs for one network in a pack, after every number already used there."""
    code = net_code(network)
    used = [p["k"] for p in map(parse_post_id, known_post_ids)
            if p and p["source"] == source_id and p["pack"] == int(pack_number) and p["net"] == code]
    start = max(used, default=0) + 1
    return [post_id(source_id, pack_number, network, start + i) for i in range(count)]


def next_request_id(prefix, known_request_ids):
    nums = [int(m["n"]) for m in (REQUEST_ID_RE.match(i or "") for i in known_request_ids)
            if m and m["prefix"] == prefix]
    return f"{prefix}-req-{max(nums, default=0) + 1:03d}"
