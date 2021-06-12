from collections import deque

price = []

def bfs(n, start, end, roads, traps, cost, visited):
    queue = deque()
    queue.append(start)

    while queue:
        v = queue.popleft()
        for i in range(len(roads)):
            if roads[i][0] == v:
                a = roads[i][1]
                cost[a-1] = cost[v-1] + roads[i][2]

                if a == end:
                    price.append(cost[a-1])


def dfs(n, start, end, roads, traps, cost, visited):
    visited[start-1] = True

    for i in range(len(roads)):
        if roads[i][0] == start:
            a = roads[i][1] # 다음 갈 곳
            if a in traps or not visited[a-1]:
                visited[a-1]=True
                cost[a - 1] = cost[start - 1] + roads[i][2]
                print("방문순서", end=' ')
                print(a)

                if a == end:
                    price.append(cost[a - 1])
                    return
                else:
                    if a in traps:
                        for j in range(len(roads)):
                            roads[j][0], roads[j][1] = roads[j][1], roads[j][0]
                    dfs(n, a, end, roads, traps, cost, visited)

                    if a in traps:
                        for j in range(len(roads)):
                            roads[j][0], roads[j][1] = roads[j][1], roads[j][0]

            else:
                return

def solution(n, start, end, roads, traps):
    answer = 0

    visited = [False] * n

    cost = [0] * n

    for i in range(len(roads)):
        if roads[i][0] == start:
            dfs(n, start, end, roads, traps, cost, visited)

    print(price)

    return answer


solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])
# solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2])
