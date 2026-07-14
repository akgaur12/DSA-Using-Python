# Arrays — Complete Guide

## 1. What Is an Array?

An **array** is one of the most fundamental data structures: a collection of elements stored
in **contiguous memory**, where each element can be accessed directly using its **index**
(position). Because elements sit next to each other in memory, the address of any element can
be calculated instantly from the starting address — giving arrays their signature **O(1)
random access**.

Analogy: an array is like a row of numbered lockers. If you want locker #7, you walk straight
to it — you don't need to open lockers #1 through #6 first. Compare this to a linked list,
where you'd have to walk through every node to reach the 7th one.

## 2. Static vs. Dynamic Arrays

| Type              | Description                                                                 |
| -------------------- | -------------------------------------------------------------------------------- |
| **Static array**      | Fixed size, decided at creation time. Cannot grow or shrink (common in C, Java's `int[]`). |
| **Dynamic array**      | Automatically resizes as elements are added/removed. Internally still a contiguous block, but when full, a new larger block is allocated and elements are copied over. |

Most high-level languages expose dynamic arrays as their default "array-like" type — Python's
`list`, Java's `ArrayList`, JavaScript's `Array`, C++'s `std::vector`. The resizing strategy
(usually **doubling** capacity when full) is what gives dynamic arrays **O(1) amortized**
append, even though a resize itself costs O(n).

## 3. Time & Space Complexity

| Operation                        | Complexity | Notes                                      |
| ------------------------------------ | ------------ | ---------------------------------------------- |
| Access by index                     | O(1)         | Direct memory offset calculation               |
| Search (unsorted)                    | O(n)         | Must scan linearly                             |
| Search (sorted)                      | O(log n)     | Binary search possible                         |
| Insert/delete at the end             | O(1)*        | Amortized for dynamic arrays                   |
| Insert/delete at the front/middle    | O(n)         | Requires shifting subsequent elements          |
| Space                                | O(n)         | n = number of elements                         |

## 4. Common Array Patterns

These are the recurring problem-solving techniques you'll see applied across array problems,
regardless of language:

| Pattern                     | Idea                                                                          |
| ------------------------------- | ---------------------------------------------------------------------------------- |
| **Two pointers**                | Move pointers from both ends (or at different speeds) toward each other — reversing, removing duplicates, pair-sum problems |
| **Sliding window**              | Maintain a running window over a subrange to avoid recomputation — subarray sums, longest/shortest subarray with a condition |
| **Prefix sum / running sum**     | Precompute cumulative sums to answer range queries in O(1) — subarray sum problems |
| **Hashing (set/map)**            | Track seen elements or frequencies for O(1) lookups — duplicates, missing elements, majority element |
| **Kadane's algorithm**           | Track the best running sum/product, resetting when it stops helping — max subarray sum/product |
| **Sort then scan**               | Sorting first simplifies many problems — kth largest, minimizing differences |

## 5. When Should You Use an Array?

✅ **Use an array when:**
- You need **ordered**, **indexed** access to elements.
- You need to **iterate** over data sequentially.
- Random access speed matters more than flexible insertion/deletion.

❌ **Consider alternatives when:**
- You need **fast membership checks** with no duplicates → use a **hash set**.
- You need **fast key-based lookups** → use a **hash map**.
- You need **frequent insert/delete at the front** → use a **deque** (O(1) at both ends
  instead of O(n)).
- You need guaranteed O(log n) insert/delete while staying sorted → use a **balanced tree** or
  **skip list**.

## 6. Real-World Use Cases

- Storing a sequence of records (transactions, sensor readings, log entries).
- Buffers, queues, and stacks are often built on top of arrays.
- Image data (pixels laid out in contiguous memory) and audio buffers.
- Lookup tables and precomputed value caches.
- Sliding-window analytics (moving averages, "last N events").

## 7. Array Operations in Python

This repo implements arrays using Python's built-in `list`, which is a dynamic array under
the hood.

```python
arr = [10, 20, 30, 40, 50]

# Access & slice
first = arr[0]
last = arr[-1]
sub = arr[1:3]                  # [20, 30]

# Modify
arr.append(60)                  # add to end — O(1) amortized
arr.insert(0, 5)                # add at index — O(n)
arr.pop()                       # remove & return last — O(1)
arr.remove(30)                  # remove first matching value — O(n)

# Two-pointer pattern (reverse in-place)
left, right = 0, len(arr) - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

# Sliding window pattern (sum of every window of size k)
window_sum = sum(arr[:k])
for i in range(k, len(arr)):
    window_sum += arr[i] - arr[i - k]

# Prefix sum pattern (fast range-sum queries)
prefix = [0] * (len(arr) + 1)
for i, val in enumerate(arr):
    prefix[i + 1] = prefix[i] + val
```

## 8. Files in This Folder

| File                                                        | Description                                                                   | Time                                | Space                    |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------- | -------------------------------------- | --------------------------- |
| [`01_reverse_array.py`](./01_reverse_array.py)                   | Reverses an array in-place using two pointers                                      | O(n)                                    | O(1)                        |
| [`02_check_sorted.py`](./02_check_sorted.py)                     | Checks whether an array is sorted (non-decreasing)                                | O(n)                                    | O(1)                        |
| [`03_max_min_of_array.py`](./03_max_min_of_array.py)             | Finds min and max via a single linear scan                                         | O(n)                                    | O(1)                        |
| [`04_second_largest.py`](./04_second_largest.py)                 | Finds the second largest distinct element in one pass                              | O(n)                                    | O(1)                        |
| [`05_remove_duplicate.py`](./05_remove_duplicate.py)             | Removes duplicates in-place from a sorted array (two-pointer)                      | O(n)                                    | O(1)                        |
| [`06_right_rotate_k.py`](./06_right_rotate_k.py)                 | Rotates an array right by k using the three-reverse trick                          | O(n)                                    | O(1)                        |
| [`07_moves_zeros_to_end.py`](./07_moves_zeros_to_end.py)         | Moves all zeroes to the end while preserving order                                | O(n)                                    | O(1)                        |
| [`08_move_negative_to_end.py`](./08_move_negative_to_end.py)     | Moves negatives to the end, preserving order, using a temp array                   | O(n)                                    | O(n)                        |
| [`09_sort_array_of_012.py`](./09_sort_array_of_012.py)           | Sorts an array of 0s, 1s, 2s (Dutch National Flag)                                 | O(n)                                    | O(1)                        |
| [`10_missing_number.py`](./10_missing_number.py)                 | Finds the missing number in `[0, n]` (hash map / sum / XOR)                        | O(n)                                    | O(n) hash map; O(1) sum/XOR |
| [`11_find_duplicate.py`](./11_find_duplicate.py)                 | Finds the duplicate number (hash map or Floyd's cycle detection)                    | O(n)                                    | O(n) hash map; O(1) Floyd's |
| [`12_max_consecutive_ones.py`](./12_max_consecutive_ones.py)     | Returns the max number of consecutive 1's in a binary array                        | O(n)                                    | O(1)                        |
| [`13_check_subset.py`](./13_check_subset.py)                     | Checks if one array is a subset of another (brute force / `in` / hash set)          | O(n+m) with hash set                    | O(n) with hash set          |
| [`14_merge_sorted.py`](./14_merge_sorted.py)                     | Merges two sorted arrays into one using extra space                                | O(n + m)                                | O(n + m)                    |
| [`15_union_of_arrays.py`](./15_union_of_arrays.py)               | Computes the union of two arrays using a set                                        | O(n + m)                                | O(n + m)                    |
| [`16_intersection_of_arrays.py`](./16_intersection_of_arrays.py) | Finds common elements between two arrays using a set                               | O(n + m)                                | O(n)                        |
| [`17_kth_max_min.py`](./17_kth_max_min.py)                       | Finds the kth max/min element (sorting or heaps)                                    | O(n log n) sort; O(n + k log n) heap    | O(1) sort; O(n) heap        |
| [`18_merge_two_array_inplace.py`](./18_merge_two_array_inplace.py) | Merges two sorted arrays in-place using the gap method                            | O((n+m) log(n+m))                       | O(1)                        |
| [`19_subarray_with_zero_sum.py`](./19_subarray_with_zero_sum.py) | Checks for a zero-sum subarray (brute force or prefix-sum hashing)                  | O(n²) brute; O(n) prefix sum            | O(1) brute; O(n) prefix sum |
| [`20_3sum.py`](./20_3sum.py)                                     | Checks for a triplet summing to a target (brute force or two-pointer)               | O(n³) brute; O(n²) two-pointer          | O(1)                        |
| [`21_factorial_of_large_num.py`](./21_factorial_of_large_num.py) | Computes factorial of a large number via digit-by-digit multiplication              | O(n · d)                                | O(d)                        |
| [`22_longest_consecutive.py`](./22_longest_consecutive.py)       | Finds the longest consecutive sequence length (sorting or hash set)                 | O(n log n) sort; O(n) hash set          | O(1) sort; O(n) hash set    |
| [`23_majority_element_II.py`](./23_majority_element_II.py)       | Finds all elements appearing more than n/3 times using a frequency map              | O(n)                                    | O(n)                        |
| [`24_smallest_subarray_sum.py`](./24_smallest_subarray_sum.py)   | Smallest subarray length with sum strictly greater than x (sliding window)          | O(n)                                    | O(1)                        |
| [`25_Kadanes_algorithm.py`](./25_Kadanes_algorithm.py)           | Maximum sum of a contiguous subarray using Kadane's Algorithm                       | O(n)                                    | O(1)                        |
| [`26_minimize_max_diff_heights.py`](./26_minimize_max_diff_heights.py) | Minimizes max height difference after ±k adjustment, via sorting              | O(n log n)                              | O(1)                        |
| [`27_min_jumps.py`](./27_min_jumps.py)                           | Minimum jumps to reach the end of the array (greedy)                                | O(n)                                    | O(1)                        |
| [`28_max_product_subarray.py`](./28_max_product_subarray.py)     | Maximum product of a contiguous subarray (brute force or Kadane-like)               | O(n²) brute; O(n) optimized             | O(1)                        |
| [`29_chocolate_distribution.py`](./29_chocolate_distribution.py) | Minimum difference between max/min in any m-sized window after sorting              | O(n log n)                              | O(1)                        |
| [`30_common_elements_three.py`](./30_common_elements_three.py)   | Common elements across three sorted arrays via three-pointer merge                  | O(n1 + n2 + n3)                         | O(1) extra                  |

## 9. Quick Recap

| Property               | Value                              |
| ------------------------- | ------------------------------------- |
| Underlying storage        | Contiguous memory block                |
| Access by index           | O(1)                                  |
| Search (unsorted)         | O(n)                                  |
| Append (dynamic array)    | O(1) amortized                        |
| Insert / delete at front  | O(n)                                  |
| Space                     | O(n)                                  |
| Python equivalent          | `list`                                |
