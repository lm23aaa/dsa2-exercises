# import of NumPy
import numpy as np

# Basic array creation
a = np.array([1, 2, 3])

# Matix creation...array of arrays
b = np.array([[1,2,3], [4,5,6], [7,8,9]])

# matrix multiplication
ab = np.matmul(a, b)
# print(ab)

# define arrays of zeros or ones
c = np.zeros(200)
d = np.ones([100, 100])
# print(c, d)

# creation of array of random elements
# randint(lowest possible number, higher possible number, size)
e = np.random.randint(0, 1000, 100)
# print(e)

# TASK
# Define a matrix (A) of size 3x6 with random integer elements between -10 and 10.
A = np.array([
    np.random.randint(-10, 10, 6),
    np.random.randint(-10, 10, 6),
    np.random.randint(-10, 10, 6)
])

# Transpose the matrix (A^T)
At = A.transpose()

# 1. i.  A * A^T
i = np.matmul(A, At)
print(i)

# 1. ii. A^T * A
ii = np.matmul(At, A)
print(ii)

# 2. Are they the same result? Can you find an example of A -any size- for which the results are the same?
# No they are not the same result. A*A^T is 3x3 in size and A^T*A is 6x6 in size, and the overlapping rusulting numbers do not match.
# To get the two resulting matrices to match, firstly A would need to be a square matrix. This is because when you multiply two matrices, the resulting matrix will have a row size of the first matrix, and the column size of the second, meaning to match the row size and column size, they both need to be the same size. Secondly, to get the same number output, A would need to be equal to A^T, which was described in 1.2.7 of DSA 1 (https://herts.instructure.com/courses/118171/pages/1-dot-2-7-operations-with-matrices-transposition?module_item_id=4302356) as a symmetric matrix.