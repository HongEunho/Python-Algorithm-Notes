n, k = map(int, input().split())

d = [[0]*(k+1) for _ in range(n+1)]

for i in range(k+1):
    d[0][i] = 1

for i in range(1, n+1):
    for j in range(1, k+1):
        d[i][j] = d[i][j-1] + d[i-1][j]
        d[i][j] %= 1000000000

print(d[n][k])