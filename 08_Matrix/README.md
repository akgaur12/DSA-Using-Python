# Matrix — Complete Guide

## 1. What Is a Matrix?

A **matrix** is a **2D grid of elements**, arranged in **rows and columns**, and accessed
using two indices: `matrix[row][column]`. Conceptually it's just an array of arrays — each row
is itself a 1D array, and the matrix is a collection of those rows.

Analogy: a matrix is like a spreadsheet — you locate a cell by its row and column number, and
traversal patterns (row-wise, column-wise, diagonal, spiral, boundary) are simply different
orders of visiting those cells.

## 2. How a Matrix Is Represented

There are two common ways to store a matrix in memory:

| Representation             | Description                                                                    |
| ------------------------------ | ------------------------------------------------------------------------------------ |
| **Array of arrays**              | Each row is a separate array/list; `matrix[i][j]` is two chained index lookups. This is what most high-level languages use (Python `list` of `list`s, Java `int[][]`). |
| **Flat 1D array**                 | All elements stored in one contiguous array, with `matrix[i][j]` mapped to `flat[i * cols + j]`. Used internally by numeric libraries (NumPy, C arrays) for cache-friendly, contiguous storage. |

Regardless of representation, accessing a single cell is **O(1)**, and any full traversal
(printing, summing, transforming every element) is **O(rows × columns)**.

## 3. Time & Space Complexity

| Operation                        | Complexity | Notes                                     |
| ------------------------------------ | ------------ | --------------------------------------------- |
| Access (`matrix[i][j]`)              | O(1)         | Direct index computation                     |
| Full traversal (row/col/diagonal)    | O(n · m)     | n = rows, m = columns — every cell visited once |
| Search in unsorted matrix            | O(n · m)     | Brute-force scan of every cell               |
| Search in row & column sorted matrix | O(n + m)     | Staircase search from a corner               |
| Transpose / rotate                   | O(n · m)     | Every cell read/written once                 |
| Space (new matrix)                   | O(n · m)     | For output matrix, if not done in-place       |
| Space (in-place)                     | O(1)         | Reuses input matrix (e.g., in-place rotation) |

## 4. Common Matrix Patterns

These recurring techniques show up across matrix problems regardless of language:

| Pattern                          | Idea                                                                       |
| ------------------------------------ | -------------------------------------------------------------------------------- |
| **Transpose + reverse**              | Rotate a matrix 90° in-place without extra space                                |
| **Boundary shrinking pointers**       | Track `top`, `bottom`, `left`, `right` bounds that shrink inward — spiral/boundary traversal |
| **Diagonal grouping**                 | Group cells where `i + j` (or `i - j`) is constant — diagonal traversal          |
| **Staircase search**                  | Start from a corner (e.g., top-right) and move based on comparison — search in a sorted matrix |
| **First row/column as marker**        | Reuse the matrix itself to store state and avoid extra space — set matrix zeroes |
| **Row/column min-max comparison**     | Compare row minimums against column maximums — saddle point                     |

## 5. When Should You Use a Matrix?

✅ **Use a matrix when:**
- Data naturally has **two dimensions** (grids, images, tables, adjacency matrices for graphs).
- You need direct `[row][col]` access without extra bookkeeping.

❌ **Consider alternatives when:**
- You need **heavy numerical computation** (linear algebra, large-scale matrix multiplication)
  — use a vectorized numeric library (like NumPy) for cache-friendly, C-speed operations
  instead of nested loops.
- The matrix is **very sparse** (mostly zeros/empty) — a hash map of `(row, col) → value`
  saves memory by only storing non-empty cells.

## 6. Real-World Use Cases

