from collections import deque
import copy

m, n, h = map(int, input().split())
graph = [[] for _ in range(h)]

dx = [0,0,0,0,1,-1]
dy = [0,0,1,-1,0,0]
dz = [1,-1,0,0,0,0]

next_queue = deque()
count = 0
flag = 0

for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int, input().split())))

def find_start():
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 1:
                    next_queue.append((i, j, k))

def bfs():
    global count
    today_queue = copy.deepcopy(next_queue)

    while today_queue:
        x, y, z = today_queue.popleft()
        next_queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
                continue
            if graph[nx][ny][nz] == 0:
                graph[nx][ny][nz] = 1
                next_queue.append((nx, ny, nz))
    count += 1


find_start()
while next_queue:
    bfs()

for i in range(h):
    for j in range(n):
        if 0 in graph[i][j]:
            flag = 1

if flag == 1:
    print(-1)
else:
    print(count-1)