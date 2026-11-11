# 1152. Analyze User Website Visit Pattern - Solutions

## Solution 1: Group by User, Enumerate 3-Subsequences

Group the visits by `username`, sorting each user's visits by `timestamp` to recover the order they were made in. For each user, every distinct combination of 3 indices `i < j < k` into their sorted visit list yields a candidate pattern `(website[i], website[j], website[k])` — these are exactly the length-3 subsequences of websites that user visited in order (the websites don't need to be contiguous or distinct).

To score a pattern, count how many *distinct users* have that pattern among their subsequences — not how many times it occurs in total, since a single user can produce the same pattern more than once (e.g. visiting `"home"` three times) but should only contribute 1 to that pattern's score. Deduplicating per user before tallying (via a `set` of that user's patterns) handles this.

Once every pattern has a score, the answer is the pattern with the highest score, breaking ties by lexicographic order — which falls out of sorting by the key `(-score, pattern)` and taking the minimum.

**Time complexity:** $O(n \cdot m^3)$ in the worst case, where $n$ is the number of distinct users and $m$ is the maximum number of websites visited by a single user — generating all 3-combinations for one user costs $O(m^3)$, and `n` is bounded by the total number of visits (at most 50 per the constraints).

**Space complexity:** $O(n \cdot m^3)$ for the pattern score map in the worst case (all generated patterns are distinct).

```python
from collections import defaultdict
from itertools import combinations


class Solution:
    def mostVisitedPattern(
        self, username: list[str], timestamp: list[int], website: list[str]
    ) -> list[str]:
        visits = defaultdict(list)
        for user, time, site in zip(username, timestamp, website):
            visits[user].append((time, site))

        score = defaultdict(int)
        for pairs in visits.values():
            pairs.sort()
            sites = [site for _, site in pairs]
            for pattern in set(combinations(sites, 3)):
                score[pattern] += 1

        best = min(score, key=lambda pattern: (-score[pattern], pattern))
        return list(best)
```
