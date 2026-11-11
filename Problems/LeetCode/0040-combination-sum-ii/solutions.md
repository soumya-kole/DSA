# 40. Combination Sum II - Solutions

## Solution 1: Backtracking with Duplicate-Skipping

This builds on the same backtracking shape as [39. Combination Sum](../0039-combination-sum/solutions.md), with two differences driven by the rules of this problem: each number may be used **at most once**, and `candidates` can itself contain duplicate values that must not produce duplicate combinations.

"Used at most once" is handled by recursing with `i + 1` instead of `i` — once a candidate is chosen, the next pick must come from strictly later in the sorted array, so the same index is never reused.

Duplicate *values* in `candidates` (e.g. the two `1`s or three `2`s in the examples) need a separate guard, since skipping a used index isn't enough — picking `candidates[1]` vs `candidates[2]` when both equal `1` would otherwise yield the same combination twice. Sorting groups equal values together, so at any fixed recursion depth (any fixed "tree level"), `if i > start and candidates[i] == candidates[i - 1]: continue` skips every *repeat* of a value at that level while still allowing the *first* occurrence — meaning a value can still be picked once per level and reused across different recursive branches below it, just never chosen as two different "first picks" in the same branch.

**Time complexity:** $O(n \cdot 2^n)$ in the worst case, where $n$ is `len(candidates)` — each candidate has exactly 2 choices, in or out of the combination, so $2 \times 2 \times \dots \times 2$ ($n$ times) $= 2^n$ possible subsets, and each successful one costs up to $O(n)$ to copy into `path`. The duplicate-skip and the `rem` cutoff both prune the explored tree further in practice.

**Space complexity:** $O(n)$ for the recursion depth and `path`, excluding the output itself.

```python
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        ans, path = [], []

        def bt(start, rem):
            if rem == 0:
                ans.append(path[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue                      # skip a duplicate at the same tree level
                if candidates[i] > rem:
                    break                         # sorted, so every later candidate is too big as well
                path.append(candidates[i])
                bt(i + 1, rem - candidates[i])    # i+1 means each element is used at most once
                path.pop()

        bt(0, target)
        return ans
```
