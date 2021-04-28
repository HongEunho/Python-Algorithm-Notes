import math
n = int(input())

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

def isPalindrome(x):
    xs = str(x)
    xsr = xs[::-1]
    if xs == xsr:
        return True
    else:
        return False

start = n
while True:
    if isPalindrome(start) and isPrime(start):
        print(start)
        break
    else:
        start+=1