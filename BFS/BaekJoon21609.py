from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

def find_group(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        