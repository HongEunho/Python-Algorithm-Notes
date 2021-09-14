t = int(input())

for i in range(t):
    n = int(input())
    count0, count1= 0, 0
    if n == 0:
        print("1 0")
    elif n == 1:
        print("0 1")

    else:
        dp0 = [0]*(n+1)
        dp0[0] = 1

        dp1 = [0]*(n+1)
        dp1[1] = 1

        for j in range(2, n+1):
            dp0[j] = dp0[j-1]+dp0[j-2]
            dp1[j] = dp1[j-1]+dp1[j-2]

        print("%d %d" % (dp0[n], dp1[n]))