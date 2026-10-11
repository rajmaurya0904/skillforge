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


def test_validate_skill_invalid_yaml(tmp_path) -> None:
    """Malformed frontmatter (a key line with no colon) fails validation."""
    (tmp_path / "SKILL.md").write_text(
        "---\nname: broken-skill\ndescription\n---\n# Broken\n",
        encoding="utf-8",
    )
    result = validate_skill(str(tmp_path))
    assert result["valid"] is False
    assert "Missing 'description' in frontmatter" in result["errors"]


def test_validate_skill_missing_referenced_file(tmp_path) -> None:
    """A file listed in 'files' that does not exist fails validation."""
    (tmp_path / "SKILL.md").write_text(
        "---\nname: ref-skill\ndescription: Refers to a missing file.\n"
        "files: nope.md\n---\n# Ref\n",
        encoding="utf-8",
    )
    result = validate_skill(str(tmp_path))
    assert result["valid"] is False
    assert "Referenced file not found: nope.md" in result["errors"]
