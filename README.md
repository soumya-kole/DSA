# DSA

A collection of LeetCode-style problems and solutions in Python, managed with [uv](https://docs.astral.sh/uv/).

This focuses on problems locked behind LeetCode's "Subscribe to unlock" paywall (premium-only problems), along with other interesting problems not available on LeetCode itself.

## Structure

Each problem lives in its own folder, named `<zero-padded-number>-<kebab-case-title>` (e.g. `0252-meeting-rooms`), containing:

- `description.md` — the problem statement, examples, and constraints
- `solutions.md` — one or more approaches, each with an explanation and time/space complexity
- `solution.py` — a skeleton with the LeetCode-style class/method signature (bodies left empty for practice; the full solutions are in `solutions.md`), plus a `__main__` block that runs a set of test cases and prints a `PASS`/`FAIL` result for each, followed by a summary count

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
| 163 | [Missing Ranges](0163-missing-ranges/description.md) | Easy |
| 252 | [Meeting Rooms](0252-meeting-rooms/description.md) | Easy |
| 253 | [Meeting Rooms II](0253-meeting-rooms-ii/description.md) | Medium |
| 703 | [Kth Largest Element in a Stream](0703-kth-largest-element-in-a-stream/description.md) | Easy |
| 2336 | [Smallest Number in Infinite Set](2336-smallest-number-in-infinite-set/description.md) | Medium |
