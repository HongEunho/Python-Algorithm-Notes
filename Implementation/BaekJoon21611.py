from collections import deque

n, m = map(int, input().split())
graph = []
cmd = []
score = [0]*3

def indexing():
    x, y = n // 2, n // 2
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    depth = 0

    while True:
        for i in range(4):
            if i % 2 == 0:
                depth += 1
            for j in range(depth):
                x += dx[i]
                y += dy[i]
                graphIdx.append((x, y))
                if x == 0 and y == 0:
                    return


def magic(dir, dist):
    x, y = n // 2, n // 2
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(dist):
        x += dx[dir]
        y += dy[dir]
        if x < 0 or x >= n or y < 0 or y >= n:
            break
        graph[x][y] = 0

    fill_blank()
    while bomb():
        fill_blank()
    grouping()


def fill_blank():
    blankIdx = deque()
    for x, y in graphIdx:
        if graph[x][y] == 0:
            blankIdx.append((x, y))
        elif graph[x][y] > 0 and blankIdx:
            nx, ny = blankIdx.popleft()
            graph[nx][ny] = graph[x][y]
            graph[x][y] = 0
            blankIdx.append((x, y))


def bomb():
    visited = deque()
    cnt = 0
    num = -1
    flag = False
    for x, y in graphIdx:
        if num == graph[x][y]:
            visited.append((x, y))
            cnt += 1
        else:
            if cnt >= 4:
                score[num-1] += cnt
                flag = True

            while visited:
                nx, ny = visited.popleft()
                if cnt >= 4:
                    graph[nx][ny] = 0

            num = graph[x][y]
            cnt = 1
            visited.append((x, y))

    return flag


def grouping():
    cnt = 1
    tmpx, tmpy = graphIdx[0]
    num = graph[tmpx][tmpy]
    nums = []

    for i in range(1, len(graphIdx)):
        x, y = graphIdx[i][0], graphIdx[i][1]
        if num == graph[x][y]:
            cnt += 1
        else:
            nums.append(cnt)
            nums.append(num)
            num = graph[x][y]
            cnt = 1

    idx = 0
    for x, y in graphIdx:
        if not nums:
            break
        graph[x][y] = nums[idx]
        idx += 1
        if idx == len(nums):
            break

for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(m):
    d, s = map(int, input().split())
    cmd.append((d, s))

graphIdx = deque()
indexing()

for a, b in cmd:
    magic(a-1, b)

answer = 0
for i in range(3):
    answer += (i+1) * score[i]

print(answer)