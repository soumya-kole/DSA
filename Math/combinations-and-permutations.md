# Combinations & Permutations

A tutorial on counting: how many ways can you select $r$ items from $n$ available items? The answer depends on just two questions.

## 1. The Two Key Questions

1. **Does order matter?**
   - Yes → **Permutation** ("which order?")
   - No → **Combination** ("which items?")
2. **Is repetition allowed?** (Can the same item be selected again?)
   - Yes → repetition formula
   - No → no-repetition formula

That gives exactly four cases:

| | Repetition allowed | No repetition |
|---|---|---|
| **Order matters (Permutation)** | $n^r$ | $\dfrac{n!}{(n-r)!}$ |
| **Order doesn't matter (Combination)** | $\dbinom{n+r-1}{r} = \dfrac{(n+r-1)!}{r!\,(n-1)!}$ | $\dbinom{n}{r} = \dfrac{n!}{r!\,(n-r)!}$ |

Throughout, $n$ = number of distinct items to choose from, $r$ = number of selections made.

## 2. The Multiplication Principle (the foundation)

Every formula above comes from one rule:

> If a process happens in independent steps, with $m_1$ choices in step 1, $m_2$ choices in step 2, …, then the total number of outcomes is $m_1 \times m_2 \times \dots \times m_k$.

**Example (two buckets):** Bucket 1 holds $\{A, B, C\}$, Bucket 2 holds $\{D, E, F\}$. Choose exactly one letter from each bucket:

$$AD,\ AE,\ AF,\ BD,\ BE,\ BF,\ CD,\ CE,\ CF$$

That's $3 \times 3 = 9$ outcomes. Note this is **not** an $\binom{n}{r}$ problem — it's a sequence of independent choices, so the product rule applies directly.

## 3. Permutation with Repetition: $n^r$

**Use when:** order matters and an item can be reused.

Each of the $r$ positions is an independent step with $n$ choices, so by the multiplication principle:

$$\underbrace{n \times n \times \dots \times n}_{r \text{ times}} = n^r$$

**Example:** A "combination" lock uses 3 digits, each from 0–9, digits may repeat:

$$10^3 = 1000 \text{ possibilities}$$

(Ironically, a combination lock is really a *permutation* lock — `1-2-3` and `3-2-1` open different locks.)

## 4. Permutation without Repetition: $\dfrac{n!}{(n-r)!}$

**Use when:** order matters and each item can be used at most once.

Again the multiplication principle, but each choice removes one option: $n$ choices for the first position, $n-1$ for the second, …, $n-r+1$ for the last:

$$n \times (n-1) \times \dots \times (n-r+1) = \frac{n!}{(n-r)!}$$

This is often written $P(n,r)$ or $^nP_r$.

**Example:** Award 1st and 2nd place among 10 people:

$$\frac{10!}{(10-2)!} = \frac{10!}{8!} = 10 \times 9 = 90$$

Order matters here: (Alice 1st, Bob 2nd) is a different outcome from (Bob 1st, Alice 2nd).

**Special case:** arranging *all* $n$ items ($r = n$) gives $\frac{n!}{0!} = n!$ arrangements.

## 5. Combination without Repetition: $\dbinom{n}{r} = \dfrac{n!}{r!\,(n-r)!}$

**Use when:** order doesn't matter and each item can be used at most once. This is the classic "n choose r", also written $C(n,r)$ or $^nC_r$.

**Derivation:** Start from the ordered count $\frac{n!}{(n-r)!}$. Every unordered selection of $r$ items was counted once for each of its $r!$ orderings — so divide the over-count out:

$$\binom{n}{r} = \frac{n!}{(n-r)!} \cdot \frac{1}{r!} = \frac{n!}{r!\,(n-r)!}$$

**Example:** Choose a team of 3 from 10 people:

$$\binom{10}{3} = \frac{10!}{3!\,7!} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = 120$$

$\{$Alice, Bob, Charlie$\}$ is the *same* team as $\{$Charlie, Alice, Bob$\}$ — only membership matters.

**Useful properties:**

