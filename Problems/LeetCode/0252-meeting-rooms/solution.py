from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        pass


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([[0, 30], [5, 10], [15, 20]], False),
        ([[7, 10], [2, 4]], True),
        ([], True),
        ([[1, 5]], True),
        ([[5, 10], [10, 15]], True),
    ]

    passed = 0
    for i, (intervals, expected) in enumerate(test_cases, 1):
        result = solution.canAttendMeetings(intervals)
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"Test case {i}: {status} | intervals={intervals} | expected={expected} | got={result}")

    print(f"\n{passed}/{len(test_cases)} test cases passed")
