import sys
bracket = list(input())

stack = []
answer = 0

for b in bracket:
    if b == ')':
        tmp = 0
        if not stack:
            print(0)
            sys.exit(0)
        else:
            while stack:
                top = stack.pop()
                if top == '(':
                    if tmp == 0:
                        stack.append(2)
                    else:
                        stack.append(2*tmp)
                    break
                elif top == '[':
                    print(0)
                    sys.exit(0)
                else:
                    tmp += int(top)

    elif b == ']':
        tmp = 0
        if not stack:
            print(0)
            sys.exit(0)
        else:
            while stack:
                top = stack.pop()
                if top == '[':
                    if tmp == 0:
                        stack.append(3)
                    else:
                        stack.append(3 * tmp)
                    break
                elif top == '(':
                    print(0)
                    sys.exit(0)
                else:
                    tmp += int(top)

    else:
        stack.append(b)

for i in stack:
    if i == '(' or i == '[':
        print(0)
        exit(0)
    else:
        answer += i

print(answer)
