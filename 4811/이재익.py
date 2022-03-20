import sys
sys.stdin = open('input.txt')
# 시간 초과 유의할 것
# 수학으로 못 푸는 문제임
# 그래프로 구현해보는 연습할 것


# def comb(N, M):
#     number1 = 1
#     for i in range(N, N-M, -1):
#         number1 *= i
#     number2 = 1
#     for i in range(M, 0, -1):
#         number2 *= i
#     return number1//number2
#
# def DP(N):
#     K = N-2
#     if N == 1:
#         return 1
#     elif N == 2:
#         return 2
#
#     else:
#         a = 1+N-1
#         b = 0
#         for i in range(K):
#             b += comb(N+i, 2+i)
#         c = 0
#         for i in range(K):
#             c += -2**(K-1+i)
#     return a+b+c

while 1:
    N = int(input())
    if N == 0:
         break

    # Phill[H][W]

    Phill = [[0]*(N+2) for j in range(N+2)] # range문제 안되게 여유롭게 이중 배열 작성
    Phill[N][0] = 1
    for W in range(N-1, -1, -1):
        for H in range(N, -1, -1):
            if H == 0: # 반개짜리가 없으면 옆으로 이동(반쪽짜리 먹을 수 있음)
                Phill[W][H] = Phill[W][H+1]
            elif H == N: # 알약 한개짜리를 모두 다 먹었을 때 대각선 1로 채움
                Phill[W][H] = Phill[W+1][H-1]
            else: # 그 외 상황
                Phill[W][H] = Phill[W+1][H-1] + Phill[W][H+1]

    print(Phill[0][0])