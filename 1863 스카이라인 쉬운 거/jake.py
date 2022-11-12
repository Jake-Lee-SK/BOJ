import sys
sys.stdin = open('input.txt')

N = int(input())
line = [list(map(int, input().split())) for _ in range(N)]
# 지도가 하나일 땐 하나만
if N == 1:
    print(1)
else:
    line.sort(key=lambda x:(x[0]))
    stack = [line[0][1]]
    count = 0
    for i in range(1, N):
        if stack and line[i][1] > stack[-1]:
            stack.append(line[i][1])
        elif stack and line[i][1] < stack[-1]:
            stack.pop()
            count += 1
        elif not stack:
            stack.append(line[i][1])
        print(count, stack)
    print(count)