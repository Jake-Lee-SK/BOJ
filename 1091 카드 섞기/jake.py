import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
N = int(input())
# 바뀌는 함수
P = list(map(int, input().split()))

# 비교용으로 남겨두기
Original = P

# 값 넣는 용
New = [0]*N

# 원하는 값
Compare = [0,1,2]*(N//3)

# 순서
S = list(map(int, input().split()))

cnt = 0

while P != Compare:
    for i in range(N):
        New[S[i]] = P[i]
    P = New
    New = [0] * N
    cnt += 1
    # 중간에 한번 다시 돌아오게 되면 아무 쓸모 없음.
    if Original == P:
        cnt = -1
        break

print(cnt)