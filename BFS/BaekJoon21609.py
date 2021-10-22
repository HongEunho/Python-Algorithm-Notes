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
    if graph[a][b] == -1 or graph[a][b] == -2:
        return
    if graph[a][b] > 0:
        myColor = graph[a][b]
    else:
        myColor = 0
    cnt = 1
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True
    while queue:
        x, y = queue.popleft()
        groupQ.append((x, y))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                continue
            if graph[nx][ny] == -1 or graph[nx][ny] == -2:
                continue
            if graph[nx][ny] > 0:
                if myColor == 0:
                    myColor = graph[nx][ny]
                elif myColor != graph[nx][ny]:
                    continue
            cnt += 1
            queue.append((nx, ny))
            visited[nx][ny] = True

    if cnt < 2:
        return

    global groupCnt, maxQ

    if cnt > groupCnt:
        groupCnt = cnt
        maxQ = groupQ
    elif cnt == groupCnt:
        thisZeroCnt, maxZeroCnt = 0, 0
        for i in range(cnt):
            if graph[groupQ[i][0]][groupQ[i][1]] == 0:
                thisZeroCnt += 1
        for i in range(groupCnt):
            if graph[maxQ[i][0]][maxQ[i][1]] == 0:
                maxZeroCnt += 1
        if thisZeroCnt == maxZeroCnt:
            groupQ.sort(key=lambda x: x[1])
            groupQ.sort(key=lambda x: x[0])
            maxQ.sort(key=lambda x: x[1])
            maxQ.sort(key=lambda x: x[0])
            gx, gy, mx, my = 0, 0, 0, 0
            for i in range(cnt):
                if graph[groupQ[i][0]][groupQ[i][1]] != 0:
                    gx = groupQ[i][0]
                    gy = groupQ[i][1]
                    break
            for i in range(groupCnt):
                if graph[maxQ[i][0]][maxQ[i][1]] != 0:
                    mx = maxQ[i][0]
                    my = maxQ[i][1]
                    break

            if gx > mx:
                maxQ = groupQ
            elif gx == mx:
                if gy > my:
                    maxQ = groupQ

        elif thisZeroCnt > maxZeroCnt:
            maxQ = groupQ

    return


def gravity():
    for i in range(n-2, -1, -1):
        for j in range(n):
            if graph[i][j] != -1:
                tmp = i
                while tmp + 1 < n and graph[tmp+1][j] == -2:
                    graph[tmp+1][j] = graph[tmp][j]
                    graph[tmp][j] = -2
                    tmp += 1


def rotate():
    newGraph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            newGraph[n - 1 - j][i] = graph[i][j]
    return newGraph


answer = 0

while True:
    groupCnt = 0
    maxQ = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                find_group(i, j)
    if not maxQ:
        break
    answer += len(maxQ)**2
    for x, y in maxQ:
        graph[x][y] = -2
    gravity()
    graph = rotate()
    gravity()
print(answer)
