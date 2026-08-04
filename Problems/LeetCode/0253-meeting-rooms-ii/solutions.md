# 253. Meeting Rooms II - Solutions

## Solution 1: Heap (Priority Queue)

Use a min-heap to track when rooms become available. For each meeting, if the earliest available room has finished before the current meeting starts, reuse it; otherwise, allocate a new room.

**Time complexity:** $O(n \log n)$, broken down as:

- Sorting the intervals: $O(n \log n)$.
- Heap operations: each of the $n$ meetings does at most one `heappop` and exactly one `heappush`. Each operation costs $O(\log k)$ where $k$ is the current heap size (number of rooms allocated so far), so $O(\log n)$ in the worst case — $2n$ operations total gives $O(n \log n)$.
- Reading the minimum end time (`min_heap[0]`) is $O(1)$, so the comparison per meeting adds nothing.

Total: $O(n \log n) + O(n \log n) = O(n \log n)$.

**Space complexity:** $O(n)$ - heap can have at most n rooms.

```python
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        iv = sorted(intervals, key=lambda x: x[0])
        min_heap = [iv[0][1]]  # min-heap of end times, one entry per room in use
        for start, end in iv[1:]:
            # intervals are half-open: a meeting starting at or after the
            # earliest end time can reuse that room
            if start >= min_heap[0]:
                heapq.heappop(min_heap)  # meeting room is freed up
            # reuse the freed room, or claim a new one if nothing was popped
            heapq.heappush(min_heap, end)
        return len(min_heap)
```

## Solution 2: Two Pointers (Optimal)

Sort start times and end times separately. Use two pointers to scan through both arrays. Increment the room count when a meeting starts before the earliest end time, and decrement when a meeting ends before the next start.

**Time complexity:** $O(n \log n)$ - dominated by sorting.

**Space complexity:** $O(n)$ - for the start and end arrays.

```python
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted(s for s, _ in intervals)
        ends = sorted(e for _, e in intervals)
        
        s_ptr = e_ptr = 0
        rooms = 0
        
        while s_ptr < len(intervals):
            if starts[s_ptr] < ends[e_ptr]:
                rooms += 1
                s_ptr += 1
            else:
                rooms -= 1
                e_ptr += 1
        
        return rooms
```
