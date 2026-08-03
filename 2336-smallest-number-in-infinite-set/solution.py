class SmallestInfiniteSet:

    def __init__(self):
        pass

    def popSmallest(self) -> int:
        pass

    def addBack(self, num: int) -> None:
        pass


if __name__ == "__main__":
    test_cases = [
        (
            ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest",
             "addBack", "popSmallest", "popSmallest", "popSmallest"],
            [[], [2], [], [], [], [1], [], [], []],
            [None, None, 1, 2, 3, None, 1, 4, 5],
        ),
        (
            ["SmallestInfiniteSet", "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest"],
            [[], [], [], [], [], []],
            [None, 1, 2, 3, 4, 5],
        ),
        (
            ["SmallestInfiniteSet", "addBack", "popSmallest"],
            [[], [1000], []],
            [None, None, 1],
        ),
        (
            ["SmallestInfiniteSet", "popSmallest", "popSmallest", "addBack", "addBack", "popSmallest", "popSmallest"],
            [[], [], [], [1], [1], [], []],
            [None, 1, 2, None, None, 1, 3],
        ),
        (
            ["SmallestInfiniteSet", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest"],
            [[], [], [], [], [2], [], []],
            [None, 1, 2, 3, None, 2, 4],
        ),
        (
            ["SmallestInfiniteSet", "popSmallest", "addBack", "addBack", "popSmallest",
             "addBack", "popSmallest", "popSmallest", "popSmallest"],
            [[], [], [1], [2], [], [1], [], [], []],
            [None, 1, None, None, 1, None, 1, 2, 3],
        ),
    ]

    passed = 0
    for i, (operations, arguments, expected) in enumerate(test_cases, 1):
        obj = SmallestInfiniteSet()
        result = [None]
        for op, args in zip(operations[1:], arguments[1:]):
            result.append(getattr(obj, op)(*args))
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"Test case {i}: {status} | operations={operations} | arguments={arguments} | expected={expected} | got={result}")

    print(f"\n{passed}/{len(test_cases)} test cases passed")
