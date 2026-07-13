# Hash Map in Python — Complete Guide

## 1. What Is a Hash Map?

A **Hash Map** (also called a **Hash Table**) is a data structure that stores data as
**key-value pairs**, using a **hashing mechanism** to map each key to a specific location
(bucket) in memory. This gives **average O(1)** time complexity for insert, lookup, update,
and delete operations — regardless of how many items are stored.

In Python, the built-in **`dict`** type *is* a hash map. There is no separate "HashMap" class
like in Java — `dict` (and `set`, which is a hash map without values) already gives you this
behavior out of the box.

```python
phone_book = {"Alice": "12345", "Bob": "67890"}
print(phone_book["Alice"])   # O(1) lookup → "12345"
```

Analogy: a hash map is like a library where every book has an address computed from its title
(the hash), instead of searching shelf by shelf — you go directly to the right shelf.

## 2. How Python's `dict` Works Internally

1. **Hashing:** When you insert a key, Python calls `hash(key)` to produce an integer.
2. **Bucket index:** That hash is reduced (via modulo) to an index into an internal array.
3. **Storage:** The key-value pair is stored at that index (bucket).
4. **Collisions:** If two different keys hash to the same bucket, Python resolves this using
   **open addressing** (it probes for the next available slot), not linked lists like some
   other languages.
5. **Resizing:** When the table gets too full (load factor exceeds a threshold), Python
   automatically allocates a bigger internal array and re-hashes all existing entries.

**Important constraint:** Only **hashable** (immutable) types can be dictionary keys —
`int`, `float`, `str`, `tuple` (of hashable items), `frozenset`. Mutable types like `list` and
`dict` **cannot** be used as keys because their hash could change after insertion.

```python
d = {}
d[(1, 2)] = "valid"     # ✅ tuple is hashable
d[[1, 2]] = "invalid"   # ❌ TypeError: unhashable type: 'list'
```

## 3. Time & Space Complexity

| Operation          | Average Case | Worst Case | Notes                                  |
| ------------------- | ------------- | ---------- | --------------------------------------- |
| Insert (`d[k] = v`) | O(1)          | O(n)       | Worst case only with many hash collisions |
| Lookup (`d[k]`)     | O(1)          | O(n)       | Same as above                           |
| Delete (`del d[k]`) | O(1)          | O(n)       | Same as above                           |
| Iteration           | O(n)          | O(n)       | Visits every key-value pair             |
| Space               | O(n)          | O(n)       | n = number of key-value pairs           |

The worst case O(n) only happens with pathological hash collisions, which is extremely rare
in practice with Python's built-in hashing.

## 4. Core Operations in Python

```python
# Create
d = {}                          # empty dict
d = {"a": 1, "b": 2}            # dict literal

# Insert / Update (same syntax — dict decides based on key existence)
d["c"] = 3                      # insert new key
d["a"] = 100                    # update existing key

# Safe lookup (avoids KeyError, provides a default)
value = d.get("z", 0)           # returns 0 if "z" is not present

# Check existence
if "a" in d:
    print("found")

# Delete
del d["a"]                      # raises KeyError if missing
d.pop("b", None)                # safe delete, no error if missing

# Iterate
for key in d:                   # iterate keys
    print(key, d[key])

for key, value in d.items():    # iterate key-value pairs
    print(key, value)

# Counting frequency — the most common hash map pattern
freq = {}
for item in [1, 2, 2, 3, 1, 1]:
    freq[item] = freq.get(item, 0) + 1
# freq = {1: 3, 2: 2, 3: 1}
```

### Related built-ins

- **`collections.Counter`** — a `dict` subclass purpose-built for frequency counting.
- **`collections.defaultdict`** — a `dict` that auto-initializes missing keys (avoids
  `.get()`/`if key in d` boilerplate).
- **`set`** — a hash map with only keys (no values); great for O(1) membership tests and
  deduplication.

```python
from collections import Counter, defaultdict

freq = Counter([1, 2, 2, 3, 1, 1])       # Counter({1: 3, 2: 2, 3: 1})

groups = defaultdict(list)
groups["evens"].append(2)                 # no KeyError even though "evens" didn't exist yet
```

## 5. When Should You Use a Hash Map?

✅ **Use a hash map when:**
- You need **fast lookups** by a key (username → user data, ID → record).
- You're **counting frequencies** of items in a collection.
- You need to check **membership/duplicates** quickly (`in` on a `dict`/`set` is O(1) vs O(n)
  for a `list`).
- You want to **group** items by some computed key.

❌ **Avoid it when:**
- You need to maintain **sorted order** by key (use a sorted structure or sort `dict.items()`
  when needed — regular dicts only preserve *insertion* order, not sorted order).
- Keys would be **mutable objects** (lists, other dicts) — they aren't hashable.
- Memory is extremely constrained — hash maps use more memory than arrays for the same data
  due to the underlying hash table overhead.

## 6. Real-World Use Cases

- Caching/memoization: mapping function inputs to previously computed outputs.
- Database indexing: mapping keys to row locations for fast retrieval.
- Counting word/character frequency in text processing.
- Detecting duplicates in a dataset in a single pass.
- Grouping records by a category (e.g., grouping transactions by user ID).
- Implementing graph adjacency lists (`{node: [neighbors]}`).

## 7. Common Interview Patterns Using Hash Maps

| Pattern                          | Idea                                                            |
| --------------------------------- | ----------------------------------------------------------------- |
| **Frequency counting**            | Count occurrences of each element in one pass — O(n)              |
| **Find the unique element**       | Track counts; the element with count 1 (or not divisible by k) is the answer |
| **Two Sum**                       | Store `value → index` while scanning; check `target - value` in map |
| **Detect duplicates**              | Insert into a `set`; if insert fails (already present), duplicate found |
| **Group Anagrams / group by key** | Use a computed key (e.g., sorted string) as the dict key, append to a list value |

## 8. Files in This Folder

| File                                                      | Description                                                              |
| ----------------------------------------------------------- | ---------------------------------------------------------------------------- |
| [`01_HashMapBasics.py`](./01_HashMapBasics.py)               | Introduction to creating, reading, updating, and deleting entries in a `dict` |
| [`02_UniqueNumber1.py`](./02_UniqueNumber1.py)               | Find the single element that occurs once while all others occur twice     |
| [`03_UniqueNumber2.py`](./03_UniqueNumber2.py)               | Find two distinct elements that occur once while all others occur twice   |
| [`04_UniqueNumber3.py`](./04_UniqueNumber3.py)               | Find the single element that occurs once while all others occur thrice    |
| [`05_FrequencyCount.py`](./05_FrequencyCount.py)             | Count frequency of each element using dictionaries, including sorting by key/value |

## 9. Quick Recap

| Property              | Value                              |
| ----------------------- | ------------------------------------- |
| Python type              | `dict` (and `set` for keys-only)      |
| Average time (insert/lookup/delete) | O(1)                     |
| Worst time (rare)        | O(n)                                  |
| Space                    | O(n)                                  |
| Key requirement          | Must be hashable (immutable)          |
| Preserves order?          | Insertion order (Python 3.7+), not sorted order |
