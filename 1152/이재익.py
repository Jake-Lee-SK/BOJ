import sys
sys.stdin = open('input.txt')

N = input()
cnt = 0
for i in range(len(N)):
    if N[i] == ' ' and i != 0 and i != len(N)-1:
        cnt+=1
print(cnt+1)