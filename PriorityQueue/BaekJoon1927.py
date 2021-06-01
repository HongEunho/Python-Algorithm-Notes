import heapq

n = int(input())
q = []
for i in range(n):
    a = int(input())
    if a > 0:
        heapq.heappush(q, a)
    else:
        if not q:
            print(0)
        else:
            b = heapq.heappop(q)
            print(b)
