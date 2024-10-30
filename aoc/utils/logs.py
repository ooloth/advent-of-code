import sys

import rich


def log(obj: object) -> None:
    """Send debugging print statements to stderr to avoid concatenating them with the puzzle answer sent to stdout."""
    rich.print(f"{obj=}", file=sys.stderr)
