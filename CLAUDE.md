# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a LeetCode-style problem-solving repository, focused on problems locked behind LeetCode's "Subscribe to unlock" paywall (premium-only problems), along with other interesting problems not available on LeetCode itself. Each solved problem lives in its own folder at the repo root, listed in the table in `README.md`.

## Commands

- Run a problem's solution and its test cases: `uv run <folder>/solution.py` (e.g. `uv run 0252-meeting-rooms/solution.py`)
- Add a dependency: `uv add <package>`
- Sync/create the virtualenv: `uv sync`

Package management is done exclusively with `uv` (not pip/poetry). Python version is pinned in `.python-version` (3.14).

## Structure per problem

Each problem folder is named `<zero-padded-number>-<kebab-case-title>` (e.g. `0252-meeting-rooms`) and contains:

- `description.md` — the problem statement, examples, and constraints (frontmatter + markdown, mirrors the source site's format, excluding `comments` and `edit_url` frontmatter fields)
- `solutions.md` — one or more approaches with an explanation and time/space complexity for each, including a code snippet
- `solution.py` — the LeetCode-style solution:
  - A `Solution` class with a method matching LeetCode's exact signature (left unimplemented when scaffolding a new problem, filled in once solved)
  - An `if __name__ == "__main__":` block with a `test_cases` list of `(input, expected_output)` tuples
  - The test loop prints a `PASS`/`FAIL` line per case (showing input, expected, and actual), followed by a final summary line: `f"{passed}/{len(test_cases)} test cases passed"`

When scaffolding a new problem, follow this exact structure so `solution.py` is runnable standalone via `uv run` immediately, with the method body left empty for the solution to be filled in later. Also add a row for it to the problems table in `README.md`.
