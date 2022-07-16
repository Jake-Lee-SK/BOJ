import sys
sys.stdin = open('input.txt')

N = int(input())
Tree = [[] for _ in range(N+1)]
# 양방향으로 Tree에 추가함
for _ in range(N-1):
    A, B, Dist = map(int, input().split())
    Tree[A].append([B, Dist])
    Tree[B].append([A, Dist])
# 가장 먼 번호를 따라가야 함.