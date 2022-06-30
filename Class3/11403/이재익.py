import sys
sys.stdin = open('input.txt')

# DFS 구현을 하는데, 자기 자신으로 돌아오는 것도 고려해야한다.
# 그래서 visited에 넣는 것을 앞이 아니라 뒤로 미뤄야 한다.
# 그거 말고는 딱히 어려운 것 없는 문제였다.

def DFS(S):
    for i in range(N):
        if M[S][i] == 1 and i not in visited:
            visited.append(i)
            DFS(i)
    return
N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]
new_M = [[0]*N for _ in range(N)]
for i in range(N):
    visited = []
    DFS(i)
    for j in range(N):
        if j in visited:
            new_M[i][j] = 1
for i in range(N):
    for j in range(N):
        print(new_M[i][j], end = ' ')
    print()