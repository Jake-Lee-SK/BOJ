import sys
sys.stdin = open('input.txt')

# 크기 N, 구해야 하는 쌍 M
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if j == 0:
            pass
        else:
            matrix[i][j] += matrix[i][j-1]
for _ in range(M):
    i, j, x, y = map(int, sys.stdin.readline().split())
    answer = 0
    for k in range(i-1, x):
        if j != 1:
            answer -= matrix[k][j-2]
        answer += matrix[k][y-1]
    print(answer)

# 구간합을 구하는 문제이기 때문에 구간합을 미리 구해놓고 구간을 정해주면 좀 더 쉽게 풀 수 있다.