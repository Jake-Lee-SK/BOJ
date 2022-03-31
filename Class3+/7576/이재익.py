import sys
from collections import deque
# sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
input = sys.stdin.readline
M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
check = [[False]*M for _ in range(N)]
queue = deque()
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            queue.append([i, j])
            check[i][j] = True
        elif matrix[i][j] == -1:
            check[i][j] = True
while queue:
    n = queue.popleft()
    for i in range(4):
        new_y = n[0]+dy[i]
        new_x = n[1]+dx[i]
        if 0<=new_y<N and 0<=new_x<M and check[new_y][new_x] == False:
            check[new_y][new_x] = True
            matrix[new_y][new_x] = matrix[n[0]][n[1]] +1
            queue.append([new_y, new_x])
check = 0
max_value = 0
for i in range(N):
    if 0 in matrix[i]:
        check += 1
        break
    else:
        if max(matrix[i]) > max_value:
            max_value = max(matrix[i])
if check == 1:
    print(-1)
else:
    print(max_value-1)
