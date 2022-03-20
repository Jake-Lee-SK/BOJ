import sys
sys.stdin = open('input.txt')
from collections import deque

# BFS, DFS 구현하는 기초 중의 기초 문제

def DFS(S):
    global visit_dfs
    stack_dfs.append(S)
    for i in range(len(N_list[S])):
        if N_list[S][i] not in stack_dfs and N_list[S][i] not in visit_dfs:
            visit_dfs.append(N_list[S][i])
            DFS(N_list[S][i])
    return

def BFS(S):
    global visit_bfs
    stack_bfs.append(S)
    queue=deque()
    queue.append(S)
    while queue:
        n = queue.popleft()
        for i in range(len(N_list[n])):
            if N_list[n][i] not in stack_bfs and N_list[n][i] not in visit_bfs:
                stack_bfs.append(N_list[n][i])
                queue.append(N_list[n][i])
    return

N, M, V = map(int, input().split())
N_list = [[] for _ in range(N+1)]
for i in range(M):
    A, B = map(int, input().split())
    N_list[A].append(B)
    N_list[B].append(A)
    N_list[A].sort()
    N_list[B].sort()
visit_bfs = [0]*N
stack_bfs = []
visit_dfs = [0]*N
stack_dfs = []
DFS(V)
for i in range(len(stack_dfs)):
    print(stack_dfs[i], end = ' ')
print()
BFS(V)
for i in range(len(stack_bfs)):
    print(stack_bfs[i], end = ' ')