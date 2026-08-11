# 11. Container With Most Water - Solutions

## Solution 1: Two Pointers

Start with the widest possible container, one pointer at each end of `height`. The area is bounded by the shorter of the two lines, so at each step move the pointer at the shorter line inward — moving the taller one can only shrink the width without any chance of increasing the limiting height, so it can never produce a better area. Keep track of the best area seen while the pointers close in.

**Time complexity:** $O(n)$ — each pointer moves at most `n` times total, and every step does $O(1)$ work.

**Space complexity:** $O(1)$ — only the two pointers and a running best are kept.

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        best = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            best = max(best, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best
```
