# 339. Nested List Weight Sum - Solutions

## Solution 1: DFS

Recurse through the nested structure, tracking the current depth. Whenever an element is a plain integer, add `value * depth` to the running total; whenever it's a list, recurse into it with `depth + 1`.

**Time complexity:** $O(n)$ - where $n$ is the total number of integers and lists across the whole nested structure, since each element is visited once.

**Space complexity:** $O(d)$ - for the recursion stack, where $d$ is the maximum nesting depth.

```python
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(items: List[NestedInteger], depth: int) -> int:
            total = 0
            for item in items:
                if item.isInteger():
                    total += item.getInteger() * depth
                else:
                    total += dfs(item.getList(), depth + 1)
            return total

        return dfs(nestedList, 1)
```

## Solution 2: BFS

Process the nested list level by level with a queue. At each level, pop every element currently in the queue: integers are added to that level's running sum, and lists have their contents pushed onto the queue for the next level. Add each level's sum to the total once per remaining level by accumulating an `unweighted` running sum that carries forward - equivalently, just multiply each level's sum by its depth directly.

**Time complexity:** $O(n)$ - each element is enqueued and processed exactly once.

**Space complexity:** $O(n)$ - for the BFS queue in the worst case (a flat list with no nesting).

```python
from collections import deque

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        queue = deque(nestedList)
        depth = 1
        total = 0

        while queue:
            for _ in range(len(queue)):
                item = queue.popleft()
                if item.isInteger():
                    total += item.getInteger() * depth
                else:
                    queue.extend(item.getList())
            depth += 1

        return total
```
