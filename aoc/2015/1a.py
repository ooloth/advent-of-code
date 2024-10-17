# TODO: inline the instructions at the top of the solution file?


def solution(input: str) -> int:
    return len(input)


def test_solution() -> None:
    test_cases: list[tuple[str, int]] = [
        ("a", 1),
        ("ab", 2),
        ("abc", 3),
    ]

    for input, expected in test_cases:
        assert solution(input) == expected


if __name__ == "__main__":
    # TODO: how does templating work? how to interpolate values?
    with open("inputs/{day}.txt") as f:
        print(solution(f.read().strip()))
