A = '55+50-40-30-30'

# 뒤에서부터 계산해서 -가 나타나면 한번 빼주고 하는 식으로 변경.

numbers = []
signs = []
number_stack = 0
decimal_stack = 0

for i in range(-1, -len(A)-1, -1):
    # 숫자일 때
    if A[i] != '-' and A[i] != '+':
        number_stack += (10**decimal_stack)*int(A[i])
        decimal_stack += 1
    else:
        decimal_stack = 0
        numbers.append(number_stack)
        number_stack = 0
        signs.append(A[i])
numbers.append(number_stack)

# 무조건 numbers의 수는 signs의 수보다 1 적다.

numbers = numbers[::-1]
signs = signs[::-1]
plus_stack = 0
total_number = numbers[0]
for i in range(len(signs)):
    # 앞에 '-'가 없는 '+'일 때는 그냥 더함
    if signs[i] == '+' and plus_stack == 0:
        total_number += numbers[i+1]
    elif signs[i] == '-' and plus_stack == 0:
        total_number -= numbers[i+1]
        plus_stack += 1
    elif signs[i] == '-' and plus_stack != 0:
        total_number -= numbers[i+1]
        plus_stack += 1
    elif signs[i] == '+' and plus_stack != 0:
        total_number -= numbers[i+1]

print(total_number)