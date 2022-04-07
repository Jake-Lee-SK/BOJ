import sys
sys.stdin = open('input.txt')
import heapq
INF = float('INF')
def dijkstra(S):
    queue = []
    heapq.heappush(queue, (0, S))
    distance[S] = 0
    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(queue, (cost, next[0]))

V, E = map(int, input().split())
S = int(input())
graph = [[] for _ in range(V+1)]
for i in range(E):
    A, B, C = map(int, input().split())
    graph[A].append([B, C])
distance = [INF]*(V+1)

dijkstra(S)

for i in range(1, V+1):
    if distance[i] != INF:
        print(distance[i])
    else:
        print('INF')


