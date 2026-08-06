import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
        ([2, 1], 2, 1),
        ([5, 5, 5, 5, 5], 3, 5),
        ([7, 6, 5, 4, 3, 2, 1], 1, 7),
    ]

    passed = 0
    for i, (nums, k, expected) in enumerate(test_cases, 1):
        result = solution.findKthLargest(list(nums), k)
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"Test case {i}: {status} | nums={nums}, k={k} | expected={expected} | got={result}")

    print(f"\n{passed}/{len(test_cases)} test cases passed")
