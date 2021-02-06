#Dijkstra's algorithm(다익스트라 알고리즘)
import heapq
import sys
input = sys.stdin.readline
inf = int(1e9)

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
distance = [inf]*(v+1)

for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        c, node = heapq.heappop(q)
        if distance[node] < c:
            continue

        for edge in graph[node]:
            cost = distance[node] + edge[1]

            if distance[edge[0]] > cost:
                distance[edge[0]] = cost
                heapq.heappush(q, (cost, edge[0]))

dijkstra(start)

for i in range(1, v+1):
    if distance[i] == inf:
        print("INFINITY")
    else:
        print(distance[i])
