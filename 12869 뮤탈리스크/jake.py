from collections import deque

N = int(input())
hp = list(map(int, input().split()))

if N == 1:
    if hp[0] >= 9 and hp[0] % 9 == 0:
        print(hp[0]//9)
    elif hp[0] < 9:
        print(1)
    else:
        print((hp[0]//9)+1)
else:
    if N == 2:
        queue = deque()
        queue.append([[hp[0], hp[1]], 0])
        while queue:
            next = queue.popleft()
            if next[0][0] <= 0 and next[0][1] <= 0:
                print(next[1])
                break
            A = [[next[0][0]-9, next[0][1]-3], next[1]+1]
            B = [[next[0][0]-3, next[0][1]-9], next[1]+1]
            if A not in queue:
                queue.append(A)
            if B not in queue:
                queue.append(B)

    else:
        queue = deque()
        queue.append([[hp[0], hp[1], hp[2]], 0])
        while queue:
            next = queue.popleft()
            if next[0][0] <= 0 and next[0][1] <= 0 and next[0][2] <= 0:
                print(next[1])
                break
            A = [[next[0][0]-9, next[0][1]-3, next[0][2]-1], next[1]+1]
            B = [[next[0][0]-9, next[0][1]-1, next[0][2]-3], next[1]+1]
            C = [[next[0][0]-3, next[0][1]-9, next[0][2]-1], next[1]+1]
            D = [[next[0][0]-3, next[0][1]-1, next[0][2]-9], next[1]+1]
            E = [[next[0][0]-1, next[0][1]-3, next[0][2]-9], next[1]+1]
            F = [[next[0][0]-1, next[0][1]-9, next[0][2]-3], next[1]+1]
            if A not in queue:
                queue.append(A)
            if B not in queue:
                queue.append(B)
            if C not in queue:
                queue.append(C)
            if D not in queue:
                queue.append(D)
            if E not in queue:
                queue.append(E)
            if F not in queue:
                queue.append(F)