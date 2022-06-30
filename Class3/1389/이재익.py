import sys

# input = sys.stdin.readline
sys.stdin = open('input.txt')

from collections import deque

N, M = map(int, input().split())
friends = [[] for _ in range(N+1)]
max = 10000000000
player = 0
for i in range(M):
    A, B = map(int, input().split())
    friends[A].append(B)
    friends[B].append(A)
check = [[-1]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    queue = deque()
    queue.append(i)
    check[i][i] += 1
    while queue:
        n = queue.popleft()
        for j in friends[n]:
            if check[i][j] == -1:
                queue.append(j)
                check[i][j] = check[i][n] + 1
for i in range(1, N+1):
    if sum(check[i])+1<max:
        max = sum(check[i])+1
        player = i
print(player)