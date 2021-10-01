import math


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def goldPartition(x):
    result = []
    for i in range(2, x//2+1):
        if isPrime(i) and isPrime(x-i):
            if not result:
                result.append(i)
                result.append(x-i)
            else:
                if result[1]-result[0] > x - 2*i:
                    result[0] = i
                    result[1] = x-i

    return result


t = int(input())

for i in range(t):
    n = int(input())
    ans = goldPartition(n)

    print(*ans)

