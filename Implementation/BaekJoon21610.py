from collections import deque

n, m = map(int, input().split())
board = []
rain = [[0] * n for _ in range(n)]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

for i in range(n):
    board.append(list(map(int, input().split())))

cloud = deque([(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)])


def raining(dir, dist):
    queue = deque()
    while cloud:
        a, b = cloud.popleft()
        nx = (a + dx[dir] * dist) % n
        ny = (b + dy[dir] * dist) % n
        board[nx][ny] += 1
        rain[nx][ny] = 1  # 사라진 칸은 1 표시
        queue.append((nx, ny))

    while queue:
        a, b = queue.popleft()
        for i in range(1, 8, 2):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] > 0:
                board[a][b] += 1

    for i in range(n):
        for j in range(n):
            if rain[i][j] == 1:
                rain[i][j] = 0
                continue
            if board[i][j] >= 2:
                cloud.append((i, j))
                board[i][j] -= 2


for i in range(m):
    d, s = map(int, input().split())
    raining(d - 1, s)

answer = 0
for i in range(n):
    answer += sum(board[i])

print(answer)
