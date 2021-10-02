import math

r = float(input())

def euclid(r):
    return math.pi * r * r

def taxi(r):
    return r*r + r*r

print(euclid(r))
print(taxi(r))