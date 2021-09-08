n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

minCost = cost[0]
result = 0

for i in range(n-1):
    if minCost > cost[i]:
        minCost = cost[i]
    result += minCost * dist[i]

print(result)