# Bit Manipulation in Python (with Examples)

Bit manipulation is a technique where we use **bitwise operators** to perform operations on the binary representation of numbers.  
It is widely used in competitive programming, system programming, cryptography, and optimization problems.

---

## 📌 Problem Statement (Base Example)

Given:
- A **32-bit unsigned integer** `num`.
- An integer `i` (1-based index from the **Least Significant Bit (LSB)**).  

Perform the following:
1. **Get the i-th bit**  
2. **Set the i-th bit**  
3. **Clear the i-th bit**

---

## 📊 Example

### Example 1:
**Input:**  
```
70 3
```

**Binary Representation of 70:**  
```
1000110
```

- **Get 3rd bit:** → `1`  
- **Set 3rd bit:** → `70`  
- **Clear 3rd bit:** → `66`

**Output:**  
```
1 70 66
```

---

### Example 2:
**Input:**  
```
8 1
```

**Binary Representation of 8:**  
```
1000
```

- **Get 1st bit:** → `0`  
- **Set 1st bit:** → `9`  
- **Clear 1st bit:** → `8`

**Output:**  
```
0 9 8
```

---

## ⚙️ Bit Manipulation Basics

### 1. **Get i-th Bit**
```python
(num >> (i-1)) & 1
```

### 2. **Set i-th Bit**
```python
num | (1 << (i-1))
```

### 3. **Clear i-th Bit**
```python
num & ~(1 << (i-1))
```

---

## 🧑‍💻 Python Implementation

```python
def bit_operations(num: int, i: int) -> None:
    # 1. Get i-th bit
    ith_bit = (num >> (i - 1)) & 1
    
    # 2. Set i-th bit
    set_bit_num = num | (1 << (i - 1))
    
    # 3. Clear i-th bit
    clear_bit_num = num & ~(1 << (i - 1))
    
    # Print results
    print(ith_bit, set_bit_num, clear_bit_num)


# Example Runs
bit_operations(70, 3)   # Output: 1 70 66
bit_operations(8, 1)    # Output: 0 9 8
```

---

## 🔎 Bitwise Operators Used

| Operator | Symbol | Meaning | Example |
|----------|--------|----------|---------|
| AND      | `&`    | 1 if both bits are 1 | `5 & 3 = 1` |
| OR       | `|`    | 1 if at least one bit is 1 | `5 | 3 = 7` |
| XOR      | `^`    | 1 if bits are different | `5 ^ 3 = 6` |
| NOT      | `~`    | Inverts bits | `~5 = -6` |
| Left Shift | `<<` | Shifts bits left | `5 << 1 = 10` |
| Right Shift| `>>` | Shifts bits right | `5 >> 1 = 2` |

---

## 🚀 Advanced Bit Manipulation Tricks (Interview Focus)

### 1. **Check if a number is Power of 2**
```python
def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0

# Examples
print(is_power_of_two(16))  # True
print(is_power_of_two(18))  # False
```

---

### 2. **Count Number of Set Bits (Brian Kernighan’s Algorithm)**
```python
def count_set_bits(n: int) -> int:
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count

# Example
print(count_set_bits(29))  # 4 (11101)
```

---

### 3. **Toggle i-th Bit**
```python
def toggle_bit(num: int, i: int) -> int:
    return num ^ (1 << (i - 1))

# Example
print(toggle_bit(8, 1))  # 9
print(toggle_bit(9, 1))  # 8
```

---

### 4. **Isolate Rightmost Set Bit**
```python
def rightmost_set_bit(n: int) -> int:
    return n & -n

# Example
print(rightmost_set_bit(12))  # 4 (1100 → 0100)
```

---

### 5. **Swap Two Numbers Without Temp Variable**
```python
def swap(a: int, b: int):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

# Example
print(swap(5, 7))  # (7, 5)
```

---

### 6. **Check if i-th Bit is Set**
```python
def is_bit_set(num: int, i: int) -> bool:
    return (num & (1 << (i - 1))) != 0

# Example
print(is_bit_set(70, 3))  # True
print(is_bit_set(8, 1))   # False
```

---

## 🎯 Key Takeaways

- **Get i-th bit** → `(num >> (i-1)) & 1`  
- **Set i-th bit** → `num | (1 << (i-1))`  
- **Clear i-th bit** → `num & ~(1 << (i-1))`  
- **Toggle i-th bit** → `num ^ (1 << (i-1))`  
- **Is Power of 2** → `(n & (n-1)) == 0`  
- **Count set bits** → `while n: n &= (n-1)`  

---

✅ This `.md` file is a **complete Bit Manipulation Cheat Sheet** for interview prep.
