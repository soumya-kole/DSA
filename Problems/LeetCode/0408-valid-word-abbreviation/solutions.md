# 408. Valid Word Abbreviation - Solutions

## Solution 1: Two Pointers

Walk `word` and `abbr` simultaneously with pointers `i` and `j`. At each step, exactly one of two things can happen:

- `word[i] == abbr[j]`: the current letter matches literally, so advance both pointers by one.
- Otherwise, `abbr[j]` must be a digit for the abbreviation to still be valid. Reject immediately on a leading `'0'`. Otherwise, consume the *entire* run of consecutive digits starting at `j` into `num` (digits can be multiple characters, e.g. `"12"`), and skip `word[i]` forward by `num` positions. If `abbr[j]` is neither a matching letter nor a digit, the abbreviation is invalid.

The loop stops when either string is exhausted. The final check `i == len(word) and j == len(abbr)` confirms both strings were fully consumed in lockstep — if `word` still has leftover letters, or `abbr` has an unconsumed trailing digit run, the match is invalid.

**Time complexity:** $O(m + n)$, where $m$ and $n$ are the lengths of `word` and `abbr` — each pointer only moves forward, and the inner digit-run loop never revisits a character already advanced past.

**Space complexity:** $O(1)$ — only the two pointers and the digit accumulator `num` are kept.

```python
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                i += num
            else:
                return False
        return i == len(word) and j == len(abbr)
```
