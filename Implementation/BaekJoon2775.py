t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    graph = [[0]*n for _ in range(k+1)]

    graph[0] = [i+1 for i in range(n)]

    for i in range(1, k+1):
        for j in range(n):
            graph[i][j] = sum(graph[i-1][:j+1])

    print(graph[k][n-1])