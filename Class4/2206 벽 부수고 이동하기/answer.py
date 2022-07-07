import sys
import collections
import itertools
sys.stdin = open('input.txt')
A, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(A)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
new_matrix = [[-1]*B for _ in range(A)]
print(new_matrix)
for i in range(A):
    for j in range(B):
        if matrix[i][j] == 1:
            new_matrix[i][j] = -2
print(matrix)

