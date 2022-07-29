import sys
sys.stdin = open('input.txt')

# 최악의 경우의 수는 8x4(모두 다른 방향을 봤을 때)
# 각 카메라 별 방향 당 잡히는 곳을 [x, y] 형태로 리스트에 저장
# 그리고 리스트를 묶어봐서 제일 많이 잡히는 것을 답으로 반환

# 1번 카메라(1방향)(총 방향은 4개)
def first_camera(x, y):
    pass

# 2번 카메라(ㅡ방향)(총 방향은 2개)
def second_camera(x, y):
    pass

# 3번 카메라(ㄱ방향)(총 방향은 4개)
def third_camera(x, y):
    pass

# 4번 카메라(ㅗ방향)(총 방향은 4개)
def fourth_camera(x, y):
    pass

# 5번 카메라(모든 방향)(딱 1방향)
def fifth_camera(x, y):
    pass

N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
camera = []

# 카메라 위치를 저장
for i in range(N):
    for j in range(M):
        if room[i][j] != 0 and room[i][j] != 6:
            camera.append([i, j, room[i][j]])

# 카메라 번호에 따라 다른 것을 저장
for i in range(len(camera)):
    if camera[i][2] == 1:
        first_camera(camera[i][0], camera[i][1])
    elif camera[i][2] == 2:
        second_camera(camera[i][0], camera[i][1])
    elif camera[i][2] == 3:
        third_camera(camera[i][0], camera[i][1])
    elif camera[i][2] == 4:
        fourth_camera(camera[i][0], camera[i][1])
    elif camera[i][2] == 5:
        fifth_camera(camera[i][0], camera[i][1])