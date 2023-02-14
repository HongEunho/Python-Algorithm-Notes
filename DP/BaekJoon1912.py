n = int(input())
nums = list(map(int, input().split()))

INF = -int(1e9)
dp = [INF]*n

if n<2:
  dp[0] = nums[0]

else:
  dp[0] = nums[0]
  dp[1] = max(nums[1], dp[0]+nums[1])
  for i in range(2, n):
    dp[i] = max(dp[i-1]+nums[i], nums[i])

print(max(dp))
