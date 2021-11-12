n, m = map(int, input().split())

a = []
b = []

for i in range(n):
    a.append(list(map(int, input().split())))

m, k = map(int, input().split())
c = [[0]*k for _ in range(n)]
for i in range(m):
    b.append(list(map(int, input().split())))

for i in range(n):
    for j in range(k):
        for z in range(m):
            c[i][j] += a[i][z] * b[z][j]

for i in range(n):
    for j in c[i]:
        print(j, end=' ')
    print()