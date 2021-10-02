n = int(input())

k = 2
while n > 1:
    if n % k == 0:
        print(k)
        n /= k
        k = 2
    else:
        k += 1
