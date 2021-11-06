n = int(input())
stairs = []
dp = [0]*301
for i in range(n):
    stairs.append(int(input()))

if n > 2:
    dp[0] = stairs[0]
    dp[1] = stairs[0]+stairs[1]
    dp[2] = max(stairs[0] + stairs[2], stairs[1]+stairs[2])
elif n > 1:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
elif n == 1:
    dp[0] = stairs[0]

for i in range(3, n):
    dp[i] = max(stairs[i] + stairs[i-1] + dp[i-3], stairs[i]+ dp[i-2])

print(dp[n-1])