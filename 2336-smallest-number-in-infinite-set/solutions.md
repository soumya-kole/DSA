# 2336. Smallest Number in Infinite Set - Solutions

## Solution 1: Min-Heap + Popped Set + Counter

The infinite set is always "everything from `smallest` upward" plus whatever was popped and then added back. So track three things:

- `smallest` — the smallest positive integer that has *never* been popped. Everything from `smallest` upward (and not popped) is implicitly in the set, so we never need to materialize the infinite tail.
- `q` — a min-heap of numbers that were popped and later added back (all `< smallest`).
- `popped` — a hash set of numbers currently *out* of the set, used to make `addBack` a no-op for numbers that are still in the set and to prevent heap duplicates.

`popSmallest` takes from the heap if it's non-empty (anything in the heap is `< smallest`); otherwise it returns `smallest` and increments the counter. `addBack(num)` only does anything if `num` was actually popped: it pushes `num` onto the heap and clears it from `popped`.

**Time complexity:** Let $m$ be the total number of operations performed and $n$ the number of elements currently in the heap ($n \le m$).

- `__init__`: $O(1)$
- `popSmallest`: $O(1)$ average when the heap is empty (counter increment + set insert); $O(\log n)$ when non-empty (`heapq.heappop`). Overall $O(\log n)$ worst case.
- `addBack`: $O(1)$ average set lookup/removal + $O(\log n)$ heap insertion (`heapq.heappush`). Overall $O(\log n)$.

Note: set operations are $O(1)$ on average; worst case is $O(\text{size})$ under adversarial hashing, and resizing is amortized $O(1)$.

**Space complexity:** $O(m)$.

- `q` stores numbers added back but not yet re-popped — bounded by the number of `addBack` calls.
- `popped` stores every number popped and not added back — bounded by the number of `popSmallest` calls, and never shrinks except via `addBack`.
- Neither is bounded by the heap size: 1000 `popSmallest` calls with no `addBack` leaves the heap empty but `popped` holding 1000 elements. So the space is $O(m)$, not $O(n)$.

```python
import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.popped = set()
        self.q = []
        self.smallest = 1

    def popSmallest(self) -> int:
        if len(self.q) == 0:
            result = self.smallest
            self.smallest += 1
        else:
            result = heapq.heappop(self.q)
        self.popped.add(result)
        return result

    def addBack(self, num: int) -> None:
        if num in self.popped:
            heapq.heappush(self.q, num)
            self.popped.remove(num)
```
