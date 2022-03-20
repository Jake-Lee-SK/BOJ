import sys
sys.stdin = open('input.txt')
# 메모리 초과되는 함수.
# 하지만 좀 더 직관적

# def divide(size, garo, sero, cnt):
#     if r == garo and c == sero: #찾으면 멈추기
#         print(int(cnt))
#         return
#
#     elif r<garo+size/2 and c<sero+size/2: # 찾는 점이 왼쪽 위에 있다면
#         divide(size/2, garo, sero, cnt) # 사이즈를 반으로 나눠서 다시 실시, x와 y축 좌표는 수정 안해도 됨
#
#     elif r<garo+size/2 and c >= sero+size/2: # 찾는 점이 왼쪽 아래에 있다면
#         cnt = cnt + (size/2)**2 # 우선 찾는 숫자는 size/2**2보다 크므로 찾는 y축 좌표를 수정
#         divide(size/2, garo, sero+size/2, cnt)
#
#     elif r>=garo+size/2 and c < sero+size/2: # 찾는 점이 오른쪽 위에 있다면
#         cnt = cnt + ((size/2)**2) *2 # 찾는 숫자는 (size/2**2)*2 보다 크므로 찾는 x축 좌표를 수정
#         divide(size/2, garo + size/2, sero, cnt)
#
#     elif r >= garo+size/2 and c >= sero+size/2: # 찾는 점이 오른쪽 아래에 있다면
#         cnt = cnt + ((size/2)**2)*3
#         divide(size/2, garo+size/2, sero+size/2, cnt) # x축과 y축 좌표를 모두 수정하고 다시 실시

N, r, c = map(int, input().split())
# r은 가로 # c는 세로
# 가로가 절반 넘으면 세로의 2배임
visit = 0
while N != 0:
    if r >= 2**(N-1): # 절반보다 r이 크다면 count의 최소치를 변경
        visit += 2**(2*N - 1) # 카운트는 최소한 2**(2*N - 1)보다는 큼.
    if c >= 2**(N-1): # 절반보다 c가 크다면 count의 최소치를 변경
        visit += 2**(2*N - 2) # 카운트는 최소한 2**(2*N - 2)보다는 큼.
        # r이 클 수록 숫자가 훨씬 커짐.
        #
    r = r % (2**(N-1)) # 절반보다 r이 크다면 r은 나눠짐
    c = c % (2**(N-1)) # 절반보다 c가 크다면 c는 나눠짐
    N -= 1
print(visit)