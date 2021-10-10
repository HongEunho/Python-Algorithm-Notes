t = int(input())
possible1 = [2, 3, 4, 5, 6, 7]
possible2 = [7, 6, 5, 4, 3, 2]

for _ in range(t):
    n = int(input())

    dp = [[0]*2 for _ in range(101)]
    dp[2][0], dp[2][1] = 1, 1
    dp[3][0], dp[3][1] = 7, 7
    dp[4][0], dp[4][1] = 4, 11
    dp[5][0], dp[5][1] = 2, 71
    dp[6][0], dp[6][1] = 6, 111
    dp[7][0], dp[7][1] = 8, 711

    if n < 8:
        print("%d %d" %(dp[n][0], dp[n][1]))
        continue

    for i in range(8, n+1):
        minR = 9999999999999999
        for j in possible2:
            if dp[i-j][0] != 0:
                if j == 6:
                    if minR > int(str(dp[i-j][0]) + "0"):
                        minR = int(str(dp[i-j][0]) + "0")

                else:
                    if minR > int(str(dp[i-j][0]) + str(dp[j][0])):
                        minR = int(str(dp[i-j][0]) + str(dp[j][0]))

        dp[i][0] = minR

    for i in range(8, n+1):
        for j in possible1:
            if dp[i-j][1] != 0:
                dp[i][1] = int(str(dp[i-j][1]) + str(dp[j][1]))
                break

    print("%d %d" %(dp[n][0], dp[n][1]))


