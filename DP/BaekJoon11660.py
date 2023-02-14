import sys

input = sys.stdin.readline
n, m = map(int, input().split())

graph = []

for i in range(n):
  graph.append(list(map(int, input().split())))

acc = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(1, n+1):
    acc[i][j] = acc[i-1][j] + acc[i][j-1] - acc[i-1][j-1] + graph[i-1][j-1]

print(acc)

for i in range(m):
  x1,y1,x2,y2 = map(int, input().split())

  print(acc[x2][y2] - acc[x1-1][y2] - acc[x2][y1-1] + acc[x1-1][y1-1])
