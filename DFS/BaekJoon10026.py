import sys
sys.setrecursionlimit(100000)

n = int(input())
graph = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[False] * n for _ in range(n)]
for i in range(n):
    graph.append(list(input()))


def dfs(x, y, color):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if not visited[x][y] and graph[x][y] == color:
        visited[x][y] = True

        for i in range(4):
            dfs(x + dx[i], y + dy[i], color)

        return True
    return False


def dfs2(x, y, color):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if visited[x][y]:
        if color == 'R' or color == 'G':
            if graph[x][y] != 'B':

                visited[x][y] = False

                for i in range(4):
                    dfs2(x + dx[i], y + dy[i], color)
                return True
            return False

        else:
            if graph[x][y] == color:
                visited[x][y] = False

                for i in range(4):
                    dfs2(x + dx[i], y + dy[i], color)
                return True
            return False


count1 = 0
count2 = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j] and dfs(i, j, graph[i][j]):
            count1 += 1

for i in range(n):
    for j in range(n):
        if visited[i][j] and dfs2(i, j, graph[i][j]):
            count2 += 1

print(count1, end=' ')
print(count2)

# 첫 번째 방법은 dfs와 dfs2를 만들고 dfs한바퀴돌고 dfs2실행
# 두 번째 방법은 dfs와 dfs2를 한번에 돌 되, visited를 두 개 생성.
