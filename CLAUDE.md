# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a LeetCode-style problem-solving repository, focused on problems locked behind LeetCode's "Subscribe to unlock" paywall (premium-only problems), along with other interesting problems not available on LeetCode itself. It also contains markdown notes on math concepts.

## Top-level layout

- `Problems/LeetCode/` — LeetCode problems, one folder per problem, listed in the LeetCode table in `README.md`
- `Problems/Other/` — non-LeetCode problems, same per-problem structure, listed in the Other table in `README.md`
- `Math/` — standalone `.md` files, one per math concept, listed in the Math section of `README.md`

## Commands

- Run a problem's solution and its test cases: `uv run <path-to-problem>/solution.py` (e.g. `uv run Problems/LeetCode/0252-meeting-rooms/solution.py`)
- Add a dependency: `uv add <package>`
- Sync/create the virtualenv: `uv sync`

Package management is done exclusively with `uv` (not pip/poetry). Python version is pinned in `.python-version` (3.14).

## Structure per problem

Each problem folder is named `<zero-padded-number>-<kebab-case-title>` (e.g. `0252-meeting-rooms`) and lives under `Problems/LeetCode/` (or `Problems/Other/` for non-LeetCode problems). It contains:

- `description.md` — the problem statement, examples, and constraints (frontmatter + markdown, mirrors the source site's format, excluding `comments` and `edit_url` frontmatter fields)
- `solutions.md` — one or more approaches with an explanation and time/space complexity for each, including a code snippet
- `solution.py` — the LeetCode-style skeleton for practicing:
  - A `Solution` class with a method matching LeetCode's exact signature (a class matching LeetCode's design template for design problems), with all bodies left as `pass`
  - An `if __name__ == "__main__":` block with a `test_cases` list of `(input, expected_output)` tuples (for design problems: `(operations, arguments, expected_outputs)` tuples replayed against a fresh instance per case)
  - The test loop prints a `PASS`/`FAIL` line per case (showing input, expected, and actual), followed by a final summary line: `f"{passed}/{len(test_cases)} test cases passed"`

When scaffolding a new problem, follow this exact structure so `solution.py` is runnable standalone via `uv run` immediately. Also add a row for it to the appropriate problems table (LeetCode or Other) in `README.md`.

IMPORTANT: `solution.py` is checked in as a skeleton only — the working code lives in `solutions.md`. When adding a solved problem, first fill in `solution.py` and verify all test cases pass via `uv run`, then revert the class to the empty skeleton (bodies as `pass`, test harness kept intact) before committing.

## Math notes

Math concepts live as standalone markdown files in `Math/`, named `<kebab-case-topic>.md`. When adding one, also link it from the Math section in `README.md`.
