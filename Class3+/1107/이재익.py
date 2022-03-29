import sys
sys.stdin = open('input.txt')

N = input()
M = int(input())
if M>0:
    nagari = list(map(int, input().split()))
else:
    nagari = []
# 가장 큰 수를 저장
max = 1000000000000000000000000000000000

# 만약 고장난 키가 없을 때
if nagari == False:
    # 만약 +, - 버튼을 한번씩 누르는 것보다 번호 버튼을 눌러서 가는 게 더 빠를 때
    if len(N)<abs(int(N)-100):
        print(len(N))
    # 만약 +, - 버튼을 누르는 게 더 빠를 때(101, 102같은 경우)
    else:
        print(abs(int(N)-100))
# 고장난 키가 있을 때
else:
    # 모두 고장나버려서 100에서 +, -로 가야 하는 경우
    if M == 10:
        print(abs(int(N)-100))
    else:
        # 100에서 +, -를 눌러서 그 채널로 가는 숫자
        gibon = abs(int(N)-100)
        for i in range(1000000):
            # 큰 수를 설정해서 bruteforce로 문제 풀기
            k = str(i)
            cnt = 0
            nagari_im = 0
            for j in k:

                # 고장난 버튼이 있는 채널인지 확인
                if int(j) in nagari:
                    nagari_im += 1
                # 고장나지 않았다면, 버튼을 누르는 횟수를 포함
                else:
                    cnt += 1

            # 만약 고장난 버튼이 포함된 채널이 있다면 제외
            if nagari_im>0:
                continue

            # 버튼이 모두 고장이 나지 않았다면, 이동한 채널과 목표 채널까지 +, - 횟수를 더해줌
            else:
                cnt += abs(int(N)-i)
            # 버튼을 눌러서 채널로 간 횟수 + 목표 채널까지 +, - 한 횟수를 더했을 때
            # 그 값이 최솟값이라면 답으로 저장
            if cnt < max:
                max = cnt
        # 만약 100번을 보고 있는 상태에서 100번을 가라고 하면 갈 필요가 없음
        if N == '100':
            print(0)
        # 100번에서 +, -로 이동하는 것보다 더 버튼을 눌러야 한다면 더 누를 필요가 없음
        elif max > gibon:
            print(gibon)
        # 나머지 경우에 답으로 반환
        else:
            print(max)
