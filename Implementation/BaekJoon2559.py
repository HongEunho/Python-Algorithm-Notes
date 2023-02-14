import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
pre = [0]
tmp_sum = []
mysum = 0

for i in range(n):
  mysum += nums[i]
  pre.append(mysum)


for i in range(n-m+1):
  tmp_sum.append(pre[i+m] - pre[i])

print(max(tmp_sum))
