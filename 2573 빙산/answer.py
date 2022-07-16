import sys
from collections import deque
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
X, Y = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(X)]
count = 0
while count < 2:
    queue = deque()
    for i in range(X):
        for j in range(Y):
            if matrix[i][j] != 0:
                queue.append(matrix[i][j])
                while queue:


    for i in range(X):
        for j in range(Y):
