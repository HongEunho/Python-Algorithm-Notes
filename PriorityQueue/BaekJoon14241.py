import heapq
n = int(input())
slime = list(map(int, input().split()))

slime.sort()

score = 0
while len(slime) > 1:
    a = slime.pop()
    b = slime.pop()

    score += a*b
    heapq.heappush(slime, a+b)



print(score)