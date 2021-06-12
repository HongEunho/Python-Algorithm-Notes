from collections import deque

n, k = map(int, input().split())
visited = [0]*100001

queue = deque()
queue.append(n)

while queue:
    v = queue.popleft()
    if v == k:
        print(visited[v])
        break
    for nx in (v-1, v+1, v*2):
        if nx < 0 or nx > 100000 or visited[nx] > 0:
            continue
        visited[nx] = visited[v]+1
        queue.append(nx)

