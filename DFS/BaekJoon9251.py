a=input()
b=input()
lenA = len(a)
lenB = len(b)
graph = [[0]*(lenB+1) for _ in range(lenA+1)]

for i in range(1, lenA+1):
    for j in range(1, lenB+1):
        if a[i-1] == b[j-1]:
            graph[i][j] = graph[i-1][j-1] + 1
        else:
            graph[i][j] = max(graph[i-1][j], graph[i][j-1])

print(graph[-1][-1])