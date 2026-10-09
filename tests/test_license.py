import pathlib


def test_license_file_exists_and_contains_text():
    license_path = pathlib.Path("LICENSE.txt")
    assert license_path.exists(), "LICENSE.txt should exist"
    text = license_path.read_text(encoding="utf-8")
    assert "MIT License" in text, "LICENSE.txt should contain MIT License text"
