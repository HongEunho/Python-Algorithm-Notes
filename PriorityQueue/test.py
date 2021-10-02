import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())

answer = []
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)


def popElement(num):
    while graph[num]:
        next = heapq.heappop(graph[num])

        if not visited[next]:
            popElement(next)
            visited[next] = True
            answer.append(next)


for i in range(m):
    first, second = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(graph[second], first)

for i in range(1, n + 1):
    if not visited[i]:
        popElement(i)

    if not visited[i]:
        visited[i] = True
        answer.append(i)


print(" ".join(map(str, answer)))
