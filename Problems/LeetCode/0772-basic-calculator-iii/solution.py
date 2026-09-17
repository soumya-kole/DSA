class Solution:
    def calculate(self, s: str) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("1+1", 2),
        ("6-4/2", 4),
        ("2*(5+5*2)/3+(6/2+8)", 21),
        ("(1)", 1),
        ("0", 0),
        ("3+2*2", 7),
        ("14/3*2", 8),
        ("(1+(4+5+2)-3)+(6+8)", 23),
        ("100*(2+12)", 1400),
        ("2-4/2", 0),
    ]

    passed = 0
    for i, (s, expected) in enumerate(test_cases, 1):
        result = solution.calculate(s)
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"Test case {i}: {status} | s={s!r} | expected={expected} | got={result}")

    print(f"\n{passed}/{len(test_cases)} test cases passed")
