import sys
sys.stdin = open('input.txt')

tc = int(input())
for _ in range(tc):
    N, M = map(int, input().split())
    matrix = [0*N]*N
    print(N, M, matrix)