# 12시부터 시계방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def dfs(x, y, n, m, graph):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(8):
            dfs(x + dx[i], y + dy[i], n, m, graph)
        return True

    return False

count = 0

while True:
    a, b = map(int, input().split()) #a=5 b=4 4x5
    if a == 0 and b == 0:
        break

    graph = []
    for i in range(b):
        graph.append(list(map(int, input().split())))

    for i in range(b):
        for j in range(a):
            if dfs(i, j, b, a, graph):
                count += 1
    print(count)
    count=0


