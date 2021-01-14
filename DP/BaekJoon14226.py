from collections import deque

n = int(input())
graph = [[-1] * 1001 for _ in range(1001)]  # screen * clipboard로 구성된 그래프


def bfs(a, b):
    queue = deque()
    queue.append((a, b))

    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()

        if graph[x][x] == -1:  # 화면->클립보드로 복사
            graph[x][x] = graph[x][y] + 1  # 복사 후는 복사 전 + 1 카운트
            queue.append((x, x))

        if x + y <= n and graph[x + y][y] == -1:  # 붙여넣기
            graph[x + y][y] = graph[x][y] + 1  # 붙여넣으면 화면+클립보드가 화면이 됨
            queue.append((x + y, y))

        if x - 1 >= 0 and graph[x - 1][y] == -1:  # 삭제
            graph[x - 1][y] = graph[x][y] + 1  # 삭제하면 삭제전 + 1 카운트
            queue.append((x - 1, y))


bfs(1, 0)
ans = min([i for i in graph[n] if i != -1])

print(ans)