n = int(input())
graph = [[" "] * n for _ in range(n)]


def recursive(n):
    if n == 3:
        graph[0][:3] = graph[2][:3] = ["*", "*", "*"]
        graph[1][:3] = ["*", " ", "*"]
        return

    div = n // 3
    recursive(div)

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(div):
                graph[div*i + k][div*j : div*(j+1)] = graph[k][:div]


recursive(n)

for i in range(n):
    for j in range(n):
        print(graph[i][j], end='')
    print()