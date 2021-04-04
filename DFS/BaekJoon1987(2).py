from collections import deque
import sys
sys.setrecursionlimit(100000)

r, c = map(int, input().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
graph = []
count = 1

def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))

    while queue:
        a, b, alpha = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if graph[nx][ny] in alpha:
                continue

            queue.append((nx, ny, alpha+graph[nx][ny]))
            print(queue)
            global count
            count = max(count, len(alpha)+1)
            print(count)


for i in range(r):
    graph.append(list(input()))

bfs(0, 0, graph[0][0])
print(count)