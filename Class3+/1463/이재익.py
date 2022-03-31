import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')

def DFS(S, count):
    global cnt
    if S == 1:
        if count < cnt:
            cnt = count
        return

    if S != 1 and count == cnt:
        return

    for i in range(3):
        if i == 0 and S%3 == 0:
            DFS(S//3, count+1)
        elif i == 1 and S%2 == 0:
            DFS(S//2, count+1)
        elif i == 2:
            DFS(S-1, count+1)
cnt = 10000000000000000000000000000000
DFS(int(input()), 0)
print(cnt)