def DP(now, index, count, max):


import sys
sys.stdin = open('input.txt')
A = int(input())
numbers = [list(map(int, input().split())) for _ in range(A)]