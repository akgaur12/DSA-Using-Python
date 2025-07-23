"""
Problem: Matrix Multiplication

Description:
-------------
This function multiplies two matrices **A** and **B**, provided their dimensions
are compatible for multiplication.

Matrix A is of size n x m  
Matrix B is of size p x q

Multiplication is only valid when:
    m == p (i.e., columns of A = rows of B)

The result is a matrix of size n x q.

Approach:
----------
- For each cell (i, j) in the result matrix, compute the sum:
      result[i][j] = sum(A[i][k] * B[k][j]) for k in [0, m)
- This is the classical matrix multiplication approach.

Time Complexity: O(n * m * q)
    - Three nested loops: one over rows of A, one over columns of B, and one over shared dimension m.

Space Complexity: O(n * q)
    - A new result matrix of size n × q is created to store the output.
"""

def multiplyMatrices(A, B):    
    # Number of rows and columns in Matrix A
    n = len(A)
    m = len(A[0])

    # Number of rows and columns in Matrix B
    p = len(B)
    q = len(B[0])

    # Check if multiplication is possible
    if m != p:
        raise ValueError("Cannot multiply: Number of columns in A must equal number of rows in B.")

    # Initialize result matrix with zeros (size: n x q)
    result = [[0 for _ in range(q)] for _ in range(n)]

    # Matrix multiplication core logic
    for i in range(n):
        for j in range(q):
            for k in range(m):
                result[i][j] += A[i][k] * B[k][j]

    return result


# Example Usage
if __name__ == "__main__":
    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    B = [
        [7, 8],
        [9, 10],
        [11, 12]
    ]

    try:
        product = multiplyMatrices(A, B)
        print("Matrix A × B is:")
        for row in product:
            print(row)
    except ValueError as e:
        print(e)
