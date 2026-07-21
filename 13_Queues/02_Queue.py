"""
===========================================================
Queue Implementation in Python
===========================================================

A **Queue** is a linear data structure that follows the
**FIFO** (First In, First Out) principle. The first element
inserted is the first one to be removed.

Three implementations are provided:
    1. `Queue`            -> naive array-based (Python list).
                             enqueue is O(1), dequeue is O(N)
                             since the front sits at index 0.
    2. `CircularQueue`    -> fixed-capacity array-based, using
                             modulo-wrapped front/rear indices
                             for true O(1) enqueue & dequeue.
    3. `LinkedListQueue`  -> linked-list-based with head (front)
                             and tail (rear) pointers, giving
                             O(1) enqueue & dequeue with no
                             fixed capacity.

Supported Operations (all classes):
-------------------------------------
1. enqueue(x)   -> insert x at the rear.
2. dequeue()    -> remove & return the front element.
3. peek()       -> return the front element without removing it.
4. is_empty()   -> check if queue has no elements.
5. size()       -> number of elements.

===========================================================
"""


# --------------------------------------------------------
# Naive array-based Queue
# --------------------------------------------------------
class Queue:
    """Naive array-based queue backed by a Python list.

    enqueue is O(1) amortized (append at rear); dequeue is O(N)
    because removing index 0 shifts every remaining element left.
    Kept simple to illustrate why a `CircularQueue` or
    `LinkedListQueue` is preferred for frequent dequeues.
    """

    def __init__(self):
        self.items = []

    # ----------------------------------------------------
    def enqueue(self, x):
        """Insert x at the rear of the queue. O(1) amortized."""
        self.items.append(x)

    # ----------------------------------------------------
    def dequeue(self):
        """Remove and return the front element. O(N)."""
        if self.is_empty():
            raise IndexError("Queue underflow: dequeue from empty queue")
        return self.items.pop(0)

    # ----------------------------------------------------
    def peek(self):
        """Return the front element without removing it. O(1)."""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    # ----------------------------------------------------
    def is_empty(self):
        """Return True if the queue has no elements."""
        return len(self.items) == 0

    # ----------------------------------------------------
    def size(self):
        """Return the number of elements in the queue."""
        return len(self.items)

    # ----------------------------------------------------
    def display(self):
        """Print the queue from front to rear."""
        print("Queue (front -> rear):", self.items)

    def __repr__(self):
        return f"Queue({self.items})"


# --------------------------------------------------------
# Circular Queue (fixed-capacity, array-based)
# --------------------------------------------------------
class CircularQueue:
    """Fixed-capacity array-based queue with O(1) enqueue/dequeue.

    Uses `front`/`rear` indices wrapped with modulo arithmetic so
    freed-up slots at the front are reused without shifting.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.rear = -1
        self.count = 0

    # ----------------------------------------------------
    def enqueue(self, x):
        """Insert x at the rear of the queue. O(1)."""
        if self.count == self.capacity:
            raise OverflowError("Queue overflow: capacity reached")
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = x
        self.count += 1

    # ----------------------------------------------------
    def dequeue(self):
        """Remove and return the front element. O(1)."""
        if self.is_empty():
            raise IndexError("Queue underflow: dequeue from empty queue")
        value = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return value

    # ----------------------------------------------------
    def peek(self):
        """Return the front element without removing it. O(1)."""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[self.front]

    # ----------------------------------------------------
    def is_empty(self):
        """Return True if the queue has no elements."""
        return self.count == 0

    # ----------------------------------------------------
    def size(self):
        """Return the number of elements in the queue."""
        return self.count

    # ----------------------------------------------------
    def display(self):
        """Print the queue from front to rear, in logical order."""
        values = [self.items[(self.front + i) % self.capacity] for i in range(self.count)]
        print("CircularQueue (front -> rear):", values)

    def __repr__(self):
        values = [self.items[(self.front + i) % self.capacity] for i in range(self.count)]
        return f"CircularQueue({values})"


# --------------------------------------------------------
# Linked-list-based Queue
# --------------------------------------------------------
class Node:
    """A Node used by the linked-list-based queue."""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListQueue:
    """Queue backed by a singly linked list with head (front) and
    tail (rear) pointers, giving O(1) enqueue/dequeue and no
    fixed capacity.
    """

    def __init__(self):
        self.head = None   # front
        self.tail = None   # rear
        self._size = 0

    # ----------------------------------------------------
    def enqueue(self, x):
        """Insert x at the rear of the queue. O(1)."""
        node = Node(x)
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self._size += 1

    # ----------------------------------------------------
    def dequeue(self):
        """Remove and return the front element. O(1)."""
        if self.is_empty():
            raise IndexError("Queue underflow: dequeue from empty queue")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return value

    # ----------------------------------------------------
    def peek(self):
        """Return the front element without removing it. O(1)."""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.head.value

    # ----------------------------------------------------
    def is_empty(self):
        """Return True if the queue has no elements."""
        return self.head is None

    # ----------------------------------------------------
    def size(self):
        """Return the number of elements in the queue."""
        return self._size

    # ----------------------------------------------------
    def display(self):
        """Print the queue from front to rear."""
        curr = self.head
        values = []
        while curr:
            values.append(curr.value)
            curr = curr.next
        print("LinkedListQueue (front -> rear):", values)

    def __repr__(self):
        curr = self.head
        values = []
        while curr:
            values.append(curr.value)
            curr = curr.next
        return f"LinkedListQueue({values})"


# --------------------------------------------------------
# Example Usage
# --------------------------------------------------------
if __name__ == "__main__":
    print("--- Naive array-based Queue ---")
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.display()             # Queue (front -> rear): [10, 20, 30]
    print("Dequeue:", q.dequeue())  # 10
    q.display()             # Queue (front -> rear): [20, 30]

    print("\n--- Circular Queue ---")
    cq = CircularQueue(capacity=3)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    try:
        cq.enqueue(4)       # raises OverflowError
    except OverflowError as e:
        print("Expected error:", e)
    print("Dequeue:", cq.dequeue())  # 1
    cq.enqueue(4)           # reuses the freed slot
    cq.display()            # CircularQueue (front -> rear): [2, 3, 4]

    print("\n--- Linked-list-based Queue ---")
    llq = LinkedListQueue()
    llq.enqueue("a")
    llq.enqueue("b")
    llq.enqueue("c")
    llq.display()           # LinkedListQueue (front -> rear): ['a', 'b', 'c']
    print("Dequeue:", llq.dequeue())  # a
    llq.display()           # LinkedListQueue (front -> rear): ['b', 'c']
