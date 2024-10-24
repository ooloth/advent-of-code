# 🎄 Advent of Code

Solutions for [Advent of Code](https://adventofcode.com/) puzzles in languages I enjoy.

## Commands

```bash
$ bin/new [YEAR]-[DAY]-[PART]
$ bin/solve [YEAR]-[DAY]-[PART]
$ bin/solve [YEAR]-[DAY]-[PART] --submit
```

For example:

```bash
$ bin/new 2015-1-1 # download the 2015, day 1, part 1 puzzle and its input and generate solution files
$ bin/solve 2023-25-2 # output my 2023, day 25, part 2 answer
$ bin/solve 2023-25-2 --submit # submit my 2023, day 25, part 2 answer
```

## Advent of Code session cookie

To download your input, you need to include your AOC `session` cookie with each API request. You can find your cookie by going to [adventofcode.com](https://adventofcode.com/) and opening your browser's developer tools.

Find the cookie named "session" and copy its value into a `.aoc-session-cookie` file at the root of this project (it won't be tracked).

When the value eventually expires, repeat these steps.
