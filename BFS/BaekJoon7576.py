from collections import deque
import copy

m, n = map(int, input().split())
graph = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

count = 0
pre_queue = deque()
flag = 0 # 다 퍼질 수 있는지 없는지 체크

for i in range(n):
    graph.append(list(map(int, input().split())))


def find_start():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                pre_queue.append((i, j))


def bfs():
    global count
    day_queue = copy.deepcopy(pre_queue)

    while day_queue:
        x, y = day_queue.popleft()
        pre_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                pre_queue.append((nx, ny))
    count += 1


find_start() #시작점을 찾고
while pre_queue: #토마토 퍼뜨리기를 수행한 후에
    bfs()

for i in graph:
    if 0 in i:
        flag = 1

if flag == 1:
    print(-1)
else:
    print(count-1) #마지막좌표에서 하나를 더 세주기 때문에 -1


