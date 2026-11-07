from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([2, 1, 5, 6, 2, 3], 10),
        ([2, 4], 4),
        ([1], 1),
        ([0], 0),
        ([2, 1, 2], 3),
        ([5, 4, 1, 2], 8),
    ]

    passed = 0
    for i, (heights, expected) in enumerate(test_cases, 1):
        result = solution.largestRectangleArea(list(heights))
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"Test case {i}: {status} | heights={heights} | expected={expected} | got={result}")

    print(f"\n{passed}/{len(test_cases)} test cases passed")
