from collections import deque

n = int(input())
graph = []
graphIdx = deque()
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
d_left = [(-1, 0, 0.01), (1, 0, 0.01), (-1, -1, 0.07), (1, -1, 0.07), (-2, -1, 0.02), (2, -1, 0.02), (-1, -2, 0.10),
          (1, -2, 0.10), (0, -3, 0.05), (0, -2, 0)]
d_right = [(-1, 0, 0.01), (1, 0, 0.01), (-1, 1, 0.07), (1, 1, 0.07), (-2, 1, 0.02), (2, 1, 0.02), (-1, 2, 0.10),
           (1, 2, 0.10), (0, 3, 0.05), (0, 2, 0)]
d_up = [(0, -1, 0.01), (0, 1, 0.01), (-1, -1, 0.07), (-1, 1, 0.07), (-1, -2, 0.02), (-1, 2, 0.02), (-2, -1, 0.10),
        (-2, 1, 0.10), (-3, 0, 0.05), (-2, 0, 0)]
d_down = [(0, -1, 0.01), (0, 1, 0.01), (1, -1, 0.07), (1, 1, 0.07), (1, -2, 0.02), (1, 2, 0.02), (2, -1, 0.10),
          (2, 1, 0.10), (3, 0, 0.05), (2, 0, 0)]

for i in range(n):
    graph.append(list(map(int, input().split())))


def indexing():
    x, y = n // 2, n // 2
    depth = 0

    while True:
        for i in range(4):
            if i % 2 == 0:
                depth += 1
            for j in range(depth):
                graphIdx.append((x, y, i))
                if x == 0 and y == 0:
                    return
                x += dx[i]
                y += dy[i]


def tornado(x, y, d):
    global answer

    nx = x + dx[d]
    ny = y + dy[d]
    tmp = graph[nx][ny]
    graph[nx][ny] = 0

    outSand = 0
    total = 0

    if d == 0:
        dir = d_left
    elif d == 1:
        dir = d_down
    elif d == 2:
        dir = d_right
    else:
        dir = d_up

    for i in range(9):
        ddx = dir[i][0]
        ddy = dir[i][1]
        ratio = dir[i][2]

        if x + ddx < 0 or x + ddx >= n or y + ddy < 0 or y + ddy >= n:
            outSand += int(tmp * ratio)
            answer += int(tmp * ratio)
            continue
        else:
            graph[x + ddx][y + ddy] += int(tmp * ratio)
            total += int(tmp * ratio)

    if x + dir[9][0] < 0 or x + dir[9][0] >= n or y + dir[9][1] < 0 or y + dir[9][1] >= n:
        answer += (tmp - total - outSand)
    else:
        graph[x + dir[9][0]][y + dir[9][1]] += (tmp - total - outSand)


answer = 0
indexing()
while graphIdx:
    x, y, d = graphIdx.popleft()
    if x == 0 and y == 0:
        break
    tornado(x, y, d)

print(answer)
