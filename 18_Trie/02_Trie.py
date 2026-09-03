"""
===========================================================
Trie (Prefix Tree) Implementation in Python
===========================================================

A **Trie** stores a set of strings character by character
along tree edges, so words sharing a prefix share the same
path. This implementation uses a `dict` for each node's
children, supporting any character set (not just lowercase
English).

Supported Operations:
-----------------------
1. insert(word)              -> O(L)
2. search(word)               -> O(L), exact word match.
3. starts_with(prefix)        -> O(L), does any word start with prefix?
4. delete(word)               -> O(L), removes a word and prunes
                                  now-unused nodes.
5. words_with_prefix(prefix)  -> O(L + K), all stored words starting
                                  with prefix (K = total characters
                                  across matches) — autocomplete.
6. count_words_with_prefix(prefix) -> O(L + K), how many words
                                  start with prefix.
7. count_words()              -> O(N), total words stored.

===========================================================
"""


# --------------------------------------------------------
# Trie Node
# --------------------------------------------------------
class TrieNode:
    """A single node of a Trie."""
    def __init__(self):
        self.children = {}          # character -> TrieNode
        self.is_end_of_word = False


# --------------------------------------------------------
# Trie Class
# --------------------------------------------------------
class Trie:
    """Trie (Prefix Tree) supporting insert, search, prefix
    queries, deletion, and autocomplete-style prefix listing.
    """

    def __init__(self):
        self.root = TrieNode()

    # ----------------------------------------------------
    def insert(self, word):
        """Insert `word` into the trie. O(len(word))."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    # ----------------------------------------------------
    def search(self, word):
        """True if `word` was inserted exactly. O(len(word))."""
        node = self._find_node(word)
        return node is not None and node.is_end_of_word

    # ----------------------------------------------------
    def starts_with(self, prefix):
        """True if any inserted word starts with `prefix`. O(len(prefix))."""
        return self._find_node(prefix) is not None

    # ----------------------------------------------------
    def delete(self, word):
        """Remove `word` from the trie, pruning nodes that become
        unused. Returns True if the word was found and removed.
        O(len(word)).
        """
        def _delete(node, i):
            if i == len(word):
                if not node.is_end_of_word:
                    return False       # word was never inserted
                node.is_end_of_word = False
                return len(node.children) == 0   # prune if now a dead end

            char = word[i]
            child = node.children.get(char)
            if child is None:
                return False            # word was never inserted

            should_prune_child = _delete(child, i + 1)
            if should_prune_child:
                del node.children[char]

            # Prune this node too if it's now a dead end (not the
            # end of another word and has no remaining children).
            return not node.is_end_of_word and len(node.children) == 0

        if not self.search(word):
            return False
        _delete(self.root, 0)
        return True

    # ----------------------------------------------------
    def words_with_prefix(self, prefix):
        """All inserted words that start with `prefix`, via DFS from
        the prefix's node. O(len(prefix) + total characters returned).
        """
        node = self._find_node(prefix)
        if node is None:
            return []

        results = []

        def _collect(node, path):
            if node.is_end_of_word:
                results.append(prefix + path)
            for char, child in node.children.items():
                _collect(child, path + char)

        _collect(node, "")
        return results

    # ----------------------------------------------------
    def count_words_with_prefix(self, prefix):
        """Number of inserted words that start with `prefix`."""
        return len(self.words_with_prefix(prefix))

    # ----------------------------------------------------
    def count_words(self):
        """Total number of words stored in the trie. O(N total nodes)."""
        return len(self.words_with_prefix(""))

    # ----------------------------------------------------
    def _find_node(self, prefix):
        """Return the node reached by following `prefix`, or None
        if the path doesn't fully exist.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node


# --------------------------------------------------------
# Example Usage
# --------------------------------------------------------
if __name__ == "__main__":
    trie = Trie()
    for word in ["cat", "car", "card", "care", "dog", "do"]:
        trie.insert(word)

    print("search('car'):", trie.search("car"))            # True
    print("search('ca'):", trie.search("ca"))               # False (only a prefix)
    print("starts_with('ca'):", trie.starts_with("ca"))     # True
    print("starts_with('do'):", trie.starts_with("do"))     # True
    print("starts_with('xy'):", trie.starts_with("xy"))     # False

    print("words_with_prefix('car'):", sorted(trie.words_with_prefix("car")))
    # ['car', 'card', 'care']
    print("count_words_with_prefix('ca'):", trie.count_words_with_prefix("ca"))
    # 4 -> cat, car, card, care
    print("Total words:", trie.count_words())               # 6

    print("\nDeleting 'card'...")
    trie.delete("card")
    print("search('card'):", trie.search("card"))            # False
    print("search('car'):", trie.search("car"))              # True (untouched)
    print("starts_with('card'):", trie.starts_with("card"))  # False (path pruned)
    print("words_with_prefix('ca'):", sorted(trie.words_with_prefix("ca")))
    # ['car', 'care', 'cat']  ('card' is gone)
