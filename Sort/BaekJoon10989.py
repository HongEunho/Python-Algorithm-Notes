import sys
n = int(input())

array = [0] * 10001
for i in range(n):
    tmp = int(sys.stdin.readline())
    array[tmp] += 1


for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)
