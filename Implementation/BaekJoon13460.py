from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(input()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def redBall(x, y, direct):
    nx = x + dx[direct]
    ny = y + dy[direct]
    while True:
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            break
        if graph[nx][ny] == '#':
            break
        if graph[nx][ny] == 'O':
            graph[x][y] = '.'
            return -1, -1
        if graph[nx][ny] == 'B':
            bx, by = blueBall(nx, ny, direct)
            if bx == nx and by == ny:
                graph[x][y] = '.'
                graph[nx-dx[direct]][ny - dy[direct]] = 'R'
                return nx - dx[direct], ny - dy[direct]
            if bx == -1 and by == -1:
                print(-1)
                exit(0)

        nx = nx + dx[direct]
        ny = ny + dy[direct]

    graph[x][y] = '.'
    graph[nx - dx[direct]][ny - dy[direct]] = 'R'

    return nx - dx[direct], ny - dy[direct]


def blueBall(x, y, direct):
    nx = x + dx[direct]
    ny = y + dy[direct]
    while True:
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            break
        if graph[nx][ny] == '#':
            break
        if graph[nx][ny] == 'O':
            return -1, -1
        if graph[nx][ny] == 'R':
            rx, ry = redBall(nx, ny, direct)
            if rx == nx and ry == ny:
                graph[x][y] = '.'
                graph[nx - dx[direct]][ny - dy[direct]] = 'B'
                return nx - dx[direct], ny - dy[direct]

        nx = nx + dx[direct]
        ny = ny + dy[direct]

    graph[x][y] = '.'
    graph[nx-dx[direct]][ny-dy[direct]] = 'B'

    return nx - dx[direct], ny - dy[direct]


def bfs(ra, rb, ba, bb):
    queue = deque()
    queue.append((ra, rb, ba, bb, 0))
    res = 0
    while queue:
        rx, ry, bx, by, cnt = queue.popleft()
        if cnt > 10:
            print(-1)
            exit(0)

        for i in range(4):
            nrx, nry = redBall(rx, ry, i)
            nbx, nby = blueBall(bx, by, i)
            if nrx == -1 and nry == -1:
                if nbx == -1 and nby == -1:
                    print(-1)
                    exit(0)
                else:
                    print(cnt + 1)
                    exit(0)
            queue.append((nrx, nry, nbx, nby, cnt+1))

        res = cnt
    return res

rx, ry, bx, by = 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            rx = i
            ry = j
        if graph[i][j] == 'B':
            bx = i
            by = j

print(bfs(rx, ry, bx, by))
