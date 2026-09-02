"""
===========================================================
Heap Implementation in Python (Array-Backed)
===========================================================

A **Heap** is a complete binary tree stored as a flat array,
where index arithmetic replaces `left`/`right` pointers:
    parent(i) = (i - 1) // 2
    left(i)   = 2*i + 1
    right(i)  = 2*i + 2

Two classes are provided (`MinHeap`, `MaxHeap`), plus a
standalone `heap_sort` function that heapifies in-place.

Supported Operations (both classes):
-------------------------------------
1. push(x)         -> insert x, sift up.               O(log N)
2. pop()           -> remove & return the root.        O(log N)
3. peek()          -> return the root without removing. O(1)
4. build_heap(arr) -> classmethod, heapify an existing list. O(N)
5. is_empty()      -> check if heap has no elements.    O(1)
6. size()          -> number of elements.               O(1)

===========================================================
"""


# --------------------------------------------------------
# Min-Heap
# --------------------------------------------------------
class MinHeap:
    """Array-backed Min-Heap: the smallest element is always at the root."""

    def __init__(self):
        self.data = []

    # ----------------------------------------------------
    @classmethod
    def build_heap(cls, arr):
        """Heapify an existing list in-place. O(N)."""
        heap = cls()
        heap.data = list(arr)
        n = len(heap.data)
        for i in range(n // 2 - 1, -1, -1):
            heap._sift_down(i)
        return heap

    # ----------------------------------------------------
    def push(self, value):
        """Insert value, then sift up to restore the heap property. O(log N)."""
        self.data.append(value)
        self._sift_up(len(self.data) - 1)

    # ----------------------------------------------------
    def pop(self):
        """Remove and return the smallest element. O(log N)."""
        if self.is_empty():
            raise IndexError("pop from empty heap")
        root = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self._sift_down(0)
        return root

    # ----------------------------------------------------
    def peek(self):
        """Return the smallest element without removing it. O(1)."""
        if self.is_empty():
            raise IndexError("peek from empty heap")
        return self.data[0]

    # ----------------------------------------------------
    def is_empty(self):
        return len(self.data) == 0

    # ----------------------------------------------------
    def size(self):
        return len(self.data)

    # ----------------------------------------------------
    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.data[i] < self.data[parent]:
                self.data[i], self.data[parent] = self.data[parent], self.data[i]
                i = parent
            else:
                break

    # ----------------------------------------------------
    def _sift_down(self, i):
        n = len(self.data)
        while True:
            left, right = 2 * i + 1, 2 * i + 2
            smallest = i
            if left < n and self.data[left] < self.data[smallest]:
                smallest = left
            if right < n and self.data[right] < self.data[smallest]:
                smallest = right
            if smallest == i:
                break
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            i = smallest

    def __repr__(self):
        return f"MinHeap({self.data})"


# --------------------------------------------------------
# Max-Heap
# --------------------------------------------------------
class MaxHeap:
    """Array-backed Max-Heap: the largest element is always at the root.
    Mirrors `MinHeap` with comparisons flipped.
    """

    def __init__(self):
        self.data = []

    # ----------------------------------------------------
    @classmethod
    def build_heap(cls, arr):
        """Heapify an existing list in-place. O(N)."""
        heap = cls()
        heap.data = list(arr)
        n = len(heap.data)
        for i in range(n // 2 - 1, -1, -1):
            heap._sift_down(i)
        return heap

    # ----------------------------------------------------
    def push(self, value):
        """Insert value, then sift up to restore the heap property. O(log N)."""
        self.data.append(value)
        self._sift_up(len(self.data) - 1)

    # ----------------------------------------------------
    def pop(self):
        """Remove and return the largest element. O(log N)."""
        if self.is_empty():
            raise IndexError("pop from empty heap")
        root = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self._sift_down(0)
        return root

    # ----------------------------------------------------
    def peek(self):
        """Return the largest element without removing it. O(1)."""
        if self.is_empty():
            raise IndexError("peek from empty heap")
        return self.data[0]

    # ----------------------------------------------------
    def is_empty(self):
        return len(self.data) == 0

    # ----------------------------------------------------
    def size(self):
        return len(self.data)

    # ----------------------------------------------------
    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.data[i] > self.data[parent]:
                self.data[i], self.data[parent] = self.data[parent], self.data[i]
                i = parent
            else:
                break

    # ----------------------------------------------------
    def _sift_down(self, i):
        n = len(self.data)
        while True:
            left, right = 2 * i + 1, 2 * i + 2
            largest = i
            if left < n and self.data[left] > self.data[largest]:
                largest = left
            if right < n and self.data[right] > self.data[largest]:
                largest = right
            if largest == i:
                break
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            i = largest

    def __repr__(self):
        return f"MaxHeap({self.data})"


# --------------------------------------------------------
# Heap Sort (in-place, ascending, via a max-heap)
# --------------------------------------------------------
def heap_sort(arr):
    """Sort `arr` in ascending order in-place using Heap Sort.
    O(N log N) time, O(1) extra space.
    """
    n = len(arr)

    def sift_down(end, i):
        while True:
            left, right = 2 * i + 1, 2 * i + 2
            largest = i
            if left < end and arr[left] > arr[largest]:
                largest = left
            if right < end and arr[right] > arr[largest]:
                largest = right
            if largest == i:
                break
            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest

    # Build a max-heap. O(N).
    for i in range(n // 2 - 1, -1, -1):
        sift_down(n, i)

    # Repeatedly move the max to the end, then re-heapify the rest.
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(end, 0)

    return arr


# --------------------------------------------------------
# Example Usage
# --------------------------------------------------------
if __name__ == "__main__":
    print("--- MinHeap ---")
    min_heap = MinHeap.build_heap([5, 3, 8, 1, 9, 2])
    print("Heapified:", min_heap)
    min_heap.push(0)
    print("After push(0):", min_heap)
    print("Peek:", min_heap.peek())          # 0
    print("Pop order:", [min_heap.pop() for _ in range(min_heap.size())])
    # [0, 1, 2, 3, 5, 8, 9]

    print("\n--- MaxHeap ---")
    max_heap = MaxHeap.build_heap([5, 3, 8, 1, 9, 2])
    print("Heapified:", max_heap)
    print("Pop order:", [max_heap.pop() for _ in range(max_heap.size())])
    # [9, 8, 5, 3, 2, 1]

    print("\n--- Heap Sort ---")
    print(heap_sort([5, 3, 8, 1, 9, 2]))       # [1, 2, 3, 5, 8, 9]
