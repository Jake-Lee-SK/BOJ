import sys
sys.stdin = open('input.txt')

N = int(input())
number = list(map(int, input().split()))
# DP => 2차원 DP 이용
# 즉 answer[index(현재 순서)][해당 숫자에 경우의 숫자가 있는지]
answer = [[0]*21 for _ in range(N)]
answer[0][number[0]] += 1
for i in range(1, N-1):
    for j in range(21):
        # 전에 숫자가 존재해야 다음으로 넘어갈 수 있으므로
        if answer[i-1][j]:
            # 해당 숫자에 지금 새롭게 만나는 숫자를 더한 값이 20 이하여야 하므로
            if j+number[i] < 21:
                answer[i][j+number[i]] += answer[i-1][j]
            if j-number[i] > -1:
                answer[i][j-number[i]] += answer[i-1][j]
# 모두 이어져 내려 왔을 때 마지막 숫자일 경우의 수를 출력.
print(answer[N-2][number[N-1]])


