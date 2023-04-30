# Task
# You are given a NXM integer array matrix with space separated elements (N = rows and M = columns).
# Your task is to print the transpose and flatten results.

# Input Format
# The first line contains the space separated values of N and M.
# The next N lines contains the space separated elements of M columns.

# Output Format
# First, print the transpose array and then print the flatten.


import numpy as np

# Take input for matrix size and elements
N, M = map(int, input().split())
elements = []
for i in range(N):
    row = list(map(int, input().split()))
    elements.extend(row)

# Create NumPy array and reshape to matrix
matrix = np.array(elements).reshape(N, M)

# Print transpose and flattened matrix
print(matrix.T)
print(matrix.flatten())
