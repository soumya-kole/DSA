from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        pass

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (([10, 1, 2, 7, 6, 1, 5], 8), [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
        (([2, 5, 2, 1, 2], 5), [[1, 2, 2], [5]]),
    ]

    passed = 0
    for i, ((candidates, target), expected) in enumerate(test_cases, 1):
        result = solution.combinationSum2(candidates, target)
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"Test case {i}: {status} | candidates={candidates}, target={target} | expected={expected} | got={result}")

    print(f"\n{passed}/{len(test_cases)} test cases passed")
