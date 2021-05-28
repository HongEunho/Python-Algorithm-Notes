import sys
sys.setrecursionlimit(100000)

n = int(input())
graph = []
ans = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x, y, i):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] > i and not visited[x][y]:
        visited[x][y] = True
        for k in range(4):
            dfs(x+dx[k], y+dy[k], i)
        return True


for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(max(map(max, graph))):
    cnt = 0
    visited = [[False]*n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if not visited[x][y] and dfs(x, y, i):
                cnt += 1

    ans = max(ans, cnt)

print(ans)