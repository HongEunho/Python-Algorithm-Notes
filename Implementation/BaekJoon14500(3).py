n, m = map(int, input().split())
board = []
visited = [[False] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    board.append(list(map(int, input().split())))

answer = 0


def dfs(x, y, mysum, depth):
    global answer

    if depth == 3:
        answer = max(answer, mysum)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
                continue

            if depth == 1:  # ㅗ 모양은 DFS로 만들 수 없으므로 예외처리
                visited[nx][ny] = True
                dfs(x, y, mysum + board[nx][ny], depth + 1)
                visited[nx][ny] = False

            visited[nx][ny] = True
            dfs(nx, ny, mysum + board[nx][ny], depth + 1)
            visited[nx][ny] = False


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, board[i][j], 0)
        visited[i][j] = False

print(answer)