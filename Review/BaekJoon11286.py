import sys
import heapq

n = int(input())
queue = []

for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    if a != 0:
        heapq.heappush(queue, (abs(a), a))
    else:
        if not queue:
            print(0)
        else:
            print(heapq.heappop(queue)[1])

