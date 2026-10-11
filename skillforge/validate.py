"""Skill validation orchestrator for skillforge.

Ties together frontmatter parsing, frontmatter validation, referenced-file
checks, and sample trigger prompts for a single skill directory.

Optional frontmatter keys read by this module:
    files: comma-separated paths (relative to the skill directory) that must exist.
    triggers: comma-separated sample prompts to run against the skill.
"""

import os
from typing import TypedDict

from skillforge.fs import check_referenced_files
from skillforge.parser import parse_frontmatter
from skillforge.prompt import run_sample_prompts
from skillforge.validator import validate_frontmatter

SKILL_FILENAME = "SKILL.md"


class ValidationResult(TypedDict):
    """Result of validating a skill directory."""

    valid: bool
    errors: list[str]
    frontmatter: dict[str, str] | None


def _split_list(value: str) -> list[str]:
    """Split a comma-separated frontmatter value into non-empty items."""
    return [item.strip() for item in value.split(",") if item.strip()]


def validate_skill(skill_dir: str) -> ValidationResult:
    """Validate the SKILL.md inside a skill directory.

    Args:
        skill_dir: Path to the directory containing SKILL.md.

    Returns:
        A dict with 'valid' (bool), 'errors' (list of str), and 'frontmatter'
        (the parsed frontmatter dict, or None if it could not be parsed).
    """
    skill_path = os.path.join(skill_dir, SKILL_FILENAME)
    if not os.path.isfile(skill_path):
        return {
            "valid": False,
            "errors": [f"{SKILL_FILENAME} not found in {skill_dir}"],
            "frontmatter": None,
        }

    frontmatter = parse_frontmatter(skill_path)
    errors = validate_frontmatter(frontmatter)

    if frontmatter is not None:
        if "files" in frontmatter:
            missing = check_referenced_files(skill_dir, _split_list(frontmatter["files"]))
            errors.extend(f"Referenced file not found: {path}" for path in missing)
        if "triggers" in frontmatter:
            triggers = _split_list(frontmatter["triggers"])
            if triggers and not run_sample_prompts(triggers):
                errors.append("Sample trigger prompts failed")

    return {"valid": not errors, "errors": errors, "frontmatter": frontmatter}
