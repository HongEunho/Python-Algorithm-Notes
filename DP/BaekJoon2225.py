n, k = map(int, input().split())

d = [[0]*(k+1) for _ in range(n+1)]
for i in range(1, n):
    for j in range(1, k+1):
        for k in range(i):
            