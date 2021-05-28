import sys

n, m = map(int, input().split())
graph = []
visited = [0]*26

dx = [0,0,1,-1]
dy = [1,-1,0,0]

cnt = 0

def dfs(x, y, incnt):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    global cnt
    cnt = max(cnt, incnt)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if visited[ord(graph[nx][ny]) - ord('A')] == 1:
            continue
        visited[ord(graph[nx][ny]) - ord('A')] = 1
        dfs(nx, ny, incnt+1)
        visited[ord(graph[nx][ny]) - ord('A')] = 0

for i in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))

visited[ord(graph[0][0]) - ord('A')] = 1
dfs(0,0,1)

print(cnt)

