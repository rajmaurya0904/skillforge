"""Frontmatter parser for SKILL.md files."""

def parse_frontmatter(path):
    """Parse YAML frontmatter from a file.

    Args:
        path (str): Path to the file.

    Returns:
        dict or None: Parsed frontmatter as a dictionary, or None if no valid frontmatter.
    """
    try:
        with open(path, encoding='utf-8') as f:
            lines = [line.rstrip('\n') for line in f]
    except FileNotFoundError:
        return None

    if not lines or lines[0] != '---':
        return None

    # Find the closing --- 
    closing = None
    for i, line in enumerate(lines[1:], start=1):
        if line == '---':
            closing = i
            break

    if closing is None:
        return None

    frontmatter_lines = lines[1:closing]
    data = {}
    for line in frontmatter_lines:
        if not line.strip():
            continue
        # Split on first colon
        if ':' not in line:
            continue
        key, value = line.split(':', 1)
        key = key.strip()
        value = value.strip()
        data[key] = value

    return data