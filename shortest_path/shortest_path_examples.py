#'미래 도시' 문제
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for t in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][t] + graph[t][b])

cost1 = graph[1][k]
cost2 = graph[k][x]

if cost1 == INF or cost2 == INF:
    print(-1)
else:
    print(cost1 + cost2)

------------------------------------------------------------------------------

#'전보' 문제
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    s, e, v = map(int, input().split())
    graph[s].append((e, v))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        c, now = heapq.heappop(q)
        if distance[now] < c:
            continue

        for line in graph[now]:
            cost = c + line[1]

            if cost < distance[line[0]]:
                distance[line[0]] = cost
                heapq.heappush(q, (cost, line[0]))

dijkstra(c)

total_num = 0
total_cost = 0
for d in distance:
    if d != INF:
        total_num += 1
        total_cost = max(total_cost, d)

print(total_num-1, total_cost)
