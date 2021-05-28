from collections import deque

n, m, v = map(int, input().split())

graph = [[0]*n for _ in range(n)]
visited = [False]*n

for i in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = graph[b-1][a-1] = 1

def DFS(v):
    visited[v] = True
    print(v+1, end=' ')

    for i in range(n):
        if not visited[i] and graph[v][i] == 1:
            DFS(i)

def BFS(v):
    visited[v] = False
    queue = deque()
    queue.append(v)

    while queue:
        a = queue.popleft()
        print(a+1, end=' ')

        for i in range(n):
            if visited[i] and graph[a][i] == 1:
                queue.append(i)
                visited[i] = False

DFS(v-1)
print()
BFS(v-1)