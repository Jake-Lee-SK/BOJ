import sys
sys.stdin = open('input.txt')
# 첫 번째와 두 번째의 정수는 사각형의 왼쪽 아래 꼭짓점의 x좌표, y좌표이고
# 세 번째와 네 번째의 정수는 사각형의 오른쪽 위 꼭짓점의 x좌표, y좌표이다.
# 모든 x좌표와 y좌표는 1이상이고 100이하인 정수이다.
M = [list(map(int, input().split())) for _ in range(4)]
xy = list([0]*100 for _ in range(100))
for i in range(4):
        M[2*i:]:[j]
