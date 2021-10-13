from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(input()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(ra, rb, ba, bb):
    queue = deque()
    queue.append((ra, rb, ba, bb))

    while queue:
        rx, ry, bx, by = queue.popleft()
        for i in range(4):
            while True:
                nrx = rx+dx[i]
                nry = ry+dy[i]
                nbx = bx+dx[i]
                nby = by+dy[i]
                if nrx < 0 or nrx >= n or nry < 0 or nry >= m:
                    break
                if graph[nx][ny] == 'O':


rx, ry, bx, by = 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            rx = i, ry = j
        if graph[i][j] == 'B':
            bx = i, by = j

bfs(rx, ry, bx, by)