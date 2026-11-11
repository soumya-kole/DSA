from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        pass

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ((3, 7), [[1, 2, 4]]),
        ((3, 9), [[1, 2, 6], [1, 3, 5], [2, 3, 4]]),
        ((4, 1), []),
    ]

    passed = 0
    for i, ((k, n), expected) in enumerate(test_cases, 1):
        result = solution.combinationSum3(k, n)
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"Test case {i}: {status} | k={k}, n={n} | expected={expected} | got={result}")

    print(f"\n{passed}/{len(test_cases)} test cases passed")
