n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 1

for i in range(n):
    board.append(list(map(int, input().split())))


def dfs(x, y, depth):
    global answer, d
    if depth == 4:
        nx = x + dx[(d - 2) % 4]
        ny = y + dy[(d - 2) % 4]
        if board[nx][ny] == 2:
            dfs(nx, ny, 0)
        else:
            print(answer)
            exit(0)

    nx = x + dx[(d - 1) % 4]
    ny = y + dy[(d - 1) % 4]

    if board[nx][ny] == 0:
        board[nx][ny] = 2
        answer += 1
        d = (d - 1) % 4
        dfs(nx, ny, 0)

    elif board[nx][ny] == 1 or board[nx][ny] == 2:
        d = (d - 1) % 4
        dfs(x, y, depth + 1)


board[r][c] = 2
dfs(r, c, 0)
