# 3737. Count Subarrays With Majority Element I - Solutions

## Solution 1: Brute Force

Enumerate every subarray `nums[i..j]` and use a `Counter` to count how many times `target` appears in it, then check whether that count is strictly more than half the subarray's length.

**Time complexity:** $O(n^3)$ - there are $O(n^2)$ subarrays, and building a `Counter` for each one (via the `nums[i:j+1]` slice) costs $O(n)$.

**Space complexity:** $O(n)$ - for the slice and its `Counter`.

```python
from collections import Counter
from typing import List


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n, res = len(nums), 0
        for i in range(n):
            for j in range(i, n):
                sub = nums[i:j + 1]
                target_cnt = Counter(sub)[target]
                if target_cnt > len(sub) / 2:
                    res += 1
        return res
```

## Solution 2: Optimized Brute Force

Instead of re-counting `target` from scratch for every subarray, fix the left endpoint `i` and extend the right endpoint `j` one step at a time, maintaining a running balance `b`: `+1` for every `target` seen and `-1` for every non-target. A subarray is a majority-`target` subarray exactly when `b > 0`, since that means `target` occurrences outnumber non-target occurrences.

**Time complexity:** $O(n^2)$ - two nested loops over `i` and `j`, with $O(1)$ work per pair.

**Space complexity:** $O(1)$ - only the running balance `b` is kept.

```python
from typing import List


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            b = 0
            for j in range(i, len(nums)):
                if nums[j] == target:
                    b += 1
                else:
                    b -= 1
                if b > 0:
                    cnt += 1
        return cnt
```

**Trace for `nums = [1,2,2,3], target = 2`:**

```
i = 0  (subarrays starting at 1)
  j=0  [1]        b = -1        ✗
  j=1  [1,2]      b =  0        ✗   (1 target, 1 non-target: not strictly more than half)
  j=2  [1,2,2]    b =  1        ✓   cnt = 1
  j=3  [1,2,2,3]  b =  0        ✗

i = 1  (subarrays starting at 2)
  j=1  [2]        b =  1        ✓   cnt = 2
  j=2  [2,2]      b =  2        ✓   cnt = 3
  j=3  [2,2,3]    b =  1        ✓   cnt = 4

i = 2
  j=2  [2]        b =  1        ✓   cnt = 5
  j=3  [2,3]      b =  0        ✗

i = 3
  j=3  [3]        b = -1        ✗

return 5
```

## Solution 3: Prefix Sum with Offset Array (Optimal)

Map each element to `+1` if it equals `target` and `-1` otherwise, and let `P[k]` be the prefix sum of the first `k` mapped values (`P[0] = 0`). A subarray `nums[l..r-1]` has `target` as its majority element if and only if `P[r] - P[l] > 0`, i.e. `P[l] < P[r]`. So the answer is the number of pairs `(l, r)` with `l < r` and `P[l] < P[r]`.

Since each step changes the prefix sum by exactly `±1`, the count of previously-seen prefixes strictly less than the *current* prefix (`less`) can be updated incrementally instead of with a Fenwick tree / BIT:

- On a `+1` step, the new prefix `p + 1` is strictly greater than every prefix that was `== p`, so those now count as "less": `less += cnt[p]`.
- On a `-1` step, the new prefix `p - 1` is strictly less than every prefix that was `== p - 1`... but those prefixes are no longer strictly less than the *new* prefix (they're equal to it now), so they must be removed from `less`: `less -= cnt[p - 1]`.

An offset array `cnt` (indexed by `prefix + n` to handle negative prefixes) records how many times each prefix value has been seen so far.

**Time complexity:** $O(n)$ - a single pass over `nums`, with $O(1)$ work per element.

**Space complexity:** $O(n)$ - the `cnt` array, sized `2n + 1` to cover prefix sums in `[-n, n]`.

```python
from typing import List


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        cnt = [0] * (2 * n + 1)  # prefix values range over [-n, n]; store at index v + n
        p = n                    # current prefix = 0, stored with the +n offset
        cnt[p] = 1                # P[0] = 0 has been "seen"
        less = 0                  # no earlier prefix is < 0 yet
        ans = 0

        for x in nums:
            if x == target:        # step +1
                less += cnt[p]      # prefixes equal to old p drop below the new p
                p += 1
            else:                   # step -1
                p -= 1
                less -= cnt[p]       # prefixes equal to new p were < old p; now equal, not less
            ans += less              # pairs (l, r) with P[l] < P[r] for this r
            cnt[p] += 1              # record P[r]
        return ans
```
