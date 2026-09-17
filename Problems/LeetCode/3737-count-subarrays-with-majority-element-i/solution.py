from typing import List


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 2, 2, 3], 2, 5),
        ([1, 1, 1, 1], 1, 10),
        ([1, 2, 3], 4, 0),
        ([1], 1, 1),
        ([1], 2, 0),
        ([2, 2, 1, 2, 2], 2, 12),
    ]

    passed = 0
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = solution.countMajoritySubarrays(nums, target)
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"Test case {i}: {status} | nums={nums}, target={target} | expected={expected} | got={result}")

    print(f"\n{passed}/{len(test_cases)} test cases passed")
