import sys
sys.stdin = open('input.txt')

N = int(input())
T = [list(map(int, input().split())) for _ in range(N)]
T.sort(key=lambda x: (x[1], x[0])) # 끝나는 시간대로 정렬.
end = 0 # 끝나는 시간을 저장
cnt = 0 # 회의실 사용 회의
for i in range(N):
    if T[i][0] >= end: # 시작시간이 end보다 크거나 같다면 저장
        end = T[i][1] # end 값을 그 회의가 끝나는 시간으로 새로 저장.
        cnt += 1 # 카운트

print(cnt)