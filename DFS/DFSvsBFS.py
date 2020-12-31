from collections import deque

n,m,v = map(int,input().split())
graph = [[0]*m for _ in range(n)]
visited = [False]*n

for i in range(m):
    a, b = map(int,input().split())
    graph[a-1][b-1] = graph[b-1][a-1] = 1

def DFS(v):
    visited[v] = True
    print(v+1, end=' ')

    for i in range(n):
        if graph[v][i]==1 and not visited[i]:
            DFS(i)



DFS(v-1)