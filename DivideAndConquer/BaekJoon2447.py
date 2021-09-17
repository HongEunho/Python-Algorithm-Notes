n = int(input())
graph = [["*"] * n for _ in range(n)]


def recursive(n):
    if n == 3:
        graph[1][2] = " "
        return

    m = n // 3
    recursive(m)

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(m):
                graph[m*i+k][m*j:m*(j+1)] = graph[k][:m]


recursive(n)
print(graph)
