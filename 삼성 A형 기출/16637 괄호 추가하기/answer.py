# 숫자와 연산자를 나눠서 저장
def num_and_operator(string, num, operator):
    for i in string:
        if i.isdigit():
            num.append(int(i))
        else:
            operator.append(i)

# 계산
def calculating(n1, n2, operator):
    if operator == '*':
        return n1 * n2
    elif operator == '+':
        return n1 + n2
    elif operator == '-':
        return n1 - n2

# idx는 포인터, result는 지금까지 더한 값
def brute(idx, result):
    # 답을 전역변수 선언
    global max_num

    # 결과를 비교해서 저장
    if idx >= len(operator):
        max_num = max(max_num, result)
        return

    # 이번에 계산 되는 경우(괄호가 나이거나, 나보다 앞에 있음)
    brute(idx + 1, calculating(result, num[idx + 1], operator[idx]))

    # 이번에 계산되지 않는 경우->뒤에가 먼저 계산되는 경우(괄호가 나보다 뒤에 있음)(dfs 응용)
    if idx + 1 < len(operator):
        brute(idx + 2, calculating(result, calculating(num[idx + 1], num[idx + 2], operator[idx + 1]), operator[idx]))


def solution(arr):
    # 숫자와 연산자를 각각 저장함.
    num_and_operator(arr, num, operator)

    # 브루트포스 이용
    brute(0, num[0])

import sys
max_num = -2**31-1
N = 9
arr = '3+8*7-9*2'
num, operator = [], []
solution(arr)
print(max_num)