from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(input()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]


def roll(x, y, direct):
    cnt = 0

    while graph[x + dx[direct]][y + dy[direct]] != '#' and graph[x][y] != 'O':
        x += dx[direct]
        y += dy[direct]
        cnt += 1

    return x, y, cnt


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
            nrx, nry, rcnt = roll(rx, ry, i)
            nbx, nby, bcnt = roll(bx, by, i)

            if graph[nbx][nby] != 'O':
                if graph[nrx][nry] == 'O':
                    print(cnt)
                    exit(0)

                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

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
