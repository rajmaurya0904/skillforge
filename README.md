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

## Frontmatter keys

| Key | Required? | Checked |
| --- | --- | --- |
| `name` | required | present, a non-empty string |
| `description` | required | present, a non-empty string |
| `files` | optional | when present: non-empty, and every comma-separated path exists relative to the skill directory |
| `triggers` | optional | when present: non-empty, and each comma-separated prompt is run as a sample trigger |

Omitting `files` or `triggers` is valid and skips that check. Including either
one with an empty value is an error, not a silent no-op. Any key outside this
table is accepted and ignored, so a skill can carry metadata that a particular
directory or runtime needs.

## Examples

### Validating a skill

Given a skill directory with this `SKILL.md`:

```yaml
---
name: csv-helper
description: Converts CSV files into tables.
files: examples.md, template.csv
triggers: convert this csv, make a table from my data
---
```

The optional `files` key lists paths (relative to the skill directory) that must exist. The optional `triggers` key lists sample prompts to run against the skill.

Run the CLI on the directory:

```bash
skillforge path/to/csv-helper
```

If `examples.md` exists but `template.csv` does not, the output is:

```text
Invalid skill: path/to/csv-helper
  - Referenced file not found: template.csv
```

The exit code is `1`. Create the missing file and run the command again to get:

```text
Valid skill: path/to/csv-helper
```

with exit code `0`.

### Interpreting the output

- `Valid skill:` means every check passed and the exit code is `0`.
- `Invalid skill:` means at least one check failed. Each following line starts with `-` and names one problem, such as a missing `name` or a referenced file that does not exist.
- `--verbose` prints the parsed frontmatter before the result, which helps when a key is not being picked up.
- `--format json` prints the same result as JSON with `valid`, `errors`, and `frontmatter` fields, which is useful in scripts and CI:

```bash
skillforge --format json path/to/csv-helper
```

```json
{
  "valid": false,
  "errors": [
    "Referenced file not found: examples.md",
    "Referenced file not found: template.csv"
  ],
  "frontmatter": {
    "name": "csv-helper",
    "description": "Converts CSV files into tables.",
    "files": "examples.md, template.csv"
  }
}
```

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
