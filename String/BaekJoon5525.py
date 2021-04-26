import sys
n = int(input())
m = int(input())
s = sys.stdin.readline()

cnt = 0
answer = 0
stack=[]

for i in range(m):
    if s[i] == "O":
        continue
    else:
        stack.append(i)

for i in range(1, len(stack)):
    if stack[i] - stack[i-1] == 2:
        cnt += 1
    else:
        cnt = 0

    if cnt >= n:
        answer += 1


print(answer)