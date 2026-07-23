# Trees in Python

A **Tree** is a non-linear, hierarchical data structure made up of nodes connected by edges, with one node designated as the **root**. Unlike arrays, linked lists, stacks, and queues (all linear), a tree lets each element branch out to multiple elements — making it the natural way to represent hierarchical relationships (file systems, org charts, HTML DOM, decision logic, etc).

---

## 1. Terminology

| Term          | Meaning                                                                 |
| ------------- | ------------------------------------------------------------------------ |
| **Root**      | The topmost node of the tree (no parent).                                |
| **Node**      | Each element of the tree, holding data and links to children.            |
| **Edge**      | The connection between a parent node and a child node.                   |
| **Parent**    | A node that has one or more child nodes.                                 |
| **Child**     | A node directly connected to (and below) a parent node.                  |
| **Sibling**   | Nodes that share the same parent.                                        |
| **Leaf**      | A node with no children.                                                 |
| **Ancestor**  | Any node on the path from the root to a given node (excluding itself).   |
| **Descendant**| Any node reachable by moving downward from a given node.                 |
| **Subtree**   | A tree formed by a node and all of its descendants.                      |
| **Depth**     | Number of edges from the **root** to a given node.                       |
| **Height**    | Number of edges on the **longest path** from a given node to a leaf.     |
| **Level**     | `depth + 1` — the "row" a node sits on (root is level 1).                |
| **Degree**    | Number of children a node has.                                           |

### Visual Representation

```text
                 1            <- root, level 1, depth 0
               /   \
              2     3         <- level 2, depth 1
             / \     \
            4   5     6       <- level 3, depth 2 (leaves: 4, 5, 6)

height of the tree = 2 (longest path: 1 -> 2 -> 4, two edges)
```

---

## 2. Types of Trees

- **General Tree**: a node can have any number of children.
- **Binary Tree**: every node has **at most 2 children** — `left` and `right`.
  - **Full Binary Tree**: every node has 0 or 2 children (never exactly 1).
  - **Complete Binary Tree**: all levels are completely filled except possibly the last, which is filled left to right. (Used for array-backed **Heaps**.)
  - **Perfect Binary Tree**: all internal nodes have 2 children **and** all leaves are at the same level.
  - **Balanced Binary Tree**: for every node, the height difference between its left and right subtrees is at most 1 (e.g. AVL tree).
  - **Degenerate / Skewed Tree**: each parent has only one child — effectively a linked list, worst case O(N) operations.
- **Binary Search Tree (BST)**: a binary tree with an ordering property (see §5).
- **Heap**: a complete binary tree with a min/max-ordering property, typically array-backed (used for priority queues).
- **Trie**: a tree specialized for storing strings, where each edge represents a character.
- **Self-balancing trees** (AVL, Red-Black Tree): BSTs that automatically re-balance after insert/delete to guarantee O(log N) operations (see §7).

```text
Full            Complete         Perfect          Skewed
  1                1                1                1
 / \              / \              / \                \
2   3            2   3            2   3                2
   / \          / \                 / \                  \
  4   5        4   5               4   5                  3
```

---

## 3. Representing a Binary Tree

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

A tree is simply a reference to its **root** `Node`; everything else is reached by following `left`/`right` pointers.

---

## 4. Tree Traversals

There are two broad traversal strategies: **Depth-First Search (DFS)** — go as deep as possible before backtracking — and **Breadth-First Search (BFS)** — visit level by level.

Given this example tree:

```text
        1
       / \
      2   3
     / \
    4   5
```

### a) Preorder (Root → Left → Right)

Visit the node before its children. Used to **copy/serialize** a tree (root is emitted first, so it can be rebuilt top-down).

```python
def preorder(node, result):
    if node is None:
        return
    result.append(node.value)   # Root
    preorder(node.left, result)  # Left
    preorder(node.right, result) # Right
```

Output: `1 2 4 5 3`

**Iterative (using an explicit stack):**

```python
def preorder_iterative(root):
    if root is None:
        return []
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        result.append(node.value)
        if node.right:   # push right first so left is processed first
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result
```

### b) Inorder (Left → Root → Right)

Visits nodes of a **BST in sorted order** — the most common reason to use inorder traversal.

```python
def inorder(node, result):
    if node is None:
        return
    inorder(node.left, result)   # Left
    result.append(node.value)    # Root
    inorder(node.right, result)  # Right
```

Output: `4 2 5 1 3`

### c) Postorder (Left → Right → Root)

Visit children before the node itself. Used to **safely delete/free a tree** (children are processed before their parent) and to evaluate expression trees.

```python
def postorder(node, result):
    if node is None:
        return
    postorder(node.left, result)   # Left
    postorder(node.right, result)  # Right
    result.append(node.value)      # Root
```

Output: `4 5 2 3 1`

### d) Level Order (Breadth-First, using a Queue)

Visits nodes level by level, left to right — this is the one traversal that is **not** naturally recursive; it needs a queue (see [`13_Queues`](../13_Queues/01_Queue_intro.md)).

```python
from collections import deque

def level_order(root):
    if root is None:
        return []
    result, q = [], deque([root])
    while q:
        node = q.popleft()
        result.append(node.value)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return result
```

Output: `1 2 3 4 5`

---

## 5. Traversal Complexity

