import sys
sys.stdin = open('input.txt')
V, E = map(int, input().split())

# 부모 테이블을 초기화

parent = [i for i in range(V+1)]

# find 연산

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# union 연산

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

# 간선 정보를 담을 리스트와 최소 신장 트리 계산 변수 정의
edges = [list(map(int, input().split())) for _ in range(E)]
total_cost = 0

edges.sort(key=lambda x: (x[2]))

# 간선 정보 하나씩 확인하면서 크루스칼 알고리즘 수행
for a, b, cost in edges:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        total_cost += cost

print(total_cost)