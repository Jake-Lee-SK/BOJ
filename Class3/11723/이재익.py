import sys
sys.stdin = open('input.txt')

N = int(input())
S = [0]*20
for i in range(N):
    a = input().split()
    if a[0] != 'empty' and a[0] != 'all':
        if a[0] == 'add':
            S[int(a[1])-1] = 1
        elif a[0] == 'remove':
            S[int(a[1])-1] = 0
        elif a[0] == 'check':
            if S[int(a[1])-1] == 1:
                print(1)
            else:
                print(0)
        elif a[0] == 'toggle':
            if S[int(a[1])-1] == 1:
                S[int(a[1])-1] = 0
            else:
                S[int(a[1])-1] = 1
    else:
        if a[0] == 'all':
            S = [1]*20
        elif a[0] == 'empty':
            S = [0]*20
