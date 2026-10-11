"""Tests for skillforge.validate."""

import os

from skillforge.validate import validate_skill

FIXTURES = os.path.join(os.path.dirname(__file__), "fixtures")
GOOD_SKILL = os.path.join(FIXTURES, "good_skill")


def test_validate_skill_valid_fixture() -> None:
    """A well-formed skill with its referenced files passes with no errors."""
    result = validate_skill(GOOD_SKILL)
    assert result["valid"] is True
    assert result["errors"] == []


def test_validate_skill_missing_skill_md(tmp_path) -> None:
    """A directory without SKILL.md fails validation with a clear error."""
    result = validate_skill(str(tmp_path))
    assert result["valid"] is False
    assert any("SKILL.md not found" in error for error in result["errors"])
