# BFS 혹은 DFS로 풀이하는 문제, 기본 형식에 충실하되, count를 어느 순간에 넣을 지 고민해볼 것
import sys
sys.stdin = open('input.txt')
from collections import deque
#
# def DFS(y, x):
#     print(y, x)
#     for i in range(N):
#         print(matrix[i])
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, 1, -1]
#
#     if matrix[y][x] == 1:
#         matrix[y][x] = 0
#     else:
#         return
#
#     for i in range(4):
#         new_x = x + dx[i]
#         new_y = y + dy[i]
#         if 0 <=new_x<M and 0 <= new_y < N and matrix[new_y][new_x]:
#             DFS(new_y, new_x)

def BFS(y, x):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    matrix[y][x] = 0
    queue = deque()
    queue.append((y, x))
    while queue:
        n = queue.popleft()
        for i in range(4):
            new_x = n[1] + dx[i]
            new_y = n[0] + dy[i]
            if 0<=new_x<M and 0<=new_y<N and matrix[new_y][new_x] == 1:
                queue.append((new_y, new_x))
                matrix[new_y][new_x] = 0
    return

T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    bugs = [list(map(int, input().split())) for _ in range(K)]
    matrix = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(K):
        matrix[bugs[i][1]][bugs[i][0]] = 1
    count = 0

    for y in range(N):
        for x in range(M):
            if matrix[y][x] == 1:
                BFS(y, x)
                count += 1


    print(count)