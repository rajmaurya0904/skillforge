import argparse
import sys

from skillforge.validate import validate_skill


def main(argv: list[str] | None = None) -> int:
    """Validate a skill directory and report the result.

    Returns:
        0 if the skill is valid, 1 otherwise.
    """
    parser = argparse.ArgumentParser(prog="skillforge")
    parser.add_argument("skill_dir", help="directory containing the skill's SKILL.md")
    args = parser.parse_args(argv)

    result = validate_skill(args.skill_dir)
    if result["valid"]:
        print(f"Valid skill: {args.skill_dir}")
        return 0

    print(f"Invalid skill: {args.skill_dir}")
    for error in result["errors"]:
        print(f"  - {error}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
