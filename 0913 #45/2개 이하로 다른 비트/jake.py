def solution(numbers):
    answer = []
    for number in numbers:
        two_number = list('0' + bin(number)[2:])
        count = 0
        # 짝수인 경우 1만 더해줌
        if number % 2 == 0:
            answer.append(number + 1)
        # 홀수인 경우 가장 앞의 0을 1로 바꾸고, 뒤의 1을 0으로 바꾸면 해결됨.
        else:
            idx = ''.join(two_number).rfind('0')
            two_number[idx] = '1'
            two_number[idx + 1] = '0'
            answer.append(int(''.join(two_number), 2))

    return answer