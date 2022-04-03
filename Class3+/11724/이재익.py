import sys
sys.stdin = open('input.txt')
from collections import deque

N, M = map(int, input().split())
tree = [[] for _ in range(N+1)]
check = [0]*(N+1)
for i in range(M):
    A, B = map(int, input().split())
    tree[A].append(B)
    tree[B].append(A)
for i in range(1, N+1):
    if check[i] == 0:
        queue = deque()
        queue.append(tree[i])
        check[i] = i
        while queue:
            n = queue.popleft()
            for j in n:
                if check[j] == 0:
                    check[j] = i
                    queue.append(tree[j])
check2 = 0
for i in range(1, N+1):
    if check[i] == i:
        check2 += 1
print(check2)

