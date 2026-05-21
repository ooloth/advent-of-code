# 🎄 Advent of Code

Solutions for [Advent of Code](https://adventofcode.com/) puzzles in languages I enjoy.

## Prerequisites

Install these tools before running any `bin/` commands:

- **[uv](https://docs.astral.sh/uv/getting-started/installation/)** — runs Python solutions and dev tools (`uv run ...`)
- **Python 3.13** — required by `pyproject.toml`; install via `uv python install 3.13`
- **[aoc-cli](https://github.com/scarvalhojr/aoc-cli)** — required by `bin/new` (download) and `bin/submit` (submission)
- **[deno](https://docs.deno.com/runtime/getting_started/installation/)** — required only if using `AOC_LANGUAGE=typescript`
- **`$EDITOR`** — `bin/new` opens scaffolded files in your editor; set `EDITOR` in your shell profile

## Environment variables

Update the `AOC_LANGUAGE` and `AOC_YEAR` environment variables in `bin/env` to match your preferences. They determine which puzzles to download and which solution files to run and submit.

Note: `AOC_YEAR` is validated to be between 2015 and 2024. Years outside this range will cause all `bin/` commands to exit with an error.

## Commands

```bash
$ bin/new <day><part> # start a new puzzle in the active year
$ bin/run <day><part> [--submit] # run a puzzle solution in the active year (pass --submit or -s to also submit the answer)
$ bin/submit <day><part> # submit a puzzle answer in the active year
```

For example:

```bash
$ bin/new 1a # download the 2024, day 1, part 1 puzzle and its input and generate solution files
$ bin/run 25b # output my 2024, day 25, part 2 answer
$ bin/run 25b --submit # output and submit my 2024, day 25, part 2 answer
$ bin/submit 25b # submit my 2024, day 25, part 2 answer
```

## Advent of Code session cookie

To download your input, you need to include your AOC `session` cookie with each API request. You can find your cookie by going to [adventofcode.com](https://adventofcode.com/) and opening your browser's developer tools.

Find the cookie named "session" and copy its value into a `.aoc-session-cookie` file at the root of this project (it won't be tracked).

When the value eventually expires, repeat these steps.
