from collections import deque
from itertools import combinations
A = '(1+(2*(3+4)))'
B = deque()
C = []
count = 0
answer = set()
# 괄호의 시작지점과 끝 지점을 저장
for i in range(len(A)):
    if A[i] == '(':
        B.append(i)
    elif A[i] == ')':
        start = B.pop()
        end = i
        C.append([start, end])
# combination으로 묶어서 경우의 수를 모두 도출.
for i in range(1, len(C)+1):
    D = list(combinations(C, i))
    for j in D:
        tmp = list(A)
        for k in j:
            start, end = k
            tmp[start] = ''
            tmp[end] = ''
        answer.add(''.join(tmp))

for i in sorted(list(answer)):
    print(i)

