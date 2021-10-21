from collections import deque

n = int(input())
like = [[] for _ in range(n*n)]
queue = deque()

for i in range(n*n):
    a, b, c, d, e = map(int, input().split())
    queue.append(a-1)
    like[a-1] = [b-1, c-1, d-1, e-1]

graph = [[-1]*n for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(n*n):
    i = queue.popleft()
    num1 = []
    max_cnt1 = 0
    for j in range(n):
        for k in range(n):
            if graph[j][k] != -1:
                continue
            cnt = 0
            x, y = j, k
            for u in range(4):
                nx = x + dx[u]
                ny = y + dy[u]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if graph[nx][ny] in like[i]:
                    cnt += 1

            if cnt == max_cnt1:
                num1.append((j, k))
            elif cnt > max_cnt1:
                while num1:
                    num1.pop()
                num1.append((j, k))
                max_cnt1 = cnt

    if len(num1) == 1:
        graph[num1[0][0]][num1[0][1]] = i
        continue

    num2 = []
    max_cnt2 = 0
    for a, b in num1:
        cnt = 0
        for u in range(4):
            nx = a + dx[u]
            ny = b + dy[u]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == -1:
                cnt += 1

        if cnt == max_cnt2:
            num2.append((a, b))
        elif cnt > max_cnt2:
            while num2:
                num2.pop()
            num2.append((a, b))
            max_cnt2 = cnt

    if len(num2) == 1:
        graph[num2[0][0]][num2[0][1]] = i
        continue

    num2.sort(key=lambda w: w[1])
    num2.sort(key=lambda w: w[0])
    graph[num2[0][0]][num2[0][1]] = i

answer = 0
for i in range(n):
    for j in range(n):
        stud = graph[i][j]
        cnt = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] in like[stud]:
                cnt += 1

        if cnt > 0:
            answer += 10**(cnt-1)

print(answer)
