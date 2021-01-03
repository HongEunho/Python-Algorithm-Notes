import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1


def dfs(v):
    visited[v] = True

    for i in range(n + 1):
        if graph[v][i] == 1 and not visited[i]:
            dfs(i)

    return True


count = 0
for i in range(1, n + 1):
    if not visited[i]:
        if dfs(i):
            count += 1

print(count)
