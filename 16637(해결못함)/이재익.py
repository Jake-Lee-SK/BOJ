import sys
sys.stdin = open('input.txt')

# 요는 +를 많이 곱하고, -를 최대한 많이 배제하는 것
N = int(input())
E = input().split()
M = []
for i in range(N):
    M.append(E[0][i])
M.append('$')

now = 0

# 수식이 없을 때는 숫자만 반환

if N == 1:

    print(E)



if N == 3:

    if M[1] == '*':
        now = int(M[0]) * int(M[2])
    if M[1] == '-':
        now = int(M[0]) - int(M[2])
    if M[1] == '+':
        now = int(M[0]) + int(M[2])

    print(now)

# 길이가 5 이상일 때부터 시작

if N >= 5:
    if M[1] == '*':
        if M[3] == '+' and int(M[0])*int(M[2]) > 0:

            now = int(M[0]) * (int(M[2]) + int(M[4]))

            M[0] = '#'
            M[1] = '#'
            M[2] = '#'
            M[3] = '#'
            M[4] = '#'

        else:
            now = int(M[0]) * int(M[2])

            M[0] = '#'
            M[1] = '#'
            M[2] = '#'

    if M[1] == '-':

        if M[3] == '-' and int(M[2]) - int(M[4]) < 0:
            now = int(M[0]) - (int(M[2]) - int(M[4]))

            M[0] = '#'
            M[1] = '#'
            M[2] = '#'
            M[3] = '#'
            M[4] = '#'

        else:
            now = int(M[0]) - int(M[2])

            M[0] = '#'
            M[1] = '#'
            M[2] = '#'

    if M[1] == '+':
        now = int(M[0]) + int(M[2])

        M[0] = '#'
        M[1] = '#'
        M[2] = '#'

    for i in range(1, int(N / 2) + 1):
        if M[2 * i - 1] == '*':
            if M[2 * i + 1] == '+' and (M[2 * i]) != '#' and now != 0 and int(M[2*i]) != 0:
                now = now * (int(M[2 * i]) + int(M[2 * i + 2]))
                M[2 * i - 1] = '#'
                M[2 * i] = '#'
                M[2 * i + 1] = '#'
                M[2 * i + 2] = '#'
            else:
                now = now * int(M[2 * i])
                M[2 * i - 1] = '#'
                M[2 * i] = '#'
        if M[2 * i - 1] == '-' and (M[2 * i]) != '#':
            if M[2 * i + 1] == '-' and int(M[2 * i]) - int(M[2 * i + 2]) < 0:
                now = now - (int(M[2 * i]) - int(M[2 * i + 2]))
                M[2 * i - 1] = '#'
                M[2 * i] = '#'
                M[2 * i + 1] = '#'
                M[2 * i + 2] = '#'
            else:
                now = now - int(M[2 * i])
                M[2 * i - 1] = '#'
                M[2 * i] = '#'
        if M[2 * i - 1] == '+' and (M[2 * i]) != '#':
            now = now + int(M[2 * i])
            M[2 * i - 1] = '#'
            M[2 * i] = '#'

        if (M[2 * i + 1]) == '#':
            continue
print(now)