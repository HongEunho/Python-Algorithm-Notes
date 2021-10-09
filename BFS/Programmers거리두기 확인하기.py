from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(candidate, place):
    queue = deque()
    visited = [[False] * 5 for _ in range(5)]
    queue.append(candidate)
    cnt = 0

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            if visited[nx][ny]:
                continue
            if place[nx][ny] == 'X':
                continue
            if place[nx][ny] == 'P':
                return False
            queue.append((nx, ny))

        cnt += 1
        if cnt == 2:
            return True
    return True


def solution(places):
    answer = []

    for place in places:
        candidates = deque()
        flag = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    candidates.append((i, j))

        for candidate in candidates:
            if not bfs(candidate, place):
                flag = False
                break

        if not flag:
            answer.append(0)
        else:
            answer.append(1)

    return answer