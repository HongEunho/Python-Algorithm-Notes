import sys

arr = sys.stdin.readline().strip()


def solution(s):
    stack = [s[0]]

    for i in range(1, len(arr)):
        if arr[i] > stack[-1]:
            stack.pop()
        stack.append(arr[i])
    return ''.join(stack)


print(solution(arr))
