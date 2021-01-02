com = int(input())
n = int(input())
visited = [False] * (com + 1)

graph = [[0] * (com + 1) for _ in range(com + 1)]
count = 0

for i in range(n):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1


def DFS(start):
    visited[start] = True

    for i in range(1, com + 1):
        if graph[start][i] == 1 and not visited[i]:
            global count
            count += 1
            DFS(i)


DFS(1)
print(count)
