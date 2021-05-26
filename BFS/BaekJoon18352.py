import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
visited[x] = True

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

queue = deque()
queue.append((x, 0))

ans = []
while queue:
    town, cnt = queue.popleft()
    if cnt == k:
        ans.append(town)
    elif cnt < k:
        for i in graph[town]:
            if not visited[i]:
                visited[i] = True
                queue.append((i, cnt+1))

if not ans:
    print(-1)
else:
    ans.sort()
    for answer in ans:
        print(answer)