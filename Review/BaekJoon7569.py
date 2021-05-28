from collections import deque

m, n, h = map(int, input().split())
graph = [[] for _ in range(h)]

dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

queue = deque()


def find_start():
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 1:
                    queue.append((i, j, k))


def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
                continue
            if graph[nx][ny][nz] == 0:
                graph[nx][ny][nz] = graph[x][y][z] + 1
                queue.append((nx, ny, nz))


def print_result():
    cnt = -1

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 0:
                    print(-1)
                    return
                cnt = max(cnt, graph[i][j][k])

    if cnt == 1:
        print(0)
        return
    else:
        print(cnt-1)
        return


for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int, input().split())))

find_start()
bfs()
print_result()
