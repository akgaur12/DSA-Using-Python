# 📘 Recursion in Python – Complete Documentation

---

## 🔁 What is Recursion?

**Recursion** is a programming technique where a function **calls itself** to solve smaller instances of the same problem. It continues until it reaches a condition where no further recursion is needed (called the **base case**).

### 💡 Example

```python
def greet(n):
    if n == 0:
        return
    print("Hello")
    greet(n - 1)
```

This function prints "Hello" `n` times using recursion.

---

## 🧱 Components of a Recursive Function

Every recursive function has two key parts:

### ✅ Base Case:

* The condition that **stops** further recursion.
* Prevents infinite loops or stack overflow.

```python
if n == 0:
    return 1
```

### ↻ Recursive Step:

* The part where the function **calls itself** with a smaller or simpler input.
* This reduces the problem toward the base case.

```python
return n * factorial(n - 1)
```

### 📌 Full Example

```python
def factorial(n):
    if n == 0:               # Base Case
        return 1
    return n * factorial(n-1)  # Recursive Step
```

---

## 🧪 Types of Recursion

Recursion can be classified based on how and where the function calls itself:

### 1. **Direct Recursion**

A function calls itself directly.

```python
def example():
    example()
```

### 2. **Indirect Recursion**

A function calls another function, which then calls the first one.

```python
def a():
    b()

def b():
    a()
```

### 3. **Linear Recursion**

Only one recursive call is made per function call.

```python
def linear(n):
    if n == 0:
        return
    linear(n - 1)
```

### 4. **Binary Recursion**

Two recursive calls are made per call.

```python
def binary(n):
    if n <= 1:
        return n
    return binary(n-1) + binary(n-2)
```

### 5. **Multiple Recursion**

More than two recursive calls per function call.

```python
def multiple(n):
    if n <= 0:
        return
    multiple(n - 1)
    multiple(n - 2)
    multiple(n - 3)
```

---

## ↺ Head Recursion vs Tail Recursion

### 🧠 Head Recursion

* Recursive call is made **before** other operations.
* Work is done after the recursive call returns.

```python
def head(n):
    if n == 0:
        return
    head(n - 1)
    print(n)
```

**Output for `head(3)`:**

```
1
2
3
```

### 🐍 Tail Recursion

* Recursive call is the **last operation** in the function.
* No work is done after the call.

```python
def tail(n):
    if n == 0:
        return
    print(n)
    tail(n - 1)
```

**Output for `tail(3)`:**

```
3
2
1
```

> 🔺 **Note:** Python does **not optimize** tail recursion (unlike some other languages), so the stack is still used.

---

## 🌲 Recursion Tree

A **recursion tree** is a diagram that shows how recursive calls break down the problem into subproblems.

### Example: Fibonacci

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### Tree for `fibonacci(4)`:

```
           fib(4)
         /        \
     fib(3)       fib(2)
     /    \        /    \
 fib(2)  fib(1)  fib(1)  fib(0)
 /   \
fib(1) fib(0)
```

* Shows how function branches out at each call.
* Helps analyze **time complexity**.

---

## 📚 Summary

| Concept        | Description                                          |
| -------------- | ---------------------------------------------------- |
| Recursion      | Function calling itself                              |
| Base Case      | Stops the recursion                                  |
| Recursive Step | Calls function with a smaller input                  |
| Head Recursion | Recursive call occurs first                          |
| Tail Recursion | Recursive call is the last step                      |
| Recursion Tree | Visualization of how calls split into subcalls       |
| Types          | Direct, Indirect, Linear, Binary, Multiple Recursion |
