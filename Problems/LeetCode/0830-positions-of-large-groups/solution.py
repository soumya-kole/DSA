from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        pass


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("abbxxxxzzy", [[3, 6]]),
        ("abc", []),
        ("abcdddeeeeaabbbcd", [[3, 5], [6, 9], [12, 14]]),
        ("aaa", [[0, 2]]),
        ("a", []),
        ("aabbccddeeaaffgg", []),
        ("aaaaaaaaaa", [[0, 9]]),
        ("aabbbaaa", [[2, 4], [5, 7]]),
    ]

    passed = 0
    for i, (s, expected) in enumerate(test_cases, 1):
        result = solution.largeGroupPositions(s)
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"Test case {i}: {status} | s={s!r} | expected={expected} | got={result}")

    print(f"\n{passed}/{len(test_cases)} test cases passed")
