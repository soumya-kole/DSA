# 252. Meeting Rooms - Solutions

## Solution 1: Sorting

Sort the meetings by start time, then scan through the sorted list. If a meeting starts before the previous meeting ends, there's an overlap, so the person can't attend all meetings.

**Time complexity:** $O(n \log n)$ - dominated by the sort.

**Space complexity:** $O(\log n)$ - space used by the sort (or $O(1)$ if sorting in place with an iterative sort).

```python
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        return all(a[1] <= b[0] for a, b in pairwise(intervals))
```
