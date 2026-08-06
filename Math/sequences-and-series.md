# Sequences & Series

## 1. Definition of a Sequence

- **Definition:** An ordered list of numbers that follows a specific rule or pattern.
- **Notation:** Terms are indexed by position ($a_1, a_2, a_3, \dots, a_n$), where $a_n$ is the general (nth) term.
- **Example:** For sequence $3, 6, 9, 12, 15, \dots$, the general term formula is $a_n = 3n$.

## 2. Arithmetic Sequences

- **Definition:** A sequence where each consecutive term increases or decreases by a constant value called the **common difference** ($d$).
- **General Term Formula:**
  $$a_n = a_1 + (n - 1)d$$
  *(where $a_1$ is the first term and $n$ is the term number)*

## 3. Geometric Sequences

- **Definition:** A sequence where each consecutive term is found by multiplying the previous term by a constant value called the **common ratio** ($r$).
- **General Term Formula:**
  $$a_n = a_1 \cdot r^{n-1}$$

## 4. Recursive Sequences

- **Definition:** A sequence where each term is defined using one or more previous terms.
- **Requirement:** Must specify at least the initial term ($a_1$).
- **Example:** $a_1 = 2$, $a_n = 2 \cdot a_{n-1}$ produces $2, 4, 8, 16, \dots$

## 5. Definition of a Series

- **Definition:** The sum of the terms of a sequence.
- **Notation:** $S_n$ represents the sum of the first $n$ terms ($S_n = a_1 + a_2 + \dots + a_n$).

## 6. Sigma Notation (∑)

- **Definition:** A compact mathematical notation used to denote the sum of a sequence.
- **Structure:**
  $$\sum_{i=1}^{n} a_i$$
  *(sum of terms $a_i$ from lower limit $i = 1$ to upper limit $n$)*

## 7. Arithmetic Series

- **Definition:** The sum of the terms of an arithmetic sequence.
- **Sum Formula:**
  $$S_n = \frac{n}{2} (a_1 + a_n)$$

## 8. Geometric Series

- **Definition:** The sum of the terms of a geometric sequence.
- **Sum Formula (for $r \ne 1$):**
  $$S_n = \frac{a_1 (1 - r^n)}{1 - r}$$
  *(when $r = 1$, every term equals $a_1$, so $S_n = n \cdot a_1$)*

## 9. Finite vs. Infinite Series

- **Finite Series:** Has a fixed, limited number of terms.
- **Infinite Series:** Continues indefinitely.
  - **Convergent:** If the absolute value of the common ratio $|r| < 1$, the sum approaches a finite number:
    $$S_{\infty} = \frac{a_1}{1 - r}$$
  - **Divergent:** If $|r| \ge 1$, the sum grows infinitely and does not approach a finite value.

## 10. Special Sequences

- **Square Numbers:** $1, 4, 9, 16, \dots \implies a_n = n^2$
- **Triangular Numbers:** $1, 3, 6, 10, 15, \dots \implies a_n = \frac{n(n + 1)}{2}$
- **Fibonacci Sequence:** $1, 1, 2, 3, 5, 8, 13, \dots \implies a_n = a_{n-1} + a_{n-2}$

## 11. Proof of the Arithmetic Series Sum Formula

### Theorem

The sum $S_n$ of the first $n$ terms of an arithmetic series with first term $a_1$ and $n$-th term $a_n$ is given by:

$$S_n = \frac{n}{2}(a_1 + a_n)$$

### Proof

An arithmetic sequence has a first term $a_1$ and a constant common difference $d$. The terms of the sequence moving forward are:

$$a_1,\ (a_1 + d),\ (a_1 + 2d),\ \dots,\ (a_n - d),\ a_n$$

Write the sum of the first $n$ terms, $S_n$, in standard order:

$$(1)\quad S_n = a_1 + (a_1 + d) + (a_1 + 2d) + \dots + (a_n - d) + a_n$$

Now, write the exact same sum $S_n$ in **reverse order**:

$$(2)\quad S_n = a_n + (a_n - d) + (a_n - 2d) + \dots + (a_1 + d) + a_1$$

Add equation $(1)$ and equation $(2)$ together column by column:

$$\begin{aligned}
S_n &= a_1 &+& \ (a_1 + d) &+& \ \dots &+& \ (a_n - d) &+& \ a_n \\
+ \ S_n &= a_n &+& \ (a_n - d) &+& \ \dots &+& \ (a_1 + d) &+& \ a_1 \\
\hline
2S_n &= (a_1 + a_n) &+& \ (a_1 + a_n) &+& \ \dots &+& \ (a_1 + a_n) &+& \ (a_1 + a_n)
\end{aligned}$$

Observe that in every pair, the $d$ terms cancel out. Since there are $n$ terms in the sequence, there are exactly $n$ identical pairs of $(a_1 + a_n)$:

