# Heap in Python

A **Heap** is a **complete binary tree** that satisfies the **heap property**:

- **Min-Heap**: every parent's value is **≤** both of its children's values → the smallest element is always at the root.
- **Max-Heap**: every parent's value is **≥** both of its children's values → the largest element is always at the root.

Unlike a BST, a heap makes **no guarantee about ordering between siblings or across subtrees** — it only guarantees the parent-child relationship. This weaker guarantee is exactly what makes heap operations O(log N) but restricted to "give me the min/max," rather than arbitrary search.

---

## 1. Why "Complete" Binary Tree Matters

A **complete binary tree** fills every level left to right, with no gaps, except possibly the last level. This property means a heap can be stored **implicitly in a flat array** — no `left`/`right` pointers needed at all.

```text
         1
       /   \
      3     5
     / \   /
    7   8 6

Array:  [1, 3, 5, 7, 8, 6]
Index:   0  1  2  3  4  5
```

### Index Arithmetic (0-indexed array)

| Relationship        | Formula            |
| --------------------- | --------------------|
| Parent of index `i`   | `(i - 1) // 2`       |
| Left child of `i`     | `2*i + 1`            |
| Right child of `i`    | `2*i + 2`            |

No pointers are stored or followed — moving between parent and child is pure arithmetic on the array index. This is also why a heap is dramatically more cache-friendly than a pointer-based tree.

---

## 2. Core Operations

| Operation           | Description                                        | Time Complexity |
| --------------------| ----------------------------------------------------| ------------------|
| `peek()`            | Return the root (min or max) without removing it.   | O(1)               |
| `push(x)`           | Insert x, then restore the heap property (**sift up**). | O(log N)       |
| `pop()`             | Remove the root, move the last element to the root, then restore the heap property (**sift down**). | O(log N) |
| `build_heap(arr)`   | Convert an arbitrary array into a valid heap in-place. | O(N) — see §4    |

### a) Sift Up (used by `push`)

Insert the new element at the **end** of the array (the next open leaf slot, keeping the tree complete), then repeatedly swap it with its parent while it violates the heap property.

```python
def sift_up(heap, i):
    while i > 0:
        parent = (i - 1) // 2
        if heap[i] < heap[parent]:      # min-heap
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
        else:
            break
```

### b) Sift Down (used by `pop` and `build_heap`)

Move a value that may be too large down the tree by repeatedly swapping it with its **smaller child** (min-heap) until the heap property holds.

```python
def sift_down(heap, i, n):
    while True:
        left, right = 2 * i + 1, 2 * i + 2
        smallest = i
        if left < n and heap[left] < heap[smallest]:
            smallest = left
        if right < n and heap[right] < heap[smallest]:
            smallest = right
        if smallest == i:
            break
        heap[i], heap[smallest] = heap[smallest], heap[i]
        i = smallest
```

### Visual: `push(2)` into a min-heap `[1, 3, 5, 7, 8, 6]`

```text
Append 2 at the end, then sift up:

        1                       1
      /   \                   /   \
     3     5                 3     2      <- 2 swapped up past 5
    / \   / \       -->     / \   / \
   7   8 6   2             7   8 6   5

Final array: [1, 3, 2, 7, 8, 6, 5]
```

---

## 3. Array Representation vs Pointer-Based Tree

| Feature                | Array-backed heap        | Pointer-based binary tree |
| ------------------------ | ---------------------------| ------------------------------|
| Space overhead           | None (just the values)     | `left`/`right` pointers per node |
| Cache locality            | Excellent (contiguous)     | Poor (scattered allocations)   |
| Requires "complete tree" | Yes                          | No                              |
| Arbitrary search          | Not supported (only min/max) | Supported (if also a BST)      |

---

## 4. Building a Heap from an Array — O(N), not O(N log N)

The naive approach — inserting N elements one at a time via `push` — costs O(N log N). Instead, **`build_heap`** starts from the last non-leaf node and sifts each one down, working backward to the root:

```python
def build_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):   # last non-leaf node down to root
        sift_down(arr, i, n)
    return arr
```

