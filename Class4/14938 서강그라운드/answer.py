import sys
import collections
sys.stdin = open('input.txt')

N, M, R = map(int, input().split())
T = list(map(int, input().split()))
Tree = [[] for _ in range(N+1)]
for _ in range(R):
    a, b, l = map(int, input().split())
    Tree[a].append([b, l])
    Tree[b].append([a, l])

max_items = 0

for i in range(1, N+1):
    queue = []
    for j in range(len(Tree[i])):
