# Strings — Complete Guide

## 1. What Is a String?

A **string** is a sequence of characters treated as a single value. Conceptually, it's an
array of characters — but with an important twist: in most modern languages (including
Python, Java, JavaScript), strings are **immutable** — once created, a string's contents
cannot be changed in place. Any "modification" (concatenation, replacement, slicing) produces
a **brand-new string**.

Analogy: think of a string as a sealed strip of beads, where each bead is a character. You can
read any bead directly by its position, but you can't swap a bead out — you'd need to make an
entirely new strip.

## 2. Why Strings Are Special (vs. a Plain Array)

| Property                  | Array                          | String                                        |
| ----------------------------- | ---------------------------------- | -------------------------------------------------- |
| Mutability                    | Usually mutable                     | Usually **immutable**                              |
| Element type                   | Any                                   | Characters only                                     |
| Common operations               | index, insert, delete, sort            | concatenation, substring, search, pattern matching  |
| Extra structure exploited        | —                                       | Alphabet size is bounded (26/128/256), enabling frequency-count tricks |

Because strings are immutable, repeatedly building one up character-by-character in a loop
(`result = result + char`) is **O(n²)** overall in many languages — each concatenation copies
the whole string so far. The idiomatic fix is to accumulate pieces in a mutable buffer (a list
in Python, a `StringBuilder` in Java) and join/convert once at the end — O(n) overall.

## 3. Time & Space Complexity

| Operation                     | Complexity | Notes                                          |
| -------------------------------- | ------------ | --------------------------------------------------- |
| Access by index                  | O(1)         | Same as array access                                |
| Concatenation (`a + b`)          | O(n + m)     | Creates a new string of combined length             |
| Substring / slice                | O(k)         | k = length of the substring                         |
| Search (naive)                   | O(n · m)     | n = text length, m = pattern length                 |
| Search (Rabin-Karp / KMP)         | O(n + m)     | Amortized/average case using rolling hash or prefix table |
| Comparison / equality             | O(n)         | Must compare character by character in the worst case |
| Building a string in a loop        | O(n) with a buffer; O(n²) with naive `+=` | Use a mutable buffer, join once at the end |

## 4. Common String Patterns

These recurring techniques show up across string problems regardless of language:

| Pattern                          | Idea                                                                          |
| ------------------------------------ | ---------------------------------------------------------------------------------- |
| **Frequency counting (hash map/array)** | Count character occurrences for anagram checks, first-unique-char, character-type counting |
| **Two pointers**                       | Compare from both ends inward — palindrome checks, reversing, valid-shuffle checks |
| **Sliding window**                     | Maintain a moving window over the string — longest substring without repeats |
| **Stack**                              | Match nested/paired structures — balanced parentheses, longest valid parentheses |
| **Dynamic programming**                | Build up a solution table from smaller substrings — edit distance, longest repeating subsequence, regex matching, decode ways |
| **Backtracking**                       | Explore all include/exclude or ordering choices — subsequences, permutations |
| **Rolling hash**                       | Compute a hash of a substring incrementally to compare/find patterns fast — Rabin-Karp |
| **Greedy scanning**                    | Make a locally optimal choice while scanning left-to-right/right-to-left — Roman numeral conversion, next greater number |

## 5. When Should You Use a String vs. Something Else?

✅ **Strings work well when:**
- You're dealing with **text** — parsing, formatting, matching, validating.
- Order and character-level access matter (as opposed to unordered character sets).

❌ **Consider alternatives when:**
- You need to **mutate** contents heavily and frequently → build with a mutable buffer (list of
  characters), convert to a string only at the end.
- You only care about **which characters appear**, not their order or count → a `set` is more
  direct than scanning a string repeatedly.
- You need frequency lookups (e.g., "how many times does each character appear?") → a hash
  map/array indexed by character keeps that O(1) per lookup.

## 6. Real-World Use Cases

- Parsing and validating user input (emails, URLs, form fields).
- Searching for patterns in text (search engines, log analysis, `grep`-like tools).
- Text processing pipelines: tokenization, normalization, compression.
- DNA sequence analysis (strings over a 4-letter alphabet).
- Autocomplete, spell-check, and fuzzy matching (edit distance).

## 7. String Operations in Python

Python strings (`str`) are immutable sequences of Unicode characters.

```python
s = "hello world"

# Access & slice
first = s[0]
sub = s[0:5]                     # "hello"
reversed_s = s[::-1]              # "dlrow olleh"

# Immutability — this creates a NEW string, doesn't modify s
new_s = s.replace("world", "python")

# Efficient building (avoid O(n²) += in a loop)
parts = []
for word in ["hello", "world"]:
    parts.append(word)
result = " ".join(parts)          # O(n) overall

# Frequency counting (bounded alphabet trick)
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

# Membership & search
"world" in s                      # O(n) substring search
s.find("world")                   # returns index or -1

# Common transforms
s.lower(), s.upper(), s.strip(), s.split(" ")
```

## 8. Files in This Folder

