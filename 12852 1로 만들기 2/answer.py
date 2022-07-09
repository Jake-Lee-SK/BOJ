from collections import deque

N = 10
# 숫자만큼 길이 가지는 리스트 생성
Route = [0]*(N+1)
# deque 안에 N 넣고 출발
queue = deque([N])
while queue:
    check_numb = queue.popleft()
    # 다음 번이 1이 된다면 멈춰도 됨
    if check_numb-1 == 1 or check_numb//2 == 1 or check_numb//2 == 1:
        Route[1] = check_numb
        break
    # 3,2로 나눠지는 수가 있다면 그 다음번째 index에다 다음번째 숫자를 저장한 후 queue에 추가
    if check_numb%3 == 0 and Route[check_numb//3] == 0:
        Route[check_numb//3] = check_numb
        queue.append(check_numb//3)
    if check_numb%2 == 0 and Route[check_numb//2] == 0:
        Route[check_numb//2] = check_numb
        queue.append(check_numb//2)
    # 그것도 아니라면 그냥 -1한 숫자를 index에 추가함.
    if check_numb-1 > 0 and Route[check_numb-1] == 0:
        Route[check_numb-1] = check_numb
        queue.append(check_numb-1)

# 즉 Route의 index에 있는 숫자는 그 다음 번째 숫자를 의미한다.
# 1에서 출발하는 숫자를 따라가면 가장 단기간 내에 N에 도달할 수 있다.
answer = [1]
while answer[-1] != N:
    index = answer[-1]
    answer.append(Route[index])
print(len(answer)-1)
print(*answer[::-1])
