"""Every brand registered in the Gemini scripts has a prompt file with a verbatim PROMPT block."""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import gemini_check as gc
import gemini_image_review as gir

BRANDS = ["vsichkikazina", "dentalvia", "elledental"]


@pytest.mark.parametrize("module", [gc, gir], ids=["gemini_check", "gemini_image_review"])
@pytest.mark.parametrize("brand", BRANDS)
def test_brand_prompt_file_exists_and_has_verbatim_block(module, brand):
    assert brand in module.BRAND_PROMPTS
    path = module.prompt_file(brand)
    assert path.exists(), path
    text = path.read_text(encoding="utf-8")
    assert "## PROMPT (verbatim" in text
    assert "## Accept / iterate" in text


def test_elledental_text_prompt_is_bulgarian_clinic():
    prompt = gc._prompt("elledental")
    assert "ELLE Dental" in prompt and "Bulgarian" in prompt
    assert "{{URGENT_CARE}}" in prompt          # the urgent-care block is untouchable
    assert "## Accept / iterate" not in prompt   # policy section is not sent to Gemini


def test_elledental_image_prompt_extracted():
    prompt = gir._prompt("elledental")
    assert "ELLE Dental" in prompt
    assert "## Accept / iterate" not in prompt


@pytest.mark.parametrize("module", [gc, gir], ids=["gemini_check", "gemini_image_review"])
def test_unknown_brand_exits(module):
    with pytest.raises(SystemExit):
        module.prompt_file("nobrand")
