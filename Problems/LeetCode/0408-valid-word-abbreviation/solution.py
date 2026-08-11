class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        pass

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("internationalization", "i12iz4n", True),
        ("apple", "a2e", False),
        ("substitution", "s10n", True),
        ("substitution", "sub4u4", True),
        ("substitution", "12", True),
        ("substitution", "su3i1u2on", True),
        ("substitution", "substitution", True),
        ("substitution", "s55n", False),
        ("substitution", "s010n", False),
        ("substitution", "s0ubstitution", False),
        ("a", "1", True),
        ("a", "01", False),
    ]

    passed = 0
    for i, (word, abbr, expected) in enumerate(test_cases, 1):
        result = solution.validWordAbbreviation(word, abbr)
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"Test case {i}: {status} | word={word!r}, abbr={abbr!r} | expected={expected} | got={result}")

    print(f"\n{passed}/{len(test_cases)} test cases passed")