- Image processing (each pixel is a matrix cell; rotation/transpose are common operations).
- Grid-based games and pathfinding (maze solving, Conway's Game of Life).
- Representing graphs as adjacency matrices.
- Spreadsheet-like tabular data processing.
- Dynamic programming tables (e.g., edit distance, longest common subsequence) are matrices.

## 7. Matrix Operations in Python

This repo represents a matrix as a `list` of `list`s.

```python
rows, cols = 3, 3
matrix = [[0] * cols for _ in range(rows)]   # correctly-initialized zero matrix

# WRONG — all rows reference the same inner list
bad = [[0] * cols] * rows
bad[0][0] = 1   # mutates every row!

# Row-major traversal
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")

# Column-major traversal
for j in range(cols):
    for i in range(rows):
        print(matrix[i][j], end=" ")

# Transpose (new matrix)
transposed = [[matrix[i][j] for i in range(rows)] for j in range(cols)]

# Transpose (in-place, square matrix only)
for i in range(rows):
    for j in range(i + 1, cols):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Rotate 90° clockwise in-place (square matrix): transpose, then reverse each row
for row in matrix:
    row.reverse()
```

## 8. Files in This Folder

| File                                                          | Description                                                                          | Time      | Space              |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- | ----------- | --------------------- |
| [`01_print_row_major.py`](./01_print_row_major.py)                   | Prints matrix elements in row-major order                                              | O(n · m)     | O(1)                  |
| [`02_print_column_major.py`](./02_print_column_major.py)             | Prints matrix elements in column-major order                                            | O(n · m)     | O(1)                  |
| [`03_transpose.py`](./03_transpose.py)                               | Computes the transpose by swapping rows and columns into a new matrix                    | O(n · m)     | O(n · m)              |
| [`04_search_element.py`](./04_search_element.py)                     | Searches for a target via brute-force scan of every element                             | O(n · m)     | O(1)                  |
| [`05_check_symmetric.py`](./05_check_symmetric.py)                    | Checks if a matrix equals its transpose                                                 | O(n²)        | O(1)                  |
| [`06_sum_elements.py`](./06_sum_elements.py)                          | Computes the sum of all elements via nested traversal                                    | O(n · m)     | O(1)                  |
| [`07_rotate_90.py`](./07_rotate_90.py)                                | Rotates a matrix 90° clockwise/anti-clockwise via transpose + row reversal              | O(n²)        | O(1)                  |
| [`08_spiral_traversal.py`](./08_spiral_traversal.py)                  | Returns elements in spiral order using four shrinking boundary pointers                  | O(n · m)     | O(1) extra            |
| [`09_diagonal_traversal.py`](./09_diagonal_traversal.py)              | Traverses diagonally (top-right to bottom-left), collecting elements per diagonal        | O(n · m)     | O(n · m)              |
| [`10_boundary_traversal.py`](./10_boundary_traversal.py)              | Collects boundary elements in clockwise order                                            | O(n + m)     | O(1)                  |
| [`11_saddle_point.py`](./11_saddle_point.py)                          | Finds a saddle point (row minimum that is also its column maximum)                       | O(n · m)     | O(1)                  |
| [`12_matrix_multiplication.py`](./12_matrix_multiplication.py)        | Multiplies two compatible matrices using triple-nested loops                             | O(n · m · q) | O(n · q)              |
| [`13_check_identity.py`](./13_check_identity.py)                      | Checks if a square matrix is an identity matrix                                          | O(n²)        | O(1)                  |
| [`14_search_sorted_matrix.py`](./14_search_sorted_matrix.py)          | Searches a target in a row/column sorted matrix, starting from the top-right corner       | O(n + m)     | O(1)                  |
| [`15_set_matrix_zeroes.py`](./15_set_matrix_zeroes.py)                | Zeroes out entire row/column for cells containing 0, using first row/column as markers   | O(n · m)     | O(1)                  |
| [`16_max_1s_row.py`](./16_max_1s_row.py)                              | Finds the row with the most 1s in a row-wise sorted binary matrix                          | O(n + m)     | O(1)                  |
| [`17_rotate_inplace.py`](./17_rotate_inplace.py)                      | Rotates a square matrix 90° clockwise in-place via transpose then row reversal            | O(n²)        | O(1)                  |

## 9. Quick Recap

| Property               | Value                              |
| ------------------------- | ------------------------------------- |
| Underlying storage         | Array of arrays (rows), or flat 1D array with index mapping |
| Access by index            | O(1) — `matrix[i][j]`                 |
| Full traversal              | O(n · m)                              |
| Sorted-matrix search        | O(n + m) with staircase search        |
| Space (new matrix)          | O(n · m)                              |
| Space (in-place ops)        | O(1)                                  |
| Python equivalent            | `list` of `list`s                     |
