from collections import deque
import sys
sys.stdin = open('input.txt')

# BFS 이용

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]
# 방문 여부 확인
check_matrix = [[0]*N for _ in range(N)]
# 단지 번호
vill = 0
# 단지 번호와 집 숫자를 저장
houses = []
for i in range(N):
    for j in range(N):
        queue = deque()
        # 아직 방문 안한 곳에 집이 있다면
        if matrix[i][j] != 0 and check_matrix[i][j] == 0:
            # 단지 번호를 추가
            vill += 1
            houses.append([vill, 1])
            queue.append([i, j])
            matrix[i][j] = vill
            check_matrix[i][j] = 1
            while queue:
                A = queue.popleft()
                for k in range(4):
                    new_x = A[0]+dx[k]
                    new_y = A[1]+dy[k]
                    if 0 <= new_x < N and 0<= new_y < N and matrix[new_x][new_y] != 0 and check_matrix[new_x][new_y] == 0:
                            queue.append([new_x, new_y])
                            matrix[new_x][new_y] = vill
                            check_matrix[new_x][new_y] = 1
                            houses[vill-1][1] += 1
# 집 숫자 오름순차로 정리
def key(houses):
    return houses[1]
houses.sort(key=key)
print(len(houses))
for i in range(len(houses)):
    print(houses[i][1])