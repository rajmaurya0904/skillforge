"""Tests for skillforge.validator"""

from skillforge.validator import validate_frontmatter


def test_validate_frontmatter_valid():
    """Test validation of valid frontmatter."""
    data = {"name": "hello", "description": "world"}
    errors = validate_frontmatter(data)
    assert errors == []


def test_validate_frontmatter_missing_name():
    """Test validation when name is missing."""
    data = {"description": "A test skill"}
    errors = validate_frontmatter(data)
    assert "Missing 'name' in frontmatter" in errors


def test_validate_frontmatter_missing_description():
    """Test validation when description is missing."""
    data = {"name": "test"}
    errors = validate_frontmatter(data)
    assert "Missing 'description' in frontmatter" in errors


def test_validate_frontmatter_empty_name():
    """Test validation when name is empty string."""
    data = {"name": "", "description": "A test skill"}
    errors = validate_frontmatter(data)
    assert "'name' must not be empty" in errors


def test_validate_frontmatter_empty_description():
    """Test validation when description is empty string."""
    data = {"name": "test", "description": ""}
    errors = validate_frontmatter(data)
    assert "'description' must not be empty" in errors


def test_validate_frontmatter_non_string_name():
    """Test validation when name is not a string."""
    data = {"name": 123, "description": "A test skill"}
    errors = validate_frontmatter(data)
    assert "'name' must be a string" in errors


def test_validate_frontmatter_non_string_description():
    """Test validation when description is not a string."""
    data = {"name": "test", "description": 456}
    errors = validate_frontmatter(data)
    assert "'description' must be a string" in errors


def test_validate_frontmatter_none():
    """Test validation when data is None."""
    errors = validate_frontmatter(None)
    assert errors == ["No frontmatter found"]


def test_validate_frontmatter_not_dict():
    """Test validation when data is not a dict."""
    errors = validate_frontmatter(["invalid"])
    assert errors == ["Frontmatter must be a dictionary"]

def test_validate_frontmatter_optional_keys_may_be_absent():
    """'files' and 'triggers' are optional: omitting both is valid."""
    data = {"name": "test", "description": "A test skill"}
    assert validate_frontmatter(data) == []


def test_validate_frontmatter_optional_keys_accepted_when_present():
    """A non-empty 'files'/'triggers' pair adds no errors."""
    data = {
        "name": "test",
        "description": "A test skill",
        "files": "examples.md",
        "triggers": "validate my skill",
    }
    assert validate_frontmatter(data) == []


def test_validate_frontmatter_empty_files():
    """A present but empty 'files' key is a mistake, not a no-op."""
    data = {"name": "test", "description": "A test skill", "files": "  "}
    errors = validate_frontmatter(data)
    assert "'files' must not be empty" in errors


def test_validate_frontmatter_empty_triggers():
    """A present but empty 'triggers' key is a mistake, not a no-op."""
    data = {"name": "test", "description": "A test skill", "triggers": ""}
    errors = validate_frontmatter(data)
    assert "'triggers' must not be empty" in errors


def test_validate_frontmatter_non_string_files():
    """'files' must be a string when present."""
    data = {"name": "test", "description": "A test skill", "files": ["examples.md"]}
    errors = validate_frontmatter(data)
    assert "'files' must be a string" in errors


def test_validate_frontmatter_unknown_keys_are_ignored():
    """Keys outside the contract are accepted and ignored."""
    data = {"name": "test", "description": "A test skill", "license": "MIT"}
    assert validate_frontmatter(data) == []
