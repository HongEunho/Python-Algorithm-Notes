import heapq
n = int(input())
slime = list(map(int, input().split()))
queue = []

for i in range(n):
    heapq.heappush(queue, -slime[i])

score = 0
while len(queue) > 1:
    a = -heapq.heappop(queue)
    b = -heapq.heappop(queue)
    print(a, end=' ')
    print(b, end=' ')
    score += a*b
    heapq.heappush(queue, a+b)

print(score)