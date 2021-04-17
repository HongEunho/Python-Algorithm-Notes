import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
pick = list(map(int, sys.stdin.readline().split()))

queue = deque([i for i in range(1, n+1)])
cnt = 0


while pick:
    if queue[0] == pick[0]:
        queue.popleft()
        del pick[0]
    else:
        if queue.index(pick[0]) > len(queue) / 2:
            while queue[0] != pick[0]:
                queue.appendleft(queue.pop())
                cnt += 1
        else:
            while queue[0] != pick[0]:
                queue.append(queue.popleft())
                cnt += 1

print(cnt)

