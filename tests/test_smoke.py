"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import skillforge


def test_version_is_set() -> None:
    assert skillforge.__version__