This achieves **O(N)** overall (not O(N log N)) because most nodes are near the bottom of the tree and only sift down a short distance — the math works out to a convergent sum rather than `N * log N`.

---

## 5. Heap Sort

Heap Sort uses `build_heap` (O(N)) followed by repeatedly swapping the root with the last element and sifting down the reduced heap (O(N log N)) — giving **O(N log N)** overall, **in-place**, with **O(1)** extra space (unlike merge sort's O(N)).

```text
1. build_heap(arr)                     -> arr is now a valid max-heap
2. for end in range(n-1, 0, -1):
       swap arr[0] and arr[end]         -> largest element goes to its final sorted position
       sift_down(arr, 0, end)           -> restore heap property on the shrunk heap
```

| Sort           | Time (Worst) | Space  | Stable? | In-place? |
| ---------------- | --------------| ---------| ---------| ------------|
| Heap Sort         | O(N log N)     | O(1)      | No        | Yes           |
| Merge Sort        | O(N log N)     | O(N)      | Yes       | No            |
| Quick Sort        | O(N²)          | O(log N)  | No        | Yes           |

---

## 6. Python's Built-in `heapq`

Python's `heapq` module implements a **min-heap** directly on top of a regular list — no custom class needed for the common case.

```python
import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
heapq.heappop(heap)          # 1 (smallest)
heapq.heapify([5, 1, 3])     # convert an existing list in-place, O(N)
heapq.nlargest(2, [5, 1, 3, 9])   # [9, 5]
heapq.nsmallest(2, [5, 1, 3, 9])  # [1, 3]
```

**Simulating a max-heap**: negate every value on push/pop (`heapq.heappush(heap, -x)`, then negate again on pop) since `heapq` only provides a min-heap directly.

---

## 7. Complexity Summary

| Operation             | Time         |
| ------------------------| --------------|
| `peek` (min/max)         | O(1)          |
| `push` (insert)          | O(log N)      |
| `pop` (extract min/max)  | O(log N)      |
| `build_heap` (heapify)   | O(N)          |
| Heap Sort                | O(N log N)    |

---

## 8. Heap vs BST vs Sorted Array

| Feature                    | Heap          | BST (balanced)  | Sorted Array   |
| ----------------------------- | ---------------| -------------------| -----------------|
| Find min/max                  | O(1)             | O(log N)             | O(1)               |
| Extract min/max                | O(log N)         | O(log N)             | O(N) — shift needed |
| Insert                          | O(log N)         | O(log N)             | O(N) — shift needed |
| Arbitrary search                | O(N)             | O(log N)             | O(log N)            |
| Get sorted order                 | O(N log N)       | O(N) — inorder        | O(1) — already sorted |

**Use a heap when you repeatedly need the min/max and don't care about full ordering** — this is exactly the **Priority Queue** abstraction.

---

## 9. Applications

- **Priority Queues** — task schedulers, Dijkstra's & Prim's algorithms (see [`15_Graph`](../15_Graph/03_Graph_Algorithms.py)).
- **Heap Sort**.
- **Top-K problems** — K largest/smallest elements, K closest points, top-K frequent elements.
- **Median of a data stream** — using two heaps (a max-heap for the lower half, a min-heap for the upper half).
- **Merge K sorted lists/arrays** — a min-heap of the current fronts of each list.
- **Huffman Coding** — a min-heap of character frequencies drives optimal prefix-code construction.
- **Load balancing / event simulation** — always process the next event, ordered by time.

---

## ✅ Summary

- A heap is a **complete binary tree**, stored as a **flat array**, satisfying the parent ≤ children (min-heap) or parent ≥ children (max-heap) property — but no ordering guarantee beyond that.
- **`push`** sifts a new element **up**; **`pop`** sifts the replacement root **down** — both O(log N).
- **`build_heap`** on an existing array is **O(N)**, not O(N log N) — always prefer it over repeated `push` when heapifying a known array upfront.
- Python's `heapq` module is a ready-made min-heap; negate values to simulate a max-heap.
- The defining use case is a **Priority Queue**: repeatedly needing the current min/max without needing full sorted order.
