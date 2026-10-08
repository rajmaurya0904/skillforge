"""Tests for the skillforge CLI."""

import subprocess
import sys


def test_cli_prints_message_and_exits_zero() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "skillforge.cli"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "Skillforge CLI" in result.stdout