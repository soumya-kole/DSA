# 703. Kth Largest Element in a Stream - Solutions

## Solution 1: Min-Heap of Size k

Keep only the `k` largest scores seen so far in a min-heap. The heap's root (`self.nums[0]`) is then the smallest of the `k` largest — i.e. exactly the `kth` largest overall.

The constructor heapifies the initial scores in place and trims the heap down to `k` elements by popping the smallest ones. Each `add` pushes the new score, trims back down to `k` (at most one pop), and returns the root. Scores that fall out of the top `k` can never re-enter it, so discarding them is safe.

**Time complexity:** Let $n$ be the initial size of `nums` and $x$ the number of `add` calls.

- Step 1 — heapify: $O(n)$. `heapify` on all $n$ elements is $O(n)$, **not** $O(n \log n)$ — bottom-up heap construction is linear.
- Step 2 — trimming pops: $O((n-k) \log n)$. Popping until only $k$ elements remain takes $n - k$ pops, each costing at most $\log n$.
- Constructor total: $O(n + (n-k) \log n)$ — worst case $O(n \log n)$ when $k = 1$.
- Step 3 — `add`: $O(\log k)$. The heap never holds more than $\sim k$ elements, so the push and the (at most one) trimming pop each cost $O(\log k)$.
- Total for $x$ calls to `add`: $O(n \log n) + x \cdot O(\log k)$ worst case.

**Space complexity:** $O(k)$ — only the top `k` elements are retained (momentarily $O(n)$ during construction, since we heapify the full input).

```python
import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        self._keep_k_largest()

    def _keep_k_largest(self):
        # keep only k largest values.
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.nums, val)
        self._keep_k_largest()
        return self.nums[0]
```
