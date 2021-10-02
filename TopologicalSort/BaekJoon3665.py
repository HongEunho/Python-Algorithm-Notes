from collections import deque
import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())

    graph = [[] for _ in range(n + 1)]
    inDegree = [0 for _ in range(n + 1)]
    queue = deque()
    answer = []
    flag = 0

    team = list(map(int, sys.stdin.readline().rstrip().split()))

    for j in range(n - 1):
        for k in range(j + 1, n):
            graph[team[j]].append(team[k])
            inDegree[team[k]] += 1

    m = int(sys.stdin.readline())
    for j in range(m):
        first, second = map(int, sys.stdin.readline().rstrip().split())
        flag = True

        for k in graph[first]:
            if k == second:
                graph[first].remove(second)
                inDegree[second] -= 1
                graph[second].append(first)
                inDegree[first] += 1
                flag = False

        if flag:
            graph[second].remove(first)
            inDegree[first] -= 1
            graph[first].append(second)
            inDegree[second] += 1

    for j in range(1, n + 1):
        if inDegree[j] == 0:
            queue.append(j)

    if not queue:
        print("IMPOSSIBLE")
        continue

    result = True
    while queue:
        if len(queue) > 1:
            result = False
            break

        tmp = queue.popleft()
        answer.append(tmp)
        for j in graph[tmp]:
            inDegree[j] -= 1
            if inDegree[j] == 0:
                queue.append(j)
            elif inDegree[j] < 0:
                result = False
                break

    if not result or len(answer) < n:
        print("IMPOSSIBLE")
    else:
        print(*answer)
