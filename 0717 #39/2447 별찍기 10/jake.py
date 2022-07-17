N = 2
#9개씩 나눠서 분할 정복
def nine_divide(num1, num2, stars):
    global tmp_stars

    for i in range(num2//3, (num2//3)*2):
        for j in range(num2//3, (num2//3)*2):
            tmp_stars[i][j] = ''
    for i in range(len(stars)):
        print(*stars[i])
    if num1 and num2 == 1:
        return
    temp = [stars[i][0:num2//3] for i in range(0, num1//3)] # 위 왼쪽
    nine_divide(num1//3, num2//3, temp)
    temp = [stars[i][0:num2//3] for i in range(num1//3, (num1//3*2))] # 가운데 왼쪽
    nine_divide(num1//3, num2//3, temp)
    temp = [stars[i][0:num2//3] for i in range((num1//3)*2, num1)] # 아래 왼쪽
    nine_divide(num1//3, num2//3, temp)
    temp = [stars[i][num2//3:num1//3*2] for i in range(0, num1//3)] # 위 가운데
    nine_divide(num1//3, num2//3, temp)
    temp = [stars[i][num2//3:num2//3*2] for i in range(num1//3, (num1//3)* 2)] # 가운데 가운데
    nine_divide(num1//3, num2//3, temp)
    temp = [stars[i][num2 // 3:num2 // 3 * 2] for i in range((num1//3)*2, num1)] # 아래 가운데
    nine_divide(num1//3, num2//3, temp)
    temp = [stars[i][(num2//3)*2:num2] for i in range(0, num1//3)] # 위 오른쪽
    nine_divide(num1//3, num2//3, temp)
    temp = [stars[i][(num2//3)*2:num2] for i in range(num1//3, num1//3*2)] # 가운데 오른쪽
    nine_divide(num1//3, (num2//3)*2, temp)
    temp = [stars[i][(num2//3)*2:num2] for i in range((num1 // 3) *2, num1)] # 아래 오른쪽
    nine_divide(num1, num2, temp)

stars = [['*']*(3**N) for _ in range(3**N)]

tmp_stars = [[0]*(3**N) for _ in range(3**N)]
for i in range(3**N):
    for j in range(3**N):
        tmp_stars[i][j] = (3**N)*i+j

nine_divide(3**N, 3**N, tmp_stars)
for i in range(3**N):
    print(*tmp_stars[i])