n, k = map(int, input().split())

coin = []
for i in range(n):
    coin.append(int(input()))

count = 0

for i in range(n-1, 0, -1):
    count += k // coin[i]
    k %= coin[i]

print(count)