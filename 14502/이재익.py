import sys
sys.stdin = open('input.txt')
from itertools import combinations
import copy

def infections(x, y, P):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    global imsi_visited
    if P[x][y] == 1:
        return
    if imsi_visited[x][y]:
        return
    else:
        imsi_visited[x][y] = True

    P[x][y] = 2

    for m in range(4):
        if 0 <= x + dx[m] < N and 0 <= y + dy[m] < M:
            infections(x+dx[m], y+dy[m], P)


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
two_x = []
two_y = []
wall = []
max = 0

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            wall.append((i, j))
        elif matrix[i][j] == 2:
            two_x.append(i)
            two_y.append(j)
K = list(combinations(wall, 3))

for i in range(len(K)):
    imsi = copy.deepcopy(matrix)
    imsi_visited = [[False]*M for _ in range(N)]
    for j in range(3):
        x = K[i][j][0]
        y = K[i][j][1]
        imsi[x][y] = 1
    count = 0
    for j in range(len(two_y)):
        infections(two_x[j], two_y[j], imsi)
    for j in range(N):
        for k in range(M):
            if imsi[j][k] == 0:
                count += 1
    if count > max:
        max = count

print(max)