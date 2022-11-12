import heapq
import sys
sys.stdin = open('input.txt')

N = int(input())
answer = 0
if N == 1:
    print(0)
else:
    cards = list(int(input()) for _ in range(N))
    heapq.heapify(cards)
    while len(cards)>1:
        stack1 = heapq.heappop(cards)
        stack2 = heapq.heappop(cards)
        answer += (stack1+stack2)
        heapq.heappush(cards, stack1+stack2)
    print(answer)