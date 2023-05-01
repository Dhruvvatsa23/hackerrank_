# Task
# You are given two integer arrays, A and B of dimensions N X M.
# Your task is to perform the following operations:

# Add (A + B)
# Subtract (A - B)
# Multiply (A * B)
# Integer Division (A / B)
# Mod (A % B)
# Power (A ** B)
# Note
# There is a method numpy.floor_divide() that works like numpy.divide() except it performs a floor division.

# Input Format
# The first line contains two space separated integers, N and M.
# The next N lines contains M space separated integers of array A.
# The following N lines contains M space separated integers of array B.

# Output Format
# Print the result of each operation in the given order under Task.

#SOLUTION-1
import numpy

def operations(array_1, array_2):
    results = []
    functions = [
        numpy.add,
        numpy.subtract,
        numpy.multiply,
        numpy.floor_divide,
        numpy.mod,
        numpy.power
    ]
    for func in functions:
        results.append(func(array_1, array_2))
    return results

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    array_1 = numpy.array([list(map(int, input().strip().split())) for _ in range(N)])
    array_2 = numpy.array([list(map(int, input().strip().split())) for _ in range(N)])
    
    result = operations(array_1, array_2)
    for res in result:
        print(res)

#SOLUTION-2

import numpy

def operations(array_1, array_2):
    results = []
    results.append(numpy.add(array_1, array_2))
    results.append(numpy.subtract(array_1, array_2))
    results.append(numpy.multiply(array_1, array_2))
    results.append(numpy.floor_divide(array_1, array_2))
    results.append(numpy.mod(array_1, array_2))
    results.append(numpy.power(array_1, array_2))    
    return results

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    l1 = list(map(int, input().strip().split()))
    l2 = list(map(int, input().strip().split()))
    array_1 = numpy.array(l1).reshape(N, M)
    array_2 = numpy.array(l2).reshape(N, M)
    
    result = operations(array_1, array_2)
    for res in result:
        print(res)
