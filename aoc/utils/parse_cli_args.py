from argparse import Namespace


def try_int_conversion(value: str, name: str) -> int:
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"Invalid value for {name}: {value}. Must be an integer.")


def parse_cli_args() -> Namespace:
    import argparse

    parser = argparse.ArgumentParser(
        description="Download puzzle and create solution files from their templates."
    )

    parser.add_argument("--year", type=int, required=True, help="Year (2015 or later)")
    parser.add_argument("--day", type=int, required=True, help="Day (1-25)")
    parser.add_argument("--part", type=int, required=True, help="Part (1 or 2)")

    args = parser.parse_args()

    year = try_int_conversion(args.year, "year")
    day = try_int_conversion(args.day, "day")
    part = try_int_conversion(args.part, "part")

    if year < 2015:
        raise ValueError("Year must be 2015 or later.")
    if day < 1 or day > 25:
        raise ValueError("Day must be between 1 and 25.")
    if part not in [1, 2]:
        raise ValueError("Part must be 1 or 2.")

    return args
