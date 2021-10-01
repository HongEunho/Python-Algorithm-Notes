import math


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def isGold(x):
    for i in range(2, x//2):
        a = x-i
        

t = int(input())

for i in range(t):
    n = int(input())
