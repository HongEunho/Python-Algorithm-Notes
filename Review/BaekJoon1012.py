from collections import deque

t = int(input())

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return


for i in range(t):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    for j in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    cnt = 0
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1:
                bfs(graph, x, y)
                cnt += 1
    print(cnt)



