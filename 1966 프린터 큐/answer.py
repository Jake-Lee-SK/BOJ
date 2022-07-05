# 테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과,
# 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다.
# 이때 맨 왼쪽은 0번째라고 하자.
# 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다.
# 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.

import sys
sys.stdin = open('input.txt')

from collections import deque

tc = int(input())
for _ in range(tc):
    queue = deque()
    New_FIFO = deque()
    count = 0
    N, M = map(int, input().split())
    FIFO = deque(list(map(int, input().split())))
    for i in range(len(FIFO)):
        New_FIFO.append([FIFO[i], i])
    while New_FIFO:
        if FIFO[0] != max(FIFO):
            New_FIFO.append(New_FIFO.popleft())
            FIFO.append(FIFO.popleft())
        elif FIFO[0] == max(FIFO) and New_FIFO[0][1] != M:
            New_FIFO.popleft()
            FIFO.popleft()
            count += 1
        elif FIFO[0] == max(FIFO) and New_FIFO[0][1] == M:
            count += 1
            print(count)
            break