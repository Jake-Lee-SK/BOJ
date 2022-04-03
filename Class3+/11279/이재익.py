import sys
sys.stdin = open('input.txt')
import heapq

N = int(input())
queue = []
for i in range(N):
    a = int(input())
    if a != 0:
        heapq.heappush(queue, (-a, a))
    elif a == 0:
        if queue:
            print(heapq.heappop(queue)[1])
        else:
            print(0)