"""Filesystem utilities for skillforge."""

import os


def check_referenced_files(base_dir: str, file_list: list[str]) -> list[str]:
    """Return list of missing paths from file_list relative to base_dir.

    Args:
        base_dir: Base directory to prepend to each file path.
        file_list: List of file paths (relative to base_dir).

    Returns:
        List of missing paths (relative to base_dir) that do not exist.
    """
    missing = []
    for relative_path in file_list:
        full_path = os.path.join(base_dir, relative_path)
        if not os.path.exists(full_path):
            missing.append(relative_path)
    return missing