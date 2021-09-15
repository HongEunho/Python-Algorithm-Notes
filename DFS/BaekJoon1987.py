r, c = map(int, input().split())

graph = []
myList = []
visited = [[False] * c for _ in range(r)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
myCount = []


def dfs(x, y, count):
    if x < 0 or x >= r or y < 0 or y >= c:
        return False

    elif visited[x][y]:
        return False

    else:
        go = [0, 0, 0, 0]  # 동서남북
        count += 1
        myCount.append(count)
        myList.append(graph[x][y])
        visited[x][y] = True
        print(x, y)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < r and 0 <= ny < c) and (graph[nx][ny] not in myList):
                go[i] = 1  # 해당 방향으로는 가도 됨

        for i in range(4):
            if go[i] == 1:
                nx = x + dx[i]
                ny = y + dy[i]
                myList.append(graph[nx][ny])
                dfs(nx, ny, count)
        return True


for i in range(r):
    graph.append(list(input()))

dfs(0, 0, 0)

print(max(myCount))
print(myList)
