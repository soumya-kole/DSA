# 2645. Minimum Additions to Make Valid String - Solutions

## Solution 1: Greedy Grouping

We can't reorder or delete any letters of `word`, only insert. So whenever we hit an out-of-order pair (`word[i - 1] >= word[i]`), a new group must start — e.g. `"ba"` needs two groups (**a**b**c**a**bc**), since rearranging into a single `"abc"` isn't possible. Bold letters above are the ones inserted; `b` and `a` are `word`'s original letters, kept in order.

Every group needs exactly 3 letters, so `3 * groups - len(word)` is the number of additional letters required.

(Comparing characters directly only works here because `"abc"` is already in ASCII order; a pattern like `"mnc"` would need an explicit `order = {char: index}` map instead.)

**Time complexity:** $O(n)$ — a single pass over `word`.

**Space complexity:** $O(1)$ — only a running group count.

```python
class Solution:
    def addMinimum(self, word: str) -> int:
        groups = 1
        for i in range(1, len(word)):
            if word[i - 1] >= word[i]:
                groups += 1
        return 3 * groups - len(word)
```
