from collections import deque

n = int(input())
m = int(input())
count = 0

graph = [[0]*n for _ in range(n)]
visited = [False]*n

for i in range(m):
    a, b = map(int,input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

queue = deque()
queue.append(0)
visited[0] = True

while queue:
    v = queue.popleft()

    for i in range(n):
        if graph[v][i] == 1 and not visited[i]:
            queue.append(i)
            visited[i] = True
            count += 1

print(count)