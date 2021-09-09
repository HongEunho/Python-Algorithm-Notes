n, l = map(int, input().split())
pos = list(map(int, input().split()))
pos.sort()

start = pos[0] - 0.5
result = 1

if l == 1:
    print(n)

else:
    for i in range(1, n):
        tmp = start + l
        if tmp < pos[i] + 0.5:
            result += 1
            start = pos[i] - 0.5

    print(result)
