# Task
# You are given two integer arrays of size NXP and MXP (N & M are rows, and P is the column). 
# Your task is to concatenate the arrays along axis 0.

# Input Format
# The first line contains space separated integers N, M and P.
# The next N lines contains the space separated elements of the P columns.
# After that, the next M lines contains the space separated elements of the P columns.

# Output Format
# Print the concatenated array of size (N+M) X P.

import numpy as np

N, M, P = map(int, input().split())
array_1 = []
array_2 = []
for i in range(N):
    row = list(map(int, input().split()))
    array_1.extend(row)
for j in range(M):
    row_2 = list(map(int, input().split()))
    array_2.extend(row_2)

array_1 = np.array(array_1)
array_2 = np.array(array_2)

array_1 = array_1.reshape(N, P)
array_2 = array_2.reshape(M, P)

print(np.concatenate((array_1,array_2), axis=0))