- **Symmetry:** $\binom{n}{r} = \binom{n}{n-r}$ — choosing $r$ items to take is the same as choosing $n-r$ items to leave behind. E.g. $\binom{10}{7} = \binom{10}{3} = 120$.
- **Edge cases:** $\binom{n}{0} = \binom{n}{n} = 1$ (one way to take nothing, one way to take everything).
- **Pascal's rule:** $\binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r}$ — either a given item is in the selection or it isn't. This is the recurrence behind Pascal's triangle.

## 6. Combination with Repetition: $\dbinom{n+r-1}{r}$

**Use when:** order doesn't matter but an item may be selected multiple times. (Also called *multisets* or *multichoose*.)

$$\binom{n+r-1}{r} = \frac{(n+r-1)!}{r!\,(n-1)!}$$

### Ice-cream example

There are $n = 5$ flavors $\{A, B, C, D, E\}$ and you take $r = 3$ scoops. Repetition is allowed ($AAA$ is valid) and order doesn't matter ($AAB$ and $ABA$ are the same selection).

$$\binom{5+3-1}{3} = \binom{7}{3} = \frac{7!}{3!\,4!} = \frac{7 \times 6 \times 5}{3 \times 2 \times 1} = 35$$

### Why $n + r - 1$? (Stars and bars)

Since order doesn't matter, a selection is fully described by *how many of each flavor* you took. Write the counts as $r$ stars separated into $n$ groups by $n-1$ bars. With 5 flavors and 3 scoops:

$$\star\star \mid \star \mid\ \mid\ \mid \qquad \text{means } 2 \times A,\ 1 \times B$$
$$\mid\ \mid \star \mid \star \mid \star \qquad \text{means } 1 \times C,\ 1 \times D,\ 1 \times E$$

Every selection corresponds to exactly one arrangement of $3$ stars and $4$ bars — a string of $3 + 4 = 7$ symbols where we choose which $3$ positions are stars:

$$\binom{7}{3} = 35$$

In general there are $r$ stars and $n-1$ bars, i.e. $n+r-1$ positions, giving $\binom{n+r-1}{r}$.

**Same idea, other disguise:** the number of non-negative integer solutions to $x_1 + x_2 + \dots + x_n = r$ is also $\binom{n+r-1}{r}$ — each $x_i$ is the number of scoops of flavor $i$.

## 7. Worked Comparison: One Scenario, Four Answers

Pick $r = 2$ letters from $n = 3$ letters $\{A, B, C\}$:

| Case | Formula | Count | Outcomes |
|---|---|---|---|
| Order matters, repetition | $3^2$ | 9 | AA AB AC BA BB BC CA CB CC |
| Order matters, no repetition | $\frac{3!}{1!}$ | 6 | AB AC BA BC CA CB |
| Order doesn't matter, repetition | $\binom{4}{2}$ | 6 | AA AB AC BB BC CC |
| Order doesn't matter, no repetition | $\binom{3}{2}$ | 3 | AB AC BC |

Notice the counts only shrink as you add restrictions — removing order merges outcomes, forbidding repetition deletes outcomes.

## 8. Quick Decision Guide

```text
Independent steps/buckets?  →  multiply the choices (product rule)

Otherwise, ask:
  Does order matter?          YES → permutation      NO → combination
  Is repetition allowed?      YES → rep. formula     NO → no-rep. formula

                        Repetition          No repetition
Order matters           n^r                 n!/(n-r)!
Order doesn't matter    C(n+r-1, r)         C(n, r)
```

**Sanity checks when unsure:**

- Are `(Alice, Bob)` and `(Bob, Alice)` *different* outcomes? If yes, order matters → permutation.
- Is `AA` a *valid* outcome? If yes, repetition is allowed.
- Does the problem decompose into independent choices? If yes, just multiply.

## 9. In Code (Python)

```python
from math import comb, perm, factorial

comb(10, 3)        # C(10, 3) = 120        combination, no repetition
perm(10, 2)        # P(10, 2) = 90         permutation, no repetition
10 ** 3            # 1000                  permutation with repetition
comb(5 + 3 - 1, 3) # C(7, 3) = 35          combination with repetition
factorial(5)       # 120                   arrangements of all 5 items
```

---

*Based on [Maths Is Fun — Combinations and Permutations](https://www.mathsisfun.com/combinatorics/combinations-permutations.html).*
