"""Tests for skillforge.fs"""

import os
import tempfile

from skillforge.fs import check_referenced_files


def test_check_referenced_files_all_exist():
    """Test when all files exist."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create some files
        file1 = os.path.join(tmpdir, 'file1.txt')
        file2 = os.path.join(tmpdir, 'subdir', 'file2.txt')
        os.makedirs(os.path.dirname(file2), exist_ok=True)
        open(file1, 'w').close()
        open(file2, 'w').close()

        base_dir = tmpdir
        file_list = ['file1.txt', 'subdir/file2.txt']
        missing = check_referenced_files(base_dir, file_list)
        assert missing == []


def test_check_referenced_files_some_missing():
    """Test when some files are missing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create only one file
        file1 = os.path.join(tmpdir, 'file1.txt')
        open(file1, 'w').close()

        base_dir = tmpdir
        file_list = ['file1.txt', 'file2.txt', 'subdir/file3.txt']
        missing = check_referenced_files(base_dir, file_list)
        # Expect the two missing ones
        assert set(missing) == {'file2.txt', 'subdir/file3.txt'}


def test_check_referenced_files_all_missing():
    """Test when no files exist."""
    with tempfile.TemporaryDirectory() as tmpdir:
        base_dir = tmpdir
        file_list = ['file1.txt', 'file2.txt']
        missing = check_referenced_files(base_dir, file_list)
        assert missing == ['file1.txt', 'file2.txt']


def test_check_referenced_files_empty_list():
    """Test with empty file list."""
    with tempfile.TemporaryDirectory() as tmpdir:
        base_dir = tmpdir
        file_list = []
        missing = check_referenced_files(base_dir, file_list)
        assert missing == []


def test_check_referenced_files_with_base_dir_being_file():
    """Edge case: base_dir is a file (should still work, joining paths)."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a file to act as base_dir
        base_file = os.path.join(tmpdir, 'base.txt')
        open(base_file, 'w').close()
        # Create a referenced file inside the directory of base_file? Actually, joining a file
        # as base_dir will just append the relative path to that file's path, which is okay.
        # We'll just test that it doesn't crash and returns expected missing.
        file_list = ['some.txt']
        missing = check_referenced_files(base_file, file_list)
        assert missing == ['some.txt']  # because the joined path doesn't exist