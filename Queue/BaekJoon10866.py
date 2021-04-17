from collections import deque
import sys

n = int(input())

queue = deque()
for i in range(n):
    comm = sys.stdin.readline().strip().split("_")
    flag = comm[0]

    if flag == 'push':
        com2 = comm[1].split()
        if com2[0] == "front":
            queue.appendleft(com2[1])
        else:
            queue.append(com2[1])
    elif flag == 'pop':
        if not queue:
            print(-1)
        else:
            if comm[1] == "front":
                print(queue.popleft())
            else:
                print(queue.pop())
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