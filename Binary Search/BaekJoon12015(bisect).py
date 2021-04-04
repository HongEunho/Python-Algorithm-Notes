from bisect import bisect_left

n = int(input())
array = list(map(int, input().split()))
stack = [0]

for i in array:
    if stack[-1] < i:
        stack.append(i)
    else:
        stack[bisect_left(stack, i)] = i

print(len(stack)-1)