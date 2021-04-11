n, l = map(int, input().split())
fix = list(map(int, input().split()))
fix.sort()

if l == 1:
    print(n)

else:
    cnt = 1
    cur = fix[0] + l/2 - 0.5

    for i in range(1, n):
        if cur+l/2 < fix[i]+0.5:
            cnt += 1
            cur = fix[i] + l/2 - 0.5
    print(cnt)