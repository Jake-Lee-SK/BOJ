A, B, C = 10, 11, 12

# 곱셈의 성격으로 계속 분할 정복을 실행
# 절반으로 계속 줄여나간다.
# 그리고 더 이상 절반으로 줄일 수 없을 때 비로소 나머지를 구함.

def remainder(A, B, C):
    if B == 1:
        return A%C
    # 짝수일 때
    elif B % 2 == 0:
        half = remainder(A, B//2, C)
        return half*half%C
    else:
        half = remainder(A, B//2, C)
        return A*half*half%C

print(remainder(A, B, C))