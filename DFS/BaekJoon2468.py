import sys

sys.setrecursionlimit(10000)

n = int(input())

graph = []
num_list = set()
max_high = 0  # 임시 최댓값 높이

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, k):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] > k and not visited[x][y]:
        visited[x][y] = True
        for i in range(4):
            dfs(x + dx[i], y + dy[i], k)
        return True

    return False


count_list = []

for i in range(n):
    a = list(map(int, input().split()))
    graph.append(a)
    num_list.update(a)

for i in num_list:
    count = 0
    visited = [[False] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if not visited[x][y] and dfs(x, y, i):
                count += 1
    count_list.append(count)

max_count = max(count_list)

if max_count == 0:
    print(1)
else:
    print(max_count)
