import sys
sys.stdin = open('input.txt')

# Dynamic Programming 구현 문제
# 시간에 유의할 것
# recursion으로 풀다가 틀렸음

def fibo(number):
    if number <= 2:
        if number == 0:
            print(1, 0)
            return
        elif number == 1:
            print(0, 1)
            return
        elif number == 2:
            print(1, 1)
            return
    else:
        left = 1
        right = 1
        now_left = 0
        now_right = 0
        for i in range(2, number):
            now_left = right
            now_right = left+right
            left = now_left
            right = now_right
        print(left, right)
        return


T = int(input())
for tc in range(1, T+1):
    zero_cnt = 0
    one_cnt = 0
    M = int(input())
    fibo(M)