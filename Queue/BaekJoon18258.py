from collections import deque
import sys

n = int(input())

queue = deque()
for i in range(n):
    comm = sys.stdin.readline().strip().split()
    flag = comm[0]

    if flag == 'push':
        queue.append(comm[1])
    elif flag == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif flag == 'size':
        print(len(queue))
    elif flag == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif flag == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif flag == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])