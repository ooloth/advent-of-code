from pathlib import Path


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
    puzzle_input_file = f"{Path(__file__).parent}/inputs/1.txt"
    with open(puzzle_input_file) as f:
        puzzle_input_string = f.read().strip()
        print(solution(puzzle_input_string))
