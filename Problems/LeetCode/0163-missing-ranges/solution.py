from itertools import pairwise
from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        pass

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (([0, 1, 3, 50, 75], 0, 99), [[2, 2], [4, 49], [51, 74], [76, 99]]),
        (([-1], -1, -1), []),
        (([], 1, 1), [[1, 1]]),
        (([], -3, -1), [[-3, -1]]),
        (([1, 2, 3], 1, 3), []),
        (([5], 1, 10), [[1, 4], [6, 10]]),
    ]

    passed = 0
    for i, ((nums, lower, upper), expected) in enumerate(test_cases, 1):
        result = solution.findMissingRanges(nums, lower, upper)
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"Test case {i}: {status} | nums={nums}, lower={lower}, upper={upper} | expected={expected} | got={result}")

    print(f"\n{passed}/{len(test_cases)} test cases passed")
