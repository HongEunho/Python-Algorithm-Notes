import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, k = map(int, sys.stdin.readline().rstrip().split())
    d = list(map(int, sys.stdin.readline().rstrip().split()))
    graph = [[] for _ in range(n + 1)]
    inDegree = [0 for _ in range(n + 1)]
    dp = [0 for _ in range(n + 1)]
    queue = deque()

    for i in range(k):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append(b)
        inDegree[b] += 1

    w = int(sys.stdin.readline().rstrip())

    for i in range(1, n + 1):
        if inDegree[i] == 0:
            queue.append(i)
            dp[i] = d[i - 1]

    while queue:
        tmp = queue.popleft()

        for i in graph[tmp]:
            inDegree[i] -= 1
            dp[i] = max(dp[i], dp[tmp] + d[i - 1])
            if inDegree[i] == 0:
                queue.append(i)

    print(dp[w])
