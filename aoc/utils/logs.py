import sys

import rich


def log(msg: str) -> None:
    """Send debugging print statements to stderr to avoid concatenating them with the puzzle answer sent to stdout."""
    rich.print(msg, file=sys.stderr)
