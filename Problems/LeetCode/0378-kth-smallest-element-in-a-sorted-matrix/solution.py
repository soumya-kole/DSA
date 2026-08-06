import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8, 13),
        ([[-5]], 1, -5),
        ([[1, 2], [1, 3]], 2, 1),
        ([[1, 2, 3, 4, 5]], 3, 3),
        ([[1, 2], [3, 4]], 4, 4),
        ([[2, 2], [2, 2]], 3, 2),
    ]

    passed = 0
    for i, (matrix, k, expected) in enumerate(test_cases, 1):
        result = solution.kthSmallest(matrix, k)
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"Test case {i}: {status} | matrix={matrix}, k={k} | expected={expected} | got={result}")

    print(f"\n{passed}/{len(test_cases)} test cases passed")
