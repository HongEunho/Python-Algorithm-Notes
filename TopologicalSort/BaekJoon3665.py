import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    team = list(map(int, sys.stdin.readline().rstrip().split()))
    m = int(sys.stdin.readline())
    for j in range(m):
        