"""
===========================================================
Binary Search Tree (BST) Implementation in Python
===========================================================

A **Binary Search Tree** is a binary tree with an ordering
property: for every node, all values in its left subtree are
smaller and all values in its right subtree are larger. This
property makes search, insert, and delete run in O(H), where
H is the height of the tree (O(log N) average, O(N) worst
case for a skewed tree).

Supported Operations:
----------------------
1. insert(value)          -> O(H)
2. search(value)          -> O(H), returns True/False
3. delete(value)          -> O(H), handles all 3 deletion cases
4. find_min() / find_max()-> O(H)
5. inorder()              -> O(N), returns values in sorted order
6. height()               -> O(N)
7. is_valid_bst()         -> O(N), verifies the BST property holds
8. inorder_successor(v)   -> O(H), smallest value greater than v
9. inorder_predecessor(v) -> O(H), largest value smaller than v
10. kth_smallest(k)       -> O(H + k), via inorder traversal

===========================================================
"""


# --------------------------------------------------------
# Node Class
# --------------------------------------------------------
class Node:
    """A Node of a Binary Search Tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# --------------------------------------------------------
# Binary Search Tree Class
# --------------------------------------------------------
class BinarySearchTree:
    """Binary Search Tree implementation with extended utilities."""

    def __init__(self):
        self.root = None

    # ----------------------------------------------------
    def insert(self, value):
        """Insert a value, maintaining the BST property. O(H)."""
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        # Duplicate values are ignored.
        return node

    # ----------------------------------------------------
    def search(self, value):
        """Return True if value exists in the tree. O(H)."""
        return self._search(self.root, value) is not None

    def _search(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)

    # ----------------------------------------------------
    def delete(self, value):
        """Delete a value from the tree, if present. O(H)."""
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            # Case 1: leaf node -> remove outright.
            if node.left is None and node.right is None:
                return None
            # Case 2: single child -> replace node with that child.
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # Case 3: two children -> replace value with the inorder
            # successor (smallest value in the right subtree), then
            # delete that successor from the right subtree.
            successor = self._find_min_node(node.right)
            node.value = successor.value
            node.right = self._delete(node.right, successor.value)

        return node

    # ----------------------------------------------------
    def find_min(self):
        """Smallest value in the tree. O(H)."""
        if self.root is None:
            return None
        return self._find_min_node(self.root).value

    def _find_min_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    # ----------------------------------------------------
    def find_max(self):
        """Largest value in the tree. O(H)."""
        if self.root is None:
            return None
        node = self.root
        while node.right is not None:
            node = node.right
        return node.value

    # ----------------------------------------------------
    def inorder(self):
        """Values in sorted order. O(N)."""
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
    def height(self):
        """Longest root-to-leaf path, in edges. Empty tree = -1."""
        def _height(node):
            if node is None:
                return -1
            return 1 + max(_height(node.left), _height(node.right))

        return _height(self.root)

    # ----------------------------------------------------
    def is_valid_bst(self):
        """Verify the BST property holds at every node. O(N)."""
        def _validate(node, low, high):
            if node is None:
                return True
            if (low is not None and node.value <= low) or \
               (high is not None and node.value >= high):
                return False
            return (_validate(node.left, low, node.value)
                    and _validate(node.right, node.value, high))

        return _validate(self.root, None, None)

    # ----------------------------------------------------
    def inorder_successor(self, value):
        """Smallest value strictly greater than `value`, or None. O(H)."""
        successor = None
        node = self.root
        while node is not None:
            if value < node.value:
                successor = node.value
                node = node.left
            else:
                node = node.right
        return successor

    # ----------------------------------------------------
    def inorder_predecessor(self, value):
        """Largest value strictly smaller than `value`, or None. O(H)."""
        predecessor = None
        node = self.root
        while node is not None:
            if value > node.value:
                predecessor = node.value
                node = node.right
            else:
                node = node.left
        return predecessor

    # ----------------------------------------------------
    def kth_smallest(self, k):
        """Return the k-th smallest value (1-indexed), or None. O(H + k)."""
        values = self.inorder()
        if k < 1 or k > len(values):
            return None
        return values[k - 1]


# --------------------------------------------------------
# Example Usage
# --------------------------------------------------------
if __name__ == "__main__":
    #         8
    #       /   \
    #      3    10
    #     / \      \
    #    1   6      14
    #       / \    /
    #      4   7  13
    bst = BinarySearchTree()
    for value in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        bst.insert(value)

    print("Inorder (sorted):", bst.inorder())   # [1, 3, 4, 6, 7, 8, 10, 13, 14]
    print("Height:", bst.height())               # 3
    print("Search 7:", bst.search(7))            # True
    print("Search 100:", bst.search(100))        # False
    print("Min:", bst.find_min())                 # 1
    print("Max:", bst.find_max())                 # 14
    print("Is valid BST?", bst.is_valid_bst())     # True

    print("Inorder successor of 7:", bst.inorder_successor(7))     # 8
    print("Inorder predecessor of 7:", bst.inorder_predecessor(7))  # 6
    print("3rd smallest:", bst.kth_smallest(3))                     # 4

    bst.delete(6)   # two-children case -> replaced with successor (7)
    print("Inorder after deleting 6:", bst.inorder())  # [1, 3, 4, 7, 8, 10, 13, 14]

    bst.delete(14)  # one-child case
    print("Inorder after deleting 14:", bst.inorder())  # [1, 3, 4, 7, 8, 10, 13]

    bst.delete(1)   # leaf case
    print("Inorder after deleting 1:", bst.inorder())   # [3, 4, 7, 8, 10, 13]
