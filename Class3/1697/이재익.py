import sys
sys.stdin = open('input.txt')
from collections import deque
# input = sys.stdin.readline

N, M = map(int,input().split())
K = [[] for _ in range(100001)]
for i in range(100001):
    if 0<=i-1<=100000:
        K[i].append(i-1)
    if 0 <= i + 1 <= 100000:
        K[i].append(i+1)
    if 0<=2*i<=100000:
        K[i].append(2*i)
check = [0 for _ in range(100001)]
queue = deque()
queue.append(N)
check[N] = 1
while queue:
    n = queue.popleft()
    for i in K[n]:
        if check[i] == 0:
            check[i] = check[n] + 1
            queue.append(i)
print(check[M]-1)

