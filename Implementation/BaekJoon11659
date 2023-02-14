import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
pre = [0]
mysum = 0

for i in range(n):
  mysum += nums[i]
  pre.append(mysum)


for i in range(m):
  a, b = map(int, input().split())
  print(pre[b] - pre[a-1])
