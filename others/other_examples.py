#'팀 결성' 문제
n, m = map(int, input().split())
team = [0]*(n+1)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(1, n+1):
    team[i] = i

for _ in range(m):
    key, a, b = map(int, input().split())
    if key == 0:
        union(team, a, b)
    else:
        if find_parent(team, a) == find_parent(team, b):
            print("YES")
        else:
            print("NO")

--------------------------------------------------------------

#'도시 분할 계획' 문제
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
edges = []
parent = [0]*(n+1)
for i in range(1,n+1):
    parent[i] = i

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

result = 0
maxcost = 0
for edge in edges:
    if find_parent(parent, edge[1]) != find_parent(parent, edge[2]):
        union(parent, edge[1], edge[2])
        result += edge[0]
        maxcost = edge[0]

print(result - maxcost)

-------------------------------------------------------------------------

#'커리큘럼' 문제
from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
times = [0] * (n+1)
result = [0] * (n+1)
indegree = [0] * (n+1)

for i in range(1, n+1):
    line = list(map(int, input().split()))
    times[i] = line[0]

    idx = 1
    while line[idx] != -1:
        graph[line[idx]].append(i)
        indegree[i] += 1
        idx += 1

q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        result[i] = times[i]

while q:
    now = q.popleft()

    for node in graph[now]:
        indegree[node] -= 1
        result[node] = max(result[now] + times[node], result[node])
        if indegree[node] == 0:
            q.append(node)

for data in result[1:]:
    print(data)
