import sys
sys.setrecursionlimit(100000)
n, m, k = map(int, input().split()) # n = 5 / m = 7

graph = [[0] * n for _ in range(m)] # 7 x 5

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

count = 0
size = 0
size_list=[]

def dfs(x, y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        global size
        size += 1
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        return True
    return False


for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[x][y] = 1


for i in range(n):  # 5
    for j in range(m):  # 7
        if dfs(j, i):
            count += 1
            size_list.append(size)
            size=0

size_list.sort()
print(count)

for i in range(len(size_list)):
    print(size_list[i],end=' ')

