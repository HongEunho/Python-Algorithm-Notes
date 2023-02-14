import sys

input = sys.stdin.readline
s = list(input().rstrip())
n = int(input().rstrip())

cList = [[0] * len(s) for _ in range(26)]

for i in range(len(s)):
  cList[ord(s[i])-ord('a')][i] += 1

for i in range(26):
  for j in range(1, len(s)):
    cList[i][j] += cList[i][j-1]

for i in range(n):
  a, l, r = input().split()
  tmp = cList[ord(a)-ord('a')][int(r)] - cList[ord(a)-ord('a')][int(l)]

  if s[int(l)] == a:
    tmp+=1
    
  print(tmp)
