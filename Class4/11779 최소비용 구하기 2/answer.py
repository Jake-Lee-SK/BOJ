import copy
import sys
sys.stdin = open('input.txt')
N = int(input())
M = int(input())
Tree = [[] for _ in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    Tree[a].append([b, c])
A, B = map(int, input().split())

# 저장할 path 생성
path = [[] for _ in range(N+1)]
# Dijkstra Algorithm
import heapq
Cities = []

for i in range(1,N+1):
    Cities.append(i)

visited_cities = [A]
def dijkstra(Tree, start):
    # 우선은 무한값으로 값을 정함(최솟값을 구하기 위함)
    distances = {node: float('inf') for node in Cities}
    # 시작하는 곳의 값은 0으로 만듦.
    distances[start] = 0
    # 빈 queue를 생성
    queue = []
    # heapq를 이용해 queue에 시작 장소를 정함.
    heapq.heappush(queue, [distances[start], start])
    while queue:
        # 탐색을 시작할 노드와 거리를 가져옴.
        current_distance, current_destination = heapq.heappop(queue)
        # 새로운 곳으로 가는 곳이 지금 가고 있는 거리보다 멀다면, 갈 필요도 없음.
        if distances[current_destination] < current_distance:
            continue
        # 우선 가는 길에 자기 자신(통과하고 있는 곳)을 추가함
        path[current_destination].append(current_destination)
        # 새로운 목적지와 거리를 가져옴
        for new_destination, new_distance in Tree[current_destination]:
            # 해당 노드를 향해 지금까지의 거리 + 새로운 거리를 계산
            distance = current_distance + new_distance
            # 지금까지의 최솟값보다 작으면 갱신
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                # 갱신할 때 깊은 복사를 통해서 다음 목적지까지 가는 루트를 내가 거쳐온 길로 복사함.
                path[new_destination] = copy.deepcopy(path[current_destination])
                # 다음 값을 위해 heapq를 이용해 queue에 새롭게 집어 넣음.
                heapq.heappush(queue, [distance, new_destination])
    return distances

print(dijkstra(Tree, A).get(B))
print(len(path[B]))
for i in path[B]:
    print(i, end=' ')