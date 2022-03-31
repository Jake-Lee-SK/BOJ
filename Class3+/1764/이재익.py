import sys
sys.stdin = open('input.txt')
N, M = map(int, input().split())
dd = {}
bd = []

for i in range(N):
    dd[input()] = 1
for i in range(M):
    a = input()
    if dd.get(a) == True:
        bd.append(a)
bd = sorted(bd)
print(len(bd))
for i in range(len(bd)):
    print(bd[i])