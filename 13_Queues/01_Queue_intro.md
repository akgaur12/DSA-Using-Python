# Queue in Python

A **Queue** is a linear data structure that follows the **FIFO** principle — **F**irst **I**n, **F**irst **O**ut. The element inserted first is the first one to be removed, just like a queue of people waiting in line: the person who joins first is served first.

---

## 1. Core Operations

| Operation         | Description                                   | Time Complexity |
| ----------------- | ----------------------------------------------| ---------------- |
| `enqueue(x)`      | Insert element `x` at the rear of the queue    | O(1)             |
| `dequeue()`       | Remove and return the element at the front     | O(1)             |
| `peek()` / `front()` | Return the front element without removing it | O(1)           |
| `is_empty()`      | Check whether the queue has no elements        | O(1)             |
| `size()`          | Return the number of elements in the queue     | O(1)             |

- **Overflow**: attempting to `enqueue` onto a queue that is already at capacity (relevant only for fixed-size array implementations).
- **Underflow**: attempting to `dequeue`/`peek` on an empty queue.

### Visual Representation

```text
enqueue(40)
front                          rear
  ↓                              ↓
[10] → [20] → [30] → [40]

dequeue() → removes 10 (front), 20 becomes the new front
```

---

## 2. Implementation Approaches

### a) Naive array-based (using a Python `list`)

```python
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, x):
        self.items.append(x)        # O(1) amortized — insert at rear

    def dequeue(self):
        return self.items.pop(0)    # O(N) — every remaining element shifts left
```

**Problem**: `list.pop(0)` is **O(N)** because every remaining element has to shift one index to the left. This makes the naive array queue inefficient for frequent dequeues.

### b) Circular Queue (fixed-size array)

A circular queue reuses freed-up space at the front by wrapping indices around with the modulo operator, avoiding the O(N) shift entirely.

```text
capacity = 5, front = 1, rear = 3
index:   0    1    2    3    4
        [_] [20] [30] [40] [_]
              ↑              ↑
            front           (rear+1) % capacity → next free slot
```

Both `front` and `rear` are advanced with `(index + 1) % capacity`, so both `enqueue` and `dequeue` are true **O(1)** with no shifting.

### c) Linked-list-based

Keeping both a `head` (front) and a `tail` (rear) pointer gives O(1) `enqueue` (append at tail) and O(1) `dequeue` (remove at head) — with no fixed capacity.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None   # front
        self.tail = None   # rear

    def enqueue(self, x):
        node = Node(x)
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    def dequeue(self):
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value
```

### d) Python's `collections.deque`

In practice, Python's built-in `collections.deque` is the idiomatic choice — it's implemented as a doubly linked list of blocks and supports **O(1)** appends/pops from *both* ends:

```python
from collections import deque

q = deque()
q.append(10)       # enqueue -> O(1)
q.popleft()         # dequeue -> O(1)
```

---

## 3. Complexity Analysis

| Operation | Naive array (`list`) | Circular Queue | Linked-list-based |
| --------- | ---------------------- | ---------------- | ------------------- |
| Enqueue   | O(1) amortized         | O(1)              | O(1)                |
| Dequeue   | O(N)                   | O(1)              | O(1)                |
| Space     | O(N)                   | O(capacity)       | O(N) + pointer overhead |

---

## 4. Variants

- **Circular Queue**: fixed-size array, wraps `front`/`rear` using modulo — avoids the O(N) shift of a naive array queue.
- **Deque (Double-Ended Queue)**: insertion/removal allowed at **both** ends. Generalizes both stack and queue behavior.
- **Priority Queue**: elements are served based on priority rather than arrival order (typically backed by a heap, not covered here).

---

## 5. Applications

- **CPU / process scheduling** (round-robin scheduling).
- **Breadth-First Search (BFS)** in graphs and trees.
- **Request handling / task queues** (e.g. print spoolers, message queues).
- **Buffering data streams** (IO buffers, producer-consumer pipelines).
- **Caching** — LRU cache design uses a deque-like structure.

---

## 6. Queue vs Stack

| Feature            | Queue (FIFO)                 | Stack (LIFO)                |
| ------------------ | ------------------------------| ------------------------------|
| Insertion           | At rear                       | At top                        |
| Removal             | From front                    | From top                      |
| Typical use case    | Scheduling, BFS, buffering    | Undo, recursion, DFS          |

---

## ✅ Summary

- A queue restricts access so insertion happens at the **rear** and removal happens at the **front**.
- A naive array-backed queue suffers **O(N)** dequeue; a **circular queue** or **linked list** fixes this to O(1).
- Python's `collections.deque` is the idiomatic, production-ready choice for O(1) operations at both ends.
- Widely used for BFS, scheduling, and buffering.
