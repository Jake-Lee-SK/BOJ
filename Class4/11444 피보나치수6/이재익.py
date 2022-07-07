import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
# 해시 테이블을 생성
fibonacci = {0: 0, 1: 1, 2: 1}


def Fibonacci(n):
    # 피보나치 해시 테이블에 값이 없다면 계속 생성해나감.
    if not fibonacci.get(n):
        # n이 홀수면 (n+1)/2한 값의 피보나치 숫자의 제곱+((n+1)/2한 값)-1의 피보나치 숫자 제곱이 피보나치 숫자임.
        if n % 2 == 1:
            fibonacci[n] = (Fibonacci((n+1)//2)**2 +
                            Fibonacci((n+1)//2-1)**2) % 1000000007
        # n이 짝수면 그냥 n+1의 피보나치숫자 - n-1의 피보나치 숫자를 계산하면 됨
        else:
            fibonacci[n] = (Fibonacci(n+1) - Fibonacci(n-1)) % 1000000007

    return fibonacci[n]


N = 1000

print(Fibonacci(N))