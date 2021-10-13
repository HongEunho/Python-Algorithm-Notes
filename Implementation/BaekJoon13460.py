from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(input()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]

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
    queue.append((ra, rb, ba, bb, 1))
    visited[ra][rb][ba][bb] = True

    while queue:
        rx, ry, bx, by, cnt = queue.popleft()
        if cnt > 10:
            print(-1)
            exit(0)

        for i in range(4):
            nrx, nry = redBall(rx, ry, i)
            nbx, nby = blueBall(bx, by, i)

            if nbx != -1 and nby != -1:
                if nrx == -1 and nry == -1:
                    print(cnt)
                    exit(0)

            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                queue.append((nrx, nry, nbx, nby, cnt+1))

    print(-1)
    return

rx, ry, bx, by = 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            rx = i
            ry = j
        if graph[i][j] == 'B':
            bx = i
            by = j

bfs(rx, ry, bx, by)
