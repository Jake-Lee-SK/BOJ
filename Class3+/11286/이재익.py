
import sys
input = sys.stdin.readline
import heapq
N = int(input())
B = []
for i in range(N):
    number = int(input())
    if number != 0:
        heapq.heappush(B, (abs(number), number))
    else:
        if B:
            print(heapq.heappop(B)[1])
        else:
            print(0)