import sys
sys.stdin = open('input.txt')

# 무지성으로 분할부터 하고 봐서 Tc 하나 틀림
# 분할정복하기 전에 이미 필요가 없는 건지 체크하는 과정 꼭 필요
from collections import deque
N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
queue = deque()
queue.append(matrix)
blue = 0
white = 0
while queue:
    n = queue.popleft()
    length = len(n)
    half = length//2
    cnt = 0
    for i in range(length):
        for j in range(length):
           if n[i][j] == 1:
               cnt += 1
    if cnt == 0:
        white += 1
        continue
    elif cnt == length*length:
        blue += 1
        continue

    if length >= 2:
        tmp1 = []
        tmp2 = []
        tmp3 = []
        tmp4 = []
        for i in range(length):
            if i < half:
                tmp1.append(n[i][:half])
                tmp2.append(n[i][half:])
            elif i >= half:
                tmp3.append(n[i][:half])
                tmp4.append(n[i][half:])
        cnt1 = 0
        cnt2 = 0
        cnt3 = 0
        cnt4 = 0
        for i in range(half):
            for j in range(half):
                if tmp1[i][j]== 1:
                    cnt1 += 1
                if tmp2[i][j]== 1:
                    cnt2 += 1
                if tmp3[i][j]==1:
                    cnt3 += 1
                if tmp4[i][j]==1:
                    cnt4 += 1
        if 0 <cnt1 < half*half:
            queue.append(tmp1)
        else:
            if cnt1 == 0:
                white += 1
            elif cnt1 == half*half:
                blue += 1
        if 0 < cnt2 < half*half:
            queue.append(tmp2)
        else:
            if cnt2 == 0:
                white += 1
            elif cnt2 == half*half:
                blue += 1
        if 0 < cnt3 < half*half:
            queue.append(tmp3)
        else:
            if cnt3 == 0:
                white += 1
            elif cnt3 == half*half:
                blue += 1
        if 0 < cnt4 < half*half:
            queue.append(tmp4)
        else:
            if cnt4 == 0:
                white += 1
            elif cnt4 == half*half:
                blue += 1
    else:
        if n[0] == 1:
            blue += 1
        else:
            white += 1

print(white)
print(blue)