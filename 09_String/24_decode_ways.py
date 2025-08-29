"""
 Problem: Count Possible Decodings of a given Digit Sequence

Description:
-----------
We are given a digit sequence, where:
    1 -> 'A', 2 -> 'B', ..., 26 -> 'Z'

The task is to count the total number of possible decodings 
of the given digit sequence.

Example:
--------
Input: "123"
Possible decodings:
    "ABC"  -> (1 2 3)
    "LC"   -> (12 3)
    "AW"   -> (1 23)
Output: 3

Approaches Implemented:
-----------------------
1. Dynamic Programming with Full Array (O(n) time, O(n) space)
2. Space-Optimized Dynamic Programming (O(n) time, O(1) space)
"""


# --------------------------------------------------------
# Approach 1: DP with full array
# --------------------------------------------------------
def countDecodings_dp(digits: str) -> int:
    """
    Count number of decodings using full DP array.

    Idea:
    -----
    - Let dp[i] = number of ways to decode substring up to index i.
    - Transition:
        * If the last digit is valid (non-zero), add dp[i-1].
        * If the last two digits form a valid code (10 to 26), add dp[i-2].
    - Answer = dp[n].

    Complexity:
    -----------
    - Time: O(n)  (each digit processed once)
    - Space: O(n) (full dp array used)

    Args:
        digits (str): Input digit string

    Returns:
        int: Number of possible decodings
    """
    n = len(digits)
    if n == 0 or digits[0] == '0':
        return 0

    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1

    for i in range(2, n + 1):
        # Single digit check (non-zero)
        if digits[i - 1] != '0':
            dp[i] += dp[i - 1]

        # Two digit check (10 <= number <= 26)
        two_digit = int(digits[i - 2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]

    return dp[n]


# --------------------------------------------------------
# Approach 2: Space-optimized DP
# --------------------------------------------------------
def countDecodings_optimized(digits: str) -> int:
    """
    Count number of decodings using space-optimized DP.

    Idea:
    -----
    - In Approach 1, dp[i] depends only on dp[i-1] and dp[i-2].
    - So, instead of keeping an array, we only track two variables:
        prev1 = dp[i-1], prev2 = dp[i-2].
    - Update them iteratively while scanning digits.

    Complexity:
    -----------
    - Time: O(n)  (linear scan of digits)
    - Space: O(1) (only 2 variables kept)

    Args:
        digits (str): Input digit string

    Returns:
        int: Number of possible decodings
    """
    n = len(digits)
    if n == 0 or digits[0] == '0':
        return 0

    prev2, prev1 = 1, 1  # dp[0], dp[1]

    for i in range(2, n + 1):
        curr = 0

        # Single digit check
        if digits[i - 1] != '0':
            curr += prev1

        # Two digit check
        two_digit = int(digits[i - 2:i])
        if 10 <= two_digit <= 26:
            curr += prev2

        # Move window forward
        prev2, prev1 = prev1, curr

    return prev1


# --------------------------------------------------------
# Driver Code for Testing
# --------------------------------------------------------
if __name__ == "__main__":
    test_cases = ["121", "1234", "10", "101", "230"]

    for digits in test_cases:
        print(f"Input: {digits}")
        print("  DP Array Result       :", countDecodings_dp(digits))
        print("  Space Optimized Result:", countDecodings_optimized(digits))
        print("-" * 40)
