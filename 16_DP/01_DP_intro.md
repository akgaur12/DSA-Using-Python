# Dynamic Programming in Python

**Dynamic Programming (DP)** is a technique for solving problems by breaking them into smaller subproblems, solving each subproblem **only once**, and reusing the stored result instead of recomputing it. It applies whenever a problem has two properties:

1. **Overlapping Subproblems** — the same smaller subproblem is needed multiple times during recursion (unlike, say, merge sort, where subproblems never repeat).
2. **Optimal Substructure** — the optimal solution to the problem can be built from the optimal solutions of its subproblems.

If a problem has *only* optimal substructure but *not* overlapping subproblems, plain recursion (or a greedy approach) is enough — DP's entire benefit comes from **not recomputing** what's already been solved.

---

## 1. Motivating Example: Fibonacci

`fib(n) = fib(n-1) + fib(n-2)` has both properties: `fib(2)` is recomputed many times inside `fib(5)`'s recursion tree, and `fib(n)`'s answer is built directly from `fib(n-1)` and `fib(n-2)`.

```text
Naive recursion tree for fib(5) — notice fib(2) computed 3 times, fib(1) computed 5 times:

                    fib(5)
                 /          \
            fib(4)            fib(3)
           /      \           /      \
       fib(3)    fib(2)   fib(2)    fib(1)
       /    \     /   \    /   \
   fib(2) fib(1) fib(1)fib(0) fib(1)fib(0)
   /   \
 fib(1)fib(0)
```

- **Naive recursion**: O(2^N) time — every subproblem is recomputed from scratch.
- **DP (memoized or tabulated)**: O(N) time — each of the N distinct subproblems is solved exactly once.

---

## 2. Two Ways to Implement DP

### a) Memoization (Top-Down)

Write the **natural recursive solution** first, then cache (`memoize`) each result the first time it's computed. Subsequent calls with the same argument return instantly from the cache.

```python
def fib_memo(n, cache=None):
    if cache is None:
        cache = {}
    if n <= 1:
        return n
    if n in cache:
        return cache[n]
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]
```

- Easiest to derive — start from the brute-force recursion and add a cache.
- Only computes the subproblems actually needed (can be an advantage over tabulation for sparse state spaces).
- Pays recursion / call-stack overhead, and risks `RecursionError` for very large `n`.

### b) Tabulation (Bottom-Up)

Build a table iteratively, starting from the base cases, until the answer for `n` is reached. No recursion at all.

```python
def fib_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

- No recursion overhead or stack-depth limit.
- Computes every subproblem from the base case up, even ones that might not be strictly necessary for a memoized approach.

### c) Space Optimization

Many tabulated DPs only ever look back a constant number of steps (here, just `dp[i-1]` and `dp[i-2]`), so the full array can be collapsed into a couple of variables — turning O(N) space into O(1).

```python
def fib_optimized(n):
    if n <= 1:
        return n
    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev1 + prev2
    return prev1
```

| Approach              | Time  | Space  |
| ---------------------- | ------- | -------- |
| Naive recursion        | O(2^N)  | O(N) — call stack |
| Memoization (top-down) | O(N)    | O(N) — cache + call stack |
| Tabulation (bottom-up) | O(N)    | O(N) — table |
| Space-optimized        | O(N)    | O(1) — constant variables |

---

## 3. How to Approach a DP Problem

1. **Identify the recursive brute-force solution first.** Define what a "state" is (the parameters that uniquely determine a subproblem) and write the recurrence relation in terms of smaller states.
2. **Check for overlapping subproblems** — if the same state is reached via different recursive paths, DP will help.
3. **Memoize** the brute-force recursion (top-down) — usually the fastest way to get a working solution.
4. **Convert to tabulation** (bottom-up) if you need to avoid recursion overhead or want to further **space-optimize**.
5. **Space-optimize** if the recurrence only depends on the last few rows/states.

---

## 4. Common DP Patterns

| Pattern                        | State definition                                    | Example problems                                  |
| -------------------------------- | ------------------------------------------------------| ----------------------------------------------------|
| **1D DP**                       | `dp[i]` = answer using the first `i` elements         | Climbing Stairs, House Robber, Fibonacci            |
| **2D Grid DP**                  | `dp[i][j]` = answer at cell `(i, j)`                  | Unique Paths, Minimum Path Sum                      |
| **0/1 Knapsack**                | `dp[i][w]` = best value using first `i` items, capacity `w` | 0/1 Knapsack, Subset Sum, Partition Equal Subset Sum |
| **Unbounded Knapsack**          | Like 0/1 but items can be reused                       | Coin Change, Rod Cutting                            |
| **Longest Common Subsequence (LCS) family** | `dp[i][j]` = answer using `s1[0..i)` and `s2[0..j)` | LCS, Edit Distance, Longest Palindromic Subsequence |
| **Longest Increasing Subsequence (LIS) family** | `dp[i]` = best subsequence ending at index `i` | LIS, Longest Bitonic Subsequence, Box Stacking       |
| **Partition / Interval DP**     | `dp[i][j]` = best answer for the range `[i, j]`        | Matrix Chain Multiplication, Palindrome Partitioning |
| **DP on Subsequences / Subsets**| `dp[i][target]` = can we reach `target` using first `i` elements | Subset Sum, Target Sum, Partition into K Subsets |

*(Implementations of the most common representative from each pattern are in [`02_DP.py`](./02_DP.py).)*

---

## 5. Recognizing When to Use DP

Ask these questions about the problem:

- Does it ask for an **optimum** (min/max), a **count** (number of ways), or a **feasibility** (can it be done)?
- Can the problem be broken into a choice at each step (**take it / skip it**, **include / exclude**, **match / don't match**) where each choice leads to a smaller version of the same problem?
- Do naive recursive calls repeat the same arguments? (Try drawing the recursion tree for a small input — repeated nodes confirm overlapping subproblems.)

If yes to these, define the state, write the recurrence, then memoize or tabulate.

---

## ✅ Summary

- DP = **recursion + caching**, applicable when subproblems overlap and the problem has optimal substructure.
- **Memoization** (top-down) is the easiest to derive from brute-force recursion; **tabulation** (bottom-up) avoids recursion overhead; **space optimization** shrinks the table once the recurrence's dependency window is understood.
- Most DP problems fall into a handful of recognizable patterns (1D, grid, knapsack, LCS-family, LIS-family, interval/partition, subset) — recognizing the pattern is most of the battle.
- Always derive the **brute-force recursive solution and state definition first** — DP is an optimization on top of it, not a separate way of thinking about the problem.
