from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([1, 2, 4, 3], 4),
        ([0, 2], 0),
    ]

    passed = 0
    for i, (height, expected) in enumerate(test_cases, 1):
        result = solution.maxArea(list(height))
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"Test case {i}: {status} | height={height} | expected={expected} | got={result}")

    print(f"\n{passed}/{len(test_cases)} test cases passed")
