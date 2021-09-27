import heapq

n = int(input())
first = list(map(int, input().split()))

queue = []
flag = 0

for i in range(n):
    heapq.heappush(queue, first[i])

for i in range(1, n+1):
    if i != heapq.heappop(queue):
        print(i)
        flag = 1
        break

if flag == 0:
    print(n+1)