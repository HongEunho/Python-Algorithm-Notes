import heapq
import sys

n = int(input())
q = []
for i in range(n):
    a = int(sys.stdin.readline())
    if a > 0:
        heapq.heappush(q, a)
    else:
        if not q:
            print(0)
        else:
            b = heapq.heappop(q)
            print(b)
