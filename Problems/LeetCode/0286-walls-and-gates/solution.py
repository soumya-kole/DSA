from typing import List

INF = 2**31 - 1


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        pass


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (
            [
                [INF, -1, 0, INF],
                [INF, INF, INF, -1],
                [INF, -1, INF, -1],
                [0, -1, INF, INF],
            ],
            [
                [3, -1, 0, 1],
                [2, 2, 1, -1],
                [1, -1, 2, -1],
                [0, -1, 3, 4],
            ],
        ),
        ([[-1]], [[-1]]),
        ([[0]], [[0]]),
        ([[INF]], [[INF]]),
    ]

    passed = 0
    for i, (rooms, expected) in enumerate(test_cases, 1):
        solution.wallsAndGates(rooms)
        ok = rooms == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"Test case {i}: {status} | expected={expected} | got={rooms}")

    print(f"\n{passed}/{len(test_cases)} test cases passed")
