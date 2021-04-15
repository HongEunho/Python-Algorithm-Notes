n = int(input())

cur = 1
plus = 6
circle = 1
if n == 1:
    print(1)
else:
    while True:
        cur += plus
        circle += 1
        if n <= cur:
            print(circle)
            break
        plus += 6