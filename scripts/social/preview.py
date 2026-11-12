#!/usr/bin/env python3
"""How each post of a pack will look on its network: Instagram, Facebook, X or LinkedIn.

    python3 scripts/social/preview.py <pack dir> [--brand vsichkikazina] [--out preview.html]
                                      [--account ig-vsichkikazina=profit.xtra:"ProfitXtra Affiliate Network"]

Writes one self-contained HTML page: the images are inside it, so it opens offline and for a
private repository too. The mockups are drawn by docs/social-preview.js, the same code the
dashboard's review panel uses: the caption folds where the network folds it, hashtags and the
link look like links, carousels can be swiped. It is a close likeness, not a screenshot: each
network renders the final post itself.
"""
import argparse
import base64
import html
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from social import brands, checks, links, pack as packmod, settings as settingsmod  # noqa: E402
from social import postnumbers as numbers  # noqa: E402

RENDERER = brands.ROOT / "docs" / "social-preview.js"


def data_uri(path):
    p = Path(path)
    mime = "image/png" if p.suffix.lower() == ".png" else "image/jpeg"
    return f"data:{mime};base64," + base64.b64encode(p.read_bytes()).decode("ascii")


def account_view(account_id, brand_key, overrides):
    """(handle, display name) of an account: from --account, else from the brand."""
    if account_id in overrides:
        return overrides[account_id]
    handle = account_id.split("-", 1)[1] if "-" in account_id else account_id
    return handle, brands.brand(brand_key)["name"]


def post_views(pack_dir, brand_key="vsichkikazina", root=brands.ROOT, overrides=None):
    """The data the page renders: one entry per post of the pack (deleted posts left out)."""
    pack = packmod.load(pack_dir)
    meta = pack["meta"]
    s = settingsmod.load(brand_key, root)
    out = []
    for post in meta.get("posts", []):
        pid = post["post_id"]
        fields = pack["posts"].get(pid)
        if fields is None:
            continue
        net = post.get("network", "")
        text = packmod.publish_text(fields)
        link = post.get("link") or {}
        address = tagged = None
        if link.get("mode") == "placeholder":
            address = checks.expected_address(meta, post, s.brand, brand_key)
            if address:
                tagged = links.tagged(address, net, link.get("campaign") or "", link.get("content") or pid)
        length = numbers.length(text, net, link_length=len(tagged) if tagged else None)   # as the length check counts
        if tagged:
            text = text.replace(links.LINK, tagged)
        handle, name = account_view(post.get("account_id", ""), brand_key, overrides or {})
        visuals = [Path(pack_dir) / "visuals" / v["file"] for v in post.get("visuals") or []]
        out.append({
            "post_id": pid, "network": net, "account_id": post.get("account_id", ""), "handle": handle, "name": name,
            "format": post.get("format", "single"), "text": text,
            "images": [data_uri(v) for v in visuals if v.exists()],
            "image_text": fields.get("image_text") or [], "alt": fields.get("alt_text", ""),
            "hashtags": fields.get("hashtags") or [], "link": address,
            "link_note": link.get("reason", "") if link.get("mode") != "placeholder" else "",
            "length": length, "limit": brands.NETWORKS.get(net, {}).get("limit"),
        })
    return {"pack_id": meta.get("pack_id"), "brand": brands.brand(brand_key)["name"],
            "source": meta.get("source") or {}, "angle": meta.get("angle", ""), "posts": out}


def render(data, renderer=RENDERER):
    """The page: the template with the renderer and the pack's data inside it."""
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    title = html.escape(f"Preview {data.get('pack_id') or ''}".strip())
    script = Path(renderer).read_text(encoding="utf-8").replace("</script", "<\\/script")
    return TEMPLATE.replace("{{TITLE}}", title).replace("{{RENDERER}}", script).replace("{{DATA}}", payload)


def parse_override(value):
    """'ig-vsichkikazina=profit.xtra:ProfitXtra Affiliate Network' → (account, (handle, name))."""
    account, _, rest = value.partition("=")
    handle, _, name = rest.partition(":")
    return account.strip(), (handle.strip(), name.strip() or handle.strip())


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("pack_dir")
    ap.add_argument("--brand", default="vsichkikazina")
    ap.add_argument("--root", default=str(brands.ROOT))
    ap.add_argument("--out", default="preview.html")
    ap.add_argument("--account", action="append", default=[], help="account_id=handle:Display name")
    a = ap.parse_args(argv)
    overrides = dict(parse_override(v) for v in a.account)
    data = post_views(a.pack_dir, a.brand, Path(a.root), overrides)
    Path(a.out).write_text(render(data), encoding="utf-8")
    print(f"preview of {data['pack_id']}: {len(data['posts'])} post(s) → {a.out}")
    return 0


TEMPLATE = r"""<!doctype html>
<html lang="bg">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{{TITLE}}</title>
<style>
  body { margin: 0; background: #eef1f5; color: #14161a;
         font: 14px/1.4 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
  header { max-width: 1180px; margin: 0 auto; padding: 24px 16px 8px; }
  header h1 { margin: 0 0 4px; font-size: 20px; }
  header p { margin: 2px 0; color: #6b7280; }
  main { max-width: 1180px; margin: 0 auto; padding: 12px 16px 40px; display: flex; flex-wrap: wrap; gap: 28px;
         align-items: flex-start; }
</style>
</head>
<body>
<header>
  <h1 id="title"></h1>
  <p id="sub"></p>
  <p>A close likeness of each network's feed. The networks render the final post themselves, so fonts and
     spacing can differ a little.</p>
</header>
<main id="grid"></main>
<script type="application/json" id="data">{{DATA}}</script>
<script>
{{RENDERER}}
</script>
<script>
const DATA = JSON.parse(document.getElementById('data').textContent);
document.getElementById('title').textContent = `Preview · ${DATA.pack_id} · ${DATA.brand}`;
const src = DATA.source || {};
document.getElementById('sub').textContent = [src.item_id && `${src.item_id} (${src.slug})`, src.request_id,
  DATA.angle && `angle: ${DATA.angle}`].filter(Boolean).join(' · ');
const grid = document.getElementById('grid');
for (const p of DATA.posts) grid.appendChild(SocialPreview.slot(p));
</script>
</body>
</html>
"""


if __name__ == "__main__":
    sys.exit(main())
