import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([[0, 30], [5, 10], [15, 20]], 2),
        ([[7, 10], [2, 4]], 1),
        ([[1, 5]], 1),
        ([[0, 30], [5, 10]], 2),
        ([[1, 2], [3, 4]], 1),
        ([[1, 10], [2, 7], [10, 13], [13, 15], [15, 20]], 2),
    ]

    passed = 0
    for i, (intervals, expected) in enumerate(test_cases, 1):
        result = solution.minMeetingRooms(intervals)
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"Test case {i}: {status} | intervals={intervals} | expected={expected} | got={result}")

    print(f"\n{passed}/{len(test_cases)} test cases passed")
