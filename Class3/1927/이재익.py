import sys
sys.stdin = open('input.txt')

# 처음 써보는 heapq 기능
# 하지만 그것으로 충분함

import heapq
N = int(input())
M = [int(input()) for i in range(N)]
C = []
for i in M:
    if i != 0:
        heapq.heappush(C, i)
    elif i == 0 and len(C) == 0:
        print(0)
    elif i == 0 and len(C) != 0:
        print(heapq.heappop(C))