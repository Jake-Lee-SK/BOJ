import sys
sys.stdin = open('input.txt')

# 또한, 앞에서부터 계산했을 때,
# 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.

def count(numb, plus, minus, multi, divide, join):
    global number, mini, maxi
    if numb == len(number):
        mini = min(join, mini)
        maxi = max(join, maxi)
        return

    for i in range(4):
        if i == 0 and plus>0 and -INF < join + number[numb] < INF:
            count(numb+1, plus-1, minus, multi, divide, join + number[numb])
        elif i == 1 and minus>0 and -INF < join - number[numb] < INF:
            count(numb+1, plus, minus-1, multi, divide, join - number[numb])
        elif i == 2 and multi>0 and -INF < join * number[numb] < INF:
            count(numb+1, plus, minus, multi-1, divide, join * number[numb])
        # 나눗셈 조건이 까다로웠음.
        # 나눗셈은 -> 음수를 나눌 경우 우선 양수로 나누고, 그 몫을 다시 음수로 바꿔서 넣어줘야 함.
        elif i == 3 and divide> 0:
            if join < 0:
                new_join = -join // number[numb]
                if -INF < new_join < INF:
                    count(numb+1, plus, minus, multi, divide-1, -new_join)
            elif join >= 0 and -INF < join // number[numb] < INF:
                count(numb + 1, plus, minus, multi, divide - 1, join//number[numb])

    return


N = int(input())
number = list(map(int, input().split()))
iterators = list(map(int, input().split()))
INF = 1000000001
mini = INF
maxi = -INF
count(1, iterators[0], iterators[1], iterators[2], iterators[3], number[0])
print(maxi)
print(mini)


