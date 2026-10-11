import argparse
import json
import sys

from skillforge import __version__
from skillforge.validate import validate_skill


def main(argv: list[str] | None = None) -> int:
    """Validate a skill directory and report the result.

    Returns:
        0 if the skill is valid, 1 otherwise.
    """
    parser = argparse.ArgumentParser(prog="skillforge")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("--verbose", action="store_true", help="print parsed frontmatter")
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="output format (default: text)",
    )
    parser.add_argument("skill_dir", help="directory containing the skill's SKILL.md")
    args = parser.parse_args(argv)

    result = validate_skill(args.skill_dir)
    if args.format == "json":
        print(json.dumps(result, indent=2))
        return 0 if result["valid"] else 1

    if args.verbose:
        print("Parsed frontmatter:")
        for key, value in (result["frontmatter"] or {}).items():
            print(f"  {key}: {value}")
    if result["valid"]:
        print(f"Valid skill: {args.skill_dir}")
        return 0

    print(f"Invalid skill: {args.skill_dir}")
    for error in result["errors"]:
        print(f"  - {error}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
