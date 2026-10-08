"""Tests for skillforge.parser"""

import os
import tempfile

from skillforge.parser import parse_frontmatter


def test_parse_frontmatter_valid():
    """Test parsing valid frontmatter."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
        f.write('---\n')
        f.write('name: test\n')
        f.write('description: A test skill\n')
        f.write('---\n')
        f.write('# Some content\n')
        fname = f.name

    try:
        result = parse_frontmatter(fname)
        assert result == {'name': 'test', 'description': 'A test skill'}
    finally:
        os.unlink(fname)


def test_parse_frontmatter_none():
    """Test parsing file without frontmatter returns None."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
        f.write('# Just a title\n')
        f.write('Some content.\n')
        fname = f.name

    try:
        result = parse_frontmatter(fname)
        assert result is None
    finally:
        os.unlink(fname)


def test_parse_frontmatter_empty():
    """Test parsing empty file returns None."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
        fname = f.name

    try:
        result = parse_frontmatter(fname)
        assert result is None
    finally:
        os.unlink(fname)


def test_parse_frontmatter_no_closing():
    """Test parsing file with opening --- but no closing --- returns None."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
        f.write('---\n')
        f.write('name: test\n')
        f.write('description: No closing\n')
        fname = f.name

    try:
        result = parse_frontmatter(fname)
        assert result is None
    finally:
        os.unlink(fname)