import math

x = [0]*1000001
x[0] = 1

for i in range(1, 1000001):
    rootX = math.floor(i-math.sqrt(i))
    lnX = int(math.log(i, math.e))
    sinX = int(i*math.sin(i)*math.sin(i))

    x[i] = int((x[rootX] + x[lnX] + x[sinX]) % 1000000)


while True:
    i = int(input())
    if i == -1:
        break

    print(x[i])


