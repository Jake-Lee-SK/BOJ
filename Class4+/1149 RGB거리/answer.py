import sys

sys.stdin = open('input.txt')

def DFS(G, cnt):
    global min_cnt
    check = [False]*3

    if G == N:
        if cnt < min_cnt:
            min_cnt = cnt
        return

    if G != N and cnt > min_cnt:
        return

    for i in range(3):
        if check[i] == False and :
            check[i] = True
            DFS(G+1, cnt+RGB[G][i])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    RGB = [list(map(int, input().split()))]
    min_cnt = 10000000000000000000
    DFS(0, 0)
    print(min_cnt)