# 215. Kth Largest Element in an Array - Solutions

## Solution 1: Quickselect (Optimal Average Case)

Pick a random pivot and three-way partition `nums` into `left` (greater than pivot), `mid` (equal to pivot), and `right` (less than pivot). Compare `k` against the sizes of `left` and `mid` to decide whether the answer lies in `left`, is the pivot itself, or lies in `right` — and recurse into only that one side.

**Time complexity:**

- One call does three linear scans of the current slice to build `left`, `mid`, `right`: $O(n)$ work (ignoring recursion).
- Only one side (`left` or `right`) is recursed into, never both — this is what keeps quickselect faster than quicksort, which recurses into both halves.
- **Average case:** a random pivot lands in the middle half of the array with probability $\frac{1}{2}$, so in expectation the surviving side shrinks by a constant fraction each call: $T(n) = T(n/2) + O(n)$, which expands to $n + n/2 + n/4 + \dots = O(n)$ (geometric series). This beats sorting, which is $O(n \log n)$.
- **Worst case:** every pivot happens to be the max (or min) of its slice, so one side has $n-1$ elements and only one element is peeled off per call: $T(n) = T(n-1) + O(n) = n + (n-1) + (n-2) + \dots = O(n^2)$. Since the pivot is chosen with `random.choice`, this isn't triggered by any specific input — you'd need to lose a random coin flip roughly $n$ times in a row.

Average: $O(n)$. Worst: $O(n^2)$.

**Space complexity:**

- Recursion depth: $O(\log n)$ average, $O(n)$ worst (Python has no tail-call elimination, so each pending call really does hold a stack frame).
- `left`/`mid`/`right` allocated per call stay alive while the recursive call runs, so they add up down the stack: $O(n)$ average, $O(n^2)$ worst.

Average: $O(n)$. Worst: $O(n^2)$.

Note this is not the in-place Hoare/Lomuto quickselect (which is $O(1)$ auxiliary space, $O(\log n)$ stack) — the three-way split trades memory for much simpler, bug-free code, and it also makes duplicates safe: an all-equal array like `[5,5,5,5,5]` puts everything into `mid` and returns immediately, whereas a naive two-way partition can degrade badly on heavy duplicates.

```python
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return
        p = random.choice(nums)
        left = [n for n in nums if n > p]
        mid = [n for n in nums if n == p]
        right = [n for n in nums if n < p]
        L, M = len(left), len(mid)
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L and k <= L + M:
            return mid[0]
        else:
            return self.findKthLargest(right, k - L - M)
```

## Solution 2: Min-Heap of Size k

Heapify the whole array into a min-heap, then pop the smallest element until only `k` elements remain. The root of what's left is the `kth` largest.

**Time complexity:** $O(n \log n)$ — `heapify` is $O(n)$, but popping down to size `k` costs up to $O(n \log n)$ in the worst case ($k$ close to $1$). A min-heap of size `k` built incrementally (push each of the `n` elements, popping when the heap exceeds size `k`) gets this down to $O(n \log k)$, which is better when `k` is small or the data is streaming.

**Space complexity:** $O(n)$ — `heapify` mutates `nums` in place, but conceptually the heap holds all `n` elements before shrinking to `k`.

```python
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]
```

## Comparison

| Approach | Time | Space |
|---|---|---|
| Sort then index | $O(n \log n)$ | $O(1)$ / $O(n)$ (sort dependent) |
| Min-heap of size k | $O(n \log k)$ | $O(k)$ |
| Quickselect (this) | $O(n)$ average, $O(n^2)$ worst | $O(n)$ average, $O(n^2)$ worst |
| Introselect (median-of-medians fallback) | $O(n)$ guaranteed worst case | — (large constants make it slower in practice) |
