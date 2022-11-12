import sys
sys.stdin = open('input.txt')
T = int(input())
for _ in range(T):
    N = int(input())
    count = 0
    candidate = [list(map(int, input().split())) for _ in range(N)]
    candidate.sort(key=lambda x:x[0])
    answer = [candidate[0]]
    for i in range(1, N):
        if candidate[i][0]<=answer[-1][0] or candidate[i][1]<=answer[-1][1]:
            answer.append(candidate[i])
    print(len(answer))

    # 한 쪽의 1등값이 갖고있는 최소한의 값과 같거나 그보다 더 이상이여야 함