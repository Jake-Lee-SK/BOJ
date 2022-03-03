import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int,input().split()))

    # Combination 구현 문제
    # mCn 형식
    if M == N:
        print(f'1')
    else:
        M_list = []
        N_list = []
        for i in range(N):
            M_list.append(M-i)
        for i in range(N):
            N_list.append(N-i)
        gob_M = 1
        gob_N = 1
        for i in range(len(M_list)):
            gob_M *= M_list[i]
        for i in range(len(N_list)):
            gob_N *= N_list[i]
        print(f'{int(gob_M/gob_N)}')


