from collections import deque

n = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def bfs(a, b):
    cnt = 1
    graph[a][b] = 0
    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                cnt += 1

    return cnt


cnt = 0
numList = []

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            cnt += 1
            num = bfs(i, j)
            numList.append(num)
            numList.sort()

print(cnt)

for i in numList:
    print(i)
