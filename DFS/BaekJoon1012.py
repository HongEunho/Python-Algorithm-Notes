import sys
sys.setrecursionlimit(100000)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
count = 0


def DFS(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(4):
            DFS(x + dx[i], y + dy[i])
        return True

    return False


t = int(input())

for i in range(t):
    n, m, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for i in range(n):
        for j in range(m):
            if DFS(i, j):
                count += 1

    print(count)
    count = 0
