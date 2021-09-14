n, k = map(int, input().split())

bag = []
d = [[0]*k for _ in range(n)]

for i in range(n):
    bag.append(list(map(int, input().split())))

print(bag)

for i in range(n):
    for j in range(k):
        w = bag[i][0]
        v = bag[i][1]

        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j - w] + v)