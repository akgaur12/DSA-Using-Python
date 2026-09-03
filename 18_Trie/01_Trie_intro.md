# Trie (Prefix Tree) in Python

A **Trie** (pronounced "try", from re**trie**val) is a tree specialized for storing a set of strings, where **each edge represents a single character** rather than a whole value. Every path from the root spells out a prefix, and words sharing a common prefix share the same path — making prefix-based operations (search, autocomplete, prefix counting) far more efficient than scanning a list of strings.

---

## 1. Structure

Each node holds:
- A mapping from **character → child node** (one child per distinct next character).
- A boolean flag `is_end_of_word` marking whether a complete word ends at this node.

```python
class TrieNode:
    def __init__(self):
        self.children = {}          # char -> TrieNode
        self.is_end_of_word = False
```

### Visual Representation

Inserting `"cat"`, `"car"`, `"card"`, `"dog"`:

```text
                root
               /    \
              c      d
              |      |
              a      o
             / \     |
            t   r    g*
            *   |
                d
                *

* marks is_end_of_word = True (for "cat", "card", "dog")
  Note: "car" is a PREFIX of "card" but not itself marked as a
  complete word unless explicitly inserted — inserting "card"
  does NOT automatically mark "car" as a word.
```

Notice `c → a` is shared by both `"cat"` and `"car"`/`"card"` — this **shared-prefix compression** is the entire point of a trie: common prefixes are stored exactly once, no matter how many words share them.

---

## 2. Core Operations

| Operation              | Description                                          | Time Complexity |
| ------------------------| -------------------------------------------------------| -------------------|
| `insert(word)`          | Add a word, creating nodes for any new characters.      | O(L)                |
| `search(word)`          | Check if the **exact word** exists in the trie.          | O(L)                |
| `starts_with(prefix)`   | Check if **any** word in the trie starts with `prefix`.  | O(L)                |
| `delete(word)`          | Remove a word (pruning now-unused nodes).                | O(L)                |

*L = length of the word/prefix being processed — crucially, this does **not** depend on how many words are stored in the trie, unlike scanning a list.*

### a) Insert

```python
def insert(self, word):
    node = self.root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.is_end_of_word = True
```

### b) Search (exact word)

```python
def search(self, word):
    node = self._find_node(word)
    return node is not None and node.is_end_of_word
```

### c) Starts With (prefix check)

Identical to `search`, but doesn't require `is_end_of_word` — just that the path exists.

```python
def starts_with(self, prefix):
    return self._find_node(prefix) is not None
```

> **The single most important distinction in a trie**: `search("car")` is False if only `"card"` was inserted, but `starts_with("car")` is True — reaching the node is not the same as a word ending there.

### d) Delete

Delete must **not** blindly remove nodes — a node might still be part of another word's path (e.g. deleting `"card"` must not remove the `c → a → r` path, since `"car"` still needs it). The standard approach recurses to the end of the word, unmarks `is_end_of_word`, then prunes nodes bottom-up **only if** they have no children and aren't the end of another word.

---

## 3. Array-based vs Dict-based Children

| Approach                         | Space per node        | Lookup      | Charset                         |
| ----------------------------------| ------------------------| -------------| -----------------------------------|
| Fixed array (e.g. `[None] * 26`)  | O(26) always, even if mostly empty | O(1)         | Fixed, known alphabet (e.g. lowercase `a-z`) |
| Dict (`{}`)                        | O(actual children)      | O(1) average | Any charset — Unicode, digits, symbols |

A fixed-size array is marginally faster (no hashing) and is the classic textbook implementation for lowercase-English-only problems, but wastes memory when the charset is large or most nodes have few children. This repo's implementation (`02_Trie.py`) uses a **dict** for flexibility.

---

## 4. Trie vs HashMap vs BST for Storing Strings

| Feature                        | Trie                    | HashMap (set of strings) | BST (of strings)         |
| --------------------------------| --------------------------| ----------------------------| -----------------------------|
| Exact word lookup                | O(L)                       | O(L) (average, for hashing) | O(L log N)                     |
| Prefix search (`starts_with`)   | O(L)                       | O(N * L) — must scan all      | O(L log N) — still needs range scan |
| Space with many shared prefixes  | Efficient (shared paths)   | No sharing — full string stored per entry | No sharing |
| Sorted (lexicographic) iteration | Natural (DFS of the trie) | Not supported natively        | Natural (inorder)               |

**The trie's superpower is prefix operations.** A hashmap can't answer "how many words start with `pre`" without scanning every entry; a trie answers it in O(L) by just walking to the `pre` node.

---

## 5. Complexity Summary

| Operation                     | Time     | Space                                  |
| --------------------------------| ----------| ------------------------------------------|
| Insert                          | O(L)       | O(L) worst case (all new characters)       |
| Search / Starts With            | O(L)       | O(1) extra                                  |
| Delete                          | O(L)       | O(1) extra                                  |
| Total space for N words, avg length L | —    | O(N * L) worst case, less with shared prefixes |

---

## 6. Applications

- **Autocomplete / Type-ahead suggestions** — walk to the prefix node, then DFS to collect all words below it.
- **Spell checkers** — quick "does this word exist" checks, and suggesting close matches.
- **IP Routing (Longest Prefix Matching)** — routers store network prefixes in a trie (bitwise, over IP address bits) to find the most specific matching route.
- **T9 / predictive text** on phone keypads.
- **Word games** (Boggle, Scrabble) — pruning search branches that don't correspond to any valid prefix.
- **Bitwise Tries (Binary Trie)** — storing numbers as fixed-length bit strings enables **Maximum XOR Pair** queries in O(32) per number instead of O(N) comparisons.

---

## ✅ Summary

- A trie stores strings **character by character** along tree edges, sharing common prefixes automatically.
- **Insert, search, and prefix-check are all O(L)** — independent of how many words are stored, which no hashmap or BST can match for prefix queries.
- `search` requires reaching a node **marked** `is_end_of_word`; `starts_with` only requires the path to **exist** — mixing these up is the most common trie bug.
- Choose a **dict** for children when the charset is large/unknown, or a **fixed array** when restricted to a small known alphabet (e.g. lowercase English).
- The defining use case is anything **prefix-shaped**: autocomplete, spell-check, routing tables, and predictive text.
