from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        pass

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (([2, 3, 6, 7], 7), [[2, 2, 3], [7]]),
        (([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        (([2], 1), []),
    ]

    passed = 0
    for i, ((candidates, target), expected) in enumerate(test_cases, 1):
        result = solution.combinationSum(candidates, target)
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"Test case {i}: {status} | candidates={candidates}, target={target} | expected={expected} | got={result}")

    print(f"\n{passed}/{len(test_cases)} test cases passed")
