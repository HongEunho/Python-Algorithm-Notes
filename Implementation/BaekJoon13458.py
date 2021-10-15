import math
n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

ans = 0
for i in a:
    tmp = i - b
    if tmp > 0:
        tmp2 = math.ceil(tmp / c)
        ans = ans + tmp2 + 1
    else:
        ans += 1

print(ans)