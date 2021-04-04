import sys

r, c = map(int, input().split())
graph = []
myStep = [0]*26
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
count = 0


def dfs(x, y, incnt):
    if x < 0 or x >= r or y < 0 or y >= c:
        return False
    global count
    count = max(incnt, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < r and 0 <= ny < c) and not myStep[ord(graph[nx][ny]) - ord('A')]:
            myStep[ord(graph[nx][ny]) - ord('A')] = 1
            dfs(nx, ny, incnt + 1)
            myStep[ord(graph[nx][ny]) - ord('A')] = 0


for i in range(r):
    graph.append(list(sys.stdin.readline().strip()))

myStep[ord(graph[0][0]) - ord('A')] = 1
dfs(0, 0, 1)
print(count)
