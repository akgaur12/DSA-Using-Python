# 📝 Edit Distance (Levenshtein Distance)

The **Edit Distance** between two strings is the minimum number of operations required to transform one string into the other.

Allowed operations are:

1. **Insertion** → Add a character  
2. **Deletion** → Remove a character  
3. **Substitution** → Replace one character with another  

This is also known as the **Levenshtein Distance**.

---

## 📖 Example

* Word1 = `"kitten"`  
* Word2 = `"sitting"`

Steps:

1. `kitten → sitten` (substitute `k → s`)  
2. `sitten → sittin` (substitute `e → i`)  
3. `sittin → sitting` (insert `g`)  

✅ **Edit Distance = 3**

---

## 🧮 Dynamic Programming Approach

We define:

```
dp[i][j] = minimum edit distance between word1[0...i-1] and word2[0...j-1]
```

### Recurrence Relation:

```
if word1[i-1] == word2[j-1]:
    dp[i][j] = dp[i-1][j-1]      # No operation needed
else:
    dp[i][j] = 1 + min(
        dp[i-1][j],   # Deletion
        dp[i][j-1],   # Insertion
        dp[i-1][j-1]  # Substitution
    )
```

### Base Cases:
- `dp[0][j] = j` → Need `j` insertions  
- `dp[i][0] = i` → Need `i` deletions  

---

## 🐍 Python Implementation

```python
def editDistance(word1: str, word2: str) -> int:
    n, m = len(word1), len(word2)
    
    # DP table
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Initialize base cases
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    
    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],     # Deletion
                    dp[i][j - 1],     # Insertion
                    dp[i - 1][j - 1]  # Substitution
                )
    return dp[n][m]

# Example
print(editDistance("kitten", "sitting"))  # Output: 3
```

---

## ⏱ Complexity Analysis

- **Time Complexity** → `O(n * m)`  
- **Space Complexity** → `O(n * m)`  
  (Can be optimized to `O(min(n, m))` using rolling arrays)

---
