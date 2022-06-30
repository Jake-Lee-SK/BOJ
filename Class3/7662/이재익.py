import sys
sys.stdin = open('input.txt')
import heapq

T = int(input())
for i in range(1, T+1):
    N = int(input())
    max_heap = []
    min_heap = []
    check = [0]*N
    for j in range(N):
        a, b = sys.stdin.readline().split()

        if a == 'I':
            heapq.heappush(max_heap, (-int(b), j))
            heapq.heappush(min_heap, (int(b), j))

        elif a == 'D':
            if b == '-1':  # 최솟값 제외
                while min_heap:
                    # 최댓값에서 삭제하지 않은 값이 아직 남아있다면 삭제.
                    if check[min_heap[0][1]] == 1:
                        heapq.heappop(min_heap)
                    else:
                        break
                if min_heap:
                    # 최댓값에서 값 삭제를 위해 check를 활성화 시킴.
                    min = min_heap[0][1]
                    check[min] = 1
                    heapq.heappop(min_heap)

            elif b == '1': # 최댓값 제외
                while max_heap:
                    # 최솟값에서 삭제하지 않은 값이 아직 남아있다면 삭제.
                    if check[max_heap[0][1]] == 1:
                        heapq.heappop(max_heap)
                    else:
                        break
                if max_heap:
                    # 최솟값에서 값 삭제를 위해 check를 활성화 시킴.
                    max = max_heap[0][1]
                    check[max] = 1
                    heapq.heappop(max_heap)

    while max_heap:
        # 다 돌리고 난 후에 값들을 삭제해줌
        if check[max_heap[0][1]] == 1:
            heapq.heappop(max_heap)
        else:
            break
    while min_heap:
        # 다 돌리고 난 후에 값들을 삭제해 줌
        if check[min_heap[0][1]] == 1:
            heapq.heappop(min_heap)
        else:
            break
    if min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")