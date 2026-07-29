# DSA

A collection of LeetCode-style problems and solutions in Python, managed with [uv](https://docs.astral.sh/uv/).

This focuses on problems locked behind LeetCode's "Subscribe to unlock" paywall (premium-only problems), along with other interesting problems not available on LeetCode itself.

## Structure

Each problem lives in its own folder, named `<zero-padded-number>-<kebab-case-title>` (e.g. `0252-meeting-rooms`), containing:

- `description.md` — the problem statement, examples, and constraints
- `solutions.md` — one or more approaches, each with an explanation and time/space complexity
- `solution.py` — a `Solution` class with the LeetCode-style method signature, plus a `__main__` block that runs a set of test cases and prints a `PASS`/`FAIL` result for each, followed by a summary count

## Usage

Run a problem's solution against its test cases:

```sh
uv run <folder>/solution.py
```

For example:

```sh
uv run 0252-meeting-rooms/solution.py
```

## Problems

| # | Title | Difficulty |
|---|-------|------------|
| 252 | [Meeting Rooms](0252-meeting-rooms/description.md) | Easy |
