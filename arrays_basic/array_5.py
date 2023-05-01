# Task
# Your task is to print an array of size N X M with its main diagonal elements as 1's and 0's everywhere else.

# Input Format

# A single line containing the space separated values of N and M.
# N denotes the rows.
# M denotes the columns.

# Output Format

# Print the desired (N X M) array.

import numpy
numpy.set_printoptions(legacy='1.13')

N, M = list(map(int, input().split()))
print(numpy.eye(N, M, k=0))
