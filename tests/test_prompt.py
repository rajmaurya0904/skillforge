"""Tests for skillforge.prompt."""

from skillforge.prompt import run_sample_prompts


def test_run_sample_prompts_exists() -> None:
    """Function run_sample_prompts exists and returns bool."""
    result = run_sample_prompts(["example"])
    assert isinstance(result, bool)
    # Currently placeholder returns True
    assert result is True