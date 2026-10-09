# Skillforge

Validates SKILL.md frontmatter, description quality, and referenced files, and runs sample trigger prompts to check the skill's description would actually get selected. For skill authors publishing to directories.

## Installation

You can install the package from PyPI:

```bash
pip install skillforge
```

For development, install the package in editable mode with the development dependencies:

```bash
pip install -e ".[dev]"
```

## Usage

Run the CLI from a terminal:

```bash
skillforge
```

Or invoke it as a module:

```bash
python -m skillforge.cli
```

Show the help text:

```bash
skillforge --help
```

## Example

TODO.

## FAQ

### Why am I getting an error about missing frontmatter?

The tool expects each SKILL.md file to have a YAML frontmatter block at the top, delimited by `---`. If your file is missing this block or it's malformed, you'll see an error. Ensure your SKILL.md starts with:

```yaml
---
name: my-skill
description: A short description
...
---
```

### Why am I getting an error about missing files?

The tool checks that all files referenced in the SKILL.md (e.g., in `trigger` or `examples`) actually exist in the skill directory. If a referenced file is missing, you'll get an error. Make sure all referenced files are present and the paths are correct relative to the SKILL.md location.

## License

MIT -- see [LICENSE](LICENSE).
