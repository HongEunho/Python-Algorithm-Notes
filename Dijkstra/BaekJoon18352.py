import heapq
import sys

INF = int(1e9)
n, m, k, x = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

dijkstra(x)
flag = 0
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        flag = 1

if flag == 0:
    print(-1)