| Traversal      | Time  | Space (recursive)         | Space (iterative) |
| -------------- | ----- | --------------------------- | -------------------- |
| Preorder       | O(N)  | O(H) — call stack           | O(H) — explicit stack |
| Inorder        | O(N)  | O(H) — call stack           | O(H) — explicit stack |
| Postorder      | O(N)  | O(H) — call stack           | O(H) — explicit stack |
| Level Order    | O(N)  | —                            | O(W) — queue          |

*H = height of the tree, W = maximum width of the tree. For a skewed tree H = N; for a balanced tree H = O(log N).*

---

## 6. Binary Search Tree (BST)

A **BST** is a binary tree with one extra rule at every node:

> **All values in the left subtree < node's value < all values in the right subtree.**

This ordering is what makes **search, insert, and delete run in O(H)** — at each step you eliminate one entire subtree, just like binary search on a sorted array.

```text
        8
       / \
      3    10
     / \      \
    1   6      14
       / \    /
      4   7  13
```

### Search

```python
def search(node, key):
    if node is None or node.value == key:
        return node
    if key < node.value:
        return search(node.left, key)
    return search(node.right, key)
```

### Insert

```python
def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.value:
        node.left = insert(node.left, key)
    elif key > node.value:
        node.right = insert(node.right, key)
    return node   # duplicates are ignored
```

### Delete — Three Cases

1. **Node is a leaf** → simply remove it.
2. **Node has one child** → replace the node with its child.
3. **Node has two children** → replace the node's value with its **inorder successor** (the smallest value in the right subtree, i.e. leftmost node of the right subtree), then delete that successor node from the right subtree.

```text
delete(6):                       replace 6 with inorder successor (7):
        8                                 8
       / \                               / \
      3    10                           3    10
     / \      \          ->            / \      \
    1   6      14                     1   7      14
       / \    /                            \    /
      4   7  13                             (7 removed from here)  13
```

### Complexity

| Operation | Average (balanced BST) | Worst case (skewed BST) |
| --------- | ------------------------ | -------------------------- |
| Search    | O(log N)                 | O(N)                        |
| Insert    | O(log N)                 | O(N)                        |
| Delete    | O(log N)                 | O(N)                        |

The worst case degrades to a linked list when elements are inserted in already-sorted order — this is exactly why **self-balancing trees** exist.

---

## 7. Self-Balancing Trees (Concept)

A plain BST can become skewed (O(N) worst case). Self-balancing trees restore balance automatically after every insert/delete, guaranteeing **O(log N)** in the worst case too.

- **AVL Tree**: after every insert/delete, checks the balance factor (`height(left) - height(right)`) at each ancestor. If it exceeds ±1, performs a **rotation** (left rotation, right rotation, or a double rotation) to restore balance. Stricter balance than Red-Black trees → faster lookups, slightly slower inserts.
- **Red-Black Tree**: each node is colored red or black following rules that bound the longest root-to-leaf path to at most twice the shortest. Looser balance than AVL → faster inserts/deletes, slightly slower lookups. Used internally by many language standard libraries (e.g. C++ `std::map`, Java `TreeMap`).

*(Rotation mechanics and full implementations are out of scope here — the key takeaway is: plain BSTs need external balancing to guarantee O(log N).)*

---

## 8. Height, Diameter & Balance Checks

```python
def height(node):
    """Height of an empty tree is -1; a single node has height 0."""
    if node is None:
        return -1
    return 1 + max(height(node.left), height(node.right))

def diameter(node):
    """Diameter = number of edges on the longest path between any 2 nodes."""
    if node is None:
        return 0, -1   # (diameter, height)
    left_dia, left_h = diameter(node.left)
    right_dia, right_h = diameter(node.right)
    curr_dia = left_h + right_h + 2
    return max(curr_dia, left_dia, right_dia), 1 + max(left_h, right_h)

def is_balanced(node):
    """A tree is height-balanced if this holds true at every node."""
    if node is None:
        return True
    lh, rh = height(node.left), height(node.right)
    return (abs(lh - rh) <= 1
            and is_balanced(node.left)
            and is_balanced(node.right))
```

---

## 9. Applications

- **File systems & directory structures** (folders containing files/folders).
- **DOM (Document Object Model)** in web browsers.
- **Databases & indexing**: B-Trees / B+ Trees power most database indexes.
- **Decision trees** in machine learning.
- **Expression / syntax trees** used by compilers and calculators.
- **Heaps** (complete binary trees) implement **priority queues**.
- **Tries** implement autocomplete and spell-checking.
- **Huffman coding trees** for compression.

---

## 10. Tree vs Linked List vs Graph

| Feature              | Linked List        | Tree                          | Graph                          |
| --------------------- | -------------------- | -------------------------------| --------------------------------|
| Structure             | Linear               | Hierarchical (no cycles)       | Can be cyclic or acyclic        |
| Number of children    | 1 (`next`)           | 0 to N (0–2 for binary trees)  | Arbitrary (via edges)           |
| Root concept           | No fixed "root"      | Exactly one root               | No inherent root                |
| Typical traversal     | Linear iteration     | DFS (pre/in/post) or BFS       | DFS / BFS                       |

---

## ✅ Summary

- A tree is a **hierarchical**, **acyclic**, **connected** structure with one root.
- **DFS** traversals (preorder, inorder, postorder) use recursion or an explicit stack; **BFS** (level order) needs a queue.
- **Inorder traversal of a BST yields sorted order** — the single most useful BST fact.
- BST search/insert/delete are **O(log N)** on average but degrade to **O(N)** when skewed — this is exactly the problem AVL/Red-Black trees solve.
- Trees underpin file systems, databases, compilers, and priority queues.
