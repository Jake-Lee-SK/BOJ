import sys
sys.stdin = open('input.txt')
# input = sys.stdin.readline
N, M = map(int, input().split())
number = {}
name = {}
for i in range(1, N+1):
    pocket_name = input()
    number[pocket_name] = i
    name[i] = pocket_name
for i in range(M):
    a = input().strip()
    try:
        print(name[int(a)])
    except:
        print(number[a])