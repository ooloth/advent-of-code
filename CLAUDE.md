# CLAUDE.md

Orientation for agents working in this repository.

## What this repo is

A collection of [Advent of Code](https://adventofcode.com/) puzzle solutions in Python and TypeScript. Each puzzle has a solution file, an input file, and a puzzle description file. The `bin/` scripts handle downloading, running, testing, and submitting solutions.

## How to run checks

```bash
uv run ruff check .      # lint
uv run mypy .            # type check (Python)
uv run pytest            # run all Python tests
```

## Commands

```bash
bin/new <day><part>              # download puzzle + input, scaffold solution, open in $EDITOR, run tests
bin/run <day><part>              # run a solution and print the answer
bin/run <day><part> --submit     # run a solution and submit the answer
bin/submit <day><part>           # submit the most recently computed answer
bin/test <day><part>             # run tests for one puzzle in watch mode
```

## Prerequisites

Every external tool must be installed before any `bin/` command will work:

| Tool | Required for | Install |
|------|-------------|---------|
| `uv` | Running Python solutions and all `uv run ...` checks | https://docs.astral.sh/uv/getting-started/installation/ |
| Python 3.13 | `pyproject.toml` specifies `requires-python = ">=3.13"` | `uv python install 3.13` |
| `aoc` (aoc-cli) | `bin/new` (download puzzle + input) and `bin/submit` (submit answer) | https://github.com/scarvalhojr/aoc-cli |
| `deno` | Running TypeScript solutions (`AOC_LANGUAGE=typescript`) | https://docs.deno.com/runtime/getting_started/installation/ |
| `$EDITOR` | `bin/new` opens scaffolded files in `$EDITOR` after download | Set `EDITOR` in your shell profile |

## Non-obvious constraints

- **`AOC_YEAR` is hard-capped at 2024.** `bin/env` line 49 rejects any year outside 2015–2024 with a non-zero exit. Attempting `bin/new` or `bin/run` with a higher year will fail immediately.
- **`.aoc-session-cookie` must exist at the repo root.** `bin/new` and `bin/submit` pass this file to `aoc-cli` for authentication. The file is gitignored. Obtain the value from your browser's developer tools at adventofcode.com (cookie named `session`).
- **`deno` must be installed to use `AOC_LANGUAGE=typescript`.** Change `AOC_LANGUAGE` in `bin/env` to switch languages; without `deno`, TypeScript solutions will fail at runtime.
- **`aoc-cli` must be installed separately.** It is not a Python package and is not managed by `uv`. Install it from https://github.com/scarvalhojr/aoc-cli before running `bin/new` or `bin/submit`.
