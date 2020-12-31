from collections import deque

n,m = map(int,input().split())
graph=[]
visited = [[False]*m for _ in range(n)]

count = 1

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(n):
    graph.append(list(map(int,input())))

def BFS(x,y):
    queue = deque([(x,y)])
    visited[x][y]=True

    while queue:
        a, b = queue.popleft()
        print(a,b)
        for i in range(len(dx)):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[a][b]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(BFS(0,0))


