# 830. Positions of Large Groups - Solutions

## Solution 1: Two Pointers

Scan `s` with a pointer `i` marking the start of the current run of identical characters, and advance a second pointer `j` while `s[j] == s[i]`. Once the run ends, `j - i` is its length — if it's at least 3, record `[i, j - 1]`. Then move `i` to `j` and repeat until `i` reaches the end of `s`.

**Time complexity:** $O(n)$ — each character is visited once.

**Space complexity:** $O(1)$ extra, not counting the output list.

```python
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = []
        i, n = 0, len(s)
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            if j - i >= 3:
                ans.append([i, j - 1])
            i = j
        return ans
```
