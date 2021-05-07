from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(board, dir):
    n = len(board)
    price = [[int(1e9)] * n for _ in range(n)]
    price[0][0] = 0

    queue = deque()
    queue.append((0, 0, 0, dir))  # (시작X, 시작Y, 시작Cost, 시작방향)

    while queue:
        x, y, c, z = queue.popleft()

        if x == n - 1 and y == n - 1:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = i

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] == 1:
                continue

            if nz == z:
                nc = c + 100
            else:
                nc = c + 600

            if nc < price[nx][ny]:
                price[nx][ny] = nc
                queue.append((nx, ny, nc, i))

    return price[-1][-1]


def solution(board):
    answer = min(bfs(board, 0), bfs(board, 2))
    return answer

