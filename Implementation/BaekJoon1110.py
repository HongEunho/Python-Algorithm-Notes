n = input()
tmp = n

if int(n) < 10:
    tmp = "0" + n

cnt = 0
while True:
    cnt += 1

    second = str(int(tmp[0]) + int(tmp[-1]))[-1]
    first = tmp[-1]

    ans = first + second

    if int(ans) == int(n):
        print(cnt)
        break
    else:
        tmp = ans
