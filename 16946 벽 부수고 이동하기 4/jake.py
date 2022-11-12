import sys
from collections import deque
sys.stdin = open('input.txt')

N, M = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]
check = matrix[:]
print(check)
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            pass
        else:
            check = matrix[:]
            check[i][j] = 0
            queue = deque()
            
