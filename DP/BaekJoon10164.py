n, m, k = map(int, input().split())
dp = [[0] * m for _ in range(n)]

if k == 0:
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    print(dp[n - 1][m - 1])

else:
    x = (k - 1) // m
    y = (k - 1) % m

    for i in range(x + 1):
        for j in range(y + 1):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    for i in range(x, n):
        for j in range(y, m):
            if i == x and j == y:
                continue
            if i == x:
                dp[i][j] = 1
            elif j == y:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    print(dp[x][y] * dp[n - 1][m - 1])
