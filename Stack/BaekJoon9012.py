import sys
t = int(input())
for i in range(t):
    count = 0
    stack = list(sys.stdin.readline().strip())
    flag = 0
    while len(stack) > 0:
        bracket = stack.pop()
        if bracket == ")":
            count += 1
        elif bracket == "(":
            if count == 0:
                print("NO")
                flag = 1
                break
            count -= 1
    if flag == 0:
        if count == 0:
            print("YES")
        else:
            print("NO")