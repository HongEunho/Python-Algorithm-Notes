from collections import deque

n = int(input())

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

for i in range(n):
    l = int(input())

    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    graph = [[0] * l for _ in range(l)]
    graph[sx][sy] = 1

    queue = deque()
    queue.append((sx, sy))

    while queue:
        x, y = queue.popleft()

        if x == ex and y == ey:
            print(graph[x][y] - 1)
            break

        for j in range(8):
            nx = x+dx[j]
            ny = y+dy[j]

            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue

            if graph[nx][ny] > 0:
                continue

            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))


