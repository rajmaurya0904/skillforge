import argparse


def main() -> None:
    """Entry point for the skillforge CLI using argparse."""
    parser = argparse.ArgumentParser(prog="skillforge")
    # No arguments expected; just parse to allow future extensions
    parser.parse_args()
    print("Skillforge CLI")


if __name__ == "__main__":
    main()