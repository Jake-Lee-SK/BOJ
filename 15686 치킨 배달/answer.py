import sys
sys.stdin = open('input.txt')
from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
chicken = []
house = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append([i, j])
        elif city[i][j] == 1:
            house.append([i, j])

min_chicken_distance = float('inf')
for i in range(1, M+1):
    survived_chicken = list(combinations(chicken, i))
    # 경우의 수 하나하나마다 따져보기
    for j in range(len(survived_chicken)):
        tmp = 0
        # 한 집에 대해 치킨 거리 계산
        for k in range(len(house)):
            chicken_distance = []
            for l in range(len(survived_chicken[j])):
                chicken_distance.append(abs(house[k][0]-survived_chicken[j][l][0])+abs(house[k][1]-survived_chicken[j][l][1]))
            tmp += min(chicken_distance)
        if tmp < min_chicken_distance:
            min_chicken_distance = tmp
print(min_chicken_distance)


