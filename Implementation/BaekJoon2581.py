import math

m = int(input())
n = int(input())

answer = []

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

for i in range(m, n+1):
    if isPrime(i):
        answer.append(i)

if not answer:
    print("-1")
else:
    print(sum(answer))
    print(answer[0])