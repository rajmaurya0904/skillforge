"""Tests for skillforge.validator"""

from skillforge.validator import validate_frontmatter


def test_validate_frontmatter_valid():
    """Test validation of valid frontmatter."""
    data = {"name": "test", "description": "A test skill"}
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