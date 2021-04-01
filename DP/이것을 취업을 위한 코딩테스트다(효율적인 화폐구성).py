n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m+1)

d[0] = 0

for i in range(n):
    for j in range(array[i], m+1):
        d[j] = min(d[j - array[i]] + 1, d[j])

if d[m] == 10001:
    print(-1)
else:
    print(d[m])