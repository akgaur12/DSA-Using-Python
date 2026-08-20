"""
===========================================================
Dynamic Programming — Classic Problems in Python
===========================================================

One representative implementation per pattern described in
`01_DP_intro.md`, each solved bottom-up (tabulation) unless
noted otherwise.

Problems (pattern -> function):
---------------------------------
1. 1D DP                  -> climbing_stairs(n)
2. Grid DP                -> min_path_sum(grid)
3. 0/1 Knapsack           -> knapsack_01(weights, values, capacity)
4. Unbounded Knapsack     -> coin_change(coins, amount)
5. LCS family             -> lcs(s1, s2)
6. LCS family             -> edit_distance(s1, s2)
7. LIS family             -> lis(nums)              [O(N^2)]
8. LIS family             -> lis_optimized(nums)    [O(N log N)]
9. Partition / Interval DP -> matrix_chain_order(dims)
10. Subset DP             -> subset_sum(nums, target)

===========================================================
"""

import bisect


# --------------------------------------------------------
# 1. 1D DP — Climbing Stairs
# --------------------------------------------------------
def climbing_stairs(n):
    """Number of distinct ways to climb `n` stairs, taking 1 or 2
    steps at a time. dp[i] = dp[i-1] + dp[i-2]. O(N) time, O(1) space.
    """
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        prev2, prev1 = prev1, prev1 + prev2
    return prev1


# --------------------------------------------------------
# 2. Grid DP — Minimum Path Sum
# --------------------------------------------------------
def min_path_sum(grid):
    """Minimum sum path from top-left to bottom-right of `grid`,
    moving only right or down. dp[i][j] = grid[i][j] + min(dp[i-1][j],
    dp[i][j-1]). O(rows * cols) time, O(cols) space.
    """
    rows, cols = len(grid), len(grid[0])
    dp = [float("inf")] * cols
    dp[0] = 0
    for i in range(rows):
        new_dp = [float("inf")] * cols
        for j in range(cols):
            best_prev = dp[j] if j == 0 else min(dp[j], new_dp[j - 1])
            new_dp[j] = grid[i][j] + best_prev
        dp = new_dp
    return dp[cols - 1]


# --------------------------------------------------------
# 3. 0/1 Knapsack
# --------------------------------------------------------
def knapsack_01(weights, values, capacity):
    """Maximum value achievable with total weight <= capacity,
    each item usable at most once.
    dp[w] = max(dp[w], dp[w - weight[i]] + value[i]).
    O(N * capacity) time, O(capacity) space.
    """
    dp = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        # Iterate capacity downwards so each item is only used once.
        for w in range(capacity, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)
    return dp[capacity]


# --------------------------------------------------------
# 4. Unbounded Knapsack — Coin Change (minimum coins)
# --------------------------------------------------------
def coin_change(coins, amount):
    """Fewest coins needed to make `amount`; -1 if impossible.
    Coins can be reused (unbounded), so capacity is iterated upward.
    dp[a] = min(dp[a], dp[a - coin] + 1). O(amount * len(coins)) time,
    O(amount) space.
    """
    dp = [0] + [float("inf")] * amount
    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a and dp[a - coin] != float("inf"):
                dp[a] = min(dp[a], dp[a - coin] + 1)
    return dp[amount] if dp[amount] != float("inf") else -1


# --------------------------------------------------------
# 5. LCS family — Longest Common Subsequence
# --------------------------------------------------------
def lcs(s1, s2):
    """Length of the Longest Common Subsequence of s1 and s2.
    dp[i][j] = dp[i-1][j-1] + 1 if s1[i-1] == s2[j-1]
             = max(dp[i-1][j], dp[i][j-1]) otherwise.
    O(len(s1) * len(s2)) time and space.
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


# --------------------------------------------------------
# 6. LCS family — Edit Distance (Levenshtein Distance)
# --------------------------------------------------------
def edit_distance(s1, s2):
    """Minimum insert/delete/replace operations to convert s1 into s2.
    dp[i][j] = dp[i-1][j-1] if s1[i-1] == s2[j-1]
             = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) otherwise.
    O(len(s1) * len(s2)) time and space.
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i          # delete all of s1[:i]
    for j in range(n + 1):
        dp[0][j] = j          # insert all of s2[:j]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],       # delete from s1
                    dp[i][j - 1],       # insert into s1
                    dp[i - 1][j - 1],   # replace
                )
    return dp[m][n]


# --------------------------------------------------------
# 7. LIS family — Longest Increasing Subsequence (O(N^2))
# --------------------------------------------------------
def lis(nums):
    """Length of the Longest Increasing Subsequence.
    dp[i] = length of the LIS ending exactly at index i.
    O(N^2) time, O(N) space.
    """
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


# --------------------------------------------------------
# 8. LIS family — LIS via Patience Sorting (O(N log N))
# --------------------------------------------------------
def lis_optimized(nums):
    """Length of the Longest Increasing Subsequence, O(N log N).
    `tails[k]` holds the smallest possible tail value of an
    increasing subsequence of length k + 1. Binary search finds
    where each new number extends or replaces a tail.
    """
    tails = []
    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    return len(tails)


# --------------------------------------------------------
# 9. Partition / Interval DP — Matrix Chain Multiplication
# --------------------------------------------------------
def matrix_chain_order(dims):
    """Minimum scalar multiplications to multiply a chain of matrices
    where matrix i has dimensions dims[i] x dims[i+1].
    dp[i][j] = min over split point k of
               dp[i][k] + dp[k+1][j] + dims[i]*dims[k+1]*dims[j+1].
    O(N^3) time, O(N^2) space, where N = number of matrices.
    """
    n = len(dims) - 1   # number of matrices
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):          # chain length
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float("inf")
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]


# --------------------------------------------------------
# 10. Subset DP — Subset Sum (feasibility)
# --------------------------------------------------------
def subset_sum(nums, target):
    """True if some subset of `nums` sums to exactly `target`.
    dp[t] = whether sum t is achievable using elements processed so far.
    O(N * target) time, O(target) space.
    """
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for t in range(target, num - 1, -1):
            if dp[t - num]:
                dp[t] = True
    return dp[target]


# --------------------------------------------------------
# Example Usage
# --------------------------------------------------------
if __name__ == "__main__":
    print("Climbing Stairs (n=5):", climbing_stairs(5))    # 8

    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1],
    ]
    print("Min Path Sum:", min_path_sum(grid))              # 7

    print("0/1 Knapsack:", knapsack_01(
        weights=[1, 3, 4, 5], values=[1, 4, 5, 7], capacity=7))  # 9

    print("Coin Change (amount=11, coins=[1,2,5]):",
          coin_change([1, 2, 5], 11))                        # 3

    print("LCS('abcde', 'ace'):", lcs("abcde", "ace"))        # 3
    print("Edit Distance('horse', 'ros'):",
          edit_distance("horse", "ros"))                     # 3

    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print("LIS:", lis(nums))                                  # 4
    print("LIS (optimized):", lis_optimized(nums))             # 4

    print("Matrix Chain Order (dims=[40,20,30,10,30]):",
          matrix_chain_order([40, 20, 30, 10, 30]))            # 26000

    print("Subset Sum([3,34,4,12,5,2], target=9):",
          subset_sum([3, 34, 4, 12, 5, 2], 9))                  # True
