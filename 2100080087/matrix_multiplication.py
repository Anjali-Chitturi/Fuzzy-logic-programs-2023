"""
Matrix Maximum of Overlapping Submatrices

This code takes two matrices as input and computes the maximum value of overlapping submatrices element-wise.

The input includes the dimensions of the matrices (n and m) and the elements of the matrices provided as lists.
The code reshapes the input lists into numpy arrays representing the matrices, and then transposes the second matrix.
For each overlapping submatrix position, it computes the maximum value between the corresponding elements of the two matrices.
The resulting maximum values are stored in a new matrix and printed as output.

"""

import numpy as np

# Get the dimensions of the matrices from the user
n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

# Get the elements of the matrices from the user and reshape them into numpy arrays
a = list(map(int, input("Enter elements of matrix 1: ").split()))
b = list(map(int, input("Enter elements of matrix 2: ").split()))
matrix1 = np.array(a).reshape(n, m)
matrix2 = np.array(b).reshape(n, m)

# Transpose matrix2
matrix2 = matrix2.T

# Print the input matrices
print("Matrix 1:")
print(matrix1)
print("Matrix 2 (transposed):")
print(matrix2)

# Initialize lists and matrix to store maximum values of overlapping submatrices
mat = list()
s = []

# Iterate over the rows and columns of the matrices to compute maximum values
for j in range(n):
    for i in range(m):
        # Extend the list 's' with elements from overlapping submatrices
        s.extend(matrix1[i][j:])
        s.extend(matrix2[i][j:])
        
        # Remove the maximum value from 's'
        s.remove(max(s))
        
        # Append the maximum value to the 'mat' list
        mat.append(max(s))
        
        # Clear the list 's' for the next iteration
        s.clear()

# Reshape the 'mat' list into a numpy array representing the matrix of maximum values
mat = np.array(mat).reshape(n, m)

# Print the resulting matrix of maximum values
print("Matrix of Maximum Values of Overlapping Submatrices:")
print(mat)
