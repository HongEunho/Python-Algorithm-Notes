import sys
t = int(input())

for i in range(t):
    n = int(input())
    arr = []
    for j in range(n):
        score = list(map(int, input().split()))
        arr.append(score)
    arr.sort(key=lambda x:x[0])
    cnt = 1
    great = arr[0][1]
    for j in range(1, n):
        if great > arr[j][1]:
            great = arr[j][1]
            cnt+=1
    print(cnt)