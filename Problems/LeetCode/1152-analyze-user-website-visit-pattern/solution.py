class Solution:
    def mostVisitedPattern(
        self, username: list[str], timestamp: list[int], website: list[str]
    ) -> list[str]:
        pass

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (
            (
                ["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"],
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                ["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"],
            ),
            ["home", "about", "career"],
        ),
        (
            (
                ["ua", "ua", "ua", "ub", "ub", "ub"],
                [1, 2, 3, 4, 5, 6],
                ["a", "b", "a", "a", "b", "c"],
            ),
            ["a", "b", "a"],
        ),
    ]

    passed = 0
    for i, ((username, timestamp, website), expected) in enumerate(test_cases, 1):
        result = solution.mostVisitedPattern(username, timestamp, website)
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(
            f"Test case {i}: {status} | username={username}, timestamp={timestamp}, website={website} "
            f"| expected={expected} | got={result}"
        )

    print(f"\n{passed}/{len(test_cases)} test cases passed")
