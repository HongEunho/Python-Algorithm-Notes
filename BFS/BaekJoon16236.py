from collections import deque

n = int(input())
graph = []
second = 0

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

for i in range(n):
    graph.append(list(map(int, input().split())))


def find_babyShark():
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 9:
                return i, j


def check_possible(size):
    for i in range(n):
        for j in range(n):
            if 0 < graph[i][j] < size:
                return True
    return False


def bfs(a, b, ss):
    global second
    queue = deque()
    queue.append((a, b, ss, 0, 0))  # x, y, 상어크기, 먹은갯수, 시간

    while True:
        queue = deque()
        queue.append((a, b, 0))
        visited = [[False]*n for _ in range(n)]
        while queue:
            x, y, cnt = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                

    while queue:
        x, y, size, eat, sec = queue.popleft()
        graph[x][y] = 0
        print("%d %d %d" % (x, y, size))
        if not check_possible(size):
            second = sec
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] > size:
                continue
            if graph[nx][ny] == size:
                queue.append((nx, ny, size, eat, sec + 1))
            elif graph[nx][ny] < size:
                if graph[nx][ny] == 0:
                    queue.append((nx, ny, size, eat, sec + 1))
                elif eat + 1 >= size:
                    queue.append((nx, ny, size + 1, 0, sec + 1))
                else:
                    queue.append((nx, ny, size, eat + 1, sec + 1))


sx, sy = find_babyShark()
graph[sx][sy] = 0
bfs(sx, sy, 2)
print(second)
