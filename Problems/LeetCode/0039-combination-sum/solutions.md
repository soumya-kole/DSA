# 39. Combination Sum - Solutions

## Solution 1: Backtracking with Reusable Candidates

Sort `candidates` first so that within any recursive call, once a candidate exceeds the remaining budget `rem`, every candidate after it (being larger) does too — letting the loop `break` instead of checking every remaining candidate.

Backtrack with a `start` index and the remaining sum `rem`: at each call, try every candidate from `start` onward, append it to `path`, and recurse. Passing `i` (not `i + 1`) as the next `start` allows the same candidate to be reused in later recursive calls, since a number can appear in a combination any number of times. When `rem` hits exactly `0`, the current `path` is a valid combination — append a *copy* of it to `ans`, since `path` keeps mutating after this point. Only a single copy is made per solution found, not per candidate tried.

Restricting the loop to `start..end` (rather than always starting from `0`) is what prevents duplicate combinations in different orders — e.g. `[2, 2, 3]` can only be built by picking `2` before `3`, never `3` before `2`, since indices never move backward.

**Time complexity:** $O\!\left(n^{T/M} \cdot \frac{T}{M}\right)$, where $n$ is `len(candidates)`, $T$ is `target`, and $M$ is the smallest candidate value. Repeatedly picking $M$ bounds the recursion depth at $T/M$, and each call branches into at most $n$ children, so the tree has at most $n^{T/M}$ nodes; each successful leaf then costs $O(T/M)$ to copy `path`. The problem's own guarantee (fewer than 150 valid combinations) keeps this fast in practice despite the loose worst case.

**Space complexity:** $O(T/M)$ for the recursion depth and `path`, excluding the output itself — the same bound that caps the depth in the time complexity above.

```python
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        ans, path = [], []

        def bt(start, rem):
            if rem == 0:
                ans.append(path[:])          # the only copy, made once per solution
                return
            for i in range(start, len(candidates)):
                if candidates[i] > rem:      # sorted, so every later candidate is too big as well
                    break
                path.append(candidates[i])
                bt(i, rem - candidates[i])   # i, not i+1: the same number can be reused
                path.pop()

        bt(0, target)
        return ans
```
