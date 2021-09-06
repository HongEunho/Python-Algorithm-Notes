n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1

    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)