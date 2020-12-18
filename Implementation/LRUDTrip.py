import sys

n = int(input())
a = list(sys.stdin.readline().rstrip().split())

pos = [1, 1]

for i in range(len(a)):
    if a[i] == 'R':
        if (pos[1] + 1) < n:
            pos[1] += 1
    elif a[i] == 'L':
        if (pos[1] - 1) > 1:
            pos[1] -= 1
    elif a[i] == 'U':
        if (pos[0] - 1) > 1:
            pos[0] -= 1
    elif a[i] == 'D':
        if (pos[0] + 1) < n:
            pos[0] += 1

print(pos[0],pos[1])
