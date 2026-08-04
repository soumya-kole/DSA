# 163. Missing Ranges - Solutions

## Solution 1: Sentinel Bounds + Pairwise Scan

Pad `nums` with two sentinels: `lower - 1` in front and `upper + 1` at the end. Now every missing range lies strictly between some adjacent pair `(a, b)` of this padded list, and the sentinels make the boundary cases (gap before the first element, gap after the last, empty `nums`) fall out of the same rule — no special-casing needed.

For each adjacent pair `(a, b)`:

- The numbers strictly between them, `a + 1 .. b - 1`, are exactly the missing ones in that gap.
- A gap exists only when `b - a > 1` (if `b == a + 1` the pair is consecutive and nothing is missing).
- When it exists, the missing range is `[a + 1, b - 1]`.

Since `nums` is sorted and unique, scanning adjacent pairs left to right (`itertools.pairwise`) emits the ranges already sorted and non-overlapping, which is precisely the shortest exact cover the problem asks for.

**Time complexity:** $O(n)$ - one pass over the padded list.

**Space complexity:** $O(n)$ - the padded copy of `nums` ($O(1)$ extra beyond input and output).

```python
from itertools import pairwise

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        bounds = [lower - 1] + nums + [upper + 1]
        return [[a + 1, b - 1] for a, b in pairwise(bounds) if b - a > 1]
```

## Solution 2: Running Pointer (Explicit Loop)

Same algorithm written as an explicit loop — the interview-friendly variant that needs no `itertools`. Track `prev`, the invariant being that every number `<= prev` is already accounted for (either present in `nums` or emitted as part of a missing range). Walk through `nums` with `upper + 1` appended as the right sentinel: whenever the current number is more than one step ahead of `prev`, the numbers in between form a missing range. This makes the "last accounted-for number" mental model concrete and is easier to step through on a whiteboard or in a debugger.

**Why `prev = lower - 1`?** The sentinel pretends there is an element just below the range, which makes the very first gap check work with the same generic rule as every other iteration:

- The gap rule emits `[prev + 1, cur - 1]`. With `prev = lower - 1`, we get `prev + 1 = lower` — so if the first real element is above `lower` (or `nums` is empty), the emitted range correctly starts at `lower`. E.g. `nums = [3], lower = 0`: first check is `3 - (-1) > 1` → emit `[0, 2]`.
- If `nums[0] == lower`, then `cur - prev = 1` — adjacent, no gap emitted, which is correct.
- It must be exactly `lower - 1`: using `lower` itself would wrongly treat `lower` as already covered (missing `[lower, lower]` ranges), and anything smaller would fabricate a gap below the range.
- The invariant holds vacuously at the start: numbers `<= lower - 1` are outside `[lower, upper]`, so they can never be missing.

The appended `upper + 1` is the mirror-image sentinel for the tail: after the last real element, the check emits `[prev + 1, upper]` if anything at the top of the range is uncovered.

**Time complexity:** $O(n)$ - one pass over `nums`.

**Space complexity:** $O(n)$ - for the `nums + [upper + 1]` copy ($O(1)$ extra beyond input and output).

```python
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        missing = []
        # sentinel just below the range: everything <= prev is accounted for,
        # and prev + 1 == lower so the first gap check can emit from lower
        prev = lower - 1
        for cur in nums + [upper + 1]:
            if cur - prev > 1:  # gap between prev and cur
                missing.append([prev + 1, cur - 1])
            prev = cur
        return missing
```
