import sys
sys.stdin = open('input.txt')
from collections import deque

N = int(input())
M = int(input())
matrix = []
for i in range(M):
    a, b = map(int, input().split())
    matrix.append([a,b])
check = [0]*(N+1)
connect = [[] for i in range(N+1)]
for i in range(M):
    connect[matrix[i][0]].append(matrix[i][1])
    connect[matrix[i][1]].append(matrix[i][0])
queue = deque()
queue.append(1)
check[1] = 1
while queue:
    n=queue.popleft()
    for i in connect[n]:
        if check[i] == 0:
            queue.append(i)
            check[i] = check[n]+1
cnt = 0
for i in range(N+1):
    if check[i] != 0:
        cnt += 1
print(cnt-1)