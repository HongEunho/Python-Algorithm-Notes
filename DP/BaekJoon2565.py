n = int(input())
lists = []
dp = [1]*n

for i in range(n):
  a, b = map(int, input().split())
  lists.append([a, b])

lists.sort()

for i in range(1, n):
  for j in range(0, i):
    if lists[j][1] < lists[i][1]:
      dp[i] = max(dp[i], dp[j]+1)
      
print(n-max(dp))
