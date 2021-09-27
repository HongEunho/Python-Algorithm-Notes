n = int(input())
graph = [[' '] * 2 * n for _ in range(n)]


def recursive(x, y, N):
    if N == 3:
        graph[x][y] = '*'
        graph[x + 1][y - 1] = graph[x + 1][y + 1] = '*'
        for i in range(-2, 3):
            graph[x + 2][y + i] = '*'
    else:
        nextN = N // 2
        recursive(x, y, nextN)
        recursive(x + nextN, y - nextN, nextN)
        recursive(x + nextN, y + nextN, nextN)


recursive(0, n - 1, n)
for i in graph:
    print("".join(i))
