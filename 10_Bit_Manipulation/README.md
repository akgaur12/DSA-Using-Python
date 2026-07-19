# Bit Manipulation — Complete Guide

## 1. What Is Bit Manipulation?

**Bit manipulation** is the technique of directly operating on the individual **binary
digits (bits)** of a number using **bitwise operators**, instead of treating the number as an
opaque value. Every integer is stored in memory as a sequence of bits (0s and 1s), and bitwise
operators let you read, set, clear, or toggle those bits directly.

Analogy: think of a number as a row of light switches, one per bit position. Bitwise
operations let you flip, check, or combine specific switches directly, instead of only being
able to add/subtract the "brightness" as a whole.

Because bitwise operations map to a handful of CPU instructions, they run in **O(1)** time per
operation — making bit tricks some of the fastest techniques available for certain classes of
problems.

## 2. The Bitwise Operators

| Operator      | Symbol | Meaning                          | Example         |
| ---------------- | -------- | ------------------------------------ | ------------------ |
| AND               | `&`      | 1 if both bits are 1                  | `5 & 3 = 1`         |
| OR                | `\|`     | 1 if at least one bit is 1            | `5 \| 3 = 7`        |
| XOR               | `^`      | 1 if bits differ                      | `5 ^ 3 = 6`         |
| NOT               | `~`      | Inverts all bits                      | `~5 = -6`           |
| Left Shift        | `<<`     | Shifts bits left (multiplies by 2ⁿ)   | `5 << 1 = 10`       |
| Right Shift       | `>>`     | Shifts bits right (divides by 2ⁿ)     | `5 >> 1 = 2`        |

See [`01_Introduction.md`](./01_Introduction.md) for a full walkthrough with worked examples
and a cheat sheet of get/set/clear/toggle-bit formulas.

## 3. Time & Space Complexity

