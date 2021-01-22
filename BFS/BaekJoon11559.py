from collections import deque

graph = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

result = 0


def bfs(a, b, c):
    queue = deque()
    queue.append((a, b))

    pang = deque()
    pang.append((a, b))

    visited = [[False] * 6 for _ in range(12)]
    visited[a][b] = True
    count = 1
    flag = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > 11 or ny < 0 or ny > 5:
                continue
            if graph[nx][ny] == c and not visited[nx][ny]:
                queue.append((nx, ny))
                pang.append((nx, ny))
                visited[nx][ny] = True
                count += 1

    if count >= 4:
        flag = 1

        for x, y in pang:
            graph[x][y] = "."

    return flag


def gravity():
    for y in range(6):
        queue = deque()
        for x in range(11, -1, -1):
            if graph[x][y] != '.':
                queue.append(graph[x][y])
        for x in range(11, -1, -1):
            if queue:
                graph[x][y] = queue.popleft()
            else:
                graph[x][y] = '.'


for i in range(12):
    graph.append(list(input()))


while True:
    chk = 0
    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.':
                chk += bfs(i, j, graph[i][j])

    if chk == 0:
        print(result)
        break
    else:
        result += 1
    gravity()

# 처음에는 result를 bfs함수 안에서 global 변수로 선언하여
# 팡이 될 때 마다 +1을 해주는 방식으로 하였는데
# 이렇게 해주면, 동시에 두 뿌요가 터지는 경우에도 두 개를 카운트를 해 준다.
# 하지만 문제에서, 동시에 여러개의 뿌요가 터질 때는 한 번 카운트를 해주라고 명시했기 때문에
# bfs 함수 안이 아닌, 바깥에서 +1을 해주는 방식으로 변경하였다. 이렇게 하니 정답이 나온다.