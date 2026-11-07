# 84. Largest Rectangle in Histogram - Solutions

## Solution 1: Monotonic Stack

Walk the bars left to right, keeping a stack of indices whose heights are strictly increasing. When the current bar is shorter than the bar on top of the stack, that top bar can no longer extend rightward, so pop it and finalize the largest rectangle that uses it as the limiting height: the width spans from the index now exposed on top of the stack (exclusive) to the current index (exclusive). Append a sentinel `0` height at the end to flush any bars still on the stack once the array is exhausted.

**Time complexity:** $O(n)$ — each index is pushed and popped from the stack at most once.

**Space complexity:** $O(n)$ — for the stack of indices.

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack: List[int] = []
        max_area = 0
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                width = i if not stack else i - 1 - stack[-1]
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area
```
