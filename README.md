# skillforge

**Checks a SKILL.md before you publish it: required frontmatter, and that every file the skill points at actually exists.**

A skill directory looks fine until something reads it. A missing `description`,
a `files:` line left over from a rename, a template you never committed -- none
of that shows up when you eyeball the file, and all of it shows up as a broken
skill for whoever installs it. `skillforge` reads the directory and tells you
which line is wrong, with an exit code CI can act on.

## Real terminal output

```text
$ python -m skillforge.cli tests/fixtures/good_skill
Valid skill: tests/fixtures/good_skill
$ echo $?
0

$ python -m skillforge.cli tests/fixtures/broken_skill
Invalid skill: tests/fixtures/broken_skill
  - Missing 'description' in frontmatter
  - Referenced file not found: examples.md
  - Referenced file not found: template.csv
$ echo $?
1
```

`tests/fixtures/broken_skill` is committed and deliberately wrong: no
`description`, and a `files:` key naming two paths that are not there.

## Install

Not on PyPI. Clone the repo and install it from the checkout:

```bash
pip install -e .
```

## Usage

```bash
skillforge path/to/my-skill                  # validate a directory; exit 0 valid, 1 invalid
skillforge --verbose path/to/my-skill        # print the parsed frontmatter before the verdict
skillforge --format json path/to/my-skill    # same result as JSON, for CI
python -m skillforge.cli path/to/my-skill    # same thing without installing the script
```

## How it works

It reads `SKILL.md` from the directory you name, parses the `---` frontmatter
block as flat `key: value` lines, and applies this contract:

| Key | Required? | Checked |
| --- | --- | --- |
| `name` | required | present, a non-empty string |
| `description` | required | present, a non-empty string |
| `files` | optional | when present: non-empty, and every comma-separated path exists relative to the skill directory |
| `triggers` | optional | when present: non-empty, and each comma-separated prompt is run as a sample trigger |

Omitting `files` or `triggers` is valid and skips that check. Including either
one with an empty value is an error, not a silent no-op. Any key outside this
table is accepted and ignored, so a skill can carry metadata that a particular
directory or runtime needs. Every failure becomes one `-` line of output, and
any failure at all means exit code 1.

## Limitations

The trigger run is a stub. `triggers:` is parsed and validated, but
`skillforge.prompt.run_sample_prompts` returns `True` without calling a model,
so a listed prompt never actually fails -- nothing here yet tells you whether
your `description` would get the skill selected.

There is no description-quality scoring either: `description` is checked for
presence, not for whether it is any good.

The frontmatter parser is deliberately dumb -- flat `key: value` lines only. No
YAML lists, block scalars, nested maps, quoting or comments; `files` and
`triggers` are comma-separated strings for that reason. A line with no colon is
skipped silently, which is why a mistyped `description` reads as missing rather
than malformed. Only a file named `SKILL.md` is read, and referenced files are
checked for existence, never for contents.

## Development

```bash
pip install -e ".[dev]"
pytest -q
ruff check .
```

## License

MIT -- see [LICENSE](LICENSE).
