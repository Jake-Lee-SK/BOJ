import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(1000000000)
def DFS(node, distance):
    global max_dist
    global check
    global max_node

    for j in range(len(Tree[node])):
        if check[Tree[node][j][0]] == 0:
            check[Tree[node][j][0]] = 1
            DFS(Tree[node][j][0], distance+Tree[node][j][1])

    if distance > max_dist:
        max_dist = distance
        max_node = node
    return

N = int(input())
Tree = [[] for _ in range(N+1)]


for _ in range(N-1):
    A, B, Dist = map(int, input().split())
    Tree[A].append([B, Dist])
    Tree[B].append([A, Dist])

# 제일 먼 거리
max_dist = 0
# 제일 먼 노드
max_node = 0

# 최상위 노드(원의 중심)에서 제일 먼 노드를 정함
check = [0]*(N+1)
check[1] = 1
DFS(1, 0)

# 제일 먼 노드에서 제일 먼 노드까지의 거리(지름)를 구함
check = [0]*(N+1)
check[max_node] = 1
DFS(max_node, 0)

print(max_dist)