from itertools import combinations


p, n, h = map(int,input().split())

pc = [[]*n for _ in range(p)]
result = [[]*1 for _ in range(p)]

for i in range(n):
    a, b = map(int, input().split())
    pc[a-1].append(b)

maxPc = 0

for i in range(p):
    for j in range(len(pc[i])):
        tmp = list(combinations(pc[i], j))
        for k in range(len(tmp)):
            if maxPc <= sum(tmp[k]) <= h:
                maxPc = sum(tmp[k])

    result[i] = maxPc

for i in range(p):
    print(i+1, end=' ')
    print(result[i]*1000)
