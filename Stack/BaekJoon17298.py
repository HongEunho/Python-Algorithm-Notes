import sys
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
stack = []
for i in range(len(A)-1, 0, -1):
    stack.append(A[i])

for i in range(n-1):




for i in range(n-1):
    flag = 0
    for j in range(i+1, n):
        if A[i] < A[j]:
            flag = 1
            print(A[j], end=' ')
            break
    if flag == 0:
        print("-1", end=' ')
print("-1")
