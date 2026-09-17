class Solution:
    def addMinimum(self, word: str) -> int:
        pass


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("b", 2),
        ("aaa", 6),
        ("abc", 0),
        ("a", 2),
        ("abcabc", 0),
        ("aabc", 2),
        ("bca", 3),
        ("cba", 6),
        ("abcabcabc", 0),
        ("ccc", 6),
    ]

    passed = 0
    for i, (word, expected) in enumerate(test_cases, 1):
        result = solution.addMinimum(word)
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"Test case {i}: {status} | word={word!r} | expected={expected} | got={result}")

    print(f"\n{passed}/{len(test_cases)} test cases passed")
