import sys
input = sys.stdin.readline

N = int(input())
c = [0]*1000001
c[1] = 1
c[2] = 2
for i in range(3, N+1):
    c[i] = (c[i-2]+c[i-1])%15746
print(c[N])