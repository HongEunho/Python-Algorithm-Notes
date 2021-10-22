from collections import deque

n, m = map(int, input().split())
graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    graph.append(list(map(int, input().split())))

def find_group(a, b, color):
    queue = deque()
    queue.append([a, b])

    block_cnt, zero_cnt = 1, 0
    blocks = [[a, b]]
    zeros = []

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                continue

            if graph[nx][ny] == color:
                visited[nx][ny] = True
                queue.append([nx, ny])
                block_cnt += 1
                blocks.append([nx, ny])

            elif graph[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append([nx, ny])
                block_cnt += 1
                zeros.append([nx, ny])
                zero_cnt += 1

    for x, y in zeros:
        visited[x][y] = False

    return [block_cnt, zero_cnt, blocks + zeros]

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
    visited = [[False]*n for _ in range(n)]
    maxQ = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0 and not visited[i][j]:
                visited[i][j] = True
                block = find_group(i, j, graph[i][j])
                if block[0] >= 2:
                    maxQ.append(block)
    print(maxQ)
    maxQ.sort(reverse=True)

    if not maxQ:
        break
    answer += maxQ[0][0]**2
    for x, y in maxQ[0][2]:
        graph[x][y] = -2
    gravity()
    graph = rotate()
    gravity()
    print(graph)
print(answer)