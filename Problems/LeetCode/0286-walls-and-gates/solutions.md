# 286. Walls and Gates - Solutions

## Solution 1: Multi-source BFS

Instead of running a BFS from every empty room to find its nearest gate, run a single BFS outward from all gates at once. Seed a queue with every gate's coordinates, then expand level by level: each step from the queue reaches cells exactly one step farther from the nearest gate than the cells that enqueued them. Skip walls and cells already visited (i.e. not still `INF`). Since the BFS expands uniformly from all gates simultaneously, the first time a room is reached is guaranteed to be via its nearest gate.

**Time complexity:** $O(mn)$ - each cell is enqueued and processed at most once.

**Space complexity:** $O(mn)$ - for the BFS queue in the worst case (e.g. all gates, no walls).

```python
from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms or not rooms[0]:
            return

        m, n = len(rooms), len(rooms[0])
        queue = deque(
            (r, c) for r in range(m) for c in range(n) if rooms[r][c] == 0
        )

        while queue:
            r, c = queue.popleft()
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and rooms[nr][nc] == 2**31 - 1:
                    rooms[nr][nc] = rooms[r][c] + 1
                    queue.append((nr, nc))
```
