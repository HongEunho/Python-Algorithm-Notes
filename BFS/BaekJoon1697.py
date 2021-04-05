from collections import deque
import copy

n, k = map(int, input().split())
visited = [False] * 100001
count = 0
flag = 0

def bfs():
    global count
    today_queue = copy.deepcopy(queue)

    while today_queue:
        x = today_queue.popleft()
        queue.popleft()
        if x == k:
            global flag
            flag = 1
            return
        for i in range(3):
            if i == 0:
                nx = x + 1
            elif i == 2:
                nx = x - 1
            else:
                nx = x * 2
            if nx < 0 or nx > 100000:
                continue
            if not visited[nx]:
                queue.append(nx)
                visited[nx] = True

    count += 1


queue = deque()
queue.append(n)
visited[n] = True

while queue:
    bfs()
    if flag == 1:
        print(count)
        break