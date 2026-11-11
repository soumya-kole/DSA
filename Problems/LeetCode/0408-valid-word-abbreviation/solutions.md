# 408. Valid Word Abbreviation - Solutions

## Solution 1: Two Pointers

Walk `word` and `abbr` simultaneously with pointers `i` and `j`. At each step, exactly one of two things can happen:

- `word[i] == abbr[j]`: the current letter matches literally, so advance both pointers by one.
- Otherwise, `abbr[j]` must be a digit for the abbreviation to still be valid. Reject immediately on a leading `'0'`. Otherwise, consume the *entire* run of consecutive digits starting at `j` into `num` (digits can be multiple characters, e.g. `"12"`), and skip `word[i]` forward by `num` positions. If `abbr[j]` is neither a matching letter nor a digit, the abbreviation is invalid.

The loop stops when either string is exhausted. The final check `i == len(word) and j == len(abbr)` confirms both strings were fully consumed in lockstep — if `word` still has leftover letters, or `abbr` has an unconsumed trailing digit run, the match is invalid.

**Time complexity:** $O(n)$, where $n$ is the length of `abbr` — every outer-loop pass advances `j` by at least one, either directly in the literal-match branch or through the inner digit-run loop (which runs at least once whenever it's entered), so the loop can execute at most `n` times total. The length of `word`, $m$, doesn't add to this: `i += num` is a single O(1) jump regardless of how large `num` is, never a loop over `word`'s characters.

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