$$2S_n = n \cdot (a_1 + a_n)$$

Dividing both sides by 2 yields:

$$S_n = \frac{n}{2}(a_1 + a_n)$$

$$\blacksquare$$

> **Alternative Form:** Since $a_n = a_1 + (n - 1)d$, substituting $a_n$ into the formula gives:
> $$S_n = \frac{n}{2}\Big(2a_1 + (n - 1)d\Big)$$

### Example: Algorithmic Work Series

Another common pattern in algorithm analysis is a series of work that decreases by a constant amount at each step:

$$n + (n - 1) + (n - 2) + \dots + 1$$

This is a finite arithmetic series with first term $a_1 = n$, last term $a_n = 1$, and $n$ terms. Applying the sum formula:

$$S_n = \frac{n}{2}(a_1 + a_n) = \frac{n}{2}(n + 1) = \frac{n^2 + n}{2}$$

Dropping the lower-order term and constant factor gives the familiar complexity bound:

$$n + (n - 1) + (n - 2) + \dots = O(n^2)$$

## 12. Proof of the Finite Geometric Series Sum Formula

### Theorem

The sum $S_n$ of the first $n$ terms of a finite geometric series with first term $a_1$ and common ratio $r \neq 1$ is given by:

$$S_n = \frac{a_1(1 - r^n)}{1 - r}$$

### Proof

A finite geometric series $S_n$ with first term $a_1$ and common ratio $r$ is:

$$(1)\quad S_n = a_1 + a_1 r + a_1 r^2 + a_1 r^3 + \dots + a_1 r^{n-1}$$

Multiply equation $(1)$ by the common ratio $r$:

$$(2)\quad r S_n = a_1 r + a_1 r^2 + a_1 r^3 + \dots + a_1 r^{n-1} + a_1 r^n$$

Subtract equation $(2)$ from equation $(1)$:

$$\begin{aligned}
S_n &= a_1 + a_1 r + a_1 r^2 + \dots + a_1 r^{n-1} \\
-\ r S_n &= \quad \ \ a_1 r + a_1 r^2 + \dots + a_1 r^{n-1} + a_1 r^n \\
\hline
S_n - r S_n &= a_1 - a_1 r^n
\end{aligned}$$

Every intermediate term cancels out completely, leaving:

$$S_n(1 - r) = a_1(1 - r^n)$$

Dividing both sides by $(1 - r)$ for $r \neq 1$:

$$S_n = \frac{a_1(1 - r^n)}{1 - r}$$

$$\blacksquare$$

> **Special Case ($r = 1$):** If $r = 1$, the sum is simply $S_n = \underbrace{a_1 + a_1 + \dots + a_1}_{n \text{ times}} = n \cdot a_1$.

## 13. Derivation of the Infinite Geometric Series Sum Formula

### Theorem

An infinite geometric series converges to a finite sum $S_{\infty}$ if and only if $|r| < 1$, and its sum is given by:

$$S_{\infty} = \frac{a_1}{1 - r}$$

### Proof

The infinite sum $S_{\infty}$ is defined as the limit of the partial sums $S_n$ as $n \to \infty$:

$$S_{\infty} = \lim_{n \to \infty} S_n$$

Using the finite geometric sum formula for $r \neq 1$:

$$S_{\infty} = \lim_{n \to \infty} \left( \frac{a_1(1 - r^n)}{1 - r} \right)$$

Algebraically split the limit into two components:

$$S_{\infty} = \frac{a_1}{1 - r} - \frac{a_1}{1 - r} \cdot \left( \lim_{n \to \infty} r^n \right)$$

Now analyze the behavior of $\lim_{n \to \infty} r^n$:

- **If $|r| < 1$**: Multiplying a fraction between $-1$ and $1$ infinitely drives its value to zero:
  $$\lim_{n \to \infty} r^n = 0$$
- **If $|r| \ge 1$**: $r^n$ does not approach zero ($r^n \to \infty$ or oscillates), causing the series to diverge.

Substituting $\lim_{n \to \infty} r^n = 0$ for $|r| < 1$:

$$S_{\infty} = \frac{a_1}{1 - r} - \frac{a_1}{1 - r} \cdot (0)$$

$$S_{\infty} = \frac{a_1}{1 - r}$$

$$\blacksquare$$

### Example: Algorithmic Work Series

A common pattern in algorithm analysis is a series of work that halves at each step:

$$n + \frac{n}{2} + \frac{n}{4} + \dots$$

This is an infinite geometric series with first term $a_1 = n$ and common ratio $r = \frac{1}{2}$. Since $|r| < 1$, it converges:

$$S_{\infty} = \frac{n}{1 - \frac{1}{2}} = \frac{n}{\frac{1}{2}} = 2n$$

Dropping the constant factor gives the familiar complexity bound:

$$n + \frac{n}{2} + \frac{n}{4} + \dots = O(n)$$
