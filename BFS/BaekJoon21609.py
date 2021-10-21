from collections import deque

n, m = map(int, input().split())
graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    graph.append(list(map(int, input().split())))


def find_group(a, b):
    visited = [[False] * n for _ in range(n)]
    groupQ = []
    if graph[a][b] == -1:
        return []
    cnt = 1
    myColor = 0
    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        groupQ.append((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] > 0:
                if myColor == 0:
                    myColor = graph[nx][ny]
                elif myColor != graph[nx][ny]:
                    continue
            cnt += 1
            queue.append((nx, ny))

    if cnt < 2:
        return []

    global groupCnt
    if cnt > groupCnt:


    groupCnt = max(groupCnt, cnt)

    return groupQ


def gravity():
    for i in range(n):
        for j in range(n - 2, -1, -1):
            if graph[i][j] >= 0:
                tmp = j
                while tmp + 1 < n and graph[i][tmp+1] == -2:
                    graph[i][tmp+1] = graph[i][tmp]
                    graph[i][tmp] = -2
                    tmp += 1



groupCnt = 0
answer = 0

for i in range(n):
    for j in range(n):
        groupQ = find_group(i, j)
        if groupQ:
            while groupQ:
                a, b = groupQ.pop()
                graph[a][b] = -2
            gravity()
