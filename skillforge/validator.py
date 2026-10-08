"""Validator for SKILL.md frontmatter."""

def validate_frontmatter(data):
    """Validate frontmatter data.

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

    # Validate required fields
    required = {
        "name": "string",
        "description": "string",
    }
    for field, _expected_type in required.items():
        if field not in data:
            errors.append(f"Missing '{field}' in frontmatter")
        elif not isinstance(data[field], str):
            errors.append(f"'{field}' must be a string")
        elif not data[field].strip():
            errors.append(f"'{field}' must not be empty")

    return errors