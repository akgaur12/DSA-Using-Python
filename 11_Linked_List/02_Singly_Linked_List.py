"""
===========================================================
Singly Linked List Implementation in Python
===========================================================

A **Singly Linked List (SLL)** is a linear data structure in 
which elements (nodes) are connected using pointers. Each node 
contains:
    1. `val` → stores the value
    2. `next` → reference (pointer) to the next node

The last node points to `None`, marking the end of the list.

Supported Operations:
---------------------
1. Display the list
2. Insert at beginning
3. Insert at end
4. Insert at specific position
5. Delete node by value
6. Search node by value
7. Length of the list
8. Reverse the list
9. Find middle element
10. Detect cycle (Floyd’s algorithm)
11. Remove duplicates (sorted list)
12. Convert linked list to Python list

===========================================================
"""

# --------------------------------------------------------
# Node Class
# --------------------------------------------------------
class Node:
    """A Node of a Singly Linked List."""
    def __init__(self, val):
        self.val = val    # store val
        self.next = None    # pointer to next node


# --------------------------------------------------------
# Singly Linked List Class
# --------------------------------------------------------
class LinkedList:
    """Singly Linked List implementation with extended utilities."""
    def __init__(self):
        self.head = None

    # ----------------------------------------------------
    def display(self):
        """Traverse and print all nodes of the linked list."""
        if self.head is None:
            print("Singly Linked List is empty")
        else:
            curr = self.head
            while curr:
                print(curr.val, end=" -> ")
                curr = curr.next
            print("None")

    # ----------------------------------------------------
    def insert_at_beginning(self, val):
        """Insert a new node at the beginning of the list. O(1)."""
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    # ----------------------------------------------------
    def insert_at_end(self, val):
        """Insert a new node at the end of the list. O(n)."""
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    # ----------------------------------------------------
    def insert_at_position(self, val, pos):
        """
        Insert a new node at a specific position (0-based index).
        If pos == 0 → insert at beginning.
        """
        if pos == 0:
            self.insert_at_beginning(val)
            return
        new_node = Node(val)
        curr = self.head
        for _ in range(pos - 1):
            if curr is None:
                print("Position out of range")
                return
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node

    # ----------------------------------------------------
    def delete_node(self, key):
        """Delete the first node containing 'key'. O(n)."""
        curr = self.head

        # If head node holds the key
        if curr and curr.val == key:
            self.head = curr.next
            curr = None
            return

        prev = None
        while curr and curr.val != key:
            prev = curr
            curr = curr.next

        if curr is None:
            print("Value not found")
            return

        prev.next = curr.next
        curr = None

    # ----------------------------------------------------
    def search(self, key):
        """Search for a node with value 'key'. Returns True/False."""
        curr = self.head
        pos = 0
        while curr:
            if curr.val == key:
                print(f"Found {key} at position {pos}")
                return True
            curr = curr.next
            pos += 1
        print(f"{key} not found")
        return False

    # ----------------------------------------------------
    def length(self):
        """Return the number of nodes in the list. O(n)."""
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    # ----------------------------------------------------
    def reverse(self):
        """Reverse the linked list in-place. O(n)."""
        prev, curr = None, self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    # ----------------------------------------------------
    def find_middle(self):
        """
        Find the middle element using slow/fast pointers.
        Returns None if list is empty.
        """
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.val if slow else None

    # ----------------------------------------------------
    def detect_cycle(self):
        """
        Detect cycle in the linked list using Floyd’s Cycle Detection.
        Returns True if cycle exists, False otherwise.
        """
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    # ----------------------------------------------------
    def remove_duplicates(self):
        """
        Remove duplicates from a sorted linked list. O(n).
        Assumes the list is sorted.
        """
        curr = self.head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

    # ----------------------------------------------------
    def to_list(self):
        """Convert linked list to a Python list."""
        result = []
        curr = self.head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result


# --------------------------------------------------------
# Example Usage
# --------------------------------------------------------
if __name__ == "__main__":
    ll = LinkedList()

    # Insert nodes
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.display()  # 10 -> 20 -> 30 -> None

    ll.insert_at_beginning(5)
    ll.display()  # 5 -> 10 -> 20 -> 30 -> None

    ll.insert_at_position(15, 2)
    ll.display()  # 5 -> 10 -> 15 -> 20 -> 30 -> None

    # Delete and search
    ll.delete_node(20)
    ll.display()  # 5 -> 10 -> 15 -> 30 -> None
    ll.search(15)
    ll.search(50)

    # Length and middle
    print("Length:", ll.length())          # 4
    print("Middle:", ll.find_middle())     # 15

    # Reverse list
    ll.reverse()
    ll.display()  # 30 -> 15 -> 10 -> 5 -> None

    # Remove duplicates (example: sorted list with duplicates)
    sorted_ll = LinkedList()
    for x in [1, 2, 2, 3, 3, 3, 4]:
        sorted_ll.insert_at_end(x)
    print("Before removing duplicates:", sorted_ll.to_list())
    sorted_ll.remove_duplicates()
    print("After removing duplicates :", sorted_ll.to_list())

    # Cycle detection (should be False here)
    print("Has cycle?", ll.detect_cycle())
