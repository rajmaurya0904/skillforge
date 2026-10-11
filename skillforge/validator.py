"""Validator for SKILL.md frontmatter.

The frontmatter contract is deliberate and small:

Required keys -- validation fails without them:
    name: the skill's identifier.
    description: the text a model reads to decide whether to select the skill.

Optional keys -- absence is fine, but a present key must be a non-empty string:
    files: comma-separated paths (relative to the skill directory) that must exist.
    triggers: comma-separated sample prompts run against the skill.

Any other key is accepted and ignored, so a skill can carry metadata that a
particular directory or runtime needs without failing validation here.
"""

#: Keys every SKILL.md must declare as a non-empty string.
REQUIRED_KEYS = ("name", "description")

#: Keys that may be omitted, but must be a non-empty string when present.
OPTIONAL_KEYS = ("files", "triggers")


def validate_frontmatter(data):
    """Validate frontmatter data against the key contract above.

    Args:
        data (dict or None): Parsed frontmatter data.

    Returns:
        list of str: List of error messages, empty if valid.
    """
    errors = []
    if data is None:
        errors.append("No frontmatter found")
        return errors

    if not isinstance(data, dict):
        errors.append("Frontmatter must be a dictionary")
        return errors

    for field in REQUIRED_KEYS:
        if field not in data:
            errors.append(f"Missing '{field}' in frontmatter")
        else:
            errors.extend(_check_non_empty_string(field, data[field]))

    for field in OPTIONAL_KEYS:
        if field in data:
            errors.extend(_check_non_empty_string(field, data[field]))

    return errors


def _check_non_empty_string(field, value):
    """Return the errors for a key that must hold a non-empty string."""
    if not isinstance(value, str):
        return [f"'{field}' must be a string"]
    if not value.strip():
        return [f"'{field}' must not be empty"]
    return []
