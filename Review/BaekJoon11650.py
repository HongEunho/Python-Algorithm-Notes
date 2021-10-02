import sys
n = int(input())

coor = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    coor.append((x, y))

coor.sort(key=lambda x:x[1])
coor.sort(key=lambda x:x[0])

for i in range(n):
    print("%d %d" %(coor[i][0], coor[i][1]))