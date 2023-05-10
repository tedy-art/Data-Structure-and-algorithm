"""
Write a program that initialize a 2-D arrays of size m x n with the value 0,
and then sets the diagonal elements to the value 1.
"""
m = 4
n = 4
arr = [[0 for j in range(n)] for i in range(m)]
for i in range(min(m, n)):
    arr[i][i] = 1
print(arr)