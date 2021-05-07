from collections import deque

n, m, v = map(int, input().split())
graph = [[]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

def dfs(graph, visited, v):
    visited[v] = True
    print(v, end=' ')

    for i in range(len(graph[v])):
        if not visited[graph[v][i]]:
            dfs(graph, visited, graph[v][i])

def bfs(graph, visited, v):
    queue = deque()
    queue.append(v)
    visited[v] = False

    while queue:
        cur = queue.popleft()
        print(cur, end=' ')
        for i in range(len(graph[cur])):
            if visited[graph[cur][i]]:
                queue.append(graph[cur][i])
                visited[graph[cur][i]] = False



dfs(graph, visited, v)
print()
bfs(graph, visited, v)