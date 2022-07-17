import sys
sys.stdin = open('input.txt')

# Things는 물건의 수, Capacity는 들 수 있는 무게
Things, Capacity = map(int, input().split())

# Weight는 무게, Value는 가치

Weight = [0]*(Things+1)
Value = [0]*(Things+1)
for i in range(Things):
    A, B = map(int, input().split())
    Weight[i+1] = A
    Value[i+1] = B

Max_Value = [[0]*(Capacity+1) for _ in range(Things+1)]
for i in range(1, Things+1):
    # j는 들 수 있는 무게를 말함
    for j in range(1, Capacity+1):
        # 무게가 들 수 있는 무게보다 크다면 위의 정보(바로 직전의 물건을 시험해본 것)를 그대로 가져옴
        if Weight[i] > j:
            Max_Value[i][j] = Max_Value[i-1][j]
        # 지금까지의 물건은 들 수 있는 물건의 최댓값이므로
        # 최댓값과 새롭게 가져온 물건을 들 지 안들지를 고려하면 꽉꽉 눌러 담을 수 있다.
        else:
            Max_Value[i][j] = max(Max_Value[i-1][j], Value[i] + Max_Value[i-1][j-Weight[i]])
print(Max_Value[-1][-1])