from itertools import combinations

n = int(input())
graph = []
number = [i for i in range(n)]

minR = int(1e9)

for i in range(n):
    graph.append(list(map(int, input().split())))


for c in combinations(number, n//2):
    visited = [False] * n
    team1 = []
    team2 = []
    for i in c:
        visited[i] = True
        team1.append(i)

    for i in range(n):
        if not visited[i]:
            team2.append(i)

    sum1 = 0
    sum2 = 0
    for i in range(n//2):
        for j in range(n//2):
            if graph[team1[i]][team1[j]] != 0:
                sum1 += graph[team1[i]][team1[j]]
            if graph[team2[i]][team2[j]] != 0:
                sum2 += graph[team2[i]][team2[j]]

    if abs(sum1-sum2) < minR:
        minR = abs(sum1-sum2)

print(minR)