| Operation                             | Complexity | Notes                                          |
| ------------------------------------------ | ------------ | --------------------------------------------------- |
| Any single bitwise operation (`&`,`\|`,`^`,`~`,`<<`,`>>`) | O(1)         | Maps directly to a CPU instruction                   |
| Get/Set/Clear/Toggle i-th bit           | O(1)         | A single shift + bitwise op                          |
| Count set bits (Brian Kernighan's)        | O(k)         | k = number of set bits, not total bit width          |
| Generate power set (all subsets)          | O(n · 2ⁿ)    | 2ⁿ subsets, O(n) to build each                       |
| Space (bit tricks in general)              | O(1)         | Typically no extra memory beyond a few integers      |

## 4. Common Bit Manipulation Patterns

| Pattern                            | Idea                                                                       |
| --------------------------------------- | -------------------------------------------------------------------------------- |
| **Check/Set/Clear/Toggle i-th bit**       | `(n >> i) & 1`, `n \| (1 << i)`, `n & ~(1 << i)`, `n ^ (1 << i)`                  |
| **Check even/odd**                        | `n & 1` — last bit tells parity, faster than `n % 2`                             |
| **Power-of-two check**                    | `n > 0 and (n & (n - 1)) == 0` — a power of 2 has exactly one set bit             |
| **Brian Kernighan's algorithm**            | `n &= (n - 1)` repeatedly clears the lowest set bit — counts set bits in O(k)     |
| **XOR for cancellation**                   | `a ^ a = 0` and `a ^ 0 = a` — pairs cancel out, useful for "find the single/odd one out" problems |
| **Isolate rightmost set bit**              | `n & -n` — isolates the lowest set bit using two's complement                     |
| **Swap without temp variable**              | Three XORs (`a ^= b; b ^= a; a ^= b`) swap values without extra storage           |
| **Bitmask enumeration**                    | Loop `mask` from `0` to `2ⁿ - 1`, using each bit of `mask` to decide inclusion — generates all subsets |

## 5. When Should You Use Bit Manipulation?

✅ **Use bit tricks when:**
- You need **maximum performance** for simple per-bit checks (flags, permissions, parity).
- You're working with **fixed-size states** (subsets, masks) — bitmask DP, generating all
  subsets.
- The problem structure has a **pairing/cancellation** property that XOR can exploit (find the
  unique element, minimum flips between two numbers).
- You need to represent a **set of boolean flags** compactly (a single integer instead of an
  array of booleans).

❌ **Avoid it when:**
- Readability matters more than micro-optimization — bit tricks can be cryptic to future
  readers; a clear boolean/array-based solution may be preferable unless performance is
  critical.
- The numbers involved are arbitrarily large and sign/overflow handling would add more
  complexity than it saves (careful handling is still needed for two's complement and negative
  shifts).

## 6. Real-World Use Cases

- **Permission/flag systems**: combining multiple boolean flags into a single integer (Unix
  file permissions, feature flags).
- **Cryptography**: XOR-based ciphers, hashing, checksums.
- **Compression**: packing multiple small values into fewer bits.
- **Graphics/color manipulation**: extracting RGBA channels from a packed pixel integer via
  shifts and masks.
- **Competitive programming**: bitmask dynamic programming (representing visited-state subsets
  compactly), fast subset generation.
- **Networking**: subnet masks and IP address manipulation are pure bitwise arithmetic.

## 7. Bit Manipulation in Python

```python
n = 70          # binary: 1000110
i = 3           # 1-based bit position from the LSB

# Get i-th bit
ith_bit = (n >> (i - 1)) & 1

# Set i-th bit
set_bit = n | (1 << (i - 1))

# Clear i-th bit
clear_bit = n & ~(1 << (i - 1))

# Toggle i-th bit
toggle_bit = n ^ (1 << (i - 1))

# Check power of two
def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0

# Count set bits (Brian Kernighan's algorithm)
def count_set_bits(n: int) -> int:
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count

# Swap without a temp variable
a, b = 5, 7
a ^= b
b ^= a
a ^= b   # a, b = 7, 5

# Find the single non-duplicated element (all others appear twice)
def find_single(arr):
    result = 0
    for num in arr:
        result ^= num
    return result
```

Note: Python integers have **arbitrary precision** (no fixed 32/64-bit width), so `~n` and
negative shifts behave differently than in fixed-width languages like C or Java — Python
simulates two's complement conceptually but doesn't wrap around at a fixed bit width.

## 8. Files in This Folder

| File                                                                     | Description                                                                                  | Time                              | Space              |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- | -------------------------------------- | --------------------- |
| [`01_Introduction.md`](./01_Introduction.md)                                    | Full cheat sheet: get/set/clear/toggle bit, bitwise operators, and interview tricks                    | —                                       | —                     |
| [`02_check_kth_bit_set.py`](./02_check_kth_bit_set.py)                           | Checks whether the k-th bit is set, via left-shift and right-shift approaches                          | O(1)                                    | O(1)                  |
| [`03_isEven_bitwise.py`](./03_isEven_bitwise.py)                                 | Determines even/odd using `n & 1`                                                                       | O(1)                                    | O(1)                  |
| [`04_isPowerOfTwo.py`](./04_isPowerOfTwo.py)                                     | Checks if a number is a power of two using `n & (n-1) == 0`                                             | O(1)                                    | O(1)                  |
| [`05_count_set_bits.py`](./05_count_set_bits.py)                                | Counts total set bits from 1 to n, via a naive loop and an efficient bit-cycle formula                   | O(n log n) naive; O(log n) efficient    | O(1)                  |
| [`06_set_rightmost_unset_bit.py`](./06_set_rightmost_unset_bit.py)               | Sets the rightmost unset bit using `n \| (n+1)` and manual scanning                                     | O(1) trick; O(log n) manual            | O(1)                  |
| [`07_swap_numbers_bitwise.py`](./07_swap_numbers_bitwise.py)                     | Swaps two numbers without a temp variable using three XORs                                              | O(1)                                    | O(1)                  |
| [`08_divide_two_integers.py`](./08_divide_two_integers.py)                      | Divides integers without `*`, `/`, `%` via shifted-subtraction, handling sign/overflow                    | O(log \|dividend\|)                     | O(1)                  |
| [`09_min_bit_flips.py`](./09_min_bit_flips.py)                                   | Minimum bit flips to convert one integer to another via XOR + Kernighan's counting                       | O(log(max(start, goal)))               | O(1)                  |
| [`10_find_single_number.py`](./10_find_single_number.py)                        | Finds the element appearing once (all others twice) by XOR-ing every element                            | O(n)                                    | O(1)                  |
| [`11_power_set.py`](./11_power_set.py)                                          | Generates all subsets (power set) by iterating over all bitmasks 0 to 2ⁿ-1                              | O(n · 2ⁿ)                               | O(2ⁿ)                 |
| [`12_is_power_of_two.py`](./12_is_power_of_two.py)                              | Checks power-of-two via the `n & (n-1)` trick and via `bin(n).count("1")`                                | O(1) bitwise; O(log n) bit-count       | O(1)                  |

## 9. Quick Recap

| Property               | Value                                    |
| ------------------------- | ------------------------------------------- |
| Operates on                | Individual binary digits of a number        |
| Core operators              | `&`, `\|`, `^`, `~`, `<<`, `>>`               |
| Typical time complexity      | O(1) per operation                           |
| Typical space complexity      | O(1)                                         |
| Signature use cases            | Flags, subsets/bitmask DP, XOR cancellation, fast parity/power-of-two checks |
| Python quirk                     | Arbitrary-precision integers — no fixed bit width, unlike C/Java |