| File                                                              | Description                                                                                | Time                                | Space                    |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | -------------------------------------- | --------------------------- |
| [`01_palindrome.py`](./01_palindrome.py)                                 | Checks whether a string is a palindrome via reversal comparison                                    | O(n)                                    | O(n)                        |
| [`02_remove_duplicates.py`](./02_remove_duplicates.py)                   | Removes duplicate characters while preserving order using a seen-set                               | O(n)                                    | O(k) unique chars           |
| [`03_first_non_repeating.py`](./03_first_non_repeating.py)               | Finds the first non-repeating character using a frequency map, two passes                          | O(n)                                    | O(1) bounded alphabet       |
| [`04_count_char_types.py`](./04_count_char_types.py)                     | Counts vowels, consonants, digits, and special characters                                          | O(n)                                    | O(1)                        |
| [`05_anagram_check.py`](./05_anagram_check.py)                           | Checks if two strings are anagrams via character frequency counts                                  | O(n)                                    | O(1) bounded alphabet       |
| [`06_rotation_check.py`](./06_rotation_check.py)                         | ⚠️ Contains a copy-paste duplicate of the first-non-repeating-character logic, not an actual rotation check | O(n)                            | O(1)                        |
| [`07_longest_common_prefix.py`](./07_longest_common_prefix.py)           | Finds the longest common prefix among strings by sorting, then comparing first/last                | O(N log N + M)                          | O(1)                        |
| [`08_isomorphic.py`](./08_isomorphic.py)                                 | Checks if two strings are isomorphic using two hash maps for bidirectional mapping                  | O(n)                                    | O(1) bounded mapping        |
| [`09_roman_to_integer.py`](./09_roman_to_integer.py)                     | Converts a Roman numeral string to an integer, scanning left to right                              | O(n)                                    | O(1)                        |
| [`10_integer_to_roman.py`](./10_integer_to_roman.py)                     | Converts an integer to a Roman numeral using greedy symbol subtraction                              | O(1)                                    | O(1)                        |
| [`11_all_subsequences.py`](./11_all_subsequences.py)                     | Generates all subsequences via recursive backtracking and iterative bitmasking                     | O(2ⁿ) / O(2ⁿ · n)                       | O(2ⁿ · n)                   |
| [`12_permutations.py`](./12_permutations.py)                             | Generates all permutations via recursive backtracking with index swapping                          | O(n · n!)                               | O(n!)                       |
| [`13_balanced_parenthesis.py`](./13_balanced_parenthesis.py)             | Validates bracket balance via a stack-based approach and a string-replacement alternative           | O(n) stack; O(n²) replacement           | O(n) stack; O(1) replacement |
| [`14_group_anagrams.py`](./14_group_anagrams.py)                         | Groups strings into anagram groups by hashing each word's character frequency                       | O(N · M)                                | O(N · M)                    |
| [`15_longest_unique_substring.py`](./15_longest_unique_substring.py)     | Finds the longest substring without repeating characters via sliding window                         | O(n)                                    | O(min(n, alphabet))         |
| [`16_valid_shuffle.py`](./16_valid_shuffle.py)                           | Checks if a string is a valid interleaved shuffle of two others via frequency arrays                | O(n)                                    | O(1)                        |
| [`17_rabin_karp.py`](./17_rabin_karp.py)                                 | Finds all pattern occurrences using the Rabin-Karp rolling-hash algorithm                            | O(n+m) avg; O(nm) worst                 | O(1)                        |
| [`18_longest_repeating_subseq.py`](./18_longest_repeating_subseq.py)     | Finds the longest repeating subsequence using DP (self-LCS, excluding same-index matches)            | O(n²)                                   | O(n²)                       |
| [`19_next_greater_number.py`](./19_next_greater_number.py)               | Finds the next greater number with the same digits via next-permutation logic                        | O(n)                                    | O(n)                        |
| [`20_min_swaps_palindrome.py`](./20_min_swaps_palindrome.py)             | Computes minimum adjacent swaps to make a string a palindrome (or -1 if impossible)                  | O(n²) worst                             | O(n)                        |
| [`21_regex_matching.py`](./21_regex_matching.py)                         | Implements regex matching with `.` and `*` using 2D dynamic programming                              | O(n · m)                                | O(n · m)                    |
| [`22_edit_distance.md`](./22_edit_distance.md)                          | Guide to Edit Distance (Levenshtein Distance) with recurrence relation and DP solution                | O(n · m)                                | O(n · m)                    |
| [`23_longest_valid_parentheses.py`](./23_longest_valid_parentheses.py)   | Finds the longest valid parentheses substring via stack, DP, and two-pass scan approaches             | O(n) all approaches                      | O(n) stack/DP; O(1) two-pass |
| [`24_decode_ways.py`](./24_decode_ways.py)                               | Counts ways to decode a digit sequence (1-26 → A-Z) via full-array and space-optimized DP             | O(n)                                    | O(n) / O(1) optimized        |

## 9. Quick Recap

| Property               | Value                              |
| ------------------------- | ------------------------------------- |
| Underlying structure       | Sequence (array) of characters        |
| Mutability                 | Immutable in most languages           |
| Access by index             | O(1)                                  |
| Concatenation                | O(n + m) per operation                |
| Naive repeated building       | O(n²) — use a buffer instead         |
| Pattern search (optimized)     | O(n + m) with rolling hash/prefix table |
| Python equivalent               | `str`                                 |
