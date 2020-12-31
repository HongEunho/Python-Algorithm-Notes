N, M = map(int, input().split())
graph = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
count = 0

for i in range(N):
    graph[i] = list(map(int, input()))


def DFS(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if not visited[x][y] and graph[x][y] == 0:
        visited[x][y] = True
        DFS(x + 1, y)
        DFS(x - 1, y)
        DFS(x, y + 1)
        DFS(x, y - 1)
        return True
    return False


for i in range(N):
     for j in range(M):
         if DFS(i, j):
             count += 1

print(count)
print(graph)
