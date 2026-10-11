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

Validate a skill by passing the directory that contains its SKILL.md:

```bash
skillforge path/to/my-skill
```

The command exits with code 0 if the skill is valid and 1 otherwise.

Or invoke it as a module:

```bash
python -m skillforge.cli path/to/my-skill
```

Show the help text or the version:

```bash
skillforge --help
skillforge --version
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
