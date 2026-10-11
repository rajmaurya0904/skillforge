"""Tests for the skillforge CLI."""

import os
import subprocess
import sys

GOOD_SKILL = os.path.join(os.path.dirname(__file__), "fixtures", "good_skill")


def test_cli_help() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "skillforge.cli", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "usage: skillforge" in result.stdout


def test_cli_valid_skill_directory() -> None:
    """Validating the good fixture exits 0 and prints a success message."""
    result = subprocess.run(
        [sys.executable, "-m", "skillforge.cli", GOOD_SKILL],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "Valid skill" in result.stdout


def test_cli_invalid_skill_directory(tmp_path) -> None:
    """A skill missing its required 'name' field exits 1 and reports the error."""
    (tmp_path / "SKILL.md").write_text(
        "---\ndescription: Has no name field.\n---\n# Bad\n",
        encoding="utf-8",
    )
    result = subprocess.run(
        [sys.executable, "-m", "skillforge.cli", str(tmp_path)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 1
    assert "Invalid skill" in result.stdout
    assert "Missing 'name' in frontmatter" in result.stdout