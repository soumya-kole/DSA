# 216. Combination Sum III - Solutions

## Solution 1: Backtracking over a Fixed Digit Range

Unlike [39. Combination Sum](../0039-combination-sum/solutions.md) and [40. Combination Sum II](../0040-combination-sum-ii/solutions.md), there's no input array to sort — the candidates are always the digits `1` through `9`, already in order, so the recursion walks `range(start, 10)` directly.

Backtrack with a `start` digit and the remaining sum `rem`, same as before: recursing with `x + 1` ensures each digit is used at most once and digits are only ever picked in increasing order, which also rules out duplicate combinations without any extra skip-logic (there are no duplicate values to begin with). The one addition is the `len(path) == k` check — a combination is only valid once it has *exactly* `k` digits, so that check gates whether a completed-sum `path` actually gets appended; reaching `rem == 0` with too few digits picked is not a valid combination and must not be recorded.

**Time complexity:** $O\!\left(\binom{9}{k} \cdot k\right)$ — the search space is bounded by choosing `k` digits out of a fixed set of 9, independent of `n`, and each successful leaf costs $O(k)$ to copy `path`. In absolute terms this is $O(1)$, since both factors are capped by the fixed digit range `1..9`.

**Space complexity:** $O(k)$ for the recursion depth and `path`, excluding the output itself.

```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        ans, path = [], []

        def bt(start, rem):
            if len(path) == k:
                if rem == 0:
                    ans.append(path[:])
                return
            for x in range(start, 10):
                if x > rem:
                    break                         # 1..9 are already in order, so later x are too big as well
                path.append(x)
                bt(x + 1, rem - x)
                path.pop()

        bt(1, n)
        return ans
```
