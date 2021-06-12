import sys
import heapq

n, m = map(int, input().split())
card = list(map(int, input().split()))

heapq.heapify(card)

for i in range(m):
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    heapq.heappush(card, a+b)
    heapq.heappush(card, a+b)

print(sum(card))