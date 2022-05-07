# N = 시험장의 수
# Ai = 응시자의 수(각 시험장에 있는)
# B = 총감독관 감시 , C = 부감독관 감시

import sys
sys.stdin = open('input.txt')

N = int(input())
rooms = list(map(int, input().split()))
B, C = map(int, input().split())
total = 0
for room in rooms:
    if room-B <= 0:
        total += 1
        continue
    else:
        if (room-B) % C == 0:
            sub = (room-B)//C
        elif (room-B) // C == 0 and (room-B) % C > 0:
            sub = 1
        else:
            sub = (room-B)//C + 1
        total += 1
        total += sub
print(total)