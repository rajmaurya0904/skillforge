"""Tests for skillforge.prompt."""

from skillforge.prompt import run_sample_prompts


def test_run_sample_prompts_returns_true_for_non_empty_input() -> None:
    """Function returns True for non-empty input."""
    assert run_sample_prompts(["trigger"]) is True