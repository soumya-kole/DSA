# 772. Basic Calculator III - Solutions

## Solution 1: Recursion + Stack

Consume the string once as a shared `deque`, `q`, passed into a recursive `dfs(q)` — `q` is mutated in place, so nested calls resume exactly where the caller left off. Each call handles one "level" of parentheses: it accumulates digits into `num`, and `sign` holds the operator from the *previous* delimiter — one step behind — so that when the *next* delimiter (or end of input) is reached, `sign` says how to combine the just-finished `num` into `stk`:

- `+` / `-`: push `num` (or `-num`) onto `stk` — addition and subtraction are deferred to a final sum, since a later `*` or `/` might still need to combine with the most recent pushed value.
- `*` / `/`: pop the top of `stk`, combine it with `num` immediately, and push the result back — multiplication and division bind tighter than the pending sum, so they're applied eagerly instead of being deferred like `+`/`-`.

The flush condition is `c in "+-*/)" or not q`: it fires on any operator, on `')'`, and also when `q` runs out — which covers both the very end of the whole expression and the case where a `'('` branch consumes the rest of `q` (leaving nothing after the recursive call returns). Encountering `'('` triggers a recursive `dfs(q)` call that evaluates the sub-expression up to its matching `')'` and returns that value, which is then treated as `num` for the enclosing level.

`')'` doesn't get its own separate check — it satisfies the same flush condition as an operator, since the number just before it needs to be finalized exactly the same way. The only thing actually special about `')'` is that this level of recursion is done, so the `break` is nested right inside the flush block (guarded by `if c == ")"`) instead of duplicating the `match` logic in a second branch.

Integer division truncates toward zero, which `int(a / b)` gives directly (Python's `//` instead floors, which differs from truncation for negative results).

**Time complexity:** $O(n)$, where $n$ is the length of `s` — each character is visited exactly once, and every stack push/pop is $O(1)$.

**Space complexity:** $O(n)$ — the recursion depth is bounded by the nesting depth of parentheses, and each level's `stk` holds at most as many terms as digits/operators at that level, both worst-case $O(n)$.

```python
from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        def dfs(q):
            num, sign, stk = 0, "+", []
            while q:
                c = q.popleft()
                if c.isdigit():
                    num = num * 10 + int(c)
                if c == "(":
                    num = dfs(q)
                if c in "+-*/)" or not q:
                    match sign:
                        case "+":
                            stk.append(num)
                        case "-":
                            stk.append(-num)
                        case "*":
                            stk.append(stk.pop() * num)
                        case "/":
                            stk.append(int(stk.pop() / num))
                    num, sign = 0, c
                    if c == ")":
                        break
            return sum(stk)

        return dfs(deque(s))
```
