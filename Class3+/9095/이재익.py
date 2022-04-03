import sys
sys.stdin = open('input.txt')

numb = [1,2,3]
def DFS(S, G):
    global cnt
    check = [False]*3
    if S == G:
        cnt += 1
        return
    if S > G:
        return

    for i in range(3):
        if check[i] == False:
            check[i] = True
            DFS(S+numb[i], G)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    DFS(0, N)
    print(cnt)