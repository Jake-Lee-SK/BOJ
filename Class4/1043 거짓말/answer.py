import sys
import itertools
sys.stdin = open('input.txt')

# 사람의 수 N, 파티의 수 M
N, M = map(int,input().split())
# 진실을 아는 사람의 숫자와 아는 사람들
truth = list(map(int, input().split()))
# 파티 정보
party = [list(map(int, input().split())) for _ in range(M)]
count = 0
know_people = set()
for i in range(1, len(truth)):
    know_people.add(truth[i])
if len(truth) == 1:
    print(M)
else:
    # 1차로 데이터 걸러내기(진실을 아는 사람과 진실을 아는 사람과 같이 있었던 사람 제외)
    # 계속 전염되는 형질의 것이므로 while문 이용해서 계속 금지사항 늘려나감.
    while 1:
        standard_count = know_people
        # 자꾸 숫자가 복사가 돼서 미리미리 copy를 시켜놓아야 한다.
        change_count = len(know_people)
        for i in range(len(party)):
            for j in range(1, len(party[i])):
                if party[i][j] in know_people:
                    for k in range(1, len(party[i])):
                        know_people.add(party[i][k])
        # 새롭게 추가되는 사람이 없을 때 비로소 break를 통해 while문 바깥으로 나감.
        if change_count == len(standard_count):
            break
    # 위의 진실을 알거나 알게 되는 사람을 제외한 파티에서 구라를 칠 수 있는 경우의 수를 계산
    for i in range(len(party)):
        check = 0
        for j in range(1, len(party[i])):
            if party[i][j] in know_people:
                check = 1
        if check == 1:
            pass
        else:
            count += 1
    print(count)

# 딴 것 보다 '전염되는지'를 아는 것을 중요시하는 문제였다.
