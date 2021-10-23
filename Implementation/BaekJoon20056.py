from collections import deque

n, m, k = map(int, input().split())
graph = [[deque() for _ in range(n)] for _ in range(n)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
fireball = deque()

for i in range(m):
    r, c, m, s, d = map(int, input().split())
    fireball.append([r-1, c-1])
    graph[r-1][c-1].append(deque([m, s, d]))

for _ in range(k):
    for j in range(len(fireball)):
        r, c = fireball.popleft()
        m, s, d = graph[r][c].popleft()
        nr = (r + s*dx[d]) % n
        nc = (c + s*dy[d]) % n
        graph[nr][nc].append(deque([m, s, d]))

    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) > 1:
                sum_m, sum_s, odd_d, even_d, cnt = 0, 0, 0, 0, 0
                while graph[i][j]:
                    m, s, d = graph[i][j].popleft()
                    sum_m += m
                    sum_s += s
                    cnt += 1
                    if d % 2 == 0:
                        even_d += 1
                    else:
                        odd_d += 1
                sum_m //= 5
                if sum_m == 0:
                    continue
                sum_s //= cnt
                if even_d == cnt or odd_d == cnt:
                    dir = [0, 2, 4, 6]
                else:
                    dir = [1, 3, 5, 7]
                for d in range(4):
                    fireball.append([i, j])
                    graph[i][j].append(deque([sum_m, sum_s, dir[d]]))
            elif len(graph[i][j]) == 1:
                fireball.append([i, j])

answer = 0
for i in range(n):
    for j in range(n):
        answer += sum(arr[0] for arr in graph[i][j])

print(answer)