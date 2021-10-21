from collections import deque

n, m = map(int, input().split())
graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[False]*n for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, input().split())))

def find_group(a, b):
    if graph[a][b] == -1:
        return 0


    queue = deque()
    queue.append((a, b))
    visited[a][b] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                continue
            if graph[nx][ny] == -1:
                continue
            