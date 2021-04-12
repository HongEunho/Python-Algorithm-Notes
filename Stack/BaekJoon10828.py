import sys
n = int(input())
stack = []
for i in range(n):
    comm = sys.stdin.readline().strip()
    if comm[:4] == "push":
        stack.append(comm[5:])
    elif comm == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif comm == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif comm == "size":
        print(len(stack))
    elif comm == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

