import sys
sys.stdin = open('input.txt')
from itertools import combinations

N, M = map(int, input().split())
Cards = list(map(int, input().split()))

C = combinations(Cards, 3)
cnt = 0
for i in C:
    if sum(i) > cnt and sum(i)<= M:
        cnt = sum(i)

print(cnt)



