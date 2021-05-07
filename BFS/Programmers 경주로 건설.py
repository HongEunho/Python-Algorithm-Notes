from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def samedir(a, b):
    if (a==0 or a==1) and (b==2 or b==3):
        return 600
    elif (a==2 or a == 3) and (b==0 or b==1):
        return 600
    else:
        return 100

def bfs(board, sx, sy, sz, n):
    price = [[int(1e9)] * n for _ in range(n)]
    price[0][0] = 0

    result = []

    queue = deque()
    queue.append((sx, sy, sz))

    while queue:
        x, y, z = queue.popleft()

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

            if z == 5:
                cost = price[x][y] + 100
            else:
                cost = price[x][y] + samedir(z, nz)

            if cost < price[nx][ny]:
                price[nx][ny] = cost
                queue.append((nx, ny, i))

    return price[-1][-1]


def solution(board):
    n = len(board)
    answer = bfs(board, 0, 0, 5, n)
    return answer

print(solution([[0, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 1, 1, 1, 1],
[1, 1, 1, 1, 0, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 1, 1, 1, 1],
[0, 1, 0, 1, 1, 1, 1, 1, 1],
[0, 1, 0, 0, 0, 1, 1, 1, 1],
[0, 1, 1, 1, 0, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 1, 1, 1, 1],
[1, 1, 1, 1, 0, 0, 0, 0, 0]]))