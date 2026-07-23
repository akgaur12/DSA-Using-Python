"""
===========================================================
Binary Tree Implementation in Python
===========================================================

A **Binary Tree** is a hierarchical data structure in which
each node has at most two children, referred to as `left`
and `right`. This file implements a generic binary tree
(no ordering property — see `03_Binary_Search_Tree.py` for
that) along with the standard traversal and metric
algorithms taught alongside it.

Supported Operations:
----------------------
1. insert(value)          -> level-order insert (keeps the tree
                              filled left-to-right, like a
                              complete binary tree).
2. preorder()             -> Root -> Left -> Right   (recursive)
3. inorder()              -> Left -> Root -> Right   (recursive)
4. postorder()            -> Left -> Right -> Root   (recursive)
5. preorder_iterative()   -> Preorder using an explicit stack.
6. level_order()          -> Breadth-first traversal using a queue.
7. height()               -> Longest root-to-leaf path (edges).
8. size()                 -> Total number of nodes.
9. diameter()             -> Longest path between any two nodes.
10. is_balanced()         -> Height-balanced check at every node.
11. is_symmetric()        -> Mirror-image check around the root.
12. mirror()              -> Invert the tree in-place.
13. max_value() / min_value() -> Largest / smallest value in the tree.

===========================================================
"""

from collections import deque


# --------------------------------------------------------
# Node Class
# --------------------------------------------------------
class Node:
    """A Node of a Binary Tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# --------------------------------------------------------
# Binary Tree Class
# --------------------------------------------------------
class BinaryTree:
    """Generic Binary Tree (no ordering property)."""

    def __init__(self):
        self.root = None

    # ----------------------------------------------------
    def insert(self, value):
        """Insert a value using level-order insertion, i.e. fill
        the first available empty left/right slot found via BFS.
        O(N) — has to search for the first empty slot.
        """
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return

        queue = deque([self.root])
        while queue:
            curr = queue.popleft()
            if curr.left is None:
                curr.left = new_node
                return
            queue.append(curr.left)

            if curr.right is None:
                curr.right = new_node
                return
            queue.append(curr.right)

    # ----------------------------------------------------
    def preorder(self):
        """Root -> Left -> Right. O(N)."""
        result = []

        def _walk(node):
            if node is None:
                return
            result.append(node.value)
            _walk(node.left)
            _walk(node.right)

        _walk(self.root)
        return result

    # ----------------------------------------------------
    def inorder(self):
        """Left -> Root -> Right. O(N)."""
        result = []

        def _walk(node):
            if node is None:
                return
            _walk(node.left)
            result.append(node.value)
            _walk(node.right)

        _walk(self.root)
        return result

    # ----------------------------------------------------
    def postorder(self):
        """Left -> Right -> Root. O(N)."""
        result = []

        def _walk(node):
            if node is None:
                return
            _walk(node.left)
            _walk(node.right)
            result.append(node.value)

        _walk(self.root)
        return result

    # ----------------------------------------------------
    def preorder_iterative(self):
        """Root -> Left -> Right, using an explicit stack. O(N)."""
        if self.root is None:
            return []
        result, stack = [], [self.root]
        while stack:
            node = stack.pop()
            result.append(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    # ----------------------------------------------------
    def level_order(self):
        """Breadth-first traversal, level by level. O(N)."""
        if self.root is None:
            return []
        result, queue = [], deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    # ----------------------------------------------------
    def height(self):
        """Longest root-to-leaf path, in edges. Empty tree = -1."""
        def _height(node):
            if node is None:
                return -1
            return 1 + max(_height(node.left), _height(node.right))

        return _height(self.root)

    # ----------------------------------------------------
    def size(self):
        """Total number of nodes. O(N)."""
        def _size(node):
            if node is None:
                return 0
            return 1 + _size(node.left) + _size(node.right)

        return _size(self.root)

    # ----------------------------------------------------
    def diameter(self):
        """Longest path between any two nodes, in edges. O(N)."""
        best = -1

        def _walk(node):
            nonlocal best
            if node is None:
                return -1
            left_h = _walk(node.left)
            right_h = _walk(node.right)
            best = max(best, left_h + right_h + 2)
            return 1 + max(left_h, right_h)

        _walk(self.root)
        return max(best, 0)

    # ----------------------------------------------------
    def is_balanced(self):
        """True if, at every node, |height(left) - height(right)| <= 1."""
        def _check(node):
            if node is None:
                return True, -1
            left_ok, left_h = _check(node.left)
            right_ok, right_h = _check(node.right)
            balanced = left_ok and right_ok and abs(left_h - right_h) <= 1
            return balanced, 1 + max(left_h, right_h)

        return _check(self.root)[0]

    # ----------------------------------------------------
    def is_symmetric(self):
        """True if the tree is a mirror image of itself around the root."""
        def _is_mirror(a, b):
            if a is None and b is None:
                return True
            if a is None or b is None:
                return False
            return (a.value == b.value
                    and _is_mirror(a.left, b.right)
                    and _is_mirror(a.right, b.left))

        if self.root is None:
            return True
        return _is_mirror(self.root.left, self.root.right)

    # ----------------------------------------------------
    def mirror(self):
        """Invert the tree in-place (swap left/right at every node)."""
        def _mirror(node):
            if node is None:
                return
            node.left, node.right = node.right, node.left
            _mirror(node.left)
            _mirror(node.right)

        _mirror(self.root)

    # ----------------------------------------------------
    def max_value(self):
        """Largest value in the tree. O(N)."""
        return max(self.preorder())

    # ----------------------------------------------------
    def min_value(self):
        """Smallest value in the tree. O(N)."""
        return min(self.preorder())


# --------------------------------------------------------
# Example Usage
# --------------------------------------------------------
if __name__ == "__main__":
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    tree = BinaryTree()
    for value in [1, 2, 3, 4, 5]:
        tree.insert(value)

    print("Preorder :", tree.preorder())              # [1, 2, 4, 5, 3]
    print("Inorder  :", tree.inorder())                # [4, 2, 5, 1, 3]
    print("Postorder:", tree.postorder())              # [4, 5, 2, 3, 1]
    print("Level Order:", tree.level_order())          # [1, 2, 3, 4, 5]
    print("Preorder (iterative):", tree.preorder_iterative())  # [1, 2, 4, 5, 3]

    print("Height   :", tree.height())                 # 2
    print("Size     :", tree.size())                   # 5
    print("Diameter :", tree.diameter())                # 3 (4 -> 2 -> 1 -> 3)
    print("Balanced?:", tree.is_balanced())             # True
    print("Symmetric?:", tree.is_symmetric())           # False
    print("Max value:", tree.max_value())               # 5
    print("Min value:", tree.min_value())               # 1

    tree.mirror()
    print("Level Order after mirror:", tree.level_order())  # [1, 3, 2, 5, 4]
