from collections import deque
import copy

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = 0


def bfs():

    tmp_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                queue.append((nx, ny))

    cnt = 0
    for i in tmp_graph:
        cnt += i.count(0)
    global answer
    answer = max(answer, cnt)


def select_wall(count):
    if count == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                select_wall(count + 1)
                graph[i][j] = 0


n, m = map(int, input().split())
graph = []
queue = deque()
for i in range(n):
    graph.append(list(map(int, input().split())))
select_wall(0)
print(answer)
