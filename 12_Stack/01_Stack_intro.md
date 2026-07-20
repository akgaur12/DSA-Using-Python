# Stack in Python

A **Stack** is a linear data structure that follows the **LIFO** principle — **L**ast **I**n, **F**irst **O**ut. The element inserted last is the first one to be removed, just like a stack of plates: you add a plate on top and remove from the top.

---

## 1. Core Operations

| Operation           | Description                                 | Time Complexity |
| ------------------- | -------------------------------------------- | ---------------- |
| `push(x)`           | Insert element `x` on top of the stack       | O(1)             |
| `pop()`             | Remove and return the top element            | O(1)             |
| `peek()` / `top()`  | Return the top element without removing it   | O(1)             |
| `is_empty()`        | Check whether the stack has no elements      | O(1)             |
| `size()`            | Return the number of elements in the stack   | O(1)             |

- **Overflow**: attempting to `push` onto a stack that is already at capacity (relevant only for fixed-size array implementations).
- **Underflow**: attempting to `pop`/`peek` on an empty stack.

### Visual Representation

```text
push(30)
         ┌────┐
         │ 30 │  ← top
         ├────┤
         │ 20 │
         ├────┤
         │ 10 │
         └────┘

pop() → removes 30, top becomes 20
```

---

## 2. Implementation Approaches

### a) Array-based (using a Python `list`)

Python's `list` already supports O(1) amortized `append`/`pop` from the end, which makes it a natural backing store — the "top" of the stack is the end of the list, not the beginning (inserting/removing from the front would be O(N)).

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)      # O(1) amortized

    def pop(self):
        return self.items.pop()   # O(1)

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0
```

**Pros**: simple, cache-friendly (contiguous memory).
**Cons**: a *fixed-capacity* array version can overflow; a dynamic one (like Python's `list`) occasionally pays O(N) to resize internally (still O(1) amortized).

### b) Linked-list-based

Each element is a node with a `next` pointer. `push`/`pop` operate on the **head** of the list, so both are O(1) with no resizing behavior at all.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None

    def push(self, x):
        node = Node(x)
        node.next = self.head
        self.head = node

    def pop(self):
        value = self.head.value
        self.head = self.head.next
        return value
```

**Pros**: true O(1) push/pop, no resizing, no fixed capacity.
**Cons**: extra memory per element (`next` pointer), poor cache locality compared to a contiguous array.

---

## 3. Complexity Analysis

| Operation | Array-based     | Linked-list-based                 |
| --------- | --------------- | ---------------------------------- |
| Push      | O(1) amortized  | O(1)                               |
| Pop       | O(1)            | O(1)                               |
| Peek      | O(1)            | O(1)                               |
| Space     | O(N)            | O(N) + pointer overhead per node   |

---

## 4. Applications

- **Function call stack / recursion**: every function call is pushed onto the call stack; returning pops it off.
- **Undo/redo mechanisms** in editors.
- **Browser back button** (page history).
- **Expression evaluation & conversion**: infix ↔ postfix ↔ prefix, and evaluating postfix/prefix expressions.
- **Balanced parentheses / bracket matching**.
- **Depth-First Search (DFS)** — explicit stack, or the implicit recursion call stack.
- **Backtracking algorithms**.

---

## 5. Stack vs Array vs Queue

| Feature          | Stack (LIFO)          | Queue (FIFO)               |
| ---------------- | ---------------------- | --------------------------- |
| Insertion        | Only at top            | Only at rear                |
| Removal          | Only from top          | Only from front             |
| Typical use case | Undo, recursion, DFS   | Scheduling, BFS, buffering  |

---

## ✅ Summary

- A stack restricts access to **one end only** — the top.
- All core operations (`push`, `pop`, `peek`) run in **O(1)**.
- Can be backed by a **dynamic array** (simple, cache-friendly) or a **linked list** (no resizing, no fixed capacity).
- Widely used for recursion, expression parsing, undo history, and DFS.
