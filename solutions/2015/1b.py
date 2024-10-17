def solution(input: str) -> int:
    return len(input)


def test_solution() -> None:
    test_cases = [
        ("a", 1),
        ("ab", 2),
        ("abc", 3),
    ]

    for input, expected in test_cases:
        assert solution(input) == expected
