n = int(input())
num = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

mymax = int(1e9)
mymin = int(-1e9)

for i in range(n):
    