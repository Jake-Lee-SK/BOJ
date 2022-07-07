A = 2
B = 22

from collections import deque

queue = deque()
queue.append([A, 1])
find = 0
while queue:
    Now = queue.popleft()
    if Now[0] != B and Now[0] < B:
        queue.append([Now[0] * 2, Now[1] + 1])
        queue.append([Now[0] * 10 + 1, Now[1] + 1])
    elif Now[0] == B:
        find = Now[1]
        break
    elif Now[0] > B:
        continue
if find != 0:
    print(find)
else:
    print(-1)
