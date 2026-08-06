# 378. Kth Smallest Element in a Sorted Matrix - Solutions

## Solution 1: Min-Heap Seeded by Row Heads

Seed a min-heap with the first `min(n_rows, k)` row heads, then pop `k - 1` times. Each pop yields the next smallest element of the whole matrix in order, so after `k - 1` pops the root of the heap is the `kth` smallest.

This works because every pop gives the next smallest element of the whole matrix, in order. Instead of heapifying every element of the matrix, we only need a seed — the heap always holds the smallest not-yet-popped element of each row, and since every row is sorted, the smallest remaining element of the whole matrix has to be the smallest remaining element of some row.

When popping an element, if the popped element has another item in the same row, that item is pushed. If not, nothing is pushed and the heap just becomes one element smaller — that row is finished, so it should not be in the heap anymore, and the other rows still have their smallest remaining element in the heap, so the root is still correct.

**Seeding optimization:** instead of seeding with every row, only the first `min(n_rows, k)` rows can matter. If `k` is less than the number of rows, seed with only `k` rows (using, e.g., the first column). This is allowed because the first column is sorted — `matrix[k][0]` already has `k` elements above it that are smaller or equal, and the rest of row `k` is even bigger, so row `k` onwards cannot be in the top `k`.

The heap never becomes empty before `k - 1` pops complete: if `k <= n_rows`, `k` rows were seeded and every row has at least one element, so at least `k` elements are available; if `k > n_rows`, all rows were seeded, and the matrix has `n_rows * n_cols >= k` elements.

```python
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n_rows, n_cols = len(matrix), len(matrix[0])

        # Seed: head of each row. Only the first min(n, k) rows can matter.
        heap = [(matrix[r][0], r, 0) for r in range(min(n_rows, k))]
        heapq.heapify(heap)

        # Pop k-1 times; the k-th smallest is then at the root.
        for _ in range(k - 1):
            _, r, c = heapq.heappop(heap)
            if c + 1 < n_cols:
                heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))

        return heap[0][0]
```

**Time complexity:** let `m = min(n_rows, k)` — the heap never holds more than `m` entries.

| Step | Cost |
|---|---|
| Build the seed list | $O(m)$ |
| `heapify` | $O(m)$ (linear, not $m \log m$) |
| Loop: `k - 1` iterations | each is `heappop` + `heappush` = $O(\log m)$ |
| **Total** | $O(m + k \log m)$ |

Since `m <= k`, the `k log m` term dominates: $O(k \log \min(n_{rows}, k))$.

Worst case `k = n^2` (per the constraints), so time is $O(n^2 \log n)$ and space is $O(n)$.

**Space complexity:** $O(\min(n_{rows}, k))$ — the heap size.

## Solution 2: Binary Search on Value + Staircase Count

Binary search over the *value range* `[matrix[0][0], matrix[n-1][n-1]]` instead of over indices. For a candidate value `x`, count how many elements are `<= x` with a staircase walk starting at the bottom-left corner, and use that count to binary-search for the smallest value whose count is `>= k` — that value is guaranteed to be an actual element of the matrix, so it's the `kth` smallest.

The staircase walk (`count_le`) exploits both sort orders at once. Starting at `(r, c) = (n_rows - 1, 0)`:

- If `matrix[r][c] <= x`: column `c` is sorted ascending top-to-bottom, so every element above row `r` in that column is also `<= x`. That's `r + 1` elements (rows `0..r`), all counted in one step. Move right (`c += 1`) to check the next column.
- Otherwise: `matrix[r][c]` and everything below/right of it is `> x`, so move up (`r -= 1`).

Each step moves either right or up, and there are at most `n_cols - 1` right-moves and `n_rows - 1` up-moves, so one `count_le` call is $O(n_{rows} + n_{cols})$.

The outer binary search narrows `[lo, hi]` over the value range rather than over `k` or indices — `count_le` is a monotonically non-decreasing step function of `x`, so the smallest `x` with `count_le(x) >= k` is well-defined and is always achieved at an actual matrix value (the search converges to it because `hi` is only ever pulled down to values that *are* in the matrix, starting from `matrix[n-1][n-1]`).

```python
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n_rows, n_cols = len(matrix), len(matrix[0])

        def count_le(x: int) -> int:
            """How many elements are <= x. Staircase walk, O(rows + cols)."""
            cnt, r, c = 0, n_rows - 1, 0      # start bottom-left
            while r >= 0 and c < n_cols:
                if matrix[r][c] <= x:
                    cnt += r + 1              # this cell + everything above it in column c
                    c += 1                    # move right
                else:
                    r -= 1                    # move up
            return cnt

        lo, hi = matrix[0][0], matrix[n_rows - 1][n_cols - 1]
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if count_le(mid) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo
```

**Time complexity:** each `count_le` call is $O(n_{rows} + n_{cols})$, and the binary search runs over the value range `[matrix[0][0], matrix[n-1][n-1]]`, taking $O(\log(\text{max} - \text{min}))$ iterations. Total: $O((n_{rows} + n_{cols}) \log(\text{max} - \text{min}))$.

For an `n x n` matrix this is $O(n \log(\text{max} - \text{min}))$ — independent of `k`, which makes it preferable to Solution 1 when `k` is close to `n^2`.

**Space complexity:** $O(1)$ auxiliary space — no heap, just a handful of pointers. This is what satisfies the problem's better-than-$O(n^2)$ memory requirement most comfortably.
