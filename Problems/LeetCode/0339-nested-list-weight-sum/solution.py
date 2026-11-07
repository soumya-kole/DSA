from typing import List, Union


class NestedInteger:
    """
    This is the interface that allows for creating nested lists.
    You should not implement it, or speculate about its implementation.

    A concrete implementation is provided here only so the test cases
    below can be built and run locally; on LeetCode this class (and its
    instances) is supplied by the judge.
    """

    def __init__(self, value: Union[int, List["NestedInteger"], None] = None):
        self._value = value

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return isinstance(self._value, int)

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        return self._value if self.isInteger() else None

    def getList(self) -> List["NestedInteger"]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        return None if self.isInteger() else self._value


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        pass


def build(value):
    if isinstance(value, list):
        return NestedInteger([build(v) for v in value])
    return NestedInteger(value)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([[1, 1], 2, [1, 1]], 10),
        ([1, [4, [6]]], 27),
        ([0], 0),
    ]

    passed = 0
    for i, (nested_list, expected) in enumerate(test_cases, 1):
        nested = [build(v) for v in nested_list]
        result = solution.depthSum(nested)
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"Test case {i}: {status} | nestedList={nested_list} | expected={expected} | got={result}")

    print(f"\n{passed}/{len(test_cases)} test cases passed")
