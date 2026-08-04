from copy import deepcopy
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        pass

    def add(self, val: int) -> int:
        pass


if __name__ == "__main__":
    test_cases = [
        (
            ["KthLargest", "add", "add", "add", "add", "add"],
            [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]],
            [None, 4, 5, 5, 8, 8],
        ),
        (
            ["KthLargest", "add", "add", "add", "add"],
            [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]],
            [None, 7, 7, 7, 8],
        ),
        (
            ["KthLargest", "add", "add", "add"],
            [[1, []], [-3], [0], [4]],
            [None, -3, 0, 4],
        ),
        (
            ["KthLargest", "add", "add", "add", "add"],
            [[2, [0]], [-1], [1], [-2], [-4]],
            [None, -1, 0, 0, 0],
        ),
    ]

    passed = 0
    for i, (operations, arguments, expected) in enumerate(test_cases, 1):
        obj = KthLargest(*deepcopy(arguments[0]))
        result = [None]
        for op, args in zip(operations[1:], arguments[1:]):
            result.append(getattr(obj, op)(*args))
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"Test case {i}: {status} | operations={operations} | arguments={arguments} | expected={expected} | got={result}")

    print(f"\n{passed}/{len(test_cases)} test cases passed")
