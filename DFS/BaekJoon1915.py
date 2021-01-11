n,m = map(int,input().split())
graph = []


for i in range(n):
    graph.append(list(map(int, input())))

ans = 0
for i in range(1, n):
    for j in range(1, m):
        if graph[i][j] == 1:
            graph[i][j] += min(graph[i-1][j-1], graph[i][j-1], graph[i-1][j])
        ans = max(ans, graph[i][j])

if ans == 0 and graph[0][0] == 1:
    print(1)
else:
    print(ans**2)



