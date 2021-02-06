#Floyd-Warshall algorithm(플로이드-워셜 알고리즘)
inf = int(1e9)

n = int(input())
m = int(input())

graph = [[inf]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    graph[a][a] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

print()
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == inf:
            print("INF", end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
