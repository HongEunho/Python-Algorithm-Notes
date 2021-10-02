import math

n = int(input())
numList = list(map(int, input().split()))

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

cnt = 0
for num in numList:
    if isPrime(num):
        cnt += 1

print(cnt)