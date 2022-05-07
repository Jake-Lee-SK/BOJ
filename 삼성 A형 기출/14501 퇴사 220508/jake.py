# Greedy? DFS? DP!
# max값 구하기.

import sys
sys.stdin = open('input.txt')

N = int(input())
M = []
profit = [0] * (N+1)
for i in range(N):
    A, B = map(int, input().split())
    M.append([A, B])
for day in range(N-1, -1, -1):
    # 만약 일할 수 있는 날을 넘어 선다면 일할 수 없다.
    if (day + M[day][0]) > N:
        profit[day] = profit[day+1]
    # 일할 수 있는 날 중에, 건너뛰는 것과 일을 하는 것의 최댓값을 비교.
    # 건너뛰면 일을 안한 것과 다를바가 없으므로 전날의 DP값과 같다.
    # 일을 하면 그 사이에 일을 못하므로, 그 다음까지 쌓았던 profit과 합친 값을 계산해야.
    else:
        profit[day] = max(profit[day+1], M[day][1]+profit[day+M[day][0]])
print(profit[0])