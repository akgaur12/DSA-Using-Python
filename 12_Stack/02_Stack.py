"""
===========================================================
Stack Implementation in Python
===========================================================

A **Stack** is a linear data structure that follows the
**LIFO** (Last In, First Out) principle. The last element
pushed onto the stack is the first one to be popped off.

Two implementations are provided:
    1. `Stack`           -> array-based (backed by a Python list),
                            with an optional fixed capacity to
                            demonstrate overflow handling.
    2. `LinkedListStack`  -> linked-list-based, true O(1) push/pop
                            with no resizing.

Supported Operations (both classes):
-------------------------------------
1. push(x)      -> insert x on top.        O(1)
2. pop()        -> remove & return top.    O(1)
3. peek()       -> return top without removing it.  O(1)
4. is_empty()   -> check if stack has no elements.  O(1)
5. size()       -> number of elements.     O(1)

===========================================================
"""


# --------------------------------------------------------
# Array-based Stack
# --------------------------------------------------------
class Stack:
    """Array-based stack backed by a Python list.

    If `capacity` is given, the stack behaves like a fixed-size
    array stack and raises `OverflowError` / `IndexError` on
    push-when-full / pop-when-empty, mirroring the classic
    array implementation taught alongside linked-list stacks.
    """

    def __init__(self, capacity=None):
        self.items = []
        self.capacity = capacity

    # ----------------------------------------------------
    def push(self, x):
        """Insert x on top of the stack. O(1) amortized."""
        if self.capacity is not None and len(self.items) >= self.capacity:
            raise OverflowError("Stack overflow: capacity reached")
        self.items.append(x)

    # ----------------------------------------------------
    def pop(self):
        """Remove and return the top element. O(1)."""
        if self.is_empty():
            raise IndexError("Stack underflow: pop from empty stack")
        return self.items.pop()

    # ----------------------------------------------------
    def peek(self):
        """Return the top element without removing it. O(1)."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    # ----------------------------------------------------
    def is_empty(self):
        """Return True if the stack has no elements."""
        return len(self.items) == 0

    # ----------------------------------------------------
    def size(self):
        """Return the number of elements in the stack."""
        return len(self.items)

    # ----------------------------------------------------
    def display(self):
        """Print the stack from bottom to top."""
        print("Stack (bottom -> top):", self.items)

    def __repr__(self):
        return f"Stack({self.items})"


# --------------------------------------------------------
# Linked-list-based Stack
# --------------------------------------------------------
class Node:
    """A Node used by the linked-list-based stack."""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListStack:
    """Stack backed by a singly linked list. push/pop operate
    on the head, giving true O(1) operations with no resizing.
    """

    def __init__(self):
        self.head = None
        self._size = 0

    # ----------------------------------------------------
    def push(self, x):
        """Insert x on top of the stack. O(1)."""
        node = Node(x)
        node.next = self.head
        self.head = node
        self._size += 1

    # ----------------------------------------------------
    def pop(self):
        """Remove and return the top element. O(1)."""
        if self.is_empty():
            raise IndexError("Stack underflow: pop from empty stack")
        value = self.head.value
        self.head = self.head.next
        self._size -= 1
        return value

    # ----------------------------------------------------
    def peek(self):
        """Return the top element without removing it. O(1)."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.head.value

    # ----------------------------------------------------
    def is_empty(self):
        """Return True if the stack has no elements."""
        return self.head is None

    # ----------------------------------------------------
    def size(self):
        """Return the number of elements in the stack."""
        return self._size

    # ----------------------------------------------------
    def display(self):
        """Print the stack from top to bottom."""
        curr = self.head
        values = []
        while curr:
            values.append(curr.value)
            curr = curr.next
        print("Stack (top -> bottom):", values)

    def __repr__(self):
        curr = self.head
        values = []
        while curr:
            values.append(curr.value)
            curr = curr.next
        return f"LinkedListStack({values})"


# --------------------------------------------------------
# Example Usage
# --------------------------------------------------------
if __name__ == "__main__":
    print("--- Array-based Stack ---")
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.display()            # Stack (bottom -> top): [10, 20, 30]

    print("Peek:", s.peek())   # 30
    print("Pop:", s.pop())     # 30
    s.display()            # Stack (bottom -> top): [10, 20]
    print("Size:", s.size())   # 2
    print("Is empty?", s.is_empty())  # False

    bounded = Stack(capacity=2)
    bounded.push(1)
    bounded.push(2)
    try:
        bounded.push(3)     # raises OverflowError
    except OverflowError as e:
        print("Expected error:", e)

    print("\n--- Linked-list-based Stack ---")
    ll_stack = LinkedListStack()
    ll_stack.push(1)
    ll_stack.push(2)
    ll_stack.push(3)
    ll_stack.display()         # Stack (top -> bottom): [3, 2, 1]
    print("Pop:", ll_stack.pop())  # 3
    ll_stack.display()         # Stack (top -> bottom): [2, 1]
