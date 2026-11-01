"""The post preview page (scripts/social/preview.py)."""
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from social import preview  # noqa: E402
from social_fixtures import edit_post, make_pack  # noqa: E402


def data_of(page):
    return json.loads(re.search(r'<script type="application/json" id="data">(.*?)</script>', page, re.S).group(1))


def test_preview_page(tmp_path):
    root, d = make_pack(tmp_path)
    edit_post(d, "vk-0001-p1-fb-1", text="Опит </script><b>x</b> [[LINK]]\n\n18+ Хазартът може да пристрасти. Играйте отговорно.")
    page = preview.render(preview.post_views(d, "vsichkikazina", root, {"ig-vsichkikazina": ("profit.xtra", "ProfitXtra")}))
    assert '<meta name="robots" content="noindex, nofollow">' in page
    assert "</script><b>" not in page                       # post text can never close the data block
    data = data_of(page)
    posts = {p["post_id"]: p for p in data["posts"]}
    fb, ig, x = posts["vk-0001-p1-fb-1"], posts["vk-0001-p1-ig-1"], posts["vk-0001-p1-x-1"]
    assert fb["text"].startswith("Опит </script><b>x</b> https://vsichkikazina.bg/blog/bakara-pravila/?utm_source=facebook")
    assert "[[LINK]]" not in fb["text"] and fb["link"] == "https://vsichkikazina.bg/blog/bakara-pravila/"
    assert ig["handle"] == "profit.xtra" and ig["link"] is None and ig["link_note"] == "link in profile"
    assert len(ig["images"]) == 4 and ig["format"] == "carousel" and ig["images"][0].startswith("data:image/jpeg;base64,")
    assert "const SocialPreview" in page                             # the dashboard's own renderer, inlined
    assert x["length"] <= 280 and x["limit"] == 280                 # X counts the link as 23
    assert data["pack_id"] == "vk-0001-p1" and data["brand"] == "Всички Казина"


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_preview_script_parses(tmp_path):
    root, d = make_pack(tmp_path)
    page = preview.render(preview.post_views(d, "vsichkikazina", root))
    js = tmp_path / "page.js"
    js.write_text("\n;\n".join(re.findall(r"<script>(.*?)</script>", page, re.S)), encoding="utf-8")
    assert subprocess.run(["node", "--check", str(js)], capture_output=True).returncode == 0